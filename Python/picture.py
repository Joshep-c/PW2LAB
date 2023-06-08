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
        return Picture(vertical)

    def horizontalMirror(self):
        """Devuelve el espejo horizontal de la imagen"""
        horizontal = []
        for row in self.img[::-1]:
            horizontal.append(row)
        return Picture(horizontal)

    def negative(self):
        """Devuelve un negativo de la imagen"""
        negative_self = []
        for row in self.img:
            value_color = ""
            for value in row:
                value_color += self._invColor(value)
            negative_self.append(value_color)

        return Picture(negative_self)

    def join(self, p):
        """Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual"""
        union_self = []
        for iterator in range(len(self.img)):
            union_self.append(self.img[iterator] + (p.img[iterator]))
            
        return Picture(union_self)

    def up(self, p):
        up_picture =  p.img + self.img
        return Picture(up_picture)

    def under(self, p):
        """Devuelve una nueva figura poniendo la figura p sobre la
        figura actual"""
        under_picture =  self.img + p.img
        return Picture(under_picture)
  
    def horizontalRepeat(self, n):
        """Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n"""
        hori_rep = self

        for iterator in range(n-1):
            hori_rep = hori_rep.join(self)

        return hori_rep

    def verticalRepeat(self, n):
        
        vert_rep = self

        for iterator in range(n-1):
            vert_rep = vert_rep.up(self)

        return vert_rep

    # Extra: Solo para realmente viciosos
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        self_rotate = []
        for i in range(len(self.img)):
            row = ""
            for j in range(len(self.img[i])):
                row += self.img[j][i]
            self_rotate.append(row)          

        return Picture(self_rotate)
