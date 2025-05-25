import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('BSTACK_USERNAME')
ACCESSKEY = os.getenv('BSTACK_ACCESSKEY')
REMOTE_URL = os.getenv('REMOTE_URL')
DEVICE_NAME = os.getenv('DEVICE_NAME')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
APP = os.getenv('app', 'bs://sample.app')


def driver_options():
    options = UiAutomator2Options()
    if DEVICE_NAME:
        options.set_capability('deviceName', DEVICE_NAME)
    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)
    options.set_capability('app', APP)
    options.set_capability('platformVersion', '9.0')
    options.set_capability(
        'bstack:options', {
            "projectName": "Test project",
            "buildName": "browserstack-build-1",
            "sessionName": "Session test",
            "userName": USERNAME,
            "accessKey": ACCESSKEY
        })

    return options