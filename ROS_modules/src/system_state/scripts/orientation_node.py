#!/usr/bin/env python

import sys
sys.path = ['', '/home/ubuntu/SPARO/ROS_modules/devel/lib/python2.7/dist-packages', '/opt/ros/kinetic/lib/python2.7/dist-packages', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-arm-linux-gnueabihf', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/home/ubuntu/.local/lib/python2.7/site-packages', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/wx-3.0-gtk2']

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K
import numpy as np
import rospy
from system_state.srv import *



global tags
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


def load_model():
	json_file = open('/home/ubuntu/SPARO/tensorflow_models/sparo_model.json','r')
	model_json = json_file.read()
	json_file.close()

	global model
	model = keras.models.model_from_json(model_json)
	model.load_weights('/home/ubuntu/SPARO/tensorflow_models/sparo_model_weights.h5')
	print("model loaded from file")

	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	print("model compiled")	

	model._make_predict_function()

	global session
	session = K.get_session()

	global graph
	graph = tf.get_default_graph()

def load_image(img_path):
	img = keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
	img_tensor = keras.preprocessing.image.img_to_array(img)
	img_tensor = np.expand_dims(img_tensor, axis=0)
	img_tensor /= 255. 

	return img_tensor

def predict_orientation(img_path):
	with session.as_default():
		with graph.as_default():
			pred = model.predict(load_image(img_path))
			return str(tags[np.argmax(pred)])

def handle_get_orientation(req):
	rospy.loginfo("Get Orientation Request")
	orientation = predict_orientation("/opt/sparo_vision/target.jpg")
	rospy.loginfo("Got orientation: %s", orientation)
	return GetOrientationResponse(orientation=orientation)

def orientation_node():
	load_model()
	rospy.init_node("orientation_node")
	s = rospy.Service("get_orientation", GetOrientation, handle_get_orientation)
	rospy.loginfo("Ready to get orientations")
	rospy.spin()

if __name__ == "__main__":
	orientation_node()