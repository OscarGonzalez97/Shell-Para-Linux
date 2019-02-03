#!/usr/bin/env python
from cmd import Cmd
import os
class LinuxShell(Cmd):
    prompt= ' (CommonShell)> '

    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True
    def do_renombrar(self, s):
        strin='mv'+ ' '+ s
        os.system(strin)
        l=s.split()
        msg='\nSe cambio el nombre del archivo'+' '+l[0]+' a '+l[1]
        print(msg)

    def do_shell(self, s):
        os.system(s)

    def help_shell(self):
        print ("execute shell commands")


LinuxShell().cmdloop("..:Bienvenido al Shell del Sistema Linux de Oscar Gonzalez:..")
print("after")
