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
