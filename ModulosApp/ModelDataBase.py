#from ..ModuloCipher.ModuloAes import *.

'''import importlib.util

spec = importlib.util.spec_from_file_location("ModuloAes", "../ModuloCipher/ModuloAes.py")
Encriptador = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Encriptador)
# Para invocar la rutina anteponemos el nombre del módulo
GestorEcrAes=Encriptador.chipherAes()# instancia la clase que esta en otra carpeta

'''
#from .ModuloAes import chipherAes
import pymysql
import mariadb
import datetime
from getpass import getuser
from datetime import date
from datetime import datetime
import platform
import os
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()


# import pymysqlpool
#from .callApi import ConsultorApi

Key=b'4uT0m4t1Z4c10NeS20222022'
__NAMEPC__=platform.node()

# pymysqlpool.logger.setLevel('DEBUG')

class ConectorDbMysql(object):
	"""clase que maneja las tansacciones a mysql"""
	def __init__(self):
		self.conn = False		
		# if __NAMEPC__ == "SERVER-1678":
		# 	db_config={'host':'10.206.170.19', 'user':'BotCndCali', 'password':'B0tCndC4Li24*', 'db':'dbcrmgnp'}
		# else:
		# 	db_config={'host':'190.60.100.100', 'user':'BotCndCen', 'password':'B0tCndC3n24*', 'db':'dbcrmgnp'}

		# Obtener el nombre del PC
		name_pc = os.getenv('NAMEPC')

		# Configurar la base de datos basada en el nombre del PC
		if name_pc == __NAMEPC__:
			db_config = {
				'host': os.getenv('DB_HOST_SERVER'),
				'user': os.getenv('DB_USER_SERVER'),
				'password': os.getenv('DB_PASSWORD_SERVER'),
				'db': os.getenv('DB_NAME_SERVER')
			}
		else:
			db_config = {
				'host': os.getenv('DB_HOST_LOCAL'),
				'user': os.getenv('DB_USER_LOCAL'),
				'password': os.getenv('DB_PASSWORD_LOCAL'),
				'db': os.getenv('DB_NAME_LOCAL')
			}

		x=0
		while x<5:
			try:
				self.conn = pymysql.connect(host=db_config['host'],user=db_config['user'],password=db_config['password'],db=db_config['db'],connect_timeout=60)
				break
			except Exception as e:
				print("error conexion ",e)
				x+=1

	'''def get_connection(self):		
		return self.db_pool.get_connection()'''

	def GetConn(self):
		return self.conn	

	def timer(self):
		FechaHora = datetime.now()	
		date_actual=FechaHora.strftime('%d/%m/%Y %H:%M:%S')
		Fecha = FechaHora.strftime('%d/%m/%Y')
		Hora = FechaHora.strftime('%H:%M:%S')
		fecha = str(Fecha)
		hora = str(Hora)
		return fecha, hora, date_actual,Fecha,Hora
	
	def GetQueryPars(self,sql):		
		cursor=self.conn.cursor()
		cursor.callproc(sql[0],args=(sql[1]))
		self.conn.commit()
		Consulta=cursor.fetchone()
		cursor.close()
		self.conn.close()
		return Consulta

	def FuncGetInfoOne(self,TipoData,Consulta,Parametros):
		"""tipo data: 1 fechone, 0 fechall"""
		if Parametros==None:
			pass
		with self.conn.cursor() as cursor:
			cursor.callproc(Consulta,args=(Parametros))
			if TipoData==1:
				data=cursor.fetchone()
			else:
				data=cursor.fetchall()
		cursor.close()
		self.conn.close()
		return data

	def FuncGetInfo(self,TipoData,sql):		
		with self.conn.cursor() as cursor:					
			cursor.execute(sql)
			if TipoData==1:
				data=cursor.fetchone()
			else:
				data=cursor.fetchall()
		cursor.close()
		self.conn.close()
		return data

	def FuncInsInfoOne(self,Consulta):				
		try:		
			with self.conn.cursor() as cursor:
				cursor.callproc(Consulta[0],args=(Consulta[1]))
				self.conn.commit()
			cursor.close()
			self.conn.close()
		except Exception as e:
			print(e)

	def FunGetProcedure(self,sql):
		with self.conn.cursor() as cursor:
			cursor.callproc(sql[0],args=(sql[1]))
			data=cursor.fetchone()
		cursor.close()
		self.conn.close()
		return data

	def RepActividad(self,Idbot):
		try:
			with self.conn.cursor() as cursor:
				cursor.callproc("SPR_UPD_TIMBOT",args=([Idbot]))
				self.conn.commit()
			cursor.close()
			self.conn.close()
		except Exception as e:
			print(e)


	def FuncGetSpr(self,tipo,procedimiento,Arraydatos=[]):
		data=[]
		with self.conn.cursor() as cursor:
			if len(Arraydatos)!=0:
				cursor.callproc(procedimiento,args=(Arraydatos))
			else:
				cursor.callproc(procedimiento)
			if tipo==1:
				data=cursor.fetchone()
			else:
				data=cursor.fetchall()
		self.conn.close()
		return data

	def FuncGetUpdSpr(self,tipo,procedimiento,Arraydatos=[]):
		data=[]
		with self.conn.cursor() as cursor:
			if len(Arraydatos)!=0:
				cursor.callproc(procedimiento,args=(Arraydatos))
			else:
				cursor.callproc(procedimiento)
				
			self.conn.commit()
			
			if tipo==1:
				data=cursor.fetchone()
			else:
				data=cursor.fetchall()
		self.conn.close()
		return data

	def FuncUpdSpr(self,procedimiento,Arraydatos=[]):
		data=[]
		with self.conn.cursor() as cursor:
			if len(Arraydatos)!=0:
				cursor.callproc(procedimiento,args=(Arraydatos))
			else:
				cursor.callproc(procedimiento)
		self.conn.commit()
		
		return True


