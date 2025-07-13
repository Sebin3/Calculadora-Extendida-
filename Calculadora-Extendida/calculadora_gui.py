import tkinter as tk
from tkinter import messagebox
# Importamos las funciones de nuestro archivo de lógica
from calculadora_login import factorial, combinatoria, permutacion

# --- Interfaz Gráfica con Tkinter ---

class AdvancedCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Combinatoria Extendida")
        master.geometry("450x400") # Aumentamos el tamaño para el texto detallado
        master.resizable(False, False)

        # Estilo de fuentes
        self.font_title = ("Helvetica", 14, "bold")
        self.font_label = ("Helvetica", 10)
        self.font_button = ("Helvetica", 10, "bold")
        self.font_result = ("Helvetica", 12, "bold") # Resultado principal
        self.font_detail = ("Helvetica", 9) # Detalles de la fórmula

        # Variables para las entradas y resultados
        self.n_var = tk.StringVar()
        self.k_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.detail_var = tk.StringVar() # Nueva variable para los detalles
        self.result_var.set("Resultado:")
        self.detail_var.set("") # Inicialmente vacío

        # --- Título ---
        self.title_label = tk.Label(master, text="Calculadora Combinatoria", font=self.font_title, fg="blue")
        self.title_label.pack(pady=10)

        # --- Entrada para 'n' ---
        self.frame_n = tk.Frame(master)
        self.frame_n.pack(pady=5)
        tk.Label(self.frame_n, text="Valor de n:", font=self.font_label).pack(side=tk.LEFT)
        self.entry_n = tk.Entry(self.frame_n, textvariable=self.n_var, width=15, relief=tk.GROOVE)
        self.entry_n.pack(side=tk.LEFT, padx=5)

        # --- Entrada para 'k' ---
        self.frame_k = tk.Frame(master)
        self.frame_k.pack(pady=5)
        tk.Label(self.frame_k, text="Valor de k:", font=self.font_label).pack(side=tk.LEFT)
        self.entry_k = tk.Entry(self.frame_k, textvariable=self.k_var, width=15, relief=tk.GROOVE)
        self.entry_k.pack(side=tk.LEFT, padx=5)

        # --- Botones de Operación ---
        self.frame_buttons = tk.Frame(master)
        self.frame_buttons.pack(pady=15)

        self.btn_factorial = tk.Button(self.frame_buttons, text="Factorial (n!)", command=self.calculate_factorial,
                                       font=self.font_button, bg="#4CAF50", fg="white", activebackground="#45a049")
        self.btn_factorial.grid(row=0, column=0, padx=5, pady=5)

        self.btn_combinatoria = tk.Button(self.frame_buttons, text="Combinatoria C(n,k)", command=self.calculate_combinatoria,
                                          font=self.font_button, bg="#2196F3", fg="white", activebackground="#1e88e5")
        self.btn_combinatoria.grid(row=0, column=1, padx=5, pady=5)

        self.btn_permutacion = tk.Button(self.frame_buttons, text="Permutación P(n,k)", command=self.calculate_permutacion,
                                         font=self.font_button, bg="#FF9800", fg="white", activebackground="#fb8c00")
        self.btn_permutacion.grid(row=1, column=0, columnspan=2, pady=5) # Ocupa 2 columnas para centrar

        # --- Etiqueta de Resultado Principal ---
        self.result_label = tk.Label(master, textvariable=self.result_var, font=self.font_result, fg="black", wraplength=400)
        self.result_label.pack(pady=5)

        # --- Etiqueta de Detalle (Nueva) ---
        self.detail_label = tk.Label(master, textvariable=self.detail_var, font=self.font_detail, fg="gray", wraplength=400, justify=tk.CENTER)
        self.detail_label.pack(pady=5)

        # --- Botón de Limpiar ---
        self.btn_clear = tk.Button(master, text="Limpiar", command=self.clear_fields, font=self.font_button,
                                   bg="#f44336", fg="white", activebackground="#d32f2f")
        self.btn_clear.pack(pady=5)

    def _get_n_k(self, require_k=False):
        """Helper para obtener y validar las entradas n y k."""
        self.result_var.set("Resultado:") # Limpiar resultados anteriores en cada intento
        self.detail_var.set("") # Limpiar detalles
        
        try:
            n_val = int(self.n_var.get())
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingresa un número entero válido para 'n'.")
            return None, None
        
        k_val = None
        if require_k:
            try:
                k_val = int(self.k_var.get())
            except ValueError:
                messagebox.showerror("Error de Entrada", "Por favor, ingresa un número entero válido para 'k'.")
                return None, None
        
        return n_val, k_val

    def calculate_factorial(self):
        n, _ = self._get_n_k(require_k=False)
        if n is None:
            return

        try:
            # Obtenemos la cadena detallada y el valor calculado
            detailed_str = factorial(n, detailed=True)
            result_val = factorial(n) # Llama de nuevo para el valor numérico
            self.result_var.set(f"{n}! = {result_val}")
            self.detail_var.set(f"{n}! = {detailed_str} = {result_val}")
        except ValueError as e:
            messagebox.showerror("Error de Cálculo", str(e))
            self.result_var.set("Resultado: Error")
            self.detail_var.set("")

    def calculate_combinatoria(self):
        n, k = self._get_n_k(require_k=True)
        if n is None or k is None:
            return
        
        try:
            result = combinatoria(n, k)
            formula_str = f"nCr = n! / (k! × (n - k)!)"
            value_str = f"C({n},{k}) = {n}! / ({k}! × ({n}-{k})!)"
            self.result_var.set(f"C({n},{k}) = {result}")
            self.detail_var.set(f"{formula_str}\n{value_str} = {result}") # Mostrar fórmula y valores
        except ValueError as e:
            messagebox.showerror("Error de Cálculo", str(e))
            self.result_var.set("Resultado: Error")
            self.detail_var.set("")

    def calculate_permutacion(self):
        n, k = self._get_n_k(require_k=True)
        if n is None or k is None:
            return

        try:
            result = permutacion(n, k)
            formula_str = f"nPr = n! / (n - k)!"
            value_str = f"P({n},{k}) = {n}! / ({n}-{k})!"
            self.result_var.set(f"P({n},{k}) = {result}")
            self.detail_var.set(f"{formula_str}\n{value_str} = {result}") # Mostrar fórmula y valores
        except ValueError as e:
            messagebox.showerror("Error de Cálculo", str(e))
            self.result_var.set("Resultado: Error")
            self.detail_var.set("")

    def clear_fields(self):
        self.n_var.set("")
        self.k_var.set("")
        self.result_var.set("Resultado:")
        self.detail_var.set("") # También limpiar los detalles


if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculatorGUI(root)
    root.mainloop()