from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element("name", "q")
search_box.send_keys("QAエンジニア 転職")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

input("ブラウザを確認したらEnterを押してください")
driver.quit()



