from pywinauto import Desktop
from pywinauto.win32structures import RECT
class Apps:
    def __init__(self):
        self.desktop = Desktop(backend="uia")
    
    def get_windows(self,):
        """
        Returns a list of all the Windows on the desktop.
        """
        return self.desktop.windows()
    
    def get_active_window(self):
        """
        Returns the active window.
        """
        windows = self.get_windows()
        for window in windows:
            try:
                if window.is_active():
                    return window
            except:
                pass
        return None