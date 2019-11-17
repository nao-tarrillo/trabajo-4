# Input
cliente=input("el cliente es:")
nro_granadillas=int(input("el nro de grnadillas es:"))
p.u=float(input("el p.u es:"))

#Procesing
total= (p.u * nro_granadillas)

#Verificador
comprador_compulsivo=( total > 345 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_granadillas,"nro_granadillas")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
