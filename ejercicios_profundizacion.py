#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    print("Ingrese el primer número")
    numero_1 = float(input())
    print("Ingrese el segundo número")
    numero_2 = float(input())
    result_suma = numero_1 + numero_2
    result_resta = numero_1 - numero_2
    result_multi = numero_1 * numero_2
    result_divi = numero_1 / numero_2
    result_expon = numero_1 ** numero_2
    print("La suma entre", numero_1, "y", numero_2, "es", result_suma, "\n"
          "La resta entre", numero_1, "y", numero_2, "es", result_resta, "\n"
          "La multiplicacion entre", numero_1, "y", numero_2, "es", result_multi, "\n"
          "La division entre", numero_1, "y", numero_2, "es", result_divi, "\n"
          "El resultado de", numero_1, "elevado a", numero_2, "es", result_expon, "\n")


def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''
    print("Por favor, indicanos cuál es tu nombre completo?")
    name_compl = str(input())
    print("Bien, ahora tu DNI")
    dni = str(input())
    print("Falta poco! Cuál es tu edad? (No nos engañes jaja)")
    age = int(input())
    print("Y por último, cuánto mides?")
    h = float(input())
    print("Nombre Completo:", name_compl, ", DNI:", dni, "\n"
          "Nombre Completo:", name_compl, ", Edad:", age, ", Altura:", h)

def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''
    '''
    Quisiera profundizar un poco más ya que en Venezuela, por ejemplo, el
    común denominador es que el nombre completo esté compuesto por 
    4 elementos 2 Nombres y 2 Apellidos (3 si contamos en binario xD).
    
    Por lo tanto, necesitaría un condicional en el que, si la lista luego
    del split() contiene 3 elementos, el apellido sea igual [2] '''

    print("Cuál es el primer Nombre y Apellido de tu Padre")
    padre = str(input())
    padre.split()
    nom_padre, apellido_padre = padre.split()
    print("Cuál es el primer Nombre y Apellido de tu Madre")
    madre = str(input())
    madre.split()
    nom_madre, apellido_madre = madre.split()
    print("Cuál es tu nombre?")
    nom_hijo = str(input())
    print("Tu nombre es:", nom_hijo.capitalize(), apellido_padre.capitalize(), apellido_madre.capitalize())


def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''
    print("Son PARIENTES?")
    print("Nombre y Apellido de la 1ra. Persona")
    persona_1 = str(input())
    print("Nombre y Apellido de la 2da. Persona")
    persona_2 = str(input())
    nombre_2, apellido_2 = persona_2.split()
    if apellido_2 in persona_1:
      print("Felicidades, son PARIENTES")
    else:
      print("Harina de otro costal jaja, NO SON PARIENTES")


def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''
    print("Cuál es tu nombre completo?")
    nomb_compl = str(input())
    nomb_compl.split()
    nombre, apellido = nomb_compl.split()
    print(nombre.lower(), apellido)
    print(nombre.upper(), apellido)
    print(nombre.capitalize(), apellido)

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
