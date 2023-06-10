def horizontalMirror(self):
    """Devuelve el espejo horizontal de la imagen"""
    horizontal = []
    for row in self.img[::-1]:
        horizontal.append(row)
    return Picture(horizontal)
