import time
#LIBRERIAS PARA CHROMEDRIVER***********************
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



class Botinteraccion():
	def __init__(self,driver):
		self.driver=driver


	def click(self,Xpath):
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, Xpath)))				
		self.driver.find_element(By.XPATH, value=Xpath).click()
		time.sleep(1)

	def dobleclick(self,ArrayXpath):		
		for i in ArrayXpath:
			WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, i)))				
			self.driver.find_element(By.XPATH, value=i).click()
			time.sleep(1)

	def ClicJs(self,xpathjs):#
		self.driver.execute_script(xpathjs)
		time.sleep(0.25)
		self.driver.execute_script('document.querySelector("#panel").setAttribute("style","display:none")')


	def scrollXpath(self,xpathjs):
		
		script="""
			var element = document.querySelector('"""+xpathjs+"""');
			element.scrollIntoView();
			"""
		self.driver.execute_script(script)

	def sendtext(self,xpath,text):
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))				
		self.driver.find_element(By.XPATH, value=xpath).clear()
		self.driver.find_element(By.XPATH, value=xpath).send_keys(text)
		time.sleep(0.5)		
		return 1


class BotinteraccionMG():
	"""Interaccion de bot con mg"""
	def __init__(self, driver):		
		self.driver = driver

	def Radar(self,xpath):
		return self.driver.find_element(by=By.XPATH,value=xpath)

	def Radares(self,xpath):
		return self.driver.find_elements(by=By.XPATH,value=xpath)

	def ScrollTo(self,xpath):
		element=self.driver.find_element(by=By.XPATH,value=xpath)	
		self.driver.execute_script("arguments[0].scrollIntoView();",element)
	

