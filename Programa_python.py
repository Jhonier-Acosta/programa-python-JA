
# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
nombre=int(input(yonier))
# Problema 4 - Videoteca Digital

# Matriz con información de títulos audiovisuales
# [Título, Año de Lanzamiento, Calificación, Género]

videoteca = [
    ["Avatar 2", 2022, 8.5, "Ciencia Ficción"],
    ["Breaking Bad", 2008, 9.5, "Drama"],
    ["Wednesday", 2022, 8.1, "Suspenso"],
    ["The Batman", 2022, 8.0, "Acción"],
    ["Dune", 2021, 8.3, "Ciencia Ficción"],
    ["Joker", 2019, 8.4, "Drama"],
    ["Stranger Things", 2022, 8.7, "Terror"]
]

# Función para contar títulos populares y recientes

def contar_titulos(matriz, calificacion_minima, anio_limite):
    contador = 0

    for titulo in matriz:
        anio = titulo[1]
        calificacion = titulo[2]

        if calificacion >= calificacion_minima and anio >= anio_limite:
            contador += 1

    return contador

# Valores de referencia
calificacion_minima = 8.0
anio_limite = 2020

# Llamado de la función
resultado = contar_titulos(videoteca, calificacion_minima, anio_limite)

# Mostrar resultado
print("Cantidad de títulos populares y recientes:", resultado)