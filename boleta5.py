# Input
cliente=input("dar el nombre del cliente:")
nro_juguetes=int(input("dar el nro de juguetes:"))
p.u=float(input("el precio unitaro es:"))

#Procesing
total= (p.u * nro_juguetes)

#Verificador
comprador_compulsivo=( total > 8000 )

#Output
print("#######################")
print("######Boleta de venta######")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_juguetes,"nro_juguetes")
print("#p.u:       S/.", p.u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)
