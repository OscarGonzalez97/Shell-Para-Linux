#!/usr/bin/python3
from cmd import Cmd
import os
import time
class LinuxShell(Cmd):
    prompt= ' (CommonShell)> '
    doc_header=' Comandos de la Shell (escribir help <funcion> o ?<funcion>): '

    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True

    def do_copia(self, s):
        '''Copia lo que esta en archivo1 al archivo2 si no existe crea archivo2: >copia [archivo1] [archivo2]'''
        archivo=s.split()
        try:
            fileCat=open(archivo[0], "r")
            fileTarget=open(archivo[1],"w")
            fileTarget.write(fileCat.read())
            print("Se copio el contenido de "+archivo[0]+" al "+archivo[1])
            fileTarget.close()
            fileCat.close()
        except:
            print("El archivo "+archivo[0]+" no se pudo abrir o no existe")

    def do_mover(self,s):
        '''Mover: >mover [file1] [ubicacion]'''
        strin='mv '+ s
        os.system(strin)
        l=s.split()
        msg='\nSe movio el archivo'+' '+l[0]+' a '+l[1]
        print(msg)

    def do_renombrar(self, s):
        '''Renombra: >renombrar [nombre1] [nombre2]'''
        strin='mv'+ ' '+ s
        os.system(strin)
        l=s.split()
        msg='\nSe cambio el nombre del archivo'+' '+l[0]+' a '+l[1]
        print(msg)

    #def do_listdir(self,s):
    #'''Lista directorio: >listdir'''

    def do_creadir(self,s):
        '''Crea un directorio en path indicado si todavia no existe: >creadir [path]'''
        strin='mkdir '+s
        os.system(strin)

    #def do_cambiadir(self,s)
    #'''Cambia de directorio al dado por el path: >cambiadir [path]  '''

    def do_cambiapermiso(self,s):
        '''Con este comando se puede cambiar permisos de archivos: >cambiapermiso [permisos] [file]'''
        l=s.split()
        permisoAntes='ls -l'+' |grep '+l[1]
        print("Se cambiaron los permisos de "+l[1]+" con los sgtes permisos: "+l[0])
        os.system(permisoAntes)
        strin='chmod '+s
        os.system(strin)
        print("Ahora\n|||||\nvvvvv")
        os.system(permisoAntes)

    def do_cambiapropietario(self,s):
        '''Cambia los propietarios sobre un archivo o conjunto de archivos: >cambiapropietario [propietario] [file] [file2] ...'''
        #Si tiene el comando stat hare esto
        argumento=s.split()

        print("Cambiando propietario...\n|||| Actual \nvvvv")
        i=1
        """while(argumento[i]):"""
        comandoStat='stat -c %U '+argumento[i]
        os.system(comandoStat)
        comandoChown='chown '+argumento[0]+' '+argumento[i]
        os.system(comandoChown)
            #i=i+1
            #print(argumento[i])
        print("Se ha cambiado...\n||||Ahora\nvvvv")
        i=1
        #while(argumento[i]):
        comandoStat='stat -c %U '+argumento[i]
        os.system(comandoStat)
            #i=i+1
            #print(argumento[i])


    def do_shell(self, s):
        '''Provee la capacidad de poder ejecutar comandos del sistema, que no sean los comandos mencionados: >shell [comandoQueDesee]'''
        os.system(s)


LinuxShell().cmdloop("..:Bienvenido al Shell del Sistema Linux de Oscar Gonzalez:..")
