
import os
import numpy as np
from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.preprocessing import image
import requests
from io import BytesIO
from PIL import Image
from . import config  # hoặc from .config import <tên phần tử>


# Load mô hình đã lưu
def choose_model():
    return load_model(config.NEW_DATA_DIR+'\\sensitive_image_detection_model.keras')

# Hàm tải hình ảnh từ URL
def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((150, 150))  # Resize ảnh về kích thước phù hợp
    img_array = image.img_to_array(img) / 255.0  # Chuẩn hóa giá trị pixel
    img_array = np.expand_dims(img_array, axis=0)  # Thêm batch dimension
    return img, img_array

# Hàm dự đoán với mô hình
def predict_image(model, img_array):
    prediction = model.predict(img_array)
    print('prediction[0]', prediction[0])
    return 'sensitive' if prediction[0] > 0.5 else 'not_sensitive'

def change_dir(image_url):
    # URL của hình ảnh trên Cloudinary

    new_sensitive_data = config.NEW_DATA_DIR
    # Đường dẫn đến thư mục chứa các hình ảnh nhạy cảm và không nhạy cảm
    sensitive_dir = os.path.join(new_sensitive_data, 'new_sensitive_data\\sensitive')
    not_sensitive_dir = os.path.join(new_sensitive_data, 'new_sensitive_data\\nonsensitive')

    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(sensitive_dir, exist_ok=True)
    os.makedirs(not_sensitive_dir, exist_ok=True)

    # Tải và chuẩn bị hình ảnh
    img, img_array = load_image_from_url(image_url)
    prediction = predict_image(choose_model(), img_array)

    # Lưu tệp vào thư mục tương ứng
    filename = os.path.basename(image_url)
    if prediction == 'sensitive':
        img.save(os.path.join(sensitive_dir, filename))
    else:
        img.save(os.path.join(not_sensitive_dir, filename))
    print(f'File: {filename}, Prediction: {prediction}, Saved to: {prediction}_dir')

    return prediction

# if __name__ == "__main__":
#     image_url = 'https://res.cloudinary.com/depgwkadm/image/upload/v1718714285/mjz4fuubkd34alj7hzaq.jpg'
#     change_dir(image_url)
