# Gender_recognition-using-cnn(convolutional neural network)
dependices -> pip install tensorflow keras matplotlib opencv pandas pickle 

Image Pixel data is loaded in x.pickle(features) and y.pickle(labels - men , women)

Download Image DataSets -> https://www.kaggle.com/playlist/men-women-classification (just 2500 images)

added wiki ppl face datasets as well 

nearly 15k images of men and women loaded_data in X.pickle(features) and labled them in y.pickle 

mkdir Datasets <- mv men women(Image Datasets) 


load_data.py -> preparing dataset(load image_data(men, women datasets) ,resize-> cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  ,create_training_data, shuffle(training_data),  reshape(-1, IMG_SIZE, IMG_SIZE, 1))

cnn_model.py -> model trining using 3-conv_layers 64-layer_size 0-dense layers

pred.py -> set test image either men or women croped one works better
