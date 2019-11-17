# Input
cliente=input("ingrese nombre del cliente:")
kg=int(input("ingrese nro de kg de mandarinas:"))
P.u=float(input("ingrese el P.u:"))

#Procesing
total=(kg * P.u)

#Verificador
comprador_compulsivo=(total>300)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("#")
print("# cliente:", cliente)
print("#item:    ",kg,"kg")
print("#P.U:      S/.", P.U)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)
