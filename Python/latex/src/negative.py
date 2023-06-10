def negative(self):
    """Devuelve un negativo de la imagen"""
    negative_self = []
    for row in self.img:
        value_color = ""
        for value in row:
            value_color += self._invColor(value)
        negative_self.append(value_color)

    return Picture(negative_self)
