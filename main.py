peliculas = []
while True:
    print("\n\n----------Catálogo de películas-----------\n1. Agregar película\n2. Mostrar todas las películas\n3. Buscar películas por género\n4. Eliminar una película\n5. Mostrar estadísticas\n6. Salir")
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
                        titulo = input(f"\nIngrese el título de la película {i+1}: ")
                        año = int(input(f"Ingrese la fecha de lazamiento: "))
                        genero = input("Ingrese el género de la película: ").lower()
                        titulo_repeat = False
                        if len(peliculas) > 0:
                            for pelicula in peliculas:
                                if pelicula['título'] == titulo:
                                    print("Ya hay una película con ese nombre")
                                    titulo_repeat = True

                        if titulo_repeat:
                            break
                        peli = {"título": titulo, "año": año, "género": genero}
                        peliculas.append(peli)
                        print("Película añadida con éxito")
                        break
                    except:
                        print("Vuelva a intentarlo por favor")

        case "2":
            if not peliculas:
                print("No hay películas registradas")
                continue

            for pelicula in peliculas:
                print(f"\nNombre: {pelicula['título']}\nLanzamiento: {pelicula['año']}\nGénero: {pelicula['género']}")

        case "3":
            if not peliculas:
                print("No hay películas registradas")
                continue

            genre_search = input("\nIngrese el género a buscar: ").lower()
            print("Películas que coinciden con ese género: ")
            match = False
            for pelicula in peliculas:
                if pelicula['género'] == genre_search:
                    match = True
                    print(f"\nNombre: {pelicula['título']}\nLanzamiento: {pelicula['año']}\nGénero: {pelicula['género']}")
            if not match:
                print("No hay películas con ese género")

        case "4":
            if not peliculas:
                print("No hay películas registradas")
                continue

            titulo_delete = input("\nIngrese el título de la película que desea eliminar: ")
            match2 = False
            for pelicula in peliculas:
                if titulo_delete == pelicula['título']:
                    match2 = True
                    peliculas.remove(pelicula)
                    print("Película eliminada")
                    break
            if not match2:
                print("No hay una película con ese nombre en la lista")

        case "5":
            if not peliculas:
                print("No hay películas registradas")
                continue
            print(f"\nPelículas registradas: {len(peliculas)}")
            genres = []
            for pelicula in peliculas:
                if pelicula['género'] not in genres:
                    genres.append(pelicula['género'])

            if genres:
                for genre in genres:
                    genre_count = 0
                    for pelicula in peliculas:
                        if pelicula['género'] == genre:
                            genre_count += 1
                    print(f"Hay {genre_count} películas de género {genre}")

            lower_age = 10000
            for pelicula in peliculas:
                if pelicula['año'] < lower_age:
                    lower_age = pelicula['año']

            for pelicula in peliculas:
                if pelicula["año"] == lower_age:
                    print(f"Película más antigua registrada:\nTítulo: {[pelicula['título']]}   Lanzamiento: {pelicula["año"]}   Género: {pelicula["género"]}")

        case "6":
            print("\nSaliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")