from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """Devuelve el espejo vertical de la imagen"""
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return vertical

    def horizontalMirror(self):
        """Devuelve el espejo horizontal de la imagen"""
        horizontal = []
        for row in self.img[::-1]:
            horizontal.append(row)
        return horizontal

    def negative(self):
        """Devuelve un negativo de la imagen"""
        negative_self = []
        for row in self.img:
            value_color = ""
            for value in row:
                value_color += self._invColor(value)
            negative_self.append(value_color)

        return negative_self

    def join(self, p):
        """Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual"""
        union_self = []
        for iterator in range(len(self.img)):
            union_self.append(self.img[iterator].extends(p.img[iterator]))

        return union_self

    def up(self, p):
        up_self = self.img.extends(p.img)

        return up_self

    def under(self, p):
        """Devuelve una nueva figura poniendo la figura p sobre la
        figura actual"""
        under_self = p.img.extends(self.img)
        
        return under_self
  
    def horizontalRepeat(self, n):
        """Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n"""
        return Picture(None)

    def verticalRepeat(self, n):
        return Picture(None)

    # Extra: Solo para realmente viciosos
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        return Picture(None)
