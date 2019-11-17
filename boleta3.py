# Input
empresa=input("nombre de la empresa:")
nro_computadoras=int(input("cantidad de nro de computadoras:"))
p.u=float(input("dar el p.u:"))

#Procesing
total=(nro_computadoras * p.u)

#Verificador
comprador_compulsivo=(total>267.000)
#Output
print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_computadoras,"nro_computadoras")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
