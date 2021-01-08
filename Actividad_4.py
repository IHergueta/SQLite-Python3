import csvfile as csvfile

f = open("empleados.txt","r")
import sqlite3
from sqlite3 import Error

from main import *

import csv

try:
    con = sqlite3.connect("Empleados.db")
    print("Conectandose a Empleados.db")
    cur = con.cursor()
except Error:
    print(Error)
    con = sqlite3.connect("Empleados.db")





try:

    for line in f:

        cur.execute("Insert into empleados(id,nombre,salario,departamento,categoria,fecha_contratacion) Values(?, ?, ?, ?, ?, ?)", line)

    con.commit()


    print("Empleados insertados correctamente")

except sqlite3.DatabaseError:

    print("No se ha isertado correctamente")


try:

    cur.execute("Select nombre,salario,fecha_contratacion,categoria from empleados")

    datos = cur.fetchall()

    con.commit()

    print("Datos -> ",datos)

except sqlite3.DatabaseError:

    print("Algo ha ido mal en los datos")



try:



    rows = [datos]

    fields = ["nombre","salario_anual", "fecha_contratacion" , "categoria"]


    file = open("Programadores.csv", "w")

    with file as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)

        csvwriter.writerows(rows)


except sqlite3.DatabaseError:

     print("Algo ha ido mal")



try:

    cur.execute("Select departamento,categoria,salario from empleados")

    datos2 = cur.fetchall()

    con.commit()

    print("Datos 2 -> ",datos2)

except sqlite3.DatabaseError:

    print("Algo ha ido mal en los datos 2")


try:



    rows = [datos2]

    fields = ["departamento","categoria", "salarioTotal"]


    file = open("Resumen.csv", "w")

    with file as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)

        csvwriter.writerows(rows)


except sqlite3.DatabaseError:

     print("Algo ha ido mal")

