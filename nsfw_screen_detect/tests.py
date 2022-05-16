from time import sleep

from .checker import Checker


checker = Checker()

checker.check(input='monitors',check_type='nsfw',parse_images=True)
checker.check(input='monitors',check_type='nsfw',parse_images=False)

checker.check(input='monitors',check_type='skin',parse_images=True)
checker.check(input='monitors',check_type='skin',parse_images=False)

checker.check(input='active_window',check_type='nsfw',parse_images=True)
checker.check(input='active_window',check_type='nsfw',parse_images=False)

checker.check(input='active_window',check_type='skin',parse_images=True)
checker.check(input='active_window',check_type='skin',parse_images=False)


