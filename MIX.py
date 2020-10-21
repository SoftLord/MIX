import math as mt
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk # importamos la libreria especifica para crear los "combobox", menus desplegables. Y más, una especie de tk, pero no tan "compleja"
from tkinter import font
from tkinter import filedialog
import os #importamos la libreria que utlizaremos para encontar la ruta de los archivos
from os import remove
import pygame
import numpy as np
import matplotlib.pyplot as plt
import engine

pygame.mixer.init() #iniciamos pygame

del_user = []
user_txt=""
punto=""

ruta_mix = os.getcwd() + "/icons/MIX.ico" #con gtcwd encontramos la ruta del archivo qu se esta ejecutando, y le añadimos la carpeta para llegar a lo siconos o al material necesario.
ruta_mix_logo = os.getcwd() + "/icons/MIX.gif"
ruta_acerca_de =  os.getcwd() + "/icons/acerca_de.ico"
ruta_nuevo_user =  os.getcwd() + "/icons/nuevo_user.ico"
ruta_delete_user = os.getcwd() + "/icons/delete_user.ico"
ruta_engine = os.getcwd() + "/data/engine/engine.txt"
ruta_audio = os.getcwd() + "/data/audio/default audio.wav"
ruta_imagen_play = os.getcwd() + "/icons/play-button.png"
ruta_imagen_stop = os.getcwd() + "/icons/stop.png"
ruta_imagen_playPause = os.getcwd() + "/icons/playPause.png"
ruta_archivo_playpause = os.getcwd() + "/data/engine/playpause.txt"

#-----------------------DEFINIENDO FUNCIONES------------------------------------#

def comprobar():

    fichero = open(ruta_engine, "r+") #definimos que fichero va a ser abrir el fichero de users pepe
    linea = fichero.readline() #leemos la primera linea
    linea=linea[0:len(linea)-1] #solo queremos toda la distancia menos la ultim posición porque el ultimo caracter es el intro.
    print(usuario) #opcional

    global user
    global nombre_usuario 
    nombre_usuario = usuario.get()
    user = engine.encriptBas(usuario.get())

    print(user)
    print(engine.encriptBas(password.get()))

    while linea.lower() != user.lower(): #esto sive para comprobar si el usuario existe, ara el bucle hasta encontrarse con los dos ateriscos, el final del documento.
        #la funcion .lower() lo que hacer es pasar todo el texto a minusculas para que no te de un problema de minusculas y mayusculas en el usuario al registrarte

        linea = fichero.readline()
        linea = fichero.readline()
        linea = fichero.readline()
        linea = linea[0:len(linea)-1]

        if linea == "**":

            break

    if linea != "**":
        linea = fichero.readline()
        linea = linea[0:len(linea)-1]

        if engine.encriptBas(password.get()) == linea:
            fichero.close() #importante cerrar el documeto
            abrirsegundaventana()

        else:
            messagebox.showwarning("Advertencia","Usuario y/o ontraseña incorrecto")

    elif password.get() == "" or usuario.get() == "":

            messagebox.showwarning("Advertencia","Introduzca usuario y/o contraseña")

    else:
        messagebox.showwarning("Advertencia","Usuario y/o ontraseña incorrecto")


def comprobar2(object): #con el object hacemos que al pulsar enter, nos loguee

    fichero = open(ruta_engine, "r+") #definimos que fichero va a ser abrir el fichero de users pepe
    linea = fichero.readline() #leemos la primera linea
    linea=linea[0:len(linea)-1] #solo queremos toda la distancia menos la ultim posición porque el ultimo caracter es el intro.
    print(usuario) #opcional

    global user
    global nombre_usuario
    nombre_usuario = usuario.get()
    user = engine.encriptBas(usuario.get())

    while linea.lower() != user.lower(): #esto sive para comprobar si el usuario existe, ara el bucle hasta encontrarse con los dos ateriscos, el final del documento.

        linea = fichero.readline()
        linea = fichero.readline()
        linea = fichero.readline()
        linea = linea[0:len(linea)-1]

        if linea == "**":

            break

    if linea != "**":

        linea = fichero.readline()
        linea = linea[0:len(linea)-1]

        if engine.encriptBas(password.get()) == linea:

            fichero.close() #importante cerrar el documeto
            abrirsegundaventana()

        else:

            messagebox.showwarning("Advertencia","Usuario y/o ontraseña incorrecto")

    elif password.get() == "" or usuario.get() == "":

        messagebox.showwarning("Advertencia", "Introduzca usuario y/o contraseña")

    else:
        messagebox.showwarning("Advertencia","Usuario y/o ontraseña incorrecto")

#----------------CREAR USUARIOS NUEVOS Y ELIMINAR ANTIGUOS------------#

def crear_usuario():

    def comprobar_password():

        fichero = open(ruta_engine, "r+")
        linea = fichero.readline()
        linea = linea[0:len(linea)-1]

        while engine.encriptBas(nuevo_usuario.get()) != linea:

            linea = fichero.readline()
            linea = fichero.readline()
            linea = fichero.readline()
            linea = linea[0:len(linea) - 1]

            if linea == "":
                break

        if engine.encriptBas(nuevo_usuario.get()) == linea:

            if nuevo_usuario.get() == "":
                messagebox.showerror("Error","Ingrese un usuario")

            else:
                messagebox.showwarning("Advertencia","El usuario deseado ya existe.\n Ingrese uno diferente")

        else:

            if nuevo_usuario.get() == "":
                messagebox.showerror("Error","Ingrese un usuario")

            else:

                if nuevo_password.get() == confirmar_password.get():

                    if nuevo_password.get() == "":
                        messagebox.showwarning("Advertencia","Ingrese un password")

                    else:
                        fichero = open(ruta_engine,"r+")
                        linea=fichero.readlines()
                        print(linea)
                        del(linea[-1])
                        linea.append(engine.encriptBas(nuevo_usuario.get())+"\n")
                        linea.append(engine.encriptBas(nuevo_password.get())+"\n")
                        linea.append("*\n")
                        linea.append("**\n")
                        txt="".join(linea)
                        print(txt)
                        txt=str(txt)
                        fichero=open(ruta_engine,"w")
                        fichero.write(txt)
                        fichero.close()
                        ventana_crear_usuario.withdraw()
                        messagebox.showinfo("completado","Usuario y contraseña registrados correctamente")


                else:
                    messagebox.showerror("Error","Las contraseñas no coinciden")

    def comprobar_password2(object):

        fichero = open(ruta_engine, "r+")
        linea = fichero.readline()
        linea = linea[0:len(linea)-1]

        while engine.encriptBas(nuevo_usuario.get()) != linea:

            linea = fichero.readline()
            linea = fichero.readline()
            linea = fichero.readline()
            linea = linea[0:len(linea) - 1]

            if linea == "":
                break

        if engine.encriptBas(nuevo_usuario.get()) == linea:

            if nuevo_usuario.get() == "":
                messagebox.showerror("Error","Ingrese un usuario")

            else:
                messagebox.showwarning("Advertencia","El usuario deseado ya existe.\n Ingrese uno diferente")

        else:

            if nuevo_usuario.get() == "":
                messagebox.showerror("Error","Ingrese un usuario")

            else:

                if nuevo_password.get() == confirmar_password.get():

                    if nuevo_password.get() == "":
                        messagebox.showwarning("Advertencia","Ingrese un password")

                    else:
                        fichero = open(ruta_engine,"r+")
                        linea=fichero.readlines()
                        print(linea)
                        del(linea[-1])
                        linea.append(engine.encriptBas(nuevo_usuario.get())+"\n")
                        linea.append(engine.encriptBas(nuevo_password.get())+"\n")
                        linea.append("*\n")
                        linea.append("**\n")
                        txt="".join(linea)
                        print(txt)
                        txt=str(txt)
                        fichero=open(ruta_engine,"w")
                        fichero.write(txt)
                        fichero.close()
                        ventana_crear_usuario.withdraw()
                        messagebox.showinfo("completado","Usuario y contraseña registrados correctamente")


                else:
                    messagebox.showerror("Error","Las contraseñas no coinciden")

    ventana_crear_usuario = tk.Toplevel(ventana)
    ventana_crear_usuario.title("Nuevo Usuario")
    ventana_crear_usuario.geometry("280x150")
    ventana_crear_usuario.configure(bg="gray40")
    ventana_crear_usuario.resizable(0,0)
    ventana_crear_usuario.iconbitmap(ruta_nuevo_user)
    ventana_crear_usuario.transient(ventana) #hacemos que la ventana quede encima de la ventana root (ventana)

    def confirmar_cancelar():

        if messagebox.askyesno('Verificar', '¿Está seguro de que quiere cancelar el registro?'):
            ventana_crear_usuario.destroy()

    espacio=Label(ventana_crear_usuario, text=" ", bg="gray40")
    espacio.grid(row=0)

    texto_crear_usuario = tk.Label(ventana_crear_usuario, text="  Usuario:   ", bg="gray40", fg="white")
    texto_crear_usuario.grid(row=1, sticky=E)

    texto_crear_password = tk.Label(ventana_crear_usuario, text="  Contraseña:   ", bg="gray40", fg="white")
    texto_crear_password.grid(row=2, sticky=E)

    nuevo_usuario = ttk.Entry(ventana_crear_usuario)
    nuevo_usuario.grid(row=1, column=1, sticky=E)

    nuevo_password = ttk.Entry(ventana_crear_usuario, show="•")
    nuevo_password.grid(row=2, column=1, sticky=E)

    texto_confirmar_password = tk.Label(ventana_crear_usuario, text="  Confirmar contraseña:   ", bg="gray40", fg="white", borderwidth=0, relief="solid")
    texto_confirmar_password.grid(row=3, sticky=E)

    confirmar_password = ttk.Entry(ventana_crear_usuario, show="•")
    confirmar_password.grid(row=3, column=1, sticky=E)

    Registrarse=Button(ventana_crear_usuario, text="Registrarse", bg="white", borderwidth=0, relief ="solid", cursor="hand2", command=comprobar_password)
    Registrarse.grid(row=4, pady=20)

    cancelar=Button(ventana_crear_usuario, text="Cancelar", bg="white", borderwidth=0, relief="solid", cursor="hand2", command=confirmar_cancelar)
    cancelar.grid(row=4, column=1)

    ventana_crear_usuario.bind("<Return>", comprobar_password2)



def delete_user():

    ventana_eliminar_usuario = tk.Toplevel(ventana)
    ventana_eliminar_usuario.title("Eliminar Usuario")
    ventana_eliminar_usuario.geometry("300x120")
    ventana_eliminar_usuario.configure(bg="gray40")
    ventana_eliminar_usuario.resizable(0, 0)
    ventana_eliminar_usuario.iconbitmap(ruta_delete_user)
    ventana_eliminar_usuario.transient(ventana)

    def eliminar_usuario():

        fichero = open(ruta_engine, "r+")
        linea = fichero.readline()
        linea = linea[0:len(linea) - 1]

        while linea != engine.encriptBas(usuario_por_eliminar.get()):

            linea = fichero.readline()
            linea = fichero.readline()
            linea = fichero.readline()
            linea = linea[0:len(linea) - 1]

            if linea == engine.encriptBas(usuario_por_eliminar.get()):

                user_txt=engine.encriptBas(str(usuario_por_eliminar.get()))
                print(user_txt)

                break

            if linea == "":

                break

        def password_eliminar_user():

            print(linea)

            if engine.encriptBas(confirmar_password_user_por_eliminar.get()) == punto:

                if confirmar_password_user_por_eliminar.get() == "":

                    messagebox.showerror("Error","Introduzca la contraseña")

                else:

                    if messagebox.askyesno('Verificar', '¿Está seguro de que quiere eliminar el usuario?'):

                        fichero = open(ruta_engine,"r+")
                        lista = fichero.readlines()
                        posicion_contra_user=lista.index(user_txt+"\n") #cogemos la posicion que ocupa la contr en la lista
                        print(lista)
                        lista.remove(user_txt+"\n") #y ahora eliminamos el usuario
                        lista.remove(engine.encriptBas(confirmar_password_user_por_eliminar.get())+"\n") #eliminamos el password
                        del lista[posicion_contra_user] #y eliminamos la antigua posicion de la contraseña, que ahora es ocupada por el *
                        print(lista)
                        txt = "".join(lista)
                        fichero = open(ruta_engine,"w")
                        fichero.write(txt)
                        fichero.close()
                        confirmar_contra_user_por_eliminar.destroy()

            else:

                messagebox.showwarning("Contraseña incorrecta","Contraseña de usuario incorrecta")

        if linea == engine.encriptBas(usuario_por_eliminar.get()):

            if usuario_por_eliminar.get() == "":

                messagebox.showerror("Error","Usuario no encontrado")

            else:

                user_txt = engine.encriptBas(str(usuario_por_eliminar.get()))
                print(user_txt)

                linea = fichero.readline()
                linea = linea[0:len(linea) -1]
                punto = linea

                ventana_eliminar_usuario.destroy()
                confirmar_contra_user_por_eliminar = tk.Toplevel()
                confirmar_contra_user_por_eliminar.transient(ventana)
                confirmar_contra_user_por_eliminar.title("Confirmar contraseña")
                confirmar_contra_user_por_eliminar.geometry("300x120")
                confirmar_contra_user_por_eliminar.configure(bg="gray40")
                confirmar_contra_user_por_eliminar.resizable(0, 0)
                confirmar_contra_user_por_eliminar.iconbitmap(ruta_delete_user)

                confirmar_password_txt = Label(confirmar_contra_user_por_eliminar, text= "Confirmar contraseña:", bg="gray40", fg="white")
                confirmar_password_txt.pack()

                confirmar_password_user_por_eliminar = ttk.Entry(confirmar_contra_user_por_eliminar, show="•")
                confirmar_password_user_por_eliminar.pack(pady = 10)

                aceptar_delete_user = tk.Button(confirmar_contra_user_por_eliminar, text="Aceptar", bg="white", fg="black", borderwidth=0, relief="solid", cursor="hand2", command=password_eliminar_user)
                aceptar_delete_user.pack(pady=10)

        else:
            messagebox.showwarning("usuario no encontrado","El usuario deseado no existe")


    usuario_a_eliminar = Label(ventana_eliminar_usuario, text="Usuario a eliminar: ", bg="gray40", fg="white")
    usuario_a_eliminar.pack(pady=10)

    usuario_por_eliminar = ttk.Entry(ventana_eliminar_usuario)
    usuario_por_eliminar.pack(pady=7)

    eliminar_usuario = tk.Button(ventana_eliminar_usuario, text="Aceptar",bg="white", fg="black", borderwidth=0, relief="solid", cursor="hand2", command=eliminar_usuario)
    eliminar_usuario.pack()



#---------ABRIR VENTANA PRINCIPAL---------------------#

def abrirsegundaventana():

    ventana.destroy()
    ventana2 = tk.Tk()
    ventana2.title("MIX of " + nombre_usuario)
    ventana2.config(bg="gray40")
    ventana2.state('zoomed') #asi hacemos que la ventana aparezca maximizada
    ventana2.geometry("1000x850")
    ventana2.minsize(1000,850) #establecemos un tamaño minimo para la ventana
    ventana2.iconbitmap(ruta_mix)

    def guardar():

        romperBucle = False

        while romperBucle == False:

            fichero=open(filedialog.asksaveasfilename(title = "Save file",initialfile = "guardado.txt", filetypes = (("Text files","*.txt"),("all files","*.*"))),"w")
            ruta = str(fichero)
            ruta = ruta[0:len(ruta)-29]
            if ruta[0:len(ruta)-3] + "txt" == ruta: 
                fichero.write(guardar_texto)
                print(guardar_texto)
                fichero.close()
                romperBucle = True
            else:
                if messagebox.askyesno('Cambiar archivo','¿Está seguro de que quiere cambiar la extensión?\nEs posible que no pueda abrir el archivo después.'):
                    fichero.write(guardar_texto)
                    fichero.close()
                    romperBucle = True
                else:
                    ruta = ruta[25:len(ruta)]
                    fichero.close()
                    os.remove(ruta)
                    romperBucle = False


    def salir():

        if messagebox.askyesno('Salir','¿Está seguro de que quiere salir?'): #asi se pone una ventana de confirmacion y que en caso de aceptar cierra la ventana
            ventana2.destroy()

    def informacion_adicional():

        informacion_adicional= tk.Toplevel()
        informacion_adicional.title("Acerca de")
        informacion_adicional.geometry("500x300")
        informacion_adicional.resizable(0,0)
        informacion_adicional.config(bg="gray40")
        informacion_adicional.iconbitmap(ruta_acerca_de)
        fuente_texto_info = font.Font(size=50,font="gotham") #creamos unj tipo de fuente donde la letra es mas grande, pero se pueden cambiar muchosos parámetros
        fuente_texto_info2 = font.Font(size=10)

        texto_info = Label (informacion_adicional, text= "Hecho por Mixed Soft™, Inc.\n ©2018-2019", bg="gray40", fg="white", font=fuente_texto_info) #aqui usamos el tipo de funte que hemos creado antes
        texto_info.place(x=130, y=150)

        texto_info2 = Label(informacion_adicional, text = "MIX", bg="gray40", fg="white", font=fuente_texto_info)
        texto_info2.place(x=150, y=64)

        texto_info3 = Label(informacion_adicional, text="Versión 2.0", bg="gray40", fg="white", font=fuente_texto_info2)
        texto_info3.place(x=220, y=67)

        logo = PhotoImage(file=ruta_mix_logo)

        imgLogo = Label(informacion_adicional, image=logo, width=85, height=28)
        imgLogo.place(x=30, y=58)

        informacion_adicional.mainloop()

    def opcion_del_desplegable_seleccionada():

        def fibonacci(cantidad):

            global guardar_texto # la definimos como global para poder utilizarla fuera de la funcion
            guardar_texto = ""

            separador = ""
            separador=str(separador)

            while (True):

                try:

                    listbox.delete(0, tk.END) #borramos todos los elementos de la posicion 0 a la final de la listbox
                    a = 1
                    b = 1

                    if cantidad <= 0:

                        listbox.insert(tk.END,"No hay valores")

                        break

                    elif cantidad == 1:

                        listbox.insert(tk.END,a) #añadimos a la listbox
                        a = str(a)
                        guardar_texto = a
                        archivos_menu.entryconfig(index="Guardar", state="normal")

                        break

                    elif cantidad == 2:

                        listbox.insert(tk.END,a,b)
                        a = str(a)
                        b= str(b)
                        guardar_texto = a + "\n" + b
                        archivos_menu.entryconfig(index="Guardar", state="normal")

                        break

                    elif cantidad > 2:

                        if cantidad >= 5000:    #ponemos un limite por si se satura demasiado el programa
                            messagebox.showinfo("Imposible","No es posible calcular tantos numeros")

                            break

                        listbox.insert(tk.END,a,separador, b, separador)
                        a = str(a)
                        b = str(b)
                        guardar_texto = a + "\n" + b + "\n"
                        a = int(a)
                        b = int(b)

                        for i in range(cantidad - 2): #-2 ya que hemos mostrado a y b anteriormente

                            c = a + b
                            c = str(c)
                            listbox.insert(END, c, separador)
                            guardar_texto = guardar_texto + c + "\n"
                            c = int(c)
                            a = b
                            b = c

                        archivos_menu.entryconfig(index="Guardar", state="normal") #habilitamos el boton de guardar

                        break

                except:

                    print("no")
                    messagebox.showerror("Error","Se ha producido un error inesperado, comprube que los datos estén bien escritos")

                    break


        def primos(cantidad):

            SePuedeHacer = False
            numero = 1
            global guardar_texto
            guardar_texto = ""
            listbox.delete(0, tk.END)
            veces = 0

            while not SePuedeHacer:

                if cantidad > 10000:
                    messagebox.showinfo("Imposible","No es posible calcular tantos numeros")
                    SePuedeHacer = True
                    break

                elif cantidad == 1 or cantidad == 2 or cantidad == 3:
                    archivos_menu.entryconfig(index="Guardar", state="normal")
                    SePuedeHacer = True

                try:

                    if cantidad <= 0:
                        listbox.insert(tk.END,"No hay valores")
                        archivos_menu.entryconfig(index="Guardar", state="normal")
                        SePuedeHacer = True

                    while veces < int(cantidad):


                        esprimo = True
                        divisor = 2

                        for i in range(int(mt.sqrt(numero))):  # basta que lo hagamos hasta la parte enterra de la raiz del numero deseado

                            if numero % divisor == 0:

                                if numero == 2:
                                    esprimo = True
                                    break

                                esprimo = False
                                archivos_menu.entryconfig(index="Guardar", state="normal")
                                SePuedeHacer = True #rompemos el bucle

                            divisor = divisor + 1

                        if esprimo == True:
                            listbox.insert(tk.END, str(numero))
                            listbox.insert(tk.END, "")
                            guardar_texto = guardar_texto + str(numero) + "\n"
                            veces = veces + 1

                        numero = numero + 1

                except:
                    messagebox.showerror("Error","Se ha producido un error inesperado, comprube que los datos estén bien escritos")
                    archivos_menu.entryconfig(index="Guardar", state="normal")
                    SePuedeHacer = True

        def fact(numero_a_factorizar):

            listbox.delete(0, tk.END)
            global guardar_texto
            guardar_texto = "1, "

            try:
            
                if numero_a_factorizar <= 0:
                    listbox.insert(tk.END, "No hay valores")
            
                else:

                    listbox.insert(tk.END, "1")
                    listbox.insert(tk.END, "")

                    for i in range (2, numero_a_factorizar+1): #ponemos 2 para que no coja el 0 como primer valor y de un fallo a la hora de dividir, y tampoco 1 porque se
                    #quedaria infinitamente en el bucle. Tambien le sumamos uno porue lo hace hasta el anteriror.

                        if numero_a_factorizar > 10000000: #(10.000.000)
                            messagebox.showinfo("Imposible","No es posible factorizar un número tan grande")
                            break
                    
                        while (numero_a_factorizar % i == 0):
                            numero_a_factorizar = numero_a_factorizar/i
                            listbox.insert(tk.END, str(i))
                            guardar_texto = guardar_texto + str(i) + ", "
                            listbox.insert(tk.END, "")
                            archivos_menu.entryconfig(index="Guardar", state="normal")

            except:
                messagebox.showerror("Error","Se ha producido un error inesperado, comprube que los datos estén bien escritos")
                archivos_menu.entryconfig(index="Guardar", state="normal")

            print(guardar_texto)

        def graficar():

            archivos_menu.entryconfig(index="Guardar", state="disabled")

            def senos():
                try:
                    frec = cantidad_frecuencia.get()
                    frec = int(frec)

                    datos = np.arange(0,frec)

                    if desplegable_unidades.get() == "Radianes":
                        datos = np.radians(datos)

                    datos = np.sin(datos)

                    if desplegable_colores.get() == "Azul":
                        plt.plot(datos,"b--")
                    elif desplegable_colores.get() == "Rojo":
                        plt.plot(datos,"r--")
                    elif desplegable_colores.get() == "Amarillo":
                        plt.plot(datos,"y--")
                    elif desplegable_colores.get() == "Verde":
                        plt.plot(datos,"g--")
                    elif desplegable_colores.get() == "Negro":
                        plt.plot(datos,"k--")

                    plt.show()

                except:
                    messagebox.showerror("Error","Introduzca un valor válido para la frecuencia.\nSi está utilizando radianes, pruebe a poner datos mayores a 250.")

            def cosenos():
                try:
                    frec = cantidad_frecuencia.get()
                    frec = int(frec)

                    datos = np.arange(0,frec)

                    if desplegable_unidades.get() == "Radianes":
                        datos = np.radians(datos)

                    datos = np.cos(datos)

                    if desplegable_colores.get() == "Azul":
                        plt.plot(datos,"b--")
                    elif desplegable_colores.get() == "Rojo":
                        plt.plot(datos,"r--")
                    elif desplegable_colores.get() == "Amarillo":
                        plt.plot(datos,"y--")
                    elif desplegable_colores.get() == "Verde":
                        plt.plot(datos,"g--")
                    elif desplegable_colores.get() == "Negro":
                        plt.plot(datos,"k--")

                    plt.show()

                except:
                    messagebox.showerror("Error","Introduzca un valor válido para la frecuencia.\nSi está utilizando radianes, pruebe a poner datos mayores a 250.")

            def tangentes():
                try:
                    frec = cantidad_frecuencia.get()
                    frec = int(frec)

                    datos = np.arange(0,frec)

                    if desplegable_unidades.get() == "Radianes":
                        datos = np.radians(datos)

                    datos = np.tan(datos)

                    if desplegable_colores.get() == "Azul":
                        plt.plot(datos,"b--")
                    elif desplegable_colores.get() == "Rojo":
                        plt.plot(datos,"r--")
                    elif desplegable_colores.get() == "Amarillo":
                        plt.plot(datos,"y--")
                    elif desplegable_colores.get() == "Verde":
                        plt.plot(datos,"g--")
                    elif desplegable_colores.get() == "Negro":
                        plt.plot(datos,"k--")

                    plt.show()

                except:
                    messagebox.showerror("Error","Introduzca un valor válido para la frecuencia.\nSi está utilizando radianes, pruebe a poner datos mayores a 250.")

            ventana_eleccion_calculo = tk.Toplevel(ventana2)
            ventana_eleccion_calculo.title("Elección")
            ventana_eleccion_calculo.geometry("280x300")
            ventana_eleccion_calculo.configure(bg="gray35")
            ventana_eleccion_calculo.resizable(0, 0)
            ventana_eleccion_calculo.iconbitmap(ruta_mix)
            ventana_eleccion_calculo.transient(ventana2)

            elegir_opcion_calculo = tk.Label(ventana_eleccion_calculo, text= "Elija una opción para graficar :", bg = "gray35", fg = "white")
            elegir_opcion_calculo.place(x = 63, y = 10)
            dibujar_senos = tk.Button(ventana_eleccion_calculo, text="Senos", bg="white", fg="black", borderwidth=0, relief="solid",cursor="hand2", command = senos)
            dibujar_senos.place(x = 10, y = 70)
            dibujar_cosenos = tk.Button(ventana_eleccion_calculo, text="Cosenos", bg="white", fg="black", borderwidth=0, relief="solid",cursor="hand2", command = cosenos)
            dibujar_cosenos.place(x = 105, y = 70)
            dibujar_tangentes = tk.Button(ventana_eleccion_calculo, text="Tangentes", bg="white", fg="black", borderwidth=0, relief="solid",cursor="hand2", command = tangentes)
            dibujar_tangentes.place(x = 210, y = 70)

            elegir_color = tk.Label(ventana_eleccion_calculo, text = "Color", bg = "gray35", fg = "white")
            elegir_color.place(x = 63, y = 150)
            unidades = tk.Label(ventana_eleccion_calculo, text = "Unidades", bg = "gray35", fg = "white")
            unidades.place(x = 173, y = 150)

            desplegable_colores = ttk.Combobox(ventana_eleccion_calculo, state="readonly")
            desplegable_colores["values"] = ["Azul","Rojo","Amarillo","Verde","Negro"]
            desplegable_colores.current(0)
            desplegable_colores.place(x = 45, y = 170, width=80, height=25)

            desplegable_unidades = ttk.Combobox(ventana_eleccion_calculo, state="readonly")
            desplegable_unidades["values"] = ["Radianes","Grados"]
            desplegable_unidades.current(0)
            desplegable_unidades.place(x = 160, y = 170, width=80, height=25)

            frecuencia = tk.Label(ventana_eleccion_calculo, text = "Frecuencia", bg = "gray35", fg = "white")
            frecuencia.place(x = 107, y = 220)

            cantidad_frecuencia = tk.Entry(ventana_eleccion_calculo)
            cantidad_frecuencia.place(x = 75, y = 250)


        opcion_seleccionada = desplegable.get()
        print(opcion_seleccionada)

        try:

            if opcion_seleccionada == "Fibonacci":
                cantidad = int(cantidad_entrada.get())
                fibonacci(cantidad)

            elif opcion_seleccionada == "Primos":
                cantidad = int(cantidad_entrada.get())
                primos(cantidad)

            elif opcion_seleccionada == "Factorizar":
                cantidad = int(cantidad_entrada.get())
                fact(cantidad)

            elif opcion_seleccionada == "Graficar":
                graficar()

        except:
            messagebox.showerror("Error","Valor no admitido\nPor favor introduzca unos valores válidos")


    def RepSonido():
        pygame.mixer.stop()
        archivo_audio = ruta_audio[0:len(ruta_audio)-4] #le quitamos la extension .wav que son 4 caracteres. si no es .wav dara un error en el if y nos alertará
        if archivo_audio + ".wav" == ruta_audio:
            try:
                pygame.mixer.Sound(ruta_audio).play()
            except:
                messagebox.showerror("Error al reproducir","Hubo un problema al reproducir el archivo.\nPuede que el problema sea que el archivo esté codificado en 32-bit, recoifiquelo en 16-bit.")
        else:
            messagebox.showerror("Error al reproducir","Compruebe que el archivo está en formato .wav")


    def PararRepSonido():
        pygame.mixer.stop()

    def PausSonido():

        fichero = open(ruta_archivo_playpause, "r+")
        linea = fichero.readline() # no ponemos la linea de quitar el ultimo caracter ya que como solo hay una linea no esta el \n
        fichero.close()

        if linea == "play":
            fichero = open(ruta_archivo_playpause,"w")
            fichero.write("pause")
            fichero.close
            pygame.mixer.pause()
        else:
            fichero = open(ruta_archivo_playpause,"w")
            fichero.write("play")
            fichero.close
            pygame.mixer.unpause()

    def cargarSonido():
        global ruta_audio 
        ruta_audio = filedialog.askopenfilename(filetypes = (("wav files", "*.wav"),("Todos los archivos","*.*")))

    BarraDeMenu=Menu(ventana2) #creamos la barra de menú

    archivos_menu=Menu(BarraDeMenu, tearoff=0) #creamos los submenus en barrademenu, y con tearoff ocultamos la barra que hay por defecto cuando creamos el menú
    BarraDeMenu.add_cascade(label="Archivo", menu=archivos_menu)  # agregamos los submenus al menu principal en el menu archivo

    archivos_menu.add_command(label="Guardar", state = "disabled", command=guardar) #dejamos este boton deshabilitado porque no hay valor
    archivos_menu.add_command(label="Salir", command=salir)

    ayuda_menu = Menu(BarraDeMenu, tearoff=0)
    BarraDeMenu.add_cascade(label="Ayuda", menu=ayuda_menu)

    ayuda_menu.add_command(label="Acerca de...", command=informacion_adicional)

    ventana2.config(menu=BarraDeMenu, width=300, height=300) #la barra de menus estara en la ventana y le damos tamaño

    desplegable = ttk.Combobox(ventana2, state="readonly") #creamos el combobox o menu desplegable con la libreria ttk. con state=read... hacemos que el usuario no pueda introducir cualquier valor, solamente los permitidos
    desplegable["values"] = ["Fibonacci","Primos","Factorizar","Graficar"] #definimos todos los valores que puede tener el menu o combobox
    desplegable.current(0) #la opcion por defecto es la primera, posicion 0
    desplegable.place(x=3,y=3,width=150, height=25)

    elegir_opcion = tk.Button(ventana2, text="Aceptar", fg="black", borderwidth=0, relief="solid", cursor="hand2",command=opcion_del_desplegable_seleccionada)
    elegir_opcion.place(x=160, y=3.5, width=60, height=23)

    imgBotonPlay = PhotoImage(file = ruta_imagen_play)
    imgBotonStop = PhotoImage(file = ruta_imagen_stop)
    imgBotonPause = PhotoImage(file = ruta_imagen_playPause)

    tocarsonido = tk.Button(ventana2, image = imgBotonPlay, height = 48, width=48, text="Rep", fg="black", borderwidth=0, relief="solid", cursor="hand2",command=RepSonido)
    tocarsonido.place(x=3, y= 200)

    pausarSonido = tk.Button(ventana2, image = imgBotonPause, height = 48, width = 48, text="Pause", fg="black", borderwidth=0, relief="solid", cursor="hand2",command=PausSonido)
    pausarSonido.place(x=70, y=200)

    paraTocarSonido = tk.Button(ventana2, image = imgBotonStop, height = 48, width = 48, text="Stop", fg="black", borderwidth=0, relief="solid", cursor="hand2",command=PararRepSonido)
    paraTocarSonido.place(x=135, y=200)

    cargar = tk.Button(ventana2,text="Cargar", fg="white",bg="gray25", borderwidth=0, relief="solid", cursor="hand2",command=cargarSonido)
    cargar.place(x=5, y = 280)

    cantidad_texto = tk.Label(ventana2, text="Cantidad:", bg="gray40", fg="white")
    cantidad_texto.place(x=3, y=30)

    cantidad_entrada = ttk.Entry(ventana2)
    cantidad_entrada.place(x=3, y=50)

    scrollbar = Scrollbar(ventana2, orient = VERTICAL)
    scrollbar.pack(side = RIGHT, fill = Y)

    scrollbar2 = Scrollbar(ventana2, orient = HORIZONTAL)
    scrollbar2.pack(side = BOTTOM, fill = X)

    listbox = Listbox(ventana2, width=100, height=57, bg="gray35",bd=0, relief="solid", yscrollcommand = scrollbar.set, xscrollcommand = scrollbar2.set) #creamos una listbox para poner los resultados, tambien integramos la scrollbar para que funcione con el listbox
    listbox.place(relx=0.33, y=20)

    scrollbar.config(command = listbox.yview) # la funcion del scrollbar será bajar la lista (eje y)
    scrollbar2.config(command = listbox.xview) #(eje x)


    ventana2.mainloop()
#---------------------------------------------VENTANA DE INICIO/REGISTRO----------------------------------------#

ventana = tk.Tk()
ventana.title("Acceso")
ventana.geometry("240x150")
ventana.configure(bg="gray35")
ventana.resizable(0, 0)
ventana.iconbitmap(ruta_mix)  # agregamos un icono a la página que aparecerá arriba a la derecha

espacio = Label(ventana, text=" ", bg="gray35", fg="black")
espacio.grid(row=0,sticky=E)  # sticky alinea los textos segun donde le digas, e = este. w = oeste. puntos cardinales.

texto_usuario = Label(ventana, text="    Usuario:  ", bg="gray35", fg="white")
texto_usuario.grid(row=1, sticky=E)

texto_password = tk.Label(ventana, text="    Contraseña:  ", bg="gray35", fg="white")
texto_password.grid(row=2, sticky=E)

usuario = ttk.Entry(ventana)
usuario.grid(row=1, column=1, sticky=E)

password = ttk.Entry(ventana, show="•")  # asi hacemos que solo se vea el punto cuando escribimos
password.grid(row=2, column=1, sticky=E)

acceder = tk.Button(ventana, text="Acceder", bg="white", fg="black", borderwidth=0, relief="solid",cursor="hand2", command=comprobar)
acceder.grid(sticky=E, pady=10)

nuevo_user_boton = tk.Button(ventana, text="Nuevo usuario", bg="white", fg="black", borderwidth=0,relief="solid", cursor="hand2", command=crear_usuario)
nuevo_user_boton.grid(row=3, column=1, sticky=E)

delete_user = tk.Button(ventana, text="Eliminar usuario", bg="white", fg="black", borderwidth=0,relief="solid", cursor="hand2", command=delete_user)
delete_user.grid(row=4, column=1, sticky=E)

ventana.bind("<Return>", comprobar2)

ventana.mainloop()