from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# url = "https://www.nike.com/tw/launch?cp=78087397488_search_%7Ctw%7CCore%2BBrand%2B-%2BGN%2B-%2BPure%2B-%2BXCategory%2B-%2BNike%2BTaiwan%2B-%2BTM%2B-%2BGeneral%2B-%2BCH_CH%2B-%2BPhrase%7CGOOGLE%7Cnike&s=upcoming"
url = "https://www.nike.com/"
options = Options()
options.add_argument("--disable-notifications")

# 指定 chrome driver
chrome = webdriver.Chrome('./linux/chromedriver', chrome_options=options)
# 設定尺寸
chrome.set_window_size(1500, 1280)
# 開啟畫面
chrome.get(url)

# btn = chrome.find_element_by_class_name("join-log-in")
# btn.click()
# btn = chrome.find_element_by_xpath("//button[@class='nav-btn'")
# btn.click()
# print(btn.get_attribute("class"))

# 輸入帳號
# email = chrome.find_element_by_name("emailAddress")
# email.send_keys("neil605164@gmail.com")

# # 輸入密碼
# email = chrome.find_element_by_name("password")
# email.send_keys("2.Gs5JEAbY@FVH5")

# # 登入
# chrome.find_element_by_css_selector("input[type='button']").click()

# 等待秒後關閉
time.sleep(5)

# 關閉
chrome.quit()
