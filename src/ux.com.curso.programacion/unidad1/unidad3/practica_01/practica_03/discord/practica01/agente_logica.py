#discord
"""
funcion que recibe un texto y decide que responder.
Implementa programacion estructurada pura.
"""

def procesar_pregunta (mensaje_usuario):
    #1.normalizacion(paso fundamental en IA)

    mensaje = mensaje_usuario.lower().strip()
    #2. base de conocimiento (diccionario)
    
    conocimiento ={
        #conceptos de estructura de control
        "if":"la sentencia 'if'es un condicional. permite que el programa 
        "tome decisiones basandose en una condicion booleana"

        #tipos de datos 

        "int":"la sentencia 'if' es un condicional. permite que el programa tome
        "decisiones basandose en una condicion boooleana"

        #tipos de datos 

        "int":"representa numeros entero(ej.5,-10,0). no tienen parte decimal.",

        #funciones y modularidad

        "def":"Es la palabra resarvada para definir una funcion en python.",

        #operadoresy sintaxis

        "print":"Funcion que muestra informacion en la consola o salida estandar",

    }

    #logica
     for clave in conocimiento:
        if clave in mensaje:
            return conocimiento[clave]
    return "lo siento, aun no se que es eso. ¡preguntame sobre variables,"               

def main():
    print("¡hola! soy tu asistente de programacion. preguntame sobre variable ")
     while True:
        user_input = input("aAlumno -> ")
        if user_input.Lower() == "salir":break

        respuesta = procesar_pregunta(user_input)
        print(f"bot->{respuesta}")


if __name__ =="__main__":
    main()

