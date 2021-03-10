from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
button = browser.find_element(By.ID, "book").click()
x_element = browser.find_element(By.ID,"input_value").text
x = x_element
input = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(str(math.log(abs(12*math.sin(int(x))))))
button1 = browser.find_element(By.ID, "solve").click()