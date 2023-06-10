def verticalRepeat(self, n):

    vert_rep = self

    for iterator in range(n-1):
        vert_rep = vert_rep.up(self)

    return vert_rep
