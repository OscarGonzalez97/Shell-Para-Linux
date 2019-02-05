import time
class Log():
    def comandos(self, s0):
        try:
            archivo=open("Shell_error_log","a")
            archivo.write(s0)
            fechaHora=time.strftime("%y-%m-%d %H:%M:%S")
            archivo.write(' '+fechaHora+'\n')
            archivo.close()
        except:
            print("No se abrio el archivo")

    def registros(s1):
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
