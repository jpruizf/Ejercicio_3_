from gestor_ventas import Gestor_ventas

def menu():
    gestor = Gestor_ventas()
    print("1.Acumular importe de factura ingreando dia y nro de sucursal")
    print("2.Obtener total de factura ingrsando nro de sucursal")
    print("3.Ingresar el dia y ver que sucursal mas facturo")
    print("4.Obtener la sucursal que menos facturo durante toda las semana")
    print("5.Obtener el total facturado por todas las suscursales durante toda la semana")
    print("0.Finalizar")
    opcion = input("Seleccione una de las opciones dadas:")
    while opcion != '0':
        if opcion == '1':
            dia = int(input("Dia-->"))
            sucursal = int(input("Sucursal-->"))
            importe = float(input("Importe de factura-->"))
            if gestor.cargar_venta(dia,sucursal,importe):
                print("Carga exitosa!")
        if opcion == '2':
            sucursal = int(input("Sucursal-->"))
            print(gestor.total_facturacion(sucursal))
        elif opcion == '3':
            dia = int(input("Dia-->"))
            sucursal = gestor.mayor_facturacion(dia)
            print(f"Sucursal que mas facturo-->{sucursal}")
        elif opcion == '4':
            sucursal = gestor.menor_facturacion()
            print(f"Sucursal que menos facturo durante toda la semana-->{sucursal}")
        elif opcion == '5':
            print(f"Total facturado por todas las sucursales-->{gestor.total_facturado_semana()}")
        print("1.Acumular importe de factura ingreando dia y nro de sucursal")
        print("2.Obtener total de factura ingrsando nro de sucursal")
        print("3.Ingresar el dia y ver que sucursal mas facturo")
        print("4.Obtener la sucursal que menos facturo durante toda las semana")
        print("5.Obtener el total facturado por todas las suscursales durante toda la semana")
        print("0.Finalizar")
        opcion = input("Seleccione una de las opciones dadas:")
if __name__ == '__main__':
    menu()