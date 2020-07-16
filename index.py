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
    print('│3  │ Creacion de los Log             │')
    print('└───┴─────────────────────────────────┘')

############################################################################################

############################################################################################
#Estados Preliminares
def EstadosPreliminares():
    os.system('ls')
    os.system('pwd')
############################################################################################

############################################################################################
#Actualizacion del sistema
def ActualizacionDelSistema():
    os.system('apt-et update')
    os.system('apt-get upgrade')
    os.system('apt-get install nano -y')
    os.system('apt-get install mc -y')
    os.system('apt-get install hollywood -y')
############################################################################################

TituloPresentacion()
TituloMenuPrincipal()
EstadosPreliminares()
opcion = input("Indique su opcion: ")

if opcion == 1:
    EstadosPreliminares()
    
if opcion == 2:
    ActualizacionDelSistema()
