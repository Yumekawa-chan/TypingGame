from selenium import webdriver
import time
import pyautogui as pg

driver = webdriver.Chrome()
driver.get('file:///C:\\Users\\rukum\\work\\typing\\index.html')

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/button").click()

for i in range(20):
     element = driver.find_element_by_class_name("question")
     pg.typewrite(element.text,interval=0.08)
     time.sleep(0.2)

exit()