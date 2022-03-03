from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.nike.com/tw/launch"
# url = "https://www.nike.com/"
# url = "https://www.google.com.tw"

options = Options()
# 不顯示「彈出的訊息」
options.add_argument("--disable-notifications")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
# 不顯示「正受到自動測試軟體控制」
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# 使用偽造的 user-agent
ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
# ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
options.add_argument("user-agent={}".format(ua))
# proxy
# options.add_argument('--proxy-server=96.9.77.71:8080')


# 指定 chrome driver
chrome = webdriver.Chrome('./linux/chromedriver', chrome_options=options)
# 設定尺寸
chrome.set_window_size(1500, 1280)
# 開啟畫面
chrome.get(url)

## google browser ##
# chrome.find_element_by_class_name("gLFyf").send_keys("nike 預購")

# btn=chrome.find_element_by_class_name("gNO89b")
# btn.click()

# result=chrome.find_element_by_class_name("LC20lb")
# result.click()

##################

btn = chrome.find_element_by_class_name("join-log-in")
btn.click()
# btn = chrome.find_element_by_xpath("//button[@class='nav-btn'")
# btn.click()
# print(btn.get_attribute("class"))

# 輸入帳號
email = chrome.find_element_by_name("emailAddress")
email.send_keys("neil605164@gmail.com")

# 輸入密碼
email = chrome.find_element_by_name("password")
email.send_keys("2.Gs5JEAbY@FVH5")

# 登入
chrome.find_element_by_css_selector("input[type='button']").click()

# 等待秒後關閉
time.sleep(60)

# 關閉
chrome.quit()
