# Input
cliente=input("dar el nombre del ciente:")
nro_cervezas=int(input("dar el nro de cervezas:"))
p.u= float(input("dar el p.u:"))

#Procesing
total=(p.u * nro_cervezas)

#Verificador
comrador_compulsivo=(total > 8000)

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_cervezas,"nro cervesas")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
