import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Select a default radio button
driver.find_element(By.CSS_SELECTOR, '#radio-btn-example > fieldset > label:nth-child(2) > input').click()

# select radio buttons based on the selection available
radioButtons_list = driver.find_elements(By.CSS_SELECTOR, "#radio-btn-example > fieldset > label")
for item in radioButtons_list:
    if item.text == "Radio2":
        item.find_element(By.NAME, "radioButton").click()

# delayed drop downs
driver.find_element(By.ID, "autocomplete").send_keys("in")
wait_time = WebDriverWait(driver, 10)
element = wait_time.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ui-id-1 > li")))
dynamic_dropdown = driver.find_elements(By.CSS_SELECTOR, "#ui-id-1 > li")
for item in dynamic_dropdown:
    if item.find_element(By.CLASS_NAME, "ui-menu-item-wrapper").text == "India":
        item.find_element(By.CLASS_NAME, "ui-menu-item-wrapper").click()

dropdown = driver.find_element(By.NAME, "dropdown-class-example")
selectFromDropdown = Select(dropdown)
selectFromDropdown.select_by_value("option2")
# selectFromDropdown.select_by_index(0)
# selectFromDropdown.select_by_visible_text("Option2")

# select a default checkbox
driver.find_element(By.ID, "checkBoxOption1").click()

# get a list of check box and select value based on the attributes
checkBox_list = driver.find_elements(By.CSS_SELECTOR, "#checkbox-example > fieldset > label")
for item in checkBox_list:
    if item.get_attribute("for") == "benz":
        item.find_element(By.CSS_SELECTOR, " input").click()

# browser handle
driver.find_element(By.ID, "openwindow").click()
# get window handles
window_handles = driver.window_handles
# switch to new browser
driver.switch_to.window(window_handles[1])
# perform task in new browser
print(driver.title)
driver.close()
# switch back to original browser
driver.switch_to.window(window_handles[0])

# tab handle
driver.find_element(By.LINK_TEXT, "Open Tab").click()
# get tabs
window_handles = driver.window_handles
# switch to new tab
driver.switch_to.window(window_handles[1])
# perform task in tab
print(driver.title)
driver.close()
# switch back to original tab
driver.switch_to.window(window_handles[0])

# handling pop up
username = "John"
driver.find_element(By.NAME, "enter-name").send_keys(username)
driver.find_element(By.XPATH, '//input[@id="alertbtn"]').click()
time.sleep(2)
popup_message = driver.switch_to.alert.text
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.find_element(By.NAME, "enter-name").send_keys("John")
driver.find_element(By.ID, "confirmbtn").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

# reading web table
webTable_elements = driver.find_elements(By.XPATH, '//*[@id="product" and @name="courses"]/tbody/tr')
print(len(webTable_elements))
webTable_list = []

for row in range(2, len(webTable_elements) + 1):
    webTable_dict = {}
    for col in range(1, 4):
        key = driver.find_element(By.CSS_SELECTOR, f'#product > tbody > tr:nth-child({1}) > th:nth-child({col})').text
        value = driver.find_element(By.XPATH, f'//*[@id="product" and @name="courses"]/tbody/tr[{row}]/td[{col}]').text
        webTable_dict[key] = value
    webTable_list.append(webTable_dict)

maximum_cost = 25
# Prints  the list of course less than or equal to the maximum cost
for item in webTable_list:
    if int(item["Price"]) <= maximum_cost:
        for key, value in item.items():
            print(f'{key} : {value}')
