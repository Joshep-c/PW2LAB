def under(self, p):
    """Devuelve una nueva figura poniendo la figura p sobre la
    figura actual"""
    under_picture = self.img + p.img
    return Picture(under_picture)
