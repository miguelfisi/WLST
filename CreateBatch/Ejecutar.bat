@echo off
title ***CREACION DE JMS, COLAS Y DATASOURCE***
color 5e
echo Ingrese el nombre de las siguientes variables
set/p DS_NAME=NOMBRE DE DATASOURCE:
echo.
set/p FS_NAME=NOMBRE DE FILE STORE (PERSITENT STORE):
echo.
set/p JMSServer_Name=NOMBRE DE SERVIDOR JMS:
echo. 
set/p Module_Name=NOMBRE DE MODULO:
echo.
set/p CF_NAME= NOMBRE DE CONNECTION FACTORY:
echo.
set/p Queue_Name= NOMBRE DE LA COLA:
echo.
echo.

echo DATASOURCE:%DS_NAME% 
echo FILE-STORE:%FS_NAME% 
echo SERVIDOR-JMS:%JMSServer_Name%
echo MODULO:%Module_Name%
echo CONNECTION_FACTORY:%CF_NAME%
echo COLA:%Queue_Name%
echo.
echo APRETE CUALQUIER TECLA PARA LA EJECUCION
pause >nul
start /d "C:\Users\synopsis\Desktop\WSLT Creacion Weblogic\Creacion bat" C:\Oracle\Middleware\Oracle_Home\wlserver\common\bin\wlst.cmd Creacion.py  .\args.py %DS_NAME% %FS_NAME% %JMSServer_Name% %Module_Name% %CF_NAME% %Queue_Name%

exit
