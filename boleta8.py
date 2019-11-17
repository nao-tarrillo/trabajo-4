# Input
comprador=input("dar el nombre del comprador:")
nro_cajas=int(input("dar el nro de cajas:"))
precio_caja=float(input("el precio po caja es:"))

#Procesing
total= (precio_caja * nro_cajas)

#Verificador
comprador_compulsivo=( total > 324 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# comprador:", comprador)
print("#item:    ",nro_cajas,"nro_cajas")
print("#precio_caja:       S/.", precio_caja)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
