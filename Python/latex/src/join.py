def join(self, p):
    """Devuelve una nueva figura poniendo la figura del argumento 
    al lado derecho de la figura actual"""
    union_self = []
    for iterator in range(len(self.img)):
        union_self.append(self.img[iterator] + (p.img[iterator]))

    return Picture(union_self)
