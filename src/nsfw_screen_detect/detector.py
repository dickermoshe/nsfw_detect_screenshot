from pathlib import Path
from typing import Dict
import numpy as np 
import tensorflow as tf
from pathlib import Path
import cv2 as cv


IMAGE_DIM = 256

class Detector:
    def __init__(self) -> None:
        model_path = str(Path( __file__ ).parent.absolute() / 'bin' /'lite_classifier.h5')
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

    def nsfw_rating_of_image(self,img : np.ndarray) -> Dict:

        img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()
        img = self._img_to_array(img)
        img /= 255
        img = np.asarray([img])[0]
        img = cv.resize(img, (IMAGE_DIM, IMAGE_DIM))
        img = np.expand_dims(img, axis=0)
        input_data = np.array(img, dtype=np.float32)
        self.interpreter.set_tensor(input_details[0]['index'], input_data)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(output_details[0]['index'])
        return  {"unsafe": output_data[0][0], "safe": output_data[0][1]}
        
    def skin_rating_of_image(self,img : np.ndarray) -> Dict:
        
        #converting from gbr to hsv color space
        img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        #skin color range for hsv color space 
        HSV_mask = cv.inRange(img_HSV, (0, 15, 0), (17,170,255)) 
        HSV_mask = cv.morphologyEx(HSV_mask, cv.MORPH_OPEN, np.ones((3,3), np.uint8))

        #converting from gbr to YCbCr color space
        img_YCrCb = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)

        #skin color range for hsv color space 
        YCrCb_mask = cv.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
        YCrCb_mask = cv.morphologyEx(YCrCb_mask, cv.MORPH_OPEN, np.ones((3,3), np.uint8))

        #merge skin detection (YCbCr and hsv)
        global_mask=cv.bitwise_and(YCrCb_mask,HSV_mask)
        global_mask=cv.medianBlur(global_mask,3)
        global_mask = cv.morphologyEx(global_mask, cv.MORPH_OPEN, np.ones((4,4), np.uint8))
        global_result=cv.bitwise_not(global_mask)

        # Get a percentage of skin pixels
        total_pixels = global_result.shape[0] * global_result.shape[1]
        skin_pixels = cv.countNonZero(cv.bitwise_not(global_result))
        skin_percentage = (skin_pixels / total_pixels) * 100
        return {
            'percentage':skin_percentage,
            'skin_pixel_count':skin_pixels,
            'total_pixel_count':total_pixels
            }

    def _img_to_array(self,img, data_format='channels_last', dtype='float32'):
        """Converts a PIL Image instance to a Numpy array.
        # Arguments
            img: PIL Image instance.
            data_format: Image data format,
                either "channels_first" or "channels_last".
            dtype: Dtype to use for the returned array.
        # Returns
            A 3D Numpy array.
        # Raises
            ValueError: if invalid `img` or `data_format` is passed.
        """
        if data_format not in {'channels_first', 'channels_last'}:
            raise ValueError('Unknown data_format: %s' % data_format)
        # Numpy array x has format (height, width, channel)
        # or (channel, height, width)
        # but original PIL image has format (width, height, channel)
        x = np.asarray(img, dtype=dtype)
        if len(x.shape) == 3:
            if data_format == 'channels_first':
                x = x.transpose(2, 0, 1)
        elif len(x.shape) == 2:
            if data_format == 'channels_first':
                x = x.reshape((1, x.shape[0], x.shape[1]))
            else:
                x = x.reshape((x.shape[0], x.shape[1], 1))
        else:
            raise ValueError('Unsupported image shape: %s' % (x.shape,))
        return x