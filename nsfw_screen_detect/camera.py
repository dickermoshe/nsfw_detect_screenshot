from pprint import pprint as pp
from typing import List

from PIL import ImageGrab
from PIL.Image import Image
from PIL import Image as PILImage

from mss import mss
from mss.screenshot import ScreenShot

import numpy as np
import cv2 as cv

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
    
    def _opencv_to_pillow(self,image : np.ndarray) -> Image:
        """
        Converts the image to the specified format.
        :param image: The image to convert.
        """
        return PILImage.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))

    def _mss_to_pillow(self,screenshot:ScreenShot) -> Image:
        """
        Converts the image to the specified format.
        :param image: The image to convert.
        """
        return PILImage.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
    
    def _mss_to_opencv(self,screenshot:ScreenShot) -> np.ndarray:
        """
        Converts the image to the specified format.
        :param image: The image to convert.
        """
        return cv.cvtColor(np.array(screenshot), cv.COLOR_BGR2RGB)

    def take_screenshot_of_monitor(self,monitor : int = 0,_format :str = 'pillow') -> List[Image|np.ndarray]:
        """
        Takes a screenshot of the monitor.
        :param monitor: The monitor to take a screenshot of. 0 will take of all the monitors.
        :param _format: The format to return the image in.
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
        
        # Convert the images to the format specified
        if _format == 'pillow':
            images = [self._mss_to_pillow(sct_img) for sct_img in images_array]
        elif _format == 'opencv':
            images = [self._mss_to_opencv(sct_img) for sct_img in images_array]
        else:
            raise ValueError("The format is not supported.")

        # Return the images
        return images

    def take_screenshot_of_active_window(self,_format :str = 'pillow') -> Image|np.ndarray:
        """
        Takes a screenshot of the active window.
        :param _format: The format to return the image in.
        """
        # Get the list of all the windows
        apps = Apps()
        active_window = apps.get_active_window()
        
        window_img = active_window.capture_as_image()


        if _format == 'pillow':
            return window_img

        elif _format == 'opencv':
            return self._pillow_to_opencv(window_img)
    