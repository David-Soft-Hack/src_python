from tkinter import Tk, Label, Entry, Button, StringVar, LEFT, W
import math


def calcular(a_str: str, b_str: str, c_str: str):
    """Valida las entradas y devuelve (perimetro, area) o lanza ValueError con mensaje."""
    try:
        a = float(a_str)
        b = float(b_str)
        c = float(c_str)
    except Exception:
        raise ValueError("Las tres entradas deben ser números (p. ej. 3.5)")

    # Verificar positivos
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Los lados deben ser mayores que cero.")

    # Verificar desigualdad triangular
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Las longitudes no cumplen la desigualdad triangular.")

    perimetro = a + b + c
    s = perimetro / 2.0
    # Herón
    area_sq = s * (s - a) * (s - b) * (s - c)
    if area_sq < 0:
        # Debería haber sido capturado por la desigualdad, pero por seguridad
        raise ValueError("No se puede calcular el área con esos valores.")
    area = math.sqrt(area_sq)
    return perimetro, area


def build_gui():
    root = Tk()
    root.title("Calcular perímetro y área - Triángulo")
    root.geometry("420x240")

    # Hacer la cuadrícula redimensionable: la columna 1 (inputs/valores) crecerá
    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(1, weight=1)
    Label(root, text="Ingrese los lados del triángulo:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 5))

    Label(root, text="Lado a:").grid(row=1, column=0, sticky=W, padx=10)
    entry_a = Entry(root, width=20)
    entry_a.grid(row=1, column=1, padx=10, pady=2, sticky="ew")

    Label(root, text="Lado b:").grid(row=2, column=0, sticky=W, padx=10)
    entry_b = Entry(root, width=20)
    entry_b.grid(row=2, column=1, padx=10, pady=2, sticky="ew")

    Label(root, text="Lado c:").grid(row=3, column=0, sticky=W, padx=10)
    entry_c = Entry(root, width=20)
    entry_c.grid(row=3, column=1, padx=10, pady=2, sticky="ew")

    result_per = StringVar()
    result_area = StringVar()
    error_msg = StringVar()

    Label(root, text="Perímetro:", font=("Arial", 10)).grid(row=5, column=0, sticky=W, padx=10, pady=(8, 2))
    Label(root, textvariable=result_per, font=("Arial", 10)).grid(row=5, column=1, sticky="w")

    Label(root, text="Área:", font=("Arial", 10)).grid(row=6, column=0, sticky=W, padx=10, pady=(2, 8))
    Label(root, textvariable=result_area, font=("Arial", 10)).grid(row=6, column=1, sticky="w")

    Label(root, textvariable=error_msg, fg="red").grid(row=7, column=0, columnspan=2)

    def on_calcular():
        error_msg.set("")
        result_per.set("")
        result_area.set("")
        a = entry_a.get().strip()
        b = entry_b.get().strip()
        c = entry_c.get().strip()
        try:
            per, area = calcular(a, b, c)
        except ValueError as e:
            error_msg.set(str(e))
            return
        result_per.set(f"{per:.4f}")
        result_area.set(f"{area:.4f}")

    btn = Button(root, text="Calcular", command=on_calcular)
    # El botón ocupa ambas columnas; usamos sticky para que se centre/estire si se quiere
    btn.grid(row=4, column=0, columnspan=2, pady=8, padx=10, sticky="ew")

    # Permitir que la fila de resultados empuje hacia abajo si la ventana se hace más alta
    root.grid_rowconfigure(7, weight=1)

    # Atajo: Enter en cualquier Entry realiza el cálculo
    entry_a.bind("<Return>", lambda event: on_calcular())
    entry_b.bind("<Return>", lambda event: on_calcular())
    entry_c.bind("<Return>", lambda event: on_calcular())

    root.mainloop()


if __name__ == "__main__":
    build_gui()
