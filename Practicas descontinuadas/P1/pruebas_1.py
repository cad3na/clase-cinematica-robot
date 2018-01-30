from numpy import pi, linspace
from IPython.utils.warn import info

def prueba_1_1(ans, var):
    
    calculo = pi*10**2
    
    if ans == calculo and var == calculo:
        print("Bien hecho!")
    else:
        if ans == calculo:
            info("¿Guardaste tu calculo en la variable c?")
        else:
            if var == calculo:
                info("¿Desplegaste el valor de tu calculo?")
            else:
                info("¿El valor de tu calculo es el correcto?")
                
def prueba_1_2(funcion):
    
    def convertir(x):
        y = 9*x/5 + 32
        return y
    
    grados = linspace(0, 100, 10)
    
    if (convertir(grados) == funcion(grados)).all():
        print("Muy buen trabajo!")
    else:
        info("Revisa tus calculos")
        
def prueba_1_3(enteros, cuadrados):
    if (enteros == [i for i in range(10)]):
        if (cuadrados == [i**2 for i in range(10)]):
            print("Perfecto!")
        else:
            info("Revisa tu ciclo for")
    else:
        info("Revisa tu arreglo de enteros")
        
def prueba_1_4(ans):
    from numpy import matrix, sin, cos, pi
    
    tau = 2*pi
    rot = matrix([[cos(tau/12), -sin(tau/12)], [sin(tau/12), cos(tau/12)]])
    vec = matrix([[2], [2]])
    
    calculo = rot@vec
    
    if (calculo == ans).all():
        print("Muy buen trabajo!")
    else:
        info("Revisa tus calculos")