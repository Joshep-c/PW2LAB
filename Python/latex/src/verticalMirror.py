def verticalMirror(self):
    """Devuelve el espejo vertical de la imagen"""
    vertical = []
    for value in self.img:
        vertical.append(value[::-1])
    return Picture(vertical)
