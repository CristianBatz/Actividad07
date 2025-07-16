estudiantes = {}
opcion = 0

while opcion != 4:
    print("=== Registro Estudiantes ===")
    print("1. Registrar estudiantes")
    print("2. Mostrar todos los estudiantes y sus cursos")
    print("3. Buscar estudiante por carnet")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print("=== Registro ===")
        cantidad = int(input("Cantidad de estudiantes que desea registrar: "))
        while cantidad <= 0 or cantidad >= 100:
            print("Ha ingresado un numero fuera de los limites,vuelva a intentarlo")
            cantidad = int(input("Cantidad de estudiantes que desea registrar: "))
        for i in range(cantidad):
            carnet = input("Ingrese su numero de carnet: ")
            while carnet in estudiantes:
                print("Ya hay un carnet con el mismo codigo,vuelva a intentarlo")
                carnet = input("Ingrese su numero de carnet: ")
            nombre = input("Nombre completo del estudiante: ")
            edad = int(input("Edad: "))
            carrera = input("Carrera: ")
            cantidadCurso = int(input("Cantidad de curso que desea registrar: "))
            while cantidadCurso <= 0 or cantidadCurso >= 50:
                print("Ha ingresado un numero fuera de los limites,vuelva a intentarlo")
                cantidadCurso = int(input("Cantidad de curso que desea registrar: "))
            for j in range(cantidadCurso):
                nombreCursoA = input("Nombre completo del curso: ")
                codigoCurso = input("Codigo del curso: ")
                tarea = float(input("Nota de la Tarea del curso (0-100) : "))
                parcial = float(input("Nota de el parcial del curso (0-100): "))
                proyecto = float(input("Nota de la proyecto del curso (0-100): "))
                promedio = (tarea + parcial + proyecto) / 3
                estudiantes[carnet] = {
                    "nombre": nombre,
                    "edad": edad,
                    "carrera": carrera,
                    "codigoCurso": {
                        "nombreCursoA": nombreCursoA,
                        "tarea": tarea,
                        "parcial": parcial,
                        "proyecto": proyecto,
                        "promedio": promedio
                    }

                }

    if opcion == 2:
        print("=== Mostrar lista de Estudiantes y cursos ===")
        for carnet, datos in estudiantes.items():
            print(f"\nCarnet: {carnet}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print("Cursos inscritos:")
            for cursos in datos["codigoCurso"]:
                print(f"nombre del curso: {datos['nombreCursoA']}")
            print(f"Punteo tarea: {datos['nombreCurso']['tarea']}")
            print(f"Punteo parcial: {datos['nombreCurso']['parcial']}")
            print(f"Punteo proyecto: {datos['nombreCurso']['proyecto']}")
            print(f"promedio: {datos['nombreCurso']['promedio']}")

    if opcion == 3:
        print("=== Buscar estudiante por carnet ===")
        buscando = input("ingrese el numero de carnet: ")
        if buscando in estudiantes:
            estudiante = estudiantes[buscando]
            print("\nEstudiante encontrado:")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")
            print(f"Carrera: {estudiante['carrera']}")
            print("Cursos inscritos:")
            print(f"nombre del curso: {estudiante['nombreCursoA']}")
            print(f"Punteo tarea: {estudiante['nombreCurso']['tarea']}")
            print(f"Punteo parcial: {estudiante['nombreCurso']['parcial']}")
            print(f"Punteo proyecto: {estudiante['nombreCurso']['proyecto']}")
        else:
            print("Estudiante no encontrado.")

    if opcion == 4:
        print("=== Salir ===")
        print("Saliendo del programa")
