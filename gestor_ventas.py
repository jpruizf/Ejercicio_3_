class Gestor_ventas:
    ventas:list

    def __init__(self):
        self.ventas = [[0 for j in range(7)] for i in range(5)]

    def cargar_venta(self,aux_sucu,aux_dia,aux_importe:float):
        self.ventas[aux_sucu-1][aux_dia-1] += aux_importe
    
    def total_facturacion(self,aux_sucu):
        total_facturacion = 0.0
        for j in range(7):
            total_facturacion += self.ventas[aux_sucu-1][j]
        
        return total_facturacion
    
    def mayor_facturacion(self,aux_dia):
        max = -1
        for i in range(5):
            if self.ventas[i][aux_dia-1] > max:
                max = self.ventas[i][aux_dia-1]
                if max == self.ventas[i][aux_dia-1]:
                    sucursal = i
        return sucursal
    
    def menor_facturacion(self):
        menor_facturacion = 0.0
        min = 99999.9999
        for i in range(5):
            for j in range(7):
                menor_facturacion += self.ventas[i][j]
                if menor_facturacion < min:
                    min = menor_facturacion
                if min == menor_facturacion:
                    sucursal = i
        return sucursal

    def total_facturado_semana(self):
        total_semana = 0.0
        for i in range(5):
            for j in range(7):
                total_semana += self.ventas[i][j]
        return total_semana