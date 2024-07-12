import os

from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.opera import options
from selenium.webdriver.chrome.options import Options

_operaDriverLoc = os.path.abspath(r'C:\dchrome\chromedriver.exe')  # Replace this path with the actual path on your machine.
_operaExeLoc = os.path.abspath('%s\\AppData\\Local\\Programs\\Opera\\opera.exe'%os.path.expanduser('~'))   # Replace this path with the actual path on your machine.

_remoteExecutor = 'http://127.0.0.1:9515'
_operaCaps = desired_capabilities.DesiredCapabilities.OPERA.copy()

_operaOpts = options.ChromeOptions()
_operaOpts._binary_location = _operaExeLoc
#_operaOpts.add_argument("--no-startup-window")
# Use the below argument if you want the Opera browser to be in the maximized state when launching. 
# The full list of supported arguments can be found on http://peter.sh/experiments/chromium-command-line-switches/
_operaOpts.add_argument('--start-maximized')   

browserDriver = webdriver.Chrome(executable_path = _operaDriverLoc, chrome_options = _operaOpts)#, desired_capabilities = _operaCaps)
browserDriver.get("https://amx-res-co.etadirect.com/")