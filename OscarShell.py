#!/usr/python
'''#!/usr/bin/python3 #para Lfs'''
from cmd import Cmd
import os
import time
import sys
import getpass
import Log


class LinuxShell(Cmd):
    prompt= ' (CommonShell)> '
    doc_header=' Comandos de la Shell (escribir help <funcion> o ?<funcion>): '

    funca=getpass.getuser()
    os.system("clear")
    print(funca)
    #veriff=Log.registros(funca)

    #funciona
    def do_exit(self, s):
        '''exit the application.'''
        logg=Log.Log()
        logg.comandos("exit")
        print("Bye")
        return True

    #funciona
    def do_copia(self, s):
        '''Copia lo que esta en archivo1 al archivo2 si no existe crea archivo2: >copia [archivo1] [archivo2]'''
        logg=Log.Log()
        logg.comandos("copia")
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
    #funciona
    def do_mover(self,s):
        '''Mover: >mover [file1] [ubicacion]'''
        logg=Log.Log()
        logg.comandos("mover")
        strin='mv '+ s
        os.system(strin)
        l=s.split()
        msg='\nSe movio el archivo'+' '+l[0]+' a '+l[1]
        print(msg)

    #funciona
    def do_renombrar(self, s):
        '''Renombra: >renombrar [nombre1] [nombre2]'''
        logg=Log.Log()
        logg.comandos("renombrar")
        strin='mv'+ ' '+ s
        os.system(strin)
        l=s.split()
        msg='\nSe cambio el nombre del archivo'+' '+l[0]+' a '+l[1]
        print(msg)

    #funciona
    def do_listdir(self,s):
        '''Lista directorio actual: >listdir'''
        logg=Log.Log()
        logg.comandos("listdir")
        #getcwd directorio actual
        dirs=os.listdir(os.getcwd())
        for archivo in dirs:
            print(archivo,end='\t')
        print('\n')

    #funciona
    def do_creadir(self,s):
        '''Crea un directorio en path indicado si todavia no existe: >creadir [path]'''
        logg=Log.Log()
        logg.comandos("creadir")
        strin='mkdir '+s
        os.system(strin)
    #funciona
    def do_cambiadir(self,s):
        '''Cambia de directorio al dado por el path: >cambiadir [path] '''
        logg=Log.Log()
        logg.comandos("cambiadir")
        os.chdir(s)
    #funciona
    def do_cambiapermiso(self):
        '''Con este comando se puede cambiar permisos de archivos: >cambiapermiso [permisos] [file1] [file2]...'''
        logg=Log.Log()
        logg.comandos("cambiapermiso",)
        l=s.split()
        cantidadArchivos=len(l)
        index=1
        while(index<cantidadArchivos):
            permisoAntes='sudo ls -l'+' |grep '+l[index]
            print("Se intentara cambiar los permisos de "+l[index]+" con los sgtes permisos: "+l[0]+" , verifique el resultado")
            os.system(permisoAntes)
            strin='sudo chmod '+l[0]+' '+l[index]
            os.system(strin)
            print("Ahora\n|||||\nvvvvv")
            os.system(permisoAntes)
            index=index+1
    #funciona
    def do_cambiapropietario(self,s):
        '''Cambia los propietarios sobre un archivo o conjunto de archivos: >cambiapropietario [propietario] [file] [file2] ...'''
        logg=Log.Log()
        logg.comandos("cambiapropietario",s)
        archivos=s.split()
        cantidadArchivos=len(archivos)
        index=1
        while(index<cantidadArchivos):
            comandoChown='sudo chown '+archivos[0]+' '+archivos[index]
            print("Cambiando propietario de "+archivos[index]+"...\n|||| Actual \nvvvv")
            comandoStat='sudo stat -c %U '+archivos[index]
            os.system(comandoStat)
            os.system(comandoChown)
            print("Se ha cambiado...\n||||Luego del cambio\nvvvv")
            os.system(comandoStat)
            index=index+1
    #Funciona
    def do_cambiapassword(self, s):
        '''Cambia contrasenha de usuario: >cambiapassword [usuario]'''
        logg=Log.Log()
        logg.comandos("cambiapassword",s)
        comandoPasswd='sudo passwd '+s
        os.system(comandoPasswd)

    #funciona si agrego el usuario a visudo
    def do_adduser(self,s):
        '''Agrega nuevo usuario,registra los datos personales como horario de trabajo y posibles lugares de conexion en el log /var/log/users: >adduser [usuario]'''
        logg=Log.Log()
        logg.comandos("adduser",s)
        comandoUseradd='sudo useradd -g admin '+s
        #se crea un usuario
        os.system(comandoUseradd)
        #se crea archivo especifico de usuario
        creaFile='/var/log/users/'+s
        archivo=open(creaFile,"w")
        print("Ingrese su horario de trabajo en formato [hhINI]:[mm]-[hhFIN]:[mm] y presione Ctrl+D 2 veces")
        scaner = sys.stdin.read()
        archivo.write(scaner)
        archivo.write('\n')
        print("\nIngrese posibles lugares de conexion como IPs o localhost y presione Ctrl+D 2 veces: ")
        scaner=sys.stdin.read()
        archivo.write(scaner)
        archivo.write('\n')
        archivo.write("\n----------------------------------------\n")
        archivo.write("Horarios de trabajo\tPosibles lugares")
        print("\n")
        archivo.close()

    #funciona
    def do_getcwd(self,s):
        ''' Se obtiene el directorio que se encuentra> getcwd'''
        logg=Log.Log()
        logg.comandos("getcwd")
        current=os.getcwd()
        print(current)

    #def do_demon

    #funciona
    def do_shell(self, s):
        '''Provee la capacidad de poder ejecutar comandos del sistema, que no sean los comandos mencionados: >shell [comandoQueDesee]'''
        logg=Log.Log()
        logg.comandos("shell",s)
        os.system(s)


LinuxShell().cmdloop("..:Bienvenido al Shell del Sistema Linux de Oscar Gonzalez:..")
