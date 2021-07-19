import time
from selenium import webdriver
import requests
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import pytesseract
from PIL import Image

# 模拟浏览器打开网站
driver = webdriver.Firefox()
url = "http://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start"
# 将窗口最大化
# browser.maximize_window()
# get verification code to path:"/home/<user>/Downloads/captcha.jsp.png"
while True:
  driver.get(url)
  time.sleep(2)
  code = driver.find_element_by_css_selector('img')
  # get picture
  action = ActionChains(driver).move_to_element(code)
  action.context_click(code)
  action.perform()
  pyautogui.typewrite(['v'])
  time.sleep(1)
  pyautogui.typewrite(['enter'])
  time.sleep(1)
  pyautogui.typewrite(['enter'])

  #recognize picture
  time.sleep(10)
  img = Image.open("/home/<user>/Downloads/captcha.jsp.png")
  result = pytesseract.image_to_string(img)
  print(result)

  elem_user = driver.find_element_by_name("username")
  elem_user.send_keys("<your_username>")
  elem_pwd = driver.find_element_by_name("password")
  elem_pwd.send_keys("<your_password>")
  elem_pwd = driver.find_element_by_name("captcha")
  elem_pwd.send_keys(result)
  time.sleep(1)
  driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div/form/div[5]/input[4]').click() # login in
  time.sleep(10)
  #enter
  try:
    driver.find_element_by_xpath('//*[@id="preview_start_button"]').click()
  except:
    print('Error!')
    time.sleep(5)
  else:
    print('success login in!')
    break

time.sleep(10)
#enter
driver.find_element_by_xpath('//*[@id="V1_CTRL262"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="V1_CTRL82"]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/ul/li[1]/a/nobr').click()
time.sleep(1)
print('clock in successfully')
time.sleep(5)
print('end')
driver.quit()
