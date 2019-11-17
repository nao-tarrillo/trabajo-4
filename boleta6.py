# Input
cliente=input("dar nombre del cliente:")
nro_cañonazos=int(input("dar el nro de cañonazos:"))
P.u=int(input("el p.u es:"))

#Procesing
total= (p.u * nro_cañonazos)

#Verificador
comprador_compulsivo=( total > 20 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_cañonazos,"nro_cañonazos")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
