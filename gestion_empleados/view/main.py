
from tkinter import Tk

#Modulos propios del proyecto
from components.label_component import label_component as lbc
from components.frame_component import frame_component as frc
from components.textbox_component import textbox_component as tbc
from components.button_component import button_component as btc
from components.treeview_component import treeview_component as trc

#Importamos la función para generar números 10000 - 99999
from common import generate_number as gn

# Definimos una variable global (sera inicializada en __main__)
id_number = 0
max_salario = 0.0
# Label que mostrará el empleado con salario máximo (referencia para actualizar)
max_label = None

#Función para agregar a la tabla
def add_Employe(master, tabla, nombre, apellido, cargo, salario, id_value=None):
    """Inserta una fila en la tabla. Si `id_value` es None usa la variable global `id_number`.

    Además calcula el salario máximo entre las filas y actualiza `max_label`
    mostrando el empleado con mayor salario y el valor.
    """
    global max_salario, max_label

    if id_value is None:
        id_value = id_number

    # Intentar convertir salario a float para orden/almacenamiento seguro
    try:
        salario_float = float(salario)
    except Exception:
        salario_float = 0.0

    # Insertar la fila (guardamos el salario como cadena formateada)
    tabla.insert("", "end", values=(id_value, nombre, apellido, cargo, f"{salario_float:.2f}"))

    # Recalcular salario máximo y empleado asociado
    children = tabla.get_children()
    empleados = []  # lista de tuplas (salario_float, nombre, apellido)
    for item in children:
        vals = tabla.item(item, "values")
        try:
            s = float(vals[4])
        except Exception:
            s = 0.0
        empleados.append((s, vals[1], vals[2]))

    if empleados:
        # Obtener el primer empleado con salario máximo
        max_item = max(empleados, key=lambda x: x[0])
        max_salario = max_item[0]
        max_nombre = max_item[1]
        max_apellido = max_item[2]
        texto = f"Mayor salario: {max_nombre} {max_apellido} - {max_salario:.2f}"

        if max_label is None:
            max_label = lbc(master=master, text=texto, font_size=13)
            # Colocamos el label en la columna 1, fila 6 (al lado del botón guardar)
            max_label.grid(row=6, column=1, pady=10, padx=10, sticky="w")
        else:
            max_label.config(text=texto)
    

#Funcion para generar numeros aleatorios
def get_generated_number_label(master, row, column):
    """Función para obtener la etiqueta del número generado.

    Actualiza la variable global `id_number` y muestra la etiqueta con el ID.
    """
    global id_number
    id_number = gn.generate_number()
    label = lbc(master, text=f"ID:{id_number}", font_size=12)
    label.grid(row=row, column=column, pady=10, padx=10, sticky="w")
    return label


# Código principal de la aplicación
if __name__ == "__main__":
    #Inicializamos la variable global
    id_number= 0
    max_salario = 0

    #Creamos el formulario
    root = Tk()
    root.title("Gestión de Empleados")
    root.geometry("800x600")

    #Argegamos los compoenentes
    layout= frc(root, width=800, height=600, bg_color="white")
    # Configuración de la cuadrícula
    layout.grid_columnconfigure(1, weight=1) # Columna 1 (cajas de texto y encabezado) se expande


    #Título de la plicación
    encabezado = lbc(layout, text="Sistema de Gestión de Empleados", font_size=16, bold=True)
    encabezado.grid(row=0, column=1, pady=20, padx=20, sticky="ew")

    # Campo de texto para el nombre
    nombre_label = lbc(layout, text="Nombre:", font_size=12)
    nombre_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")
    # Caja de texto para el nombre
    nombre_textbox = tbc(layout, width=30, font_size=12)
    nombre_textbox.grid(row=1, column=1, pady=10, padx=5, sticky="ew")

    # Campo de texto para el apellido
    apellido_label = lbc(layout, text="Apellido:", font_size=12)
    apellido_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
    # Caja de texto para el apellido
    apellido_textbox = tbc(layout, width=30, font_size=12)
    apellido_textbox.grid(row=2, column=1, pady=10, padx=5, sticky="ew")

    # Campo de texto para el cargo
    cargo_label = lbc(layout, text="Cargo:", font_size=12)
    cargo_label.grid(row=3, column=0, pady=10, padx=10, sticky="w")
    # Caja de texto para el Cargo
    cargo_textbox = tbc(layout, width=30, font_size=12)
    cargo_textbox.grid(row=3, column=1, pady=10, padx=5, sticky="ew")

    # Campo de texto para el Salario
    salario_label = lbc(layout, text="Salario:", font_size=12)
    salario_label.grid(row=4, column=0, pady=10, padx=10, sticky="w")
    # Caja de texto para el Salario
    salario_textbox = tbc(layout, width=30, font_size=12)
    salario_textbox.grid(row=4, column=1, pady=10, padx=5, sticky="ew")

    #Botón para generar numeros aleatorios
    generate_number_button = btc(layout, text="Generar ID", width=15, height=2, font_size=12)
    generate_number_button.grid(row=5, column=0, pady=20, padx=5, sticky="w")

    #Guardar los cambios y mostrar la ventana
    save_button = btc(layout, text="Guardar Empleado", width=20, height=2, font_size=12)
    save_button.grid(row=6, column=0, pady=20, padx=5, sticky="w")

    #Cargar el árbol de empleados
    employee_tree = trc(layout,7,0)
    
    #Ejecutamos los eventos de los botones
    generate_number_button.config(command=lambda: get_generated_number_label(master=layout, row=5, column=1))

    # Acción de guardado: usamos la id global actual (si existe) y los valores de las cajas
    def save_employee():
        nombre = nombre_textbox.get()
        apellido = apellido_textbox.get()
        cargo = cargo_textbox.get()
        salario = salario_textbox.get()

        # Si desea agregar más campos (puesto, salario) puede crear más cajas y leerlas aquí
        # Si no se ha generado un ID, generamos uno automáticamente
        global id_number
        if not id_number:
            get_generated_number_label(master=layout, row=5, column=1)

        add_Employe(layout, tabla=employee_tree, nombre=nombre.capitalize(), apellido=apellido.capitalize(), cargo=cargo.capitalize(), salario=salario, id_value=id_number)
       
        # Limpiar cajas tras guardar
        nombre_textbox.delete(0, "end")
        apellido_textbox.delete(0, "end")
        cargo_textbox.delete(0,"end")
        salario_textbox.delete(0,"end")

    save_button.config(command=save_employee)

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()

