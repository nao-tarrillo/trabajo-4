# Input
cliente=input("el nombre del cliente es:")
bolsas_caramelo=int(input("dar el nro de bolsas de caramelos:"))
precio.bolsa=float(input("dar el precio por bolsa:"))

#Procesing
total= (p.u * p.bolsa )

#Verificador
comprador_compulsivo=( total > 200 )

#Output

print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",bolsas_caramelo,"bolsas_caramelo")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
