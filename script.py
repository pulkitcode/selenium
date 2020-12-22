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
#Add your username here
elem.send_keys("username")
#Add your password here
elem2 = driver.find_element(By.ID, "password")
#Add your reponame here
elem2.send_keys("reponame")
elem3 = driver.find_element(By.NAME, "commit")
elem3.send_keys(Keys.RETURN)



URL = "https://github.com/username/reponame/edit/main/README.md"

# Change 100 to the number of commits you need
for x in range(1,100):
    
	newfilename = "READ" + str(x) + "E.md"
	driver.get(URL)
	elem4 = driver.find_element(By.NAME, "filename")
	elem4.send_keys((Keys.BACKSPACE)*9 + newfilename)
	elem4 = driver.find_element(By.ID, "submit-file")
	elem4.send_keys(Keys.RETURN)
	URL = "https://github.com/username/reponame/edit/main/READ" + str(x) + "E.md"


wait = WebDriverWait(driver, 30)

