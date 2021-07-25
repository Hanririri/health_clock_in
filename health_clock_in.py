import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
url = "http://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start"

while True:
  driver.get(url)
  time.sleep(2)

  elem_user = driver.find_element_by_name("un")
  elem_user.send_keys("<your_student_ID>")
  elem_pwd = driver.find_element_by_name("pd")
  elem_pwd.send_keys("<your_password>")
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="index_login_btn"]').click() # login in
  time.sleep(6)
  
  driver.find_element_by_xpath('//*[@id="preview_start_button"]').click()
  time.sleep(10)

  try:
    driver.find_element_by_xpath('//*[@id="V1_CTRL262"]').click()
  except:
    print('Error!')
    time.sleep(5) # restart
  else:
    print('success login in!')
    break

time.sleep(1)
driver.find_element_by_xpath('//*[@id="V1_CTRL82"]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/form/div/div[1]/div[2]/ul/li[1]/a/nobr').click()
time.sleep(1)
print('clock in successfully')
time.sleep(5)
print('end')
driver.quit()
