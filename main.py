peliculas = []
while True:
    print("\n\n----------Catálogo de películas-----------\n1. Agregar película\n2. Mostrar todas las películas\n3. Buscar películas por género\n4. Eliminar una película\n5. Mostrar estadísticas\n5. Salir")
    selection = input("Seleccione una opción: ")
    match selection:
        case "1":
            while True:
                try:
                    cant = int(input("\n¿Cuántas películas va a ingresar?: "))
                    if cant<=0:
                        print("La cantidad debe ser mayor a 0")
                    else:
                        break
                except:
                    print("Ingrese un numero entero")

            for i in range(cant):
                while True:
                    try:
                        title = input(f"\nIngrese el título de la película {i+1}: ")
                        launch = int(input(f"Ingrese la fecha de lazamiento: "))
                        genre = input("Ingrese el género de la película: ").lower()
                        break
                    except:
                        print("Vuelva a intentarlo por favor")

            peli = {"title": title,"lauch": launch,"genre": genre,}
            peliculas.append(peli)
            print("Película añadida con éxito")

        case "2":
            for pelicula in peliculas:
                print("\nNombre: "+pelicula["title"] + "\nLanzamiento:" + pelicula["launch"] + "\nGénero: " + pelicula["genre"])

        case "3":
            genre_search = input("\nIngrese el género a buscar: ").lower()
            print("Películas que coinciden con ese género: ")
            for pelicula in peliculas:
                if pelicula["genre"] == genre_search:
                    print("\nNombre: " + pelicula["title"] + "\nLanzamiento:" + pelicula["launch"] + "\nGénero: " + pelicula["genre"])

        case "4":
            pass
        case "5":
            print("\nSaliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")