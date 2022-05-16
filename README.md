
# NSFW Screen Detect

[![PyPi version](https://badgen.net/pypi/v/pip/)](https://pypi.org/project/nsfw-screen-detect/)

A small python package for detecting NSFW content on a Windows display.

# Usage

This package does the following by default:  
1. Take a screenshot on all connected displays. You can take a screenshot of just the active window by passing `input='active_window'` to the `check` method. You can also pass in a Pillow image like so : `input=Image`
2. Detect actual images from the screenshot. You can skip this by passing `parse_images=False` to the `check` method.
3. Run skin detection. You can set the `skin_threshold` parameter to have NSFW checking skipped if an image contains very little skin.
4. Use AI to detect how NSFW each image is. You can pass `check_type='skin'` to just get a skin color score.
5. Returns each analyzed picture along with its results.

# Examples

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