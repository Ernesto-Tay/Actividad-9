peliculas = []
while True:
    print("\n----------Catálogo de películas-----------\n1. Agregar película\n2. Mostrar todas las películas\n3. Buscar películas por género\n4. Eliminar una película\n5. Mostrar estadísticas\n5. Salir")
    selection = input("Seleccione una opción: ")
    match selection:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("\nSaliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")