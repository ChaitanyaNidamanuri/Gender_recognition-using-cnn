import cv2
import tensorflow as tf

label=["male", "female"]


def prepare(filepath):
    IMG_SIZE = 70
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("shadey.model")

prediction = model.predict([prepare('Vijitha.jpg')])
print(prediction)
print(label[int(prediction[0][0])])
