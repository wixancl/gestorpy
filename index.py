# -*- coding: utf-8 -*-

# Importacion de Librerias sistema Operativo
import os
import os.path as path
# Importacion librerias para Fecha 
from datetime import date
from datetime import datetime
# Libreria de Errores
import errno

############################################################################################
# Directorios y Estructura principal

class estructura():
# Directorios	
	def directorios(self):
	    try:
	        os.mkdir('log')
	    except OSError as e:
	        if e.errno != errno.EEXIST:
	            raise

	    try:
	        os.mkdir('backup')
	    except OSError as e:
	        if e.errno != errno.EEXIST:
	            raise

	    try:
	        os.mkdir('inform')
	    except OSError as e:
	        if e.errno != errno.EEXIST:
	            raise

# Crear archivo de configuracion 
	def configuracion(self):
		if path.exists('config.txt'):
			os.system('echo "\e[92m Ya existe un archivo de configuracion \e[0m"')
#		else:
#		    file = open ('config.txt','a')
#		    file.write('------------- Archivo de Configuracion -------------\n')
#	    	file.close()

#Reset Programa
	def reset(self):
	    os.system('clear')
	    os.system('rm -rf config.txt backup/ inform/ log/ terminalweb/')



#Creacion de Un Log
	def log(self,instruccion):    
	    registro = str(instruccion)
	    pathlog = 'log/'
	    now = datetime.now()
	    fecha = now.strftime('%Y-%m-%d_%H-%M-%S')

	    file = open ('log/log.txt','a')
	    file.write(os.linesep)
	    file.write('--------------------------------------------------------------------------------'+ os.linesep)
	    file.write('Fecha ' + fecha + os.linesep)
	    file.write(registro + os.linesep)
	    file.write('--------------------------------------------------------------------------------'+ os.linesep)
	    file.write(os.linesep)
	    file.close()
	   
############################################################################################


############################################################################################
# Crear Titulos y Menus

class Presentacion():
	version = 1
# Presentacion
	def titulo(self):
	    os.system('echo "\e[92m ╔══════════════╦══════╦═════════════════════════════╗ \e[0m"')
	    os.system('echo "\e[92m ║ AGS Server   ║ 1.0  ║ www.Wixan.cl                ║ \e[0m"')
	    os.system('echo "\e[92m ╚══════════════╩══════╩═════════════════════════════╝ \e[0m"')
	    os.system('echo "\e[92m  \e[0m"')   
	    os.system('echo "\e[92m ╔═══════════════════════════════════════════════════╗ \e[0m"')
	    os.system('echo "\e[92m ║ Linux Server                                      ║ \e[0m"')
	    os.system('echo "\e[92m ║                                                   ║ \e[0m"')
	    os.system('echo "\e[92m ║ Julio 2020                                        ║ \e[0m"')
	    os.system('echo "\e[92m ║                                                   ║ \e[0m"')
	    os.system('echo "\e[92m ╚═══════════════════════════════════════════════════╝ \e[0m"')    
#Menu	
	def menu(self):
	    os.system('echo "\e[92m ┌───────────────────────────────────────────────────┐ \e[0m"')
	    os.system('echo "\e[92m │ Menu                                              │ \e[0m"')
	    os.system('echo "\e[92m ├───┬───────────────────────────────────────────────┤ \e[0m"')
	    os.system('echo "\e[92m │1  │ Estados Preliminares                          │ \e[0m"')
	    os.system('echo "\e[92m ├───┼───────────────────────────────────────────────┤ \e[0m"')
	    os.system('echo "\e[92m │2  │ Actualizacion del Sistema                     │ \e[0m"')
	    os.system('echo "\e[92m ├───┼───────────────────────────────────────────────┤ \e[0m"')
	    os.system('echo "\e[92m │3  │ Instalacion de Componenetes                   │ \e[0m"')
	    os.system('echo "\e[92m ├───┼───────────────────────────────────────────────┤ \e[0m"')
	    os.system('echo "\e[92m │4  │ Instalacion de Django                         │ \e[0m"')
	    os.system('echo "\e[92m ├───┼───────────────────────────────────────────────┤ \e[0m"')
	    os.system('echo "\e[92m │5  │ Crear Informe                                 │ \e[0m"')    
	    os.system('echo "\e[92m ├───┼───────────────────────────────────────────────┤ \e[0m"')    
	    os.system('echo "\e[92m │6  │ Reset Programa (Borrar archivos y Directorios)│ \e[0m"')    
	    os.system('echo "\e[92m ├───┼───────────────────────────────────────────────┤ \e[0m"')
	    os.system('echo "\e[92m │7  │ Salir                                         │ \e[0m"')
	    os.system('echo "\e[92m └───┴───────────────────────────────────────────────┘ \e[0m"')   

	    opcion = input("Indique su opcion: ")
		
	    if opcion == 1:
	        EstadosPreliminares()

	    if opcion == 2:
	        ActualizacionDelSistema()

	    if opcion == 3:
	        InstalacionDeComponentes()

	    if opcion == 4:
	        InstalacionDeDjango()

	    if opcion == 5:
	        CrearInforme()   

	    if opcion == 6:
	        ResetPrograma()      

	    if opcion == 7:
	        os.system('exit') 

		 
############################################################################################





############################################################################################
aplicacion = estructura()
grafica = Presentacion()


############################################################################################








############################################################################################
#Estados Preliminares
def EstadosPreliminares():
    os.system('clear')
    os.system('echo "\e[94m ┌───┬─────────────────────────────────┐ \e[0m"')
    os.system('echo "\e[94m │1  │ Estados Preliminares            │ \e[0m"')
    os.system('echo "\e[94m └───┴─────────────────────────────────┘ \e[0m"')
    os.system('echo "\e[93m ls \e[0m"')
    os.system('ls')
    aplicacion.log('ls')
    os.system('echo "\e[93m pwd \e[0m"')
    aplicacion.log('ls')
    os.system('pwd')

############################################################################################

############################################################################################
#Actualizacion del sistema
def ActualizacionDelSistema():
    os.system('clear')
    os.system('echo "\e[94m ┌───┬─────────────────────────────────┐ \e[0m"')
    os.system('echo "\e[94m │2  │ Actualizacion del Sistema       │ \e[0m"')
    os.system('echo "\e[94m └───┴─────────────────────────────────┘ \e[0m"')
    os.system('echo "\e[93m apt-get update \e[0m"')
    os.system('apt-get update')
    os.system('echo "\e[93m apt-get upgrade \e[0m"')
    os.system('apt-get upgrade')


############################################################################################

############################################################################################
#Intalacion de Componenetes
def InstalacionDeComponentes():
    os.system('clear')
    os.system('echo "\e[94m ┌───┬─────────────────────────────────┐ \e[0m"')
    os.system('echo "\e[94m │3  │ Instalacion de Componenetes     │ \e[0m"')
    os.system('echo "\e[94m └───┴─────────────────────────────────┘ \e[0m"')
    os.system('echo "\e[93m apt-get install nano -y \e[0m"')
    os.system('apt-get install nano -y')
    os.system('echo "\e[93m apt-get install mc -y \e[0m"')
    os.system('apt-get install mc -y')
    os.system('echo "\e[93m apt-get install htop -y \e[0m"')
    os.system('apt-get install htop -y')
    os.system('echo "\e[93m apt-get install bmon -y \e[0m"')
    os.system('apt-get install bmon -y')
    os.system('echo "\e[93m apt-get install expect -y \e[0m"')
    os.system('apt-get install expect -y')
    os.system('echo "\e[93m apt-get install pdmenu -y \e[0m"')
    os.system('apt-get install pdmenu -y')
  
 
############################################################################################

############################################################################################
#Intalacion de Componenetes
def InstalacionDeDjango():
    os.system('clear')
    os.system('echo "\e[94m ┌───┬─────────────────────────────────┐ \e[0m"')
    os.system('echo "\e[94m │4  │ Instalacion de Django           │ \e[0m"')
    os.system('echo "\e[94m └───┴─────────────────────────────────┘ \e[0m"')
    os.system('echo "\e[93m apt-get update -y \e[0m"')
    os.system('apt-get update -y')
    os.system('echo "\e[93m apt-get update -y \e[0m"')
    os.system('apt-get upgrade -y')
    os.system('echo "\e[93m apt-get python-django -y \e[0m"')
    os.system('apt-get python-django -y')
    os.system('echo "\e[93m pip3 install django -y \e[0m"')
    os.system('pip3 install django -y')
    os.system('echo "\e[93m django-admin startproject terminalweb \e[0m"')
    os.system('django-admin startproject terminalweb')


############################################################################################


############################################################################################
#Creacion de un Informe
def CrearInforme():
    os.system('clear')
    os.system('echo "\e[94m ┌───┬─────────────────────────────────┐ \e[0m"')
    os.system('echo "\e[94m │5  │ Crear Informe                   │ \e[0m"')
    os.system('echo "\e[94m └───┴─────────────────────────────────┘ \e[0m"')
    
    pathlog = 'inform/'
    now = datetime.now()
    fecha = now.strftime('%Y-%m-%d_%H-%M-%S')
    archivo = pathlog + fecha + '.txt'

    f = open (archivo,'wb')
    f.write('hola mundo')
    f.close()
    
 
############################################################################################


aplicacion.directorios()
aplicacion.configuracion()
aplicacion.log('test')
grafica.titulo()
grafica.menu()





