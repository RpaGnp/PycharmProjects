#('Error on line 225', 'TimeoutException', TimeoutException('', None, None))

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
from selenium.webdriver.firefox.service import Service
import time
import csv
import sys
import os
from datetime import date
from datetime import datetime,timedelta



from tkinter import messagebox as m
from tkinter import messagebox



from ..interaccionChrome import Botinteraccion
from ..ModelDataBase import ConectorDbMysql
from .InteraccionesMG import BotMg


from funciones_varias import *
from reloj_casio import *



def SelectorActualizarOts(self,idbot,idAct,Trabajo):	
	driver=self.driver
	BotGestion=BotMg(driver)	
	urlPin ="https://moduloagenda.cable.net.co"
	sql="""
			SELECT dx_nid,dx_corden,dx_caliado,dx_cciudad,dx_dfechaage,dx_cobservacion
			FROM tbl_hagndasdxrx
			WHERE dx_nidbot='"""+str(idAct)+"""' AND  dx_cestgestion='Pendiente';
		"""
	

	for data in ConectorDbMysql().FuncGetInfo(0,sql):		
		#data=dato.split(";")
		try:
			print(data)
			ConectorDbMysql().RepActividad(idbot)
			# funcion de salida, pausa del bot
			Dato = ConectorDbMysql().FunGetProcedure(("SPR_GET_ESTBOTGES", [idbot]))
			# print(Dato[0])
			if Dato[0] != None:
				if Dato[0] == "Eliminar":
					ConectorDbMysql().FuncInsInfoOne(("SPR_UPD_LIBBOT", [idbot, idAct, 'Detenido por usuario']))
					#driver.find_element(by=By.XPATH, value='//*[@data-bind="text: initials"]').click()
					time.sleep(1)					
					driver.quit()
					return
			else:
				pass
			BotGestion.ConsultaOts(urlPin,data[1],data[5])

			# verificar orden agenda pr wfm
			if driver.current_url!='https://moduloagenda.cable.net.co/MGW/MGW/Agendamiento/agendamiento.php':
				sql = ("spr_upd_estgesdx", [data[0], 'Orden no agendada, Redirige a modulo agendamiento antiguo!'])			
				ConectorDbMysql().FuncInsInfoOne(sql)
				continue

			for buttonAccion in driver.find_elements(By.XPATH,'//div[@class="buttons-form"]/input'):
				if buttonAccion.get_attribute("style")=='display: inline-block;':											
					if buttonAccion.get_attribute('value')=="Actualizar":					
						buttonAccion.click()
						element = WebDriverWait(driver, 145).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="dialog_msg_dialog"]')))
						break
			sql = ("spr_upd_estgesdx", [data[0], 'Orden Actualizada con exito'])			
			ConectorDbMysql().FuncInsInfoOne(sql)
			continue
		except:
			sql = ("spr_upd_estgesdx", [data[0], 'Orden NO Actualizada Error'])			
			ConectorDbMysql().FuncInsInfoOne(sql)
			del BotGestion
			driver.quit()
			return
	
	ConectorDbMysql().FuncInsInfoOne(("SPR_UPD_LIBBOT", [idbot, idAct, 'Labor Terminada']))		
	driver.quit()
	