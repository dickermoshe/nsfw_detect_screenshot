from .camera import Camera
from .detector import Detector
import cv2  as cv
from PIL import Image

class Checker:
    def __init__(self) -> None:
        self.camera = Camera()
        self.detector = Detector()
    
    def check(self,input:str = 'monitors',check_type : str = 'nsfw', parse_images:bool=True,skin_threshold:float=0) -> dict:
        """
        Checks the specified input for inappropriate content.

        :param input: The input to check. Must be one of the following:
            - monitors
            - active_window
        :param check_type: The type of content to check for. Must be one of the following:
            - nsfw - NSFW content
            - skin - Skin content
        :param parse_images: Whether to parse individual images from the input or to process the entire input at once.
        :param skin_threshold: How much skin content needed to run the nsfw detection. If you want to run the nsfw detection even if there is no skin content, set this to 0.
        """

        if input == 'monitors':
            images = self.camera.take_screenshot_of_monitor(parse_pics=parse_images)
        elif input == 'active_window':
            images = self.camera.take_screenshot_of_active_window(parse_pics=parse_images)

        results = {'title':images['title'],'results':[]}
        for image in images['images']:
            skin_rating = self.detector.skin_rating_of_image(image)

            if check_type == 'skin' or skin_rating['percentage'] < skin_threshold:
                results['results'].append({'image':Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB)),'skin_rating':skin_rating,'nsfw_rating':None})
                continue
            else:
                nsfw_rating = self.detector.nsfw_rating_of_image(image)
                results['results'].append({'image':Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB)),'skin_rating':skin_rating,'nsfw_rating':nsfw_rating})
                continue
        return results


    
                

        

        







    


    
        
    


        


