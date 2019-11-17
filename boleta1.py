# Input
cliente=input("dar el nombre del cliente:")
cajero=input("dar el nombre del cajero:")
nro_carteras=int(input("ingresar el nro de carteras:"))
p.u=float(input("insertar el precio unitario:"))

#Procesing
total=(P.U * nro_carteras)

#Verificador
comprador_compulsivo=(total>25000)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_carteras,"nro_carteras")
print("#p.u:      S/.", p.u)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)


