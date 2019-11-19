#Gabi Gervasi
#Gabrielle.Gervasi1@marist.edu
#volume and surface area of spheres


from math import *

class Spheres:

    def __init__(self, radius):
        self.radius= radius
        self.volume = ((4/3)*pi*(self.radius**3))
        self.surfacearea = (4*pi*(self.radius**2))

    def Radius (self):
        return self.radius

    def surfaceArea(self):
        return self.surfacearea

    def Volume(self):
        return self.volume
    
def main():
    
    radius= float(input("Enter a number for the radius: "))
    sphere= Spheres(radius)
    print("The volume of this sphere is: ", sphere.Volume())
    print("The surface area of this sphere is: ", sphere.surfaceArea())


main()
