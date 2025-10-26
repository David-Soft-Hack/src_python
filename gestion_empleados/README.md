# Gestión de Empleados (GUI)

Aplicación de escritorio simple para gestionar empleados con una interfaz construida sobre Tkinter.

## Requisitos

- Python: se ha desarrollado y probado con Python 3.14 (ruta en mi entorno: `.../Python314/...`). La aplicación usa sólo la librería estándar (`tkinter`, `random`) por lo que funcionará con Python 3.8+ también, pero recomendamos 3.10+ o la versión instalada en tu sistema.
- Sistema operativo: multiplataforma (Windows, macOS, Linux) — en el workspace actual se desarrolla en Windows y los comandos de ejemplo asumen PowerShell.

## Estructura del proyecto (relevante)

- `view/main.py` - punto de entrada de la aplicación y la lógica principal (widgets, gestión de eventos).
- `view/components/` - pequeños wrappers para crear widgets Tkinter reutilizables:
  - `label_component.py` - devuelve un `tkinter.Label` con estilo.
  - `frame_component.py` - devuelve un `tkinter.Frame` que agrupa la UI.
  - `textbox_component.py` - devuelve un `tkinter.Entry` (caja de texto).
  - `button_component.py` - devuelve un `tkinter.Button`.
  - `treeview_component.py` - devuelve un `ttk.Treeview` configurado con las columnas: `ID, Nombre, Apellido, Puesto, Salario`.
- `view/common/generate_number.py` - función `generate_number()` que devuelve un entero aleatorio entre 10000 y 99999 (usa `random.randint`).

## Módulos / librerías usadas

- tkinter (tkinter, ttk)
  - Para construir la UI: ventanas, labels, entrys, botones y `Treeview`.
- random
  - Para generar IDs aleatorios (`generate_number()`).

Ninguna dependencia externa es requerida.

## Resumen de la lógica y componentes principales

En `view/main.py` hay varias partes clave que conviene conocer:

- Variables globales:
  - `id_number` — entero que contiene el ID actualmente generado en la sesión. Se actualiza cuando se pulsa "Generar ID" y se reusa al guardar un empleado (si no existe se genera automáticamente al guardar).
  - `max_salario` — almacena el mayor salario detectado entre los registros del `Treeview`.
  - `max_label` — referencia al `Label` que muestra en pantalla el empleado con el salario máximo (se crea la primera vez y luego se actualiza mediante `.config(text=...)`).

- Funciones principales:
  - `get_generated_number_label(master, row, column)`:
    - Llama a `gn.generate_number()` (el módulo `view/common/generate_number.py`) y guarda el valor en la variable global `id_number`.
    - Muestra un `Label` con `ID:<valor>` en la interfaz.
  - `add_Employe(master, tabla, nombre, apellido, cargo, salario, id_value=None)`:
    - Inserta una fila en el `Treeview`. Si `id_value` no se proporciona, usa la variable global `id_number`.
    - Convierte el salario a `float` (si se puede) y lo guarda formateado con 2 decimales.
    - Recorre las filas del `Treeview` para calcular cuál es el salario máximo y qué empleado corresponde. Luego crea o actualiza `max_label` para mostrar "Mayor salario: <Nombre> <Apellido> - <Salario>".
  - `save_employee()` (definida localmente en `__main__`):
    - Lee los valores de las cajas de texto (`Entry.get()`), capitaliza nombre/apellidos, genera un ID si no existe, llama a `add_Employe(...)` y luego limpia las cajas con `.delete(0, "end")`.

- Componentes (API y notas de uso)
  - `textbox_component(...)` devuelve un `tkinter.Entry`. Usar `.get()` para obtener su texto y `.delete(0, 'end')` para limpiarla.
  - `treeview_component(...)` devuelve un `ttk.Treeview` con `columns=("ID","Nombre","Apellido","Puesto","Salario")`. Las filas se obtienen con `tree.get_children()` y los valores con `tree.item(item, 'values')`.

## Cómo ejecutar

En PowerShell, desde la raíz del proyecto (o desde `d:\src_python`) ejecuta:

```powershell
& "C:/Users/<tu_usuario>/AppData/Local/Programs/Python/Python314/python.exe" d:/src_python/gestion_empleados/view/main.py
```

O, si tu `python` en PATH apunta a la versión adecuada:

```powershell
python d:/src_python/gestion_empleados/view/main.py
```

Pasos de uso dentro de la aplicación:
1. (Opcional) Pulsar "Generar ID" para obtener un ID para el nuevo empleado.
2. Escribir `Nombre`, `Apellido`, `Cargo` y `Salario`.
3. Pulsar "Guardar Empleado" — el registro aparecerá en el `Treeview`.
4. La interfaz muestra en pantalla el empleado con mayor salario y su valor (etiqueta cerca del botón guardar).

## Consideraciones y mejoras sugeridas

- Persistencia de datos: Actualmente los empleados y el ID sólo existen en memoria durante la ejecución. Para persistencia entre ejecuciones puede usar:
  - Un archivo CSV/JSON (fácil): escribir/leer al guardar/cargar.
  - Una base de datos SQLite (más robusto): almacenar registros y consultar el salario máximo con SQL.
- Control de entradas: validar que `salario` sea numérico antes de guardar y mostrar mensajes de error al usuario si no lo es.
- Un único `Label` para el ID: hoy se crea un label cada vez que se genera el ID; es posible conservar una referencia y actualizarlo en lugar de crear duplicados.
- Encabezados y ordenamiento en `Treeview`: permitir ordenar por columnas y/o borrar/editar registros.
- Tests y separación de lógica: extraer la lógica de negocio (cálculo del salario máximo, validaciones) fuera de la UI para facilitar pruebas unitarias.

## Archivos importantes

- `view/main.py` - ejecución y lógica principal.
- `view/components/*.py` - componentes UI.
- `view/common/generate_number.py` - generación de IDs.

---