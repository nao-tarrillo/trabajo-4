# Input
cliente=input("el cliente es:")
nro_prendas=int(input("dar el nro de prendas:"))
p.u=int(input("el p. es:"))
#Procesing
total= (p.u * nro_prendas)

#Verificador
comprador_compulsivo=( total > 5600 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_prendas,"nro_prendas")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
