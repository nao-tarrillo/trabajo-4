# Input
cliente=input("el nombre del cliente es:")
producto=input("el nombre del producto es:")
p.u=input("el p.u es:")
#Procesing
total= (p.u * producto)

#Verificador
comprador_compulsivo=( total > 456 )

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
