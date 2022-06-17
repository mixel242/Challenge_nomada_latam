from select import select
from selenium import webdriver
from selenium.webdriver.support.ui import Select

website = 'http://miguel-numpad.hebercamargo.com/'
path = 'chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

#button button

press_button_button = driver.find_element_by_xpath('/html/body/form/button')
press_button_button.click()

#dropdown

dropdown = Select(driver.find_element_by_id('element_list'))
dropdown.select_by_visible_text('Canal')

#clik on number
    #5
number_5 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type=button]').click()
number_5 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type=button]').click()
    #1
number_1 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(6) > td:nth-child(1) > input[type=button]').click()
number_1 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(6) > td:nth-child(1) > input[type=button]').click()
    #2
number_2 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > input[type=button]').click()
number_2 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > input[type=button]').click()
    #3
number_3 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(6) > td:nth-child(3) > input[type=button]').click()
number_3 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(6) > td:nth-child(3) > input[type=button]').click()
    #4
number_4 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(5) > td:nth-child(1) > input[type=button]').click()
number_4 = driver.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(5) > td:nth-child(1) > input[type=button]').click()


