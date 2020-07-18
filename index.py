# -*- coding: utf-8 -*-

# Importacion de Librerias sistema Operativo
import os
# Importacion librerias para Fecha 
from datetime import date
from datetime import datetime
# Libreria de Errores
import errno



############################################################################################
#Crear Estructura
def CrearEsturctura():
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
############################################################################################

############################################################################################
# Titulo Principal

def TituloPresentacion():
    print('╔══════════════╦══════╦══════════════╗')
    print('║ AGS Server   ║ 1.0  ║ www.Wixan.cl ║')
    print('╚══════════════╩══════╩══════════════╝')
    CrearEsturctura()
############################################################################################

############################################################################################
# Titulo Principal Menu
def TituloMenuPrincipal():
    print('┌─────────────────────────────────────┐')
    print('│ Menu                                │')
    print('├───┬─────────────────────────────────┤')
    print('│1  │ Estados Preliminares            │')
    print('├───┼─────────────────────────────────┤')
    print('│2  │ Actualizacion del Sistema       │')
    print('├───┼─────────────────────────────────┤')
    print('│3  │ Instalacion de Componenetes     │')
    print('├───┼─────────────────────────────────┤')
    print('│4  │ Instalacion de Django           │')
    print('├───┼─────────────────────────────────┤')
    print('│5  │ Crear Log                       │')    
    print('├───┼─────────────────────────────────┤')
    print('│6  │ Salir                           │')
    print('└───┴─────────────────────────────────┘')

############################################################################################

############################################################################################
#Opciones
def Opciones():
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
        CrearLog()   

    if opcion == 6:
        os.system('Exit')       
############################################################################################

############################################################################################
#Estados Preliminares
def EstadosPreliminares():
    os.system('clear')
    print('┌───┬─────────────────────────────────┐')
    print('│1  │ Estados Preliminares            │')
    print('└───┴─────────────────────────────────┘')
    os.system('ls')
    os.system('pwd')
    TituloMenuPrincipal()
    Opciones()
############################################################################################

############################################################################################
#Actualizacion del sistema
def ActualizacionDelSistema():
    os.system('clear')
    print('┌───┬─────────────────────────────────┐')
    print('│2  │ Actualizacion del Sistema       │')
    print('└───┴─────────────────────────────────┘')
    os.system('apt-get update')
    os.system('apt-get upgrade')
    TituloMenuPrincipal()
    Opciones()
 #   os.system('apt-get install hollywood -y')
############################################################################################

############################################################################################
#Intalacion de Componenetes
def InstalacionDeComponentes():
    os.system('clear')
    print('┌───┬─────────────────────────────────┐')
    print('│3  │ Instalacion de Componenetes     │')
    print('└───┴─────────────────────────────────┘')
    os.system('apt-get install nano -y')
    os.system('apt-get install mc -y')
    os.system('apt-get install htop -y')
    os.system('apt-get install bmon -y')
    os.system('apt-get install expect -y')
    os.system('apt-get install pdmenu -y')
    TituloMenuPrincipal()
    Opciones()
 #   os.system('apt-get install hollywood -y')
############################################################################################

############################################################################################
#Intalacion de Componenetes
def InstalacionDeDjango():
    os.system('clear')
    print('┌───┬─────────────────────────────────┐')
    print('│4  │ Instalacion de Django           │')
    print('└───┴─────────────────────────────────┘')
    os.system('apt-get update -y')
    os.system('apt-get upgrade -y')
    os.system('apt-get python-django -y')
    os.system('pip3 install django -y')
    os.system('django-admin startproject terminalweb')
    TituloMenuPrincipal()
    Opciones()
 #   os.system('apt-get install hollywood -y')
############################################################################################


############################################################################################
#Creacion de Un Log
def CrearLog():
    os.system('clear')
    print('┌───┬─────────────────────────────────┐')
    print('│4  │ Crear log                       │')
    print('└───┴─────────────────────────────────┘')
    
    pathlog = 'log/'
    now = datetime.now()
    fecha = now.strftime('%Y-%m-%d_%H-%M-%S')
    archivo = pathlog + fecha + '.txt'
    print(archivo)

    f = open (archivo,'wb')
    f.write('hola mundo')
    f.close()
    
    TituloMenuPrincipal()
    Opciones()
 #   os.system('apt-get install hollywood -y')
############################################################################################




TituloPresentacion()
TituloMenuPrincipal()
Opciones()





