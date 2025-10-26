from tkinter import ttk as tkk

def treeview_component(master,row,column):
    tree =tkk.Treeview(master, columns=("ID", "Nombre", "Apellido", "Puesto", "Salario"), show="headings")
    # Configurar los encabezados de las columnas
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("Puesto", text="Puesto")
    tree.heading("Salario", text="Salario")
    tree.grid(row=row, column=column, pady=10, padx=10, sticky="nsew",columnspan=2)
    return tree
    