import csv
import os
import qrcode

def generarQR_lista():
    with open('lista_etapa_1.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            nombreUsuarios=row[0]
            apellidoUsuario=row[1]
            rutUsuario=row[2]
            cliente={
                "rut":rutUsuario,
                "nombre": nombreUsuarios,
                "apellido":apellidoUsuario
            }
            img = qrcode.make(cliente)
            img.save("qrs/"+rutUsuario+".png")



generarQR_lista()