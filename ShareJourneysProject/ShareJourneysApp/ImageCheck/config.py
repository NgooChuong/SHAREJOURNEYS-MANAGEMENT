# Đường dẫn đến dữ liệu hình ảnh
DATA_DIR = r'D:\OU\PythonAI\sensitive'
NEW_DATA_DIR = r'G:\BaiThiLTHD\ShareJourneysProject\ShareJourneysApp\ImageCheck'
PICTURE = r'D:\OU\PythonAI\picture'

# Kích thước ảnh
TARGET_SIZE = (150, 150)

# Batch size cho generator
BATCH_SIZE = 32

# Số lượng epochs cho quá trình huấn luyện
EPOCHS = 10

# Tên file mô hình đã lưu
MODEL_PATH = 'sensitive_image_detection_model.h5'
FINE_TUNED_MODEL_PATH = 'sensitive_image_detection_model_finetuned.h5'
CLASS_MODE = 'binary'


RESCALE = 1.0/255.0

SUBNET_TRAINING = 'training'
SUBNET_VALIDATION = 'validation'
