from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,)
driver.get("https://www.uanl.mx/enlinea/")

loginbox = driver.find_element(By.NAME, "loginbox")
driver.switch_to.frame(loginbox)
user = input("Matricula:")
password = input("PASS: ")

html_user_login = driver.find_element(By.ID, "cuenta")
html_user_password = driver.find_element(By.ID, "pass")
html_user_login.send_keys(user)
html_user_password.send_keys(password)
button = driver.find_element(By.XPATH, "//button[contains(text(),'Entrar')]")
button.click()
time.sleep(2)
driver.switch_to.default_content()
nexus = driver.find_element(By.CSS_SELECTOR, "img[src='https://deimos.dgi.uanl.mx/uanlimg/ws/nexus_btn.jpg']")
nexus.click()
nexus = driver.find_element(By.NAME, "btnNexus")
nexus.click()
input("listening")
#cuenta id name htmlusucve input type text
#id pass name htmlPassword type password