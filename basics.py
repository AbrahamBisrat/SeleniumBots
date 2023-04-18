from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PATH = "/Users/MPB/repos/ChromeDriverDir/ChromeDriver"
s = Service(PATH)
print(PATH)

browser = webdriver.Chrome(service=s)


def launchBrowser():
    browser.get("https://www.github.com/abrahammehari")
    while (True):  # Keep it from sleeping
        pass


browser = launchBrowser()

print(browser.title)

# browser.quit()
