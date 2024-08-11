import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('duLieuNhayCam.csv')

# Chia dữ liệu thành văn bản và nhãn
texts = df['text'].tolist()
labels = df['label'].tolist()

# Tính toán số lượng tài liệu huấn luyện
num_documents = len(texts)

# Tính toán giá trị tương đối cho min_df và max_df
max_df_relative = 0.90  # Tỷ lệ phần trăm tài liệu lớn nhất

max_df = int(max_df_relative * num_documents)

# Tách dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.1, random_state=42)

# Tạo pipeline với TfidfVectorizer và LogisticRegression
pipeline = make_pipeline(TfidfVectorizer(min_df=1, max_df=max_df, sublinear_tf=True), LogisticRegression())

# Định nghĩa các siêu tham số cần tìm kiếm
param_grid = {
    'tfidfvectorizer__ngram_range': [(1, 1), (1, 2), (1, 3)],
    'logisticregression__C': [0.1, 1, 10, 100]
}

# Sử dụng GridSearchCV để tìm siêu tham số tốt nhất
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# In ra các siêu tham số tốt nhất
print("Best parameters found: ", grid_search.best_params_)

# Huấn luyện lại mô hình với siêu tham số tốt nhất
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# Đánh giá mô hình trên tập kiểm tra
accuracy = best_model.score(X_test, y_test)
print(f"Test accuracy: {accuracy:.2f}")

# Lưu mô hình
joblib.dump(best_model, 'content_model.pkl')
