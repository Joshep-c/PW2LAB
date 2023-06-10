def horizontalRepeat(self, n):
    """Devuelve una nueva figura repitiendo la figura actual al costado
    la cantidad de veces que indique el valor de n"""
    hori_rep = self

    for iterator in range(n-1):
        hori_rep = hori_rep.join(self)

    return hori_rep
