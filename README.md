# Gender_recognition-using-cnn(convolutional neural network)
dependices -> pip install tensorflow keras matplotlib opencv pandas pickle 

Image Pixel data is loaded in x.pickle(features) and y.pickle(labels - men , women)

Download Image DataSets -> https://www.kaggle.com/playlist/men-women-classification (just 2500 images)

i collected data from various sources like wiki ppl face datasets and some other

nearly 15k images of men and women loaded_data in X.pickle(features) and labled them in y.pickle 

mkdir Datasets <- mv men women(Image Datasets) 


load_data.py -> preparing dataset, resize(50,50) as gray_scale images, preparing trining datasets as x features for y labels,shuffle the train data, rshaping btw(-1,2500,1),using pickle we can store variable data like x and y so that we can user these train data to train our model in cnn_model.py 

cnn_model.py -> model trining using 3-conv_layers 64-layer_size 0-dense layers

pred.py -> set test image either men or women croped one works better
