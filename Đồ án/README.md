# XÁC ĐỊNH VÀ PHÂN TÍCH KÝ TỰ BIỂN SỐ XE
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


# Cài đặt các thư viện bắt buộc - Python

  - scikit-learn
  - pandas
  - tensorflow==1.15
  - keras
  - numpy
  - opencv2

### Cấu trúc Folder
                        --------------------|Code|

                                                -------|images

                                                -------|result

                                                -------|step

                                                -------|weight

                                                -------|File_Plate.ipynb

                                                -------|Training_CNN.ipynb
  
                                                -------|Training_SVMandKNN.ipynb
  
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
