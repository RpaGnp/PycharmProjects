import pymysql
import platform
import schedule 
import time


class despertador:
	def ring(self):
		__NAMEPC__=platform.node()
		if __NAMEPC__ == "SERVER-1678":
			db_config={'host':'10.206.170.19', 'user':'root', 'password':'AdmCndCal2023*', 'db':'dbcrmgnp'}
		else:
			db_config={'host':'172.19.101.83', 'user':'BotCND', 'password':'1234', 'db':'dbcrmgnp'}


		db = pymysql.connect(host=db_config['host'],user=db_config['user'],password=db_config['password'],db=db_config['db'])

		try:
			with db.cursor() as cursor:
				cursor.execute("SHOW PROCESSLIST;")
				processes = cursor.fetchall()

				for process in processes:
					print(process)
					if process[4] == 'Sleep':# and process[5] > 300:
						cursor.execute(f"KILL {process[0]};")
						
			db.commit()

		finally:
		    db.close()

	def programar(self):
		#schedule.every(15).seconds.do(self.fenix)        
		schedule.every(1).minutes.do(self.ring)
		print("=" * 30, "Mangosta inicio su caceria", "*" * 30)
		#t0=threading.Thread(target=self.lanzador_memoria, daemon=True).start()
		#self.label_estado.config(text="La mangosta inicio su caceria",bg="#cc0000",fg="white")
		while 1:
		    schedule.run_pending()
		    time.sleep(1)

despertador().programar()