
# NSFW Screen Detect

[![PyPi version](https://badgen.net/pypi/v/pip/)](https://pypi.org/project/nsfw-screen-detect/)


A small python package for detecting nsfw on a Windows display.

```
# Import and initialize the main Checker class

from nsfw_screen_detect import Checker
checker = Checker()

# Run check on all monitors
results = checker.check()

# Run check on active window
results = checker.check(input='active_window')

# Run check for skin content
results = checker.check(check_type='skin')

# Run check without parsing real pictures from screenshot
results = checker.check(parse_images=False)
```

Big thanks to NudeNet for their AI model.