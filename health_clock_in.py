import time
from selenium import webdriver
# import requests
from selenium.webdriver.common.action_chains import ActionChains
# import pyautogui
# import pytesseract
# from PIL import Image

driver = webdriver.Firefox()
url = "http://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start"

while True:
  driver.get(url)
  time.sleep(2)
  #code = driver.find_element_by_css_selector('img')
  ## get picture
  #action = ActionChains(driver).move_to_element(code)
  #action.context_click(code)
  #action.perform()
  #pyautogui.typewrite(['v'])
  #time.sleep(1)
  #pyautogui.typewrite(['enter'])
  #time.sleep(1)
  #pyautogui.typewrite(['enter'])
  
  ## recognize picture
  #time.sleep(10)
  #img = Image.open("/home/hanri/Downloads/captcha.jsp.png")
  #result = pytesseract.image_to_string(img)
  #print(result)

  elem_user = driver.find_element_by_name("un")
  elem_user.send_keys("<学号>")
  elem_pwd = driver.find_element_by_name("pd")
  elem_pwd.send_keys("<密码>")
  #elem_pwd = driver.find_element_by_name("captcha")
  #elem_pwd.send_keys(result)
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="index_login_btn"]').click() # login in
  time.sleep(6)
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
