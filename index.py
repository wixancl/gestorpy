# -*- coding: utf-8 -*-

# Importacion de Librerias
import os

# Titulo Principal
############################################################################################
def TituloPresentacion():
    print('╔══════════════╦══════╦══════════════╗')
    print('║ AGS Server   ║ 1.0  ║ www.Wixan.cl ║')
    print('╚══════════════╩══════╩══════════════╝')
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
    print('│3  │ Salir                           │')
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
        os.system('exit')
############################################################################################

############################################################################################
#Estados Preliminares
def EstadosPreliminares():
    print('┌───┬─────────────────────────────────┐')
    print('│2  │ Actualizacion del Sistema       │')
    print('└───┴─────────────────────────────────┘')
    os.system('ls')
    os.system('pwd')
    Opciones()
############################################################################################

############################################################################################
#Actualizacion del sistema
def ActualizacionDelSistema():
    print('┌───┬─────────────────────────────────┐')
    print('│2  │ Estados Preliminares            │')
    print('└───┴─────────────────────────────────┘')
    os.system('apt-get update')
    os.system('apt-get upgrade')
    os.system('apt-get install nano -y')
    os.system('apt-get install mc -y')
    os.system('apt-get install htop -y')
    os.system('apt-get install bmon -y')
    os.system('apt-get install pdmenu -y')
    Opciones()
 #   os.system('apt-get install hollywood -y')
############################################################################################




TituloPresentacion()
TituloMenuPrincipal()
Opciones()





