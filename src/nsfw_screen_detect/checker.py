from .camera import Camera
from .detector import Detector
import cv2  as cv
from PIL import Image

class Checker:
    def __init__(self) -> None:
        self.camera = Camera()
        self.detector = Detector()
    
    def check(self,input:str = 'monitors',check_type : str = 'nsfw', parse_images:bool=True):
        """
        Checks the specified input for inappropriate content.

        :param input: The input to check. Must be one of the following:
            - monitors
            - active_window
        :param check_type: The type of content to check for. Must be one of the following:
            - nsfw - NSFW content
            - skin - Skin content
        :param parse_images: Whether to parse individual images from the input or to process the entire input at once.
        """

        if input == 'monitors':
            images = self.camera.take_screenshot_of_monitor(parse_pics=parse_images)
        elif input == 'active_window':
            images = self.camera.take_screenshot_of_active_window(parse_pics=parse_images)

        results = {'title':images['title'],'results':[]}
        for image in images['images']:
            if check_type == 'nsfw':
                rating = self.detector.nsfw_rating_of_image(image)
            elif check_type == 'skin':
                rating = self.detector.skin_rating_of_image(image)
            else:
                raise ValueError("The check_type must be one of the following: nsfw, skin")

            results['results'].append({'rating':rating,'image':Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))})

        return results


    
                

        

        







    


    
        
    


        


