# CNN-model
Sử dụng CNN model để đánh giá góc xoay và vận tốc của xe:
Chúng ta sẽ train hai model một cho góc xoay và một cho vận tốc:
Bước 1:
    Trước khi train, cần chạy file DataCollect.py để thu thập dữ liệu. Dữ liệu thu thập bao gồm: Mỗi frame ảnh cùng với giá trị góc và vận tốc của sẽ lúc đó.
    Dữ liệu ảnh lưu trong IMG_{X} sẽ được tạo khi chạy xong chương trình. 
    Dữ liệu góc lưu vào log_angle_{X}.csv, Dữ liệu vận tốc lưu vào log_speed_{X}.csv
Bước 2:
    Train model cho góc chạy file training.py
    Train model cho vận tốc chạy file training.py nhưng lần này trong utils dùng cơ sở dữ liệu vận tốc.
Bước 3:
    Sử dụng model để chạy client.py
    
