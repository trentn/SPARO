import tensorflow as tf
from tensorflow import keras
import numpy as np
import os

tags = {0: 'B000',
 1: 'B001',
 2: 'B010',
 3: 'B011',
 4: 'B100',
 5: 'B101',
 6: 'B110',
 7: 'B111',
 8: 'GVF',
 9: 'GVU',
 10: 'LVF',
 11: 'SHFC',
 12: 'SHFO',
 13: 'SHUC',
 14: 'SHUO'}


json_file = open('sparo_model.json','r')
model_json = json_file.read()
json_file.close()

model = keras.models.model_from_json(model_json)
model.load_weights('sparo_model_weights.h5')
print("model loaded from file")

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print("model compiled")


def load_image(img_path):
	img = keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
	img_tensor = keras.preprocessing.image.img_to_array(img)
	img_tensor = np.expand_dims(img_tensor, axis=0)
	img_tensor /= 255. 

	return img_tensor


def predict_orientation(img_path):
	pred = model.predict(load_image(img_path))
	print(tags[np.argmax(pred)])



img_dir = '/home/ubuntu/demo_images'
for image in os.listdir(img_dir):
	print(image)
	predict_orientation('%s/%s' % (img_dir, image))


