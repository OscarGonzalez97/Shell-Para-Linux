#!/usr/bin/python3
from cmd import Cmd
import os
import time
import sys
import getpass

class LinuxShell(Cmd):
    prompt= ' (CommonShell)> '
    doc_header=' Comandos de la Shell (escribir help <funcion> o ?<funcion>): '
    def registros(s):
        horaActual=time.strftime("%H:%M")
        horaActual=horaActual.split(":")
        print(horaActual[0])
        horaActualInt=int(horaActual[0])
        usuario="/var/log/users/"+"s"
        archivo=open(usuario,"r")
        print(usuario)
        horaTrabajoIni=int(archivo.read(2))
        archivo.read(4)
        horaTrabajoFin=int(archivo.read(2))
        archivo.read(6)
        #Si la persona entro/salio antes de su hora o si la persona entra/sale despues de su hora entonces se escribira en el log
        if(horaActualInt<horaTrabajoIni or horaActualInt>horaTrabajoFin):
            pillado=open("/var/log/personal_horarios_log","a")
            pillado.write("\nUsuario inicio/cerro sesion fuera del rango")
            #pillado.write
            pillado.close()
        else:
            print("Horario correcto amigo")
        lugar=archivo.readline()
        if(lugar!="localhost"):
            pillado=open("/var/log/personal_lugares_log","a")
            pillado.write("\nUsuario no ingreso desde donde registro")
            pillado.close()
        else:
            print("Lugar correcto amigo")

    registros(getpass.getuser())

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
        '''Con este comando se puede cambiar permisos de archivos: >cambiapermiso [permisos] [file1] [file2]...'''
        l=s.split()
        cantidadArchivos=len(l)
        index=1
        while(index<cantidadArchivos):
            permisoAntes='ls -l'+' |grep '+l[index]
            print("Se intentara cambiar los permisos de "+l[index]+" con los sgtes permisos: "+l[0]+" , verifique el resultado")
            os.system(permisoAntes)
            strin='chmod '+l[index]
            os.system(strin)
            print("Ahora\n|||||\nvvvvv")
            os.system(permisoAntes)
            index=index+1

    def do_cambiapropietario(self,s):
        '''Cambia los propietarios sobre un archivo o conjunto de archivos: >cambiapropietario [propietario] [file] [file2] ...'''
        archivos=s.split()
        cantidadArchivos=len(archivos)
        index=1
        while(index<cantidadArchivos):
            comandoChown='chown '+archivos[0]+' '+archivos[index]
            print("Cambiando propietario de "+archivos[index]+"...\n|||| Actual \nvvvv")
            comandoStat='stat -c %U '+archivos[index]
            os.system(comandoStat)
            os.system(comandoChown)
            print("Se ha cambiado...\n||||Luego del cambio\nvvvv")
            os.system(comandoStat)
            index=index+1

    def do_cambiapassword(self, s):
        '''Cambia contrasenha de usuario: >cambiapassword [usuario]'''
        comandoPasswd='passwd '+s
        os.system(comandoPasswd)

    def do_adduser(self,s):
        '''Agrega nuevo usuario,registra los datos personales como horario de trabajo y posibles lugares de conexion en el log /var/log/users: >adduser [usuario]'''
        comandoUseradd='useradd '+s
        #se crea un usuario
        os.system(comandoUseradd)
        #se crea archivo especifico de usuario
        creaFile='/var/log/users/'+s
        archivo=open(creaFile,"w")
        print("Ingrese su horario de trabajo en formato [hhINI]:[mm]-[hhFIN]:[mm] y presione Ctrl+D 2 veces")
        scaner = sys.stdin.read()
        archivo.write(scaner)
        archivo.write('\t\t\t')
        print("\nIngrese posibles lugares de conexion como IPs o localhost y presione Ctrl+D 2 veces: ")
        scaner=sys.stdin.read()
        archivo.write(scaner)
        archivo.write('\n')
        archivo.write("\n----------------------------------------\n")
        archivo.write("Horarios de trabajo\tPosibles lugares")
        print("\n")
        archivo.close()

    #def do_demon

    def do_shell(self, s):
        '''Provee la capacidad de poder ejecutar comandos del sistema, que no sean los comandos mencionados: >shell [comandoQueDesee]'''
        os.system(s)

    '''def registros(s):
        horaActual=time.strftime("%H:%M")
        print(horaActual)
        usuario="/var/log/users/"+"s"
        archivo=open(usuario,"r")
        print(usuario)
        horaTrabajoIni=int(archivo.read(2))
        archivo.read(4)
        horaTrabajoFin=int(archivo.read(2))
        archivo.read(6)
        print(horaActual+' '+horaTrabajoIni+' '+horaTrabajoFin)
        #Si la persona entro/salio antes de su hora o si la persona entra/sale despues de su hora entonces se escribira en el log
        if(horaActual<horaTrabajoIni or horaActual>horaTrabajoFin):
            pillado=open("/var/log/personal_horarios_log","a")
            pillado.write("\nUsuario inicio/cerro sesion fuera del rango")
            #pillado.write
            pillado.close()
        else:
            print("Horario correcto amigo")
        lugar=archivo.readline()
        if(lugar!="localhost"):
            pillado=open("/var/log/personal_lugares_log","a")
            pillado.write("\nUsuario no ingreso desde donde registro")
            pillado.close()
        else:
            print("Lugar correcto amigo")'''

LinuxShell().cmdloop("..:Bienvenido al Shell del Sistema Linux de Oscar Gonzalez:..")
