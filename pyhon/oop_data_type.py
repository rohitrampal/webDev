class Fraction:

    def __init__(self,n,d):
        self.num = n
        self.den = d

    def __str__(self) :
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,a,b):
        add_frac_num = (a.num*b.den+b.num*a.den)
        add_frac_den = (a.den*b.den)
        return '{}/{}'.format(add_frac_num,add_frac_den)
    
    def __sub__(self,a,b):
        add_frac_num = (a.num*b.den-b.num*a.den)
        add_frac_den = (a.den*b.den)
        return '{}/{}'.format(add_frac_num,add_frac_den)
    
    def __mul__(self,a,b):
        add_frac_num = (a.num*b.num)
        add_frac_den = (a.den*b.den)
        return '{}/{}'.format(add_frac_num,add_frac_den)
    
    def __truediv__(self,a,b):
        add_frac_num = (a.num*b.den)
        add_frac_den = (a.den*b.num)
        return '{}/{}'.format(add_frac_num,add_frac_den)