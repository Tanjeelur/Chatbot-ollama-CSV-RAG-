from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website= 'https://en.wikipedia.org/wiki/Quantum_mechanics'

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(website)
