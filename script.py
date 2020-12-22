from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://github.com/login")
elem = driver.find_element(By.ID, "login_field")

#Replace your username here
elem.send_keys("username")
elem2 = driver.find_element(By.ID, "password")

#Replace your password here (line 18)
elem2.send_keys("password")
elem3 = driver.find_element(By.NAME, "commit")
elem3.send_keys(Keys.RETURN)


#Replace your username and reponame here
URL = "https://github.com/username/reponame/edit/main/README.md"

#Replace the number 5 with the number of commits you want
for x in range(1,5):
    
	newfilename = "READ" + str(x) + "E.md"
	driver.get(URL)
	elem4 = driver.find_element(By.NAME, "filename")
	elem4.send_keys((Keys.BACKSPACE)*9 + newfilename)
	elem4 = driver.find_element(By.ID, "submit-file")
	elem4.send_keys(Keys.RETURN)
	URL = "https://github.com/username/reponame/edit/main/READ" + str(x) + "E.md"

newfilename2 = "README.md"
driver.get(URL)
elem5 = driver.find_element(By.NAME, "filename")
elem5.send_keys((Keys.BACKSPACE)*9 + newfilename2)
elem5 = driver.find_element(By.ID, "submit-file")
elem5.send_keys(Keys.RETURN)


wait = WebDriverWait(driver, 30)

