from typing import List
import cv2 as cv
import numpy as np

class Parser:
    @staticmethod
    def parse_real_pictures(img:np.ndarray) -> List[np.ndarray]:
        """
        :param rectangles: list of rectangles
        :return: list of images in numpy array
        """
        shifted_up = np.roll(img, 1, axis=0)
        # Shift the image down one pixel
        shifted_down = np.roll(img, -1, axis=0)
        # Shift the image left one pixel
        shifted_left = np.roll(img, 1, axis=1)
        # Shift the image right one pixel
        shifted_right = np.roll(img, -1, axis=1)

        # Blur the images together
        t_img = cv.addWeighted(shifted_up, 1, shifted_down, 0, 0.0)
        t_img = cv.addWeighted(t_img, 1, shifted_left, 0, 0.0)
        mask = cv.addWeighted(t_img, 1, shifted_right, 0, 0.0)


        # Create a new image that is completely black besides any pixels that are the same between the two images
        diff = cv.absdiff(img, mask)

        # Threshhold any pixels that are not black
        _, thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY)

        # Make the image grayscale
        gray = cv.cvtColor(thresh, cv.COLOR_BGR2GRAY)

        # Blur the image
        #blurred = cv.GaussianBlur(gray, (5, 5), 0)

        # Find the contours
        contours, _ = cv.findContours(gray, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Remove the contours that are too small
        contours = [c for c in contours if cv.contourArea(c) > 1000]


        bounding_boxes = []

        for cnt in contours:
            x,y,w,h = cv.boundingRect(cnt)
            # if box is too short or thin, skip it
            if w < 100 or h < 100:
                continue

            bounding_boxes.append((x,y,w,h))
        
        # Save the image
        images= []
        for box in bounding_boxes:
            x,y,w,h = box
            cropped_image = img[y:y+h, x:x+w]
            if cropped_image.size != 0:
                images.append(cropped_image)
        
        return images
