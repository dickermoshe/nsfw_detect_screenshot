from pprint import pprint as pp
from typing import Dict, List

from PIL.Image import Image

from mss import mss
from mss.screenshot import ScreenShot

import numpy as np
import cv2 as cv

from.parser import Parser
from .windows import Apps

class Camera:
    def __init__(self) -> None:
        self.sct = mss()
    
    def _pillow_to_opencv(self,image : Image) -> np.ndarray:
        """
        Converts the image to the specified format.
        :param image: The image to convert.
        """
        return cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)

    def _mss_to_opencv(self,screenshot:ScreenShot) -> np.ndarray:
        """
        Converts the image to the specified format.
        :param image: The image to convert.
        """
        return np.array(screenshot)

    def take_screenshot_of_monitor(self,monitor : int = 0, parse_pics=False) -> Dict:
        """
        Takes a screenshot of the monitor.
        :param monitor: The monitor to take a screenshot of. 0 will take of all the monitors.
        """
        # Create a list of all the screens
        if monitor == 0:
            monitor_ids = range(1,len(self.sct.monitors))
        elif monitor < len(self.sct.monitors):
            monitor_ids = [monitor]
        else:
            raise ValueError("The monitor id is out of range.")
        
        # Take a screenshot of each monitor
        images_array = []
        for monitor_id in monitor_ids:
            monitor = self.sct.monitors[monitor_id]
            sct_img = self.sct.grab(monitor)
            images_array.append(sct_img)
        
        # Convert the images to opencv
        images = [self._mss_to_opencv(v) for v in images_array]
        title = 'Monitor'
        if parse_pics:
            images = self.real_pics_from_image(images)

        # Return the images
        return {'title':title,'images':images}

    def take_screenshot_of_active_window(self,parse_pics=False) -> Dict:
        """
        Takes a screenshot of the active window.
        :param _format: The format to return the image in.
        """
        # Get the list of all the windows
        apps = Apps()
        active_window = apps.get_active_window()
        
        window_img = active_window.capture_as_image()

        images = [self._pillow_to_opencv(window_img)]
        title = active_window.window_text()
        if parse_pics:
            images = self.real_pics_from_image(images)
        
        # Return the images
        return {'title':title,'images':images}
    
    def real_pics_from_image(self,images :List[np.ndarray]):
        image_list = []
        for img in images:
            image_list.extend(Parser.parse_real_pictures(img))
        return image_list

    