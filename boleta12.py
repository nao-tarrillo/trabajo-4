# Input
cliente=input(("nombre del cliente:"))
gaseosas=int(input("la cantidad de gaseosas es:"))
precio_unitario=float(input("el precio unitario es:"))

#Procesing
total= (precio_unitario * gaseosas)

#Verificador
comprador_compulsivo=( total > 578 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",gaseosas,"gaseosas")
print("#precio unitario:       S/.", precio_unitario)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
