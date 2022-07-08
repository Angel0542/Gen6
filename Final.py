#Importamos las librerias.
from hashlib import new
import tkinter as tk
from tkinter import Label, Menu, messagebox
import random as rd
from werkzeug.security import generate_password_hash
import os

#Crear la interfaz:

#Comandos del menu de opciones:
def ok():
    messagebox.showinfo('Listo', 'A casa certificadito!')


def salir():
    opcion = messagebox.askquestion('Salir', '¿Quieres salir de la aplicacion?')
    #print(opcion)
    if opcion == 'yes':
        ventana.destroy()

def aacerca():
    messagebox.showinfo('Codigazo!!!', 'Este programita te ayuda a elegir contraseñas aleatoriamente y de paso los va a enciptar por si lo necesitas. A pesar de ser tan sencillo tenemos 2 funcionalidades. Espero te guste! :)')

def opc():
    messagebox.showwarning('Error', 'No hay xd')

#Ventana + Menu:
ventana = tk.Tk()       
ventana.title('LastPass') #Titulo de ventana.
ventana.resizable(False, False) #Aca colocamos si quemos que la ventana se pueda redimencionar. En este caso no lo cual le coloque falso.
ventana.geometry('350x426') #Dimenciones de la ventana.
ventana.iconbitmap('.Imagenes\\skull.ico') #Icono de ventana.
ventana.config(background = '#000000') #Color.
ventana.wm_attributes('-alpha', 0.9) #Transparencia.
barraMenu = Menu(ventana) 
ventana.config(menu=barraMenu)
menuArchivo = Menu(barraMenu, tearoff=0)
menuArchivo.add_command(label='Abrir', command= ok)
menuArchivo.add_separator()
menuArchivo.add_command(label='Salir', command=salir)
menuAyuda = Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label='*Opciones Avanzadas*', command=opc)
menuAyuda.add_separator()
menuAyuda.add_command(label= 'Acerca de', command= aacerca)
barraMenu.add_cascade(label='Archivo', menu=menuArchivo)
barraMenu.add_cascade(label='Opciones', menu=menuAyuda) #Menu.

titulo = tk.Label(ventana, text = '***PASSWORDS***', bg='black', fg='White', font= 'Calibri', bd=2, width=20, pady=10)
titulo.pack(padx=20, pady=20) #Titulo dentro de la ventana con color, fuente y dimeciones.

#Personalizacion con imagen de fondo de ventana:
img = tk.PhotoImage(file='.Imagenes\\fondito.png')
lbl_img = tk.Label(ventana, image = img)
lbl_img.pack()
    
#Crear los comandos:
def Pass1(): #Boton1.
    letras_minus = 'abcdefghijklmnopqrstuvwxyz'
    letras_mayus = letras_minus.upper() #En vez de colocar todas las letras en mayusculas solo agarramos la variable de las minusculuas y le colocamos .upper().
    numeros = '012356789'
    simbolos = '!@#$%^&*()/¿?;[]<>' #Se puede colocar todo en una sola variable, solo es prolijidad.

#Creamos un bucle para generar un rango de claves.
    for i in range(1): #Una sola clave.
        #Unimos y formateamos las variable de cada muestra.
        unidos = f'{letras_minus}{letras_mayus}{numeros}{simbolos}'  
        #Definimos la variable para el generador de las contraseñas.
        password = ''.join(rd.sample(unidos,12)) #Numeros de caracteres para cada contraseña en este caso 12.
        password_encriptado = generate_password_hash(password) #Importamos la libreria del Enciptador.
        print('{} ==> {}'.format(password, password_encriptado))

def Pass2(): #Boton2.
    letras_minus = 'abcdefghijklmnopqrstuvwxyz'
    letras_mayus = letras_minus.upper()
    numeros = '012356789'
    simbolos = '!@#$%^&*()/¿?;[]<>'

    for i in range(10): #Diez claves.
        unidos = f'{letras_minus}{letras_mayus}{numeros}{simbolos}'  
        password = ''.join(rd.sample(unidos,12)) 
        password_encriptado = generate_password_hash(password)
        print('{} ==> {}'.format(password, password_encriptado))

def Pass3(): #Boton3.
    letras_minus = 'abcdefghijklmnopqrstuvwxyz'
    letras_mayus = letras_minus.upper()
    numeros = '012356789'
    simbolos = '!@#$%^&*()/¿?;[]<>'

    for i in range(30): #Cincuenta claves.
        unidos = f'{letras_minus}{letras_mayus}{numeros}{simbolos}'  
        password = ''.join(rd.sample(unidos,12)) 
        password_encriptado = generate_password_hash(password)
        print('{} ==> {}'.format(password, password_encriptado))

def reset(): #Boton4.
    command = 'Clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command) #Limpia o elimina el registro de la Terminal.

def salir(): #Boton5.
    ventana.destroy() #Cierra la ventana.


#Crear los Botones:
boton1 = tk.Button(ventana, text= 'Generar 1', command= Pass1, bg= 'Black', fg = 'Yellow')
boton1.pack()
boton1.place(x= 125, y =130, height= 50, width= 100) 

boton2 = tk.Button(ventana, text= 'Generar 10', command= Pass2, bg= 'Black', fg = 'Blue')
boton2.pack()
boton2.place(x= 60, y =200, height= 50, width= 100) 

boton3 = tk.Button(ventana, text= 'Generar 30', command= Pass3, bg= 'Black', fg = 'Red')
boton3.pack()
boton3.place(x= 190, y =200, height= 50, width= 100) 

boton4 = tk.Button(ventana, text= 'Salir', command= salir, bg= 'Black', fg = 'Green')
boton4.pack()
boton4.place(x= 180, y =350, height= 40, width= 100)

boton5 = tk.Button(ventana, text= 'Limpiar', command= reset, bg= 'Black', fg = 'Purple')
boton5.pack()
boton5.place(x= 60, y =350, height= 40, width= 100)

ventana.mainloop()