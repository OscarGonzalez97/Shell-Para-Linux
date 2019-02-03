#!/usr/bin/python3
from cmd import Cmd
import os
class LinuxShell(Cmd):
    prompt= ' (CommonShell)> '

    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True
    def do_renombrar(self, s):
        '''Renombra: >renombrar [nombre1] [nombre2]'''
        strin='mv'+ ' '+ s
        os.system(strin)
        l=s.split()
        msg='\nSe cambio el nombre del archivo'+' '+l[0]+' a '+l[1]
        print(msg)
    def do_mover(self,s):
        '''Mover: >mueve [file1] [ubicacion]'''
        strin='mv '+ s
        os.system(strin)
        l=s.split()
        msg='\nSe movio el archivo'+' '+l[0]+' a '+l[1]
        print(msg)
    def do_cambiapermiso(self,s):
        '''Con este comando se puede cambiar permisos de archivos'''
        l=s.split()
        permisoAntes='ls -l'+' |grep '+l[1]
        print("Se cambiaron los permisos de "+l[1]+" con los sgtes permisos: "+l[0])
        os.system(permisoAntes)
        strin='chmod '+s
        os.system(strin)
        print("Ahora\n|||||\nvvvvv")
        os.system(permisoAntes)

    def do_shell(self, s):
        os.system(s)

    def help_shell(self):
        print ("execute shell commands")


LinuxShell().cmdloop("..:Bienvenido al Shell del Sistema Linux de Oscar Gonzalez:..")
print("after")
