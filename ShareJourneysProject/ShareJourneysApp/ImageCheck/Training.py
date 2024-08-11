import os
import shutil

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from . import config  # hoặc from .config import <tên phần tử>


def has_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            return True
    return False
def del_image(dir):
    print(dir)
    for dir_path in [dir]:
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            print(file_path)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
def load_and_train_model():
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

    # Đường dẫn đến dữ liệu mới
    new_data_dir = config.NEW_DATA_DIR

    # Load mô hình đã huấn luyện trước đó
    model = load_model(config.NEW_DATA_DIR+'\\sensitive_image_detection_model.keras')

    # Tạo các đối tượng ImageDataGenerator cho huấn luyện và kiểm tra
    new_train_datagen = ImageDataGenerator(rescale=config.RESCALE, validation_split=0.2)

    # Tạo các generator
    new_train_generator = new_train_datagen.flow_from_directory(
        new_data_dir,
        target_size=config.TARGET_SIZE,
        batch_size=config.BATCH_SIZE,
        class_mode=config.CLASS_MODE,
        subset='training'
    )

    new_validation_generator = new_train_datagen.flow_from_directory(
        new_data_dir,
        target_size=config.TARGET_SIZE,
        batch_size=config.BATCH_SIZE,
        class_mode=config.CLASS_MODE,
        subset='validation'
    )

    # Kiểm tra số lượng mẫu trong generator
    if new_train_generator.samples != 0 and new_validation_generator.samples != 0:

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        model.fit(
            new_train_generator,
            steps_per_epoch=max(new_train_generator.samples // new_train_generator.batch_size, 1),
            validation_data=new_validation_generator,
            validation_steps=max(new_validation_generator.samples // new_validation_generator.batch_size, 1),
            epochs=config.EPOCHS  # Bạn có thể điều chỉnh số lượng epochs theo nhu cầu
        )

    # Lưu mô hình đã huấn luyện tiếp tục
    model.save(config.NEW_DATA_DIR+'\\sensitive_image_detection_model.keras')

    # Xóa tất cả các ảnh trong hai thư mục sensitive và nonsensitive
    sensitive_dir = os.path.join(new_data_dir, 'new_sensitive_data\\sensitive')
    nonsensitive_dir = os.path.join(new_data_dir, 'new_sensitive_data\\nonsensitive')
    if has_images(sensitive_dir):
        print(1)
        del_image(sensitive_dir)
    if has_images(nonsensitive_dir):
        print(2)
        del_image(nonsensitive_dir)


# # Chạy hàm load_and_train_model khi file này được chạy trực tiếp
# if __name__ == "__main__":
#     load_and_train_model()
