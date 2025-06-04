# Permitir ingresar los nombres de 3 alumnos y para cada uno una tupla de 3 notas.
# Luego, mostrar el promedio de cada alumno.
# Ejempo alumnos= {
#     "Sofía":(10,9,8),
#     "Luis":(6,7,7),
#     "Marcos":(5,10,7)
# }

alumnos={}
for i in range (3):
    alumno=input("Ingrese el nombre de un alumno: ")
    nota1=int(input("Ingrese la nota 1: "))
    nota2=int(input("Ingrese la nota 2: "))
    nota3=int(input("Ingrese la nota 3: "))
    tupla_notas=(nota1,nota2,nota3)
    alumnos[alumno]=tupla_notas

for alumno in alumnos:
    suma_notas=0
    for nota in alumnos[alumno]:
        suma_notas+=nota
    promedio=suma_notas/3
    print(f"El promedio de las notas de {alumno} es {promedio:.2f}")