# encoding: UTF-8
#Blanca Flor Cldern Vzquez   
#Aŕeas de rectángulos
 
 
from Graphics import*
 
def calcularArea(b1,h1,b2,h2):
   areaRectangulo1=b1*h1
   areaRectangulo2=b2*h2
   return (areaRectangulo1,areaRectangulo2)
 
def calcularPerimetro(b1,h1,b2,h2):
   perimetroRectangulo1=(b1*2)+(h1*2)
   perimetroRectangulo2=(b2*2)+(h2*2)
   return (perimetroRectangulo1,perimetroRectangulo2)
    
def main():
   rectangulo1base=float(input("Introduce la base del rectangulo 1"))
   rectangulo1altura=float(input("Introduce la altura del rectangulo 1"))
   rectangulo2base=float(input("Introduce la base del rectangulo 2"))
   rectangulo2altura=float(input("Introduce la base del rectangulo 2"))
   (area1,area2)=calcularArea(rectangulo1base,rectangulo1altura,rectangulo2base,rectangulo2altura)
   (perimetro1,perimetro2)=calcularPerimetro(rectangulo1base,rectangulo1altura,rectangulo2base,rectangulo2altura)
    
   print("El area del rectangulo 1 es",area1,"El area del rectangulo  es",area2)
   print ("El perimetro del rectangulo 1 es",perimetro1,"El perimetro del rectangulo 2 es",perimetro2)
   if area1==area2:
       resultado= "las areas son iguales"
   elif area1>area2 :
       resultado="el area 1 es mayor que el area 2"
   else:
       resultado="el area 2 es mayor que el area 1"
   print (resultado)
    
   v=Window("Top-Down",800,800)
   t=Arrow((400,400),90)
   t.penDown()
   t.draw(v)
   #t.color("red") no recuerdo cómo poner color
   t.forward(rectangulo1altura)
   t.rotate(90)
   t.forward(rectangulo1base)
   t.rotate(90)
   t.forward(rectangulo1altura)
   t.rotate(90)
   t.forward(rectangulo1base)
   t.rotate(270)
   #Aquí incia rectángulo 2
   #t.color("blue")
   t.forward(rectangulo2altura)
   t.rotate(90)
   t.forward(rectangulo2base)
   t.rotate(90)
   t.forward(rectangulo2altura)
   t.rotate(90)
   t.forward(rectangulo2base)
   
     
main()
 


