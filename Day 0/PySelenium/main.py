from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import service as EdgeService  #?? How to import all from webdriver?
browser = webdriver.Edge()
browser.get("https://github.com/")

octicon_link = browser.find_element(by=By.CLASS_NAME, value="octicon-three-bars")
octicon_link.click()  # does not need an object; it's just a process

signin_link = browser.find_element(by=By.LINK_TEXT,value="Sign in")  # LINK_TEXT != NAME (Do not confuse text w/ CSS Class)
signin_link.click()

browser.implicitly_wait(0.5)  # program will move so fast it will read the wrong template without this

username_box = browser.find_element(by=By.ID, value="login_field")  # http literally says ID
username_box.send_keys("The-Captain-William")
password_box = browser.find_element(by=By.ID, value="password")
password_box.send_keys("GodisanEngineer12!")
password_box.submit()

# browser.quit() to close


