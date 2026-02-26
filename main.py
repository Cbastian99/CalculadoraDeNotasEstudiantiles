def calcular_promedio(notas):
    return sum(notas) / len(notas)


print("=== CALCULADORA DE NOTAS ESTUDIANTILES ===")

nombre = input("Ingrese el nombre del estudiante: ")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

notas = [nota1, nota2, nota3]

promedio = calcular_promedio(notas)

print("\n--- RESULTADOS ---")
print("Estudiante:", nombre)
print("Promedio:", round(promedio, 2))

if promedio >= 3.0:
    print("Estado: APROBADO ✅")
else:
    print("Estado: REPROBADO ❌")