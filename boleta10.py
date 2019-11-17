# Input
cliente=input("el nombre del cliente es:")
producto=input("el produco es:")
p.u=float(input("el p.u es:"))

#Procesing
total= (p.u * producto )

#Verificador
comprador_compulsivo=( total > 345 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",producto,"producto")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
