class MercadoLineal:
    """
    Clase para modelar un mercado básico de Oferta y Demanda Lineal.
    Usa el estándar de ejes: Precio (Y), Cantidad (X).
    
    Demanda: P = a - b*Q
    Oferta: P = c + d*Q
    """
    def __init__(self, a, b, c, d):
        self.a = a  # Intercepto Demanda (Precio Maximo dispuesto a pagar)
        self.b = b  # Pendiente Demanda
        self.c = c  # Intercepto Oferta (Precio Mínimo dispuesto a vender)
        self.d = d  # Pendiente Oferta
        
    def encontrar_equilibrio(self):
        """Calcula la Cantidad (Q) y Precio (P) de equilibrio algebraicamente."""
        # a - bQ = c + dQ  =>  a - c = Q * (b + d)
        if (self.b + self.d) == 0:
            return 0, 0
            
        q_eq = (self.a - self.c) / (self.b + self.d)
        p_eq = self.a - self.b * q_eq
        
        # Validación de mercado posible (precios/cantidades no pueden ser negativos en modelos básicos)
        if q_eq < 0 or p_eq < 0:
            return 0, 0
            
        return q_eq, p_eq
        
    def calcular_excedentes(self):
        """
        Calcula el bienestar social:
        Excedente Consumidor (Área por encima del precio y debajo de la demanda)
        Excedente Productor (Área por debajo del precio y por encima de la oferta)
        """
        q_eq, p_eq = self.encontrar_equilibrio()
        if q_eq <= 0:
            return 0, 0
            
        # Área del triángulo = (base * altura) / 2
        # Base es q_eq. Altura de demanda es (a - p_eq). Altura de oferta es (p_eq - c).
        exc_consumidor = 0.5 * q_eq * (self.a - p_eq)
        exc_productor = 0.5 * q_eq * (p_eq - self.c)
        
        return exc_consumidor, exc_productor
    
    def generar_coordenadas(self, q_max=None):
        """Genera arrays para plotear las rectas fácilmente en Matplotlib."""
        import numpy as np
        
        q_eq, _ = self.encontrar_equilibrio()
        if q_max is None:
            q_max = q_eq * 2 if q_eq > 0 else 100
            
        q_array = np.linspace(0, q_max, 100)
        
        # P = a - bQ
        p_demanda = self.a - self.b * q_array
        p_demanda = np.where(p_demanda < 0, 0, p_demanda) # No permitimos precios negativos visualmente
        
        # P = c + dQ
        p_oferta = self.c + self.d * q_array
        p_oferta = np.where(p_oferta < 0, 0, p_oferta)
        
        return q_array, p_demanda, p_oferta
