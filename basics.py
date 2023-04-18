from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PATH = "/Users/MPB/repos/ChromeDriverDir/ChromeDriver"
s = Service(PATH)

print(PATH)


driver = webdriver.Chrome(service=s)


def launchBrowser():
    driver.get("https://www.github.com/abrahammehari")
    while (True):  # Keep it from sleeping
        pass


driver = launchBrowser()

print(driver.title)

# driver.quit()
