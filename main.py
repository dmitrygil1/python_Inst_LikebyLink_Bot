from auth import login, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random

login1 = login
password1 = password

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.instagram.com/');
time.sleep(5) # Let the user actually see something!


login = driver.find_element(By.NAME, "username")
login.send_keys(login1)

time.sleep(random.randrange(1, 2))

password = driver.find_element(By.NAME, "password")
password.send_keys(password1)
time.sleep(random.randrange(1, 2))

password.send_keys(Keys.ENTER)
time.sleep(random.randrange(5, 8))

driver.get(f"https://www.instagram.com/explore/locations/2282981348424659/")

time.sleep(random.randrange(5, 8))

for i in range(1,4):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.randrange(2, 5))

hrefs = driver.find_elements_by_tag_name('a')
urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
print(urls)

for url in urls:
    driver.get(url)
    time.sleep(random.randrange(2, 5))
    like = driver.find_element(By.CSS_SELECTOR, "#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.ltpMr.Slqrh > span.fr66n > button > div.QBdPU.rrUvL > span > svg")
    like.click()
    time.sleep(random.randrange(25, 40))

def close_browser():
    global browser
    browser.close()
    browser.quit()

