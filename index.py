asignaturas = {}

def registrar_asignatura():
    nombre = input("Nombre de las asignatura: ")
    try:
        creditos = int(input("Cantidad de créditos: "))
        costo_credito = float(input("Costo por crédito: "))
        asignaturas[nombre] = {"creditos": creditos, "costo": costo_credito, "estudiantes": []}
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

def registrar_estudiante():
    nombre_asignatura = input("Nombre de la asignatura: ")
    if nombre_asignatura not in asignaturas:
        print("Esa asignatura no existe.")
        return
    nombre = input("Nombre del estudiante: ")
    try:
        edad = int(input("Edad: "))
        genero = input("Género: ")
        estrato = int(input("Estrato (1-3): "))
        if estrato not in [1, 2, 3]:
            print("Estrato no válido.")
            return
        descuento = {1: 0.5, 2: 0.3, 3: 0.1}[estrato]
        asignaturas[nombre_asignatura]["estudiantes"].append({"nombre": nombre, "edad": edad, "genero": genero, "estrato": estrato, "descuento": descuento})
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

def estudiantes_por_asignatura():
    for asignatura, datos in asignaturas.items():
        print(f"{asignatura}: {len(datos['estudiantes'])} estudiantes")

def asignatura_mayor_recaudo():
    max_recaudo = 0
    mejor_asignatura = ""
    for asignatura, datos in asignaturas.items():
        total = sum(datos['creditos'] * datos['costo'] * (1 - e['descuento']) for e in datos['estudiantes'])
        if total > max_recaudo:
            max_recaudo = total
            mejor_asignatura = asignatura
    if mejor_asignatura:
        print(f"La asignatura con más recaudo es {mejor_asignatura} con ${max_recaudo}")
    else:
        print("No hay asignaturas con estudiantes matriculados.")

def promedio_costo_credito():
    if not asignaturas:
        print("No hay asignaturas registradas.")
        return
    total_costo = sum(datos['costo'] for datos in asignaturas.values())
    print(f"Promedio costo de créditos: {total_costo / len(asignaturas):.2f}")

def total_descuentos_por_estrato():
    try:
        estrato = int(input("Ingrese estrato (1-3): "))
        if estrato not in [1, 2, 3]:
            print("Estrato no válido.")
            return
        total_descuento = sum(datos['creditos'] * datos['costo'] * e['descuento'] for datos in asignaturas.values() for e in datos['estudiantes'] if e['estrato'] == estrato)
        print(f"Total descuentos para estrato {estrato}: ${total_descuento}")
    except ValueError:
        print("Error: Ingresa un número válido.")

def estudiantes_estrato1_por_asignatura():
    for asignatura, datos in asignaturas.items():
        total = sum(1 for e in datos['estudiantes'] if e['estrato'] == 1)
        print(f"{asignatura}: {total} estudiantes de estrato 1")

def total_recaudado():
    total = sum(datos['creditos'] * datos['costo'] * (1 - e['descuento']) for datos in asignaturas.values() for e in datos['estudiantes'])
    print(f"Total dinero recaudado: ${total}")

def menu():
    while True:
        print("\n1. Registrar asignatura\n2. Registrar estudiante\n3. Ver estudiantes por asignatura\n4. Asignatura con mayor recaudo\n5. Promedio costo de créditos\n6. Total descuentos por estrato\n7. Estudiantes de estrato 1 por asignatura\n8. Total recaudado\n9. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_asignatura()
        elif opcion == "2":
            registrar_estudiante()
        elif opcion == "3":
            estudiantes_por_asignatura()
        elif opcion == "4":
            asignatura_mayor_recaudo()
        elif opcion == "5":
            promedio_costo_credito()
        elif opcion == "6":
            total_descuentos_por_estrato()
        elif opcion == "7":
            estudiantes_estrato1_por_asignatura()
        elif opcion == "8":
            total_recaudado()
        elif opcion == "9":
            break
        else:
            print("Opción no válida.")

menu()