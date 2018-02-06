#!/usr/bin/python3

file = open('/etc/passwd','r')
info = file.readlines()
  
diccionario = {}	#creo diccionario vacío
for linea in info:
    datos = linea.split(':') #troceo
    usuario = datos[0]
    shell = datos[-1][:-1]		#elimino el \n
    diccionario[usuario] = shell

try:
    usuario = 'root'
    print('El usuario '+ usuario + ' tiene la shell: ' + diccionario[usuario])
    usuario = 'imaginario'
    print('El usuario '+ usuario + ' tiene la shell: ' + diccionario[usuario])

except KeyError:
    print("El usuario '%s' no está en el diccionario." %usuario)

file.close()

