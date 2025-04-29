import os

# Función para mostrar el menú
def mostrar_menu():
    print("\n---- TO-DO LIST ----")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

# Función para cargar las tareas desde un archivo
def cargar_tareas():
    if os.path.exists("tareas.txt"):
        with open("tareas.txt", "r") as archivo:
            tareas = archivo.readlines()
        return [tarea.strip() for tarea in tareas]
    return []

# Función para guardar las tareas en un archivo
def guardar_tareas(tareas):
    with open("tareas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

# Función para agregar una tarea
def agregar_tarea(tareas):
    tarea = input("Introduce la tarea: ")
    tareas.append(tarea)
    guardar_tareas(tareas)
    print("Tarea agregada.")

# Función para mostrar todas las tareas
def ver_tareas(tareas):
    if tareas:
        print("\nTus tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No tienes tareas.")

# Función para eliminar una tarea
def eliminar_tarea(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("\nSelecciona el número de la tarea a eliminar: "))
        if 1 <= indice <= len(tareas):
            tarea = tareas.pop(indice - 1)
            guardar_tareas(tareas)
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print("Índice no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def main():
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
