from PIL import Image
import cv2 as cv
from .checker import Checker
from .camera import Camera

checker = Checker()
def run():
    print(checker.check(input='monitors',check_type='nsfw',parse_images=True))
    print(checker.check(input='monitors',check_type='nsfw',parse_images=False))

    print(checker.check(input='monitors',check_type='skin',parse_images=True))
    print(checker.check(input='monitors',check_type='skin',parse_images=False))

    print(checker.check(input='active_window',check_type='nsfw',parse_images=True))
    print(checker.check(input='active_window',check_type='nsfw',parse_images=False))

    print(checker.check(input='active_window',check_type='skin',parse_images=True))
    print(checker.check(input='active_window',check_type='skin',parse_images=False))

    pics = Camera().take_screenshot_of_active_window(parse_pics=True)
    single_pic = Image.fromarray(cv.cvtColor(pics['images'][0], cv.COLOR_BGR2RGB))
    x = checker.check(input=single_pic,check_type='nsfw',parse_images=False)
    print(x)







