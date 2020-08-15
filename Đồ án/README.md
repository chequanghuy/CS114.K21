# XÁC ĐỊNH VÀ PHÂN TÍCH KÝ TỰ BIỂN SỐ XE
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Ở Việt Nam đã có nhiều công trình nghiên cứu các hệ thống thông minh ứng
dụng Trí tuệ nhân tạo như Bệnh viện thông minh, giao thông thông minh, nhà
thông minh, xe tự lái,… Trong đó, ứng dụng nhận diện biển số xe cũng được chú
trọng nghiên cứu và đẩy mạnh phát triển tại thị trường xe máy lớn thứ 4 thế giới là
Việt Nam. Công nghệ tự động nhận diện biển số xe được ra mắt từ năm 1976 (theo
Wikipedia.org) được sử dụng tại nhiều nước phát triển trên thế giới như Australia,
Canada, Denmark, United States …. Nó được chính phủ các nước sử dụng để giám
sát giao thông tại các nút giao thông quan trọng, tại các trạm thu phí tự động và
cũng được các tổ chức sử dụng nhằm mục đích thương mại như xây dựng bãi giữ
xe thông minh.
Sau khi đã tìm hiểu qua về những ứng dụng mạnh mẽ mà công nghệ nhận
diện biển số xe này mang lại, chúng em tự hỏi liệu có thể tự phát triển một hệ
thống của riêng mình dựa vào những công nghệ đã có sẵn. Từ đó bài toán được đặt
ra là thiết kế mô hình nhận diện và phân tích kí tự biển số xe máy dựa vào lượng
dữ liệu đang có tại bãi giữ xe UIT.
# Cài đặt các thư viện bắt buộc - Python

  - scikit-learn
  - pandas
  - tensorflow==1.15
  - keras
  - numpy
  - opencv2
  - matplotlib

### Cấu trúc Folder
                        --------------------|Code|

                                                -------|images

                                                -------|result

                                                -------|step

                                                -------|weight

                                                -------|File_Plate.ipynb

                                                -------|Training_CNN.ipynb
  
                                                -------|Training_SVMandKNN.ipynb

                                                -------|plateDetection.ipynb

                        --------------------|Haar Cascade|
                        
                                                -------|DataSet
                        
                                                -------|GreenParking

                                                -------|TrainImg
                                                
                        --------------------|Report|
                        
                                                -------|CS114.K21 - PLATE BIKE - FINAL REPORT.pdf
                        
                                                -------|CS114.K21 - PLATE BIKE.pdf
* Code: 
    + data: Chứa các ký tự riêng lẻ xuất hiện trên biển số xe máy Việt Nam
    + images: Chứa hình ảnh biển số xe để nhận diện
	+ result: Chứa kết quả sau khi dự đoán
	+ step: Folder chứa các hình ảnh cho việc debug ở code plateDetection.ipynb
	+ weight: chứa các model đã training bao gồm : KNN, SVM, CNN, HaarCasCade
	+ plateDetection.ipynb: Code chạy từng bước khi nhận diện một tấm ảnh chứa biển số xe
	+ File_Plate.ipynb: Code dự đoán tất cả hình ảnh chứa biển số xe ở file images
	+ Traning_CNN: Code traning model CNN 
	+ Training_SVMandKNN: Code training model SVM và KNN
* Haar Cascade: 
    + DataSet: Ảnh cho training HarrCascade, gồm ảnh positive và negative, trong đó ảnh positive là ảnh chứa biển số xe, negative là các ảnh không chứa biển số xe
    + GreenParking và TrainImg: Chứa hình ảnh dữ liệu ban đầu trước khi label vùng chứa biển số xe
* Haar Cascade: 
    + CS114.K21 - PLATE BIKE - FINAL REPORT.pdf: báo cáo hoàn chỉnh
    + CS114.K21 - PLATE BIKE.pdf: slide

## Authors

* **Ly Hong Phong** - *Develope and Operation* - [phonghongs](https://github.com/phonghongs)

* **Che Quang Huy** - *Develope and Operation* - [chequanghuy](https://github.com/chequanghuy)

## License
