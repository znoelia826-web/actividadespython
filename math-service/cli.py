import tkinter as tk
from tkinter import messagebox
import socket
import threading

# === CONFIGURACIÓN ===
SERVER_IP = "172.17.131.155"
SERVER_PORT = 5000

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Calculadora Concurrente - Cliente")
        self.root.geometry("420x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")  # Fondo oscuro elegante

        # Variables
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Esperando operación...")

        # Socket
        self.client_socket = None

        # Construir interfaz
        self.create_widgets()
        self.connect_to_server()

    def create_widgets(self):
        # === Título ===
        title = tk.Label(
            self.root,
            text="🧮 Calculadora Concurrente",
            font=("Segoe UI", 18, "bold"),
            bg="#1a1a2e",
            fg="#ffd700"
        )
        title.pack(pady=(15, 5))

        # === Pantalla de Resultado ===
        result_frame = tk.LabelFrame(
            self.root,
            text=" Pantalla de Resultado ",
            font=("Segoe UI", 12, "bold"),
            fg="#dddddd",
            bg="#162447",
            bd=2,
            relief="groove"
        )
        result_frame.pack(pady=(5, 15), padx=30, fill="x")

        self.result_display = tk.Entry(
            result_frame,
            textvariable=self.result_var,
            font=("Consolas", 16, "bold"),
            justify="center",
            state="readonly",
            readonlybackground="#0f3460",
            fg="#00ff9d",
            relief="flat",
            bd=0,
            highlightthickness=0
        )
        self.result_display.pack(padx=10, pady=10, fill="x")

        # === Marco de entradas ===
        input_frame = tk.Frame(self.root, bg="#1a1a2e")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Número 1:", font=("Segoe UI", 12), bg="#1a1a2e", fg="#ffffff").grid(row=0, column=0, sticky="e", padx=5, pady=8)
        num1_entry = tk.Entry(input_frame, textvariable=self.num1_var, font=("Segoe UI", 14), width=12, justify="center", relief="solid", bd=1)
        num1_entry.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(input_frame, text="Número 2:", font=("Segoe UI", 12), bg="#1a1a2e", fg="#ffffff").grid(row=1, column=0, sticky="e", padx=5, pady=8)
        num2_entry = tk.Entry(input_frame, textvariable=self.num2_var, font=("Segoe UI", 14), width=12, justify="center", relief="solid", bd=1)
        num2_entry.grid(row=1, column=1, padx=10, pady=8)

        # === Botones de operación ===
        op_frame = tk.Frame(self.root, bg="#1a1a2e")
        op_frame.pack(pady=15)

        self.operation = tk.StringVar(value="add")

        # Primera fila: Suma y Resta
        add_btn = tk.Radiobutton(
            op_frame,
            text="➕ Sumar",
            variable=self.operation,
            value="add",
            indicatoron=0,
            width=14,
            font=("Segoe UI", 12, "bold"),
            bg="#00b894",
            fg="white",
            selectcolor="#00b894",
            activebackground="#019875",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8
        )
        add_btn.grid(row=0, column=0, padx=8, pady=5)

        sub_btn = tk.Radiobutton(
            op_frame,
            text="➖ Restar",
            variable=self.operation,
            value="sub",
            indicatoron=0,
            width=14,
            font=("Segoe UI", 12, "bold"),
            bg="#0984e3",
            fg="white",
            selectcolor="#0984e3",
            activebackground="#0652c5",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8
        )
        sub_btn.grid(row=0, column=1, padx=8, pady=5)

        # Segunda fila: Multiplicación y División
        mul_btn = tk.Radiobutton(
            op_frame,
            text="✖️ Multiplicar",
            variable=self.operation,
            value="mul",
            indicatoron=0,
            width=14,
            font=("Segoe UI", 12, "bold"),
            bg="#fd79a8",
            fg="white",
            selectcolor="#fd79a8",
            activebackground="#d6306a",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8
        )
        mul_btn.grid(row=1, column=0, padx=8, pady=5)

        div_btn = tk.Radiobutton(
            op_frame,
            text="➗ Dividir",
            variable=self.operation,
            value="div",
            indicatoron=0,
            width=14,
            font=("Segoe UI", 12, "bold"),
            bg="#6c5ce7",
            fg="white",
            selectcolor="#6c5ce7",
            activebackground="#341f97",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8
        )
        div_btn.grid(row=1, column=1, padx=8, pady=5)

        # === Botón Calcular ===
        calc_btn = tk.Button(
            self.root,
            text="🚀 Calcular",
            command=self.send_calculation,
            font=("Segoe UI", 13, "bold"),
            bg="#00cec9",
            fg="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            activebackground="#009c9f"
        )
        calc_btn.pack(pady=12)

        # === Botón Salir ===
        exit_btn = tk.Button(
            self.root,
            text="❌ Salir",
            command=self.on_closing,
            font=("Segoe UI", 10),
            bg="#e17055",
            fg="white",
            relief="flat",
            padx=15,
            pady=5,
            cursor="hand2",
            activebackground="#d35400"
        )
        exit_btn.pack(pady=5)

    def connect_to_server(self):
        def connect():
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((SERVER_IP, SERVER_PORT))
                self.update_result("✅ Conectado al servidor")
            except Exception as e:
                self.update_result("❌ Error: Sin conexión")
                messagebox.showerror(
                    "Error de conexión",
                    f"No se pudo conectar al servidor en {SERVER_IP}:{SERVER_PORT}\n\nError: {e}"
                )
                self.root.after(2000, self.root.quit)
        threading.Thread(target=connect, daemon=True).start()

    def update_result(self, text):
        self.result_var.set(text)

    def send_calculation(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
        except ValueError:
            self.update_result("⚠️ Ingresa números válidos")
            return

        op = self.operation.get()
        request = f"{num1},{num2},{op}"

        def communicate():
            try:
                if not self.client_socket:
                    raise Exception("Socket no inicializado")
                self.client_socket.send(request.encode('utf-8'))
                response = self.client_socket.recv(1024).decode('utf-8').strip()

                if response.startswith("RESULT:"):
                    result = response.split(":", 1)[1]
                    self.update_result(f"= {result}")
                elif response.startswith("ERROR:"):
                    error_msg = response.split(":", 1)[1]
                    self.update_result(f"❌ {error_msg}")
                else:
                    self.update_result("⚠️ Respuesta no válida")

            except Exception as e:
                self.update_result("❌ Error de red")
                messagebox.showerror("Error", f"Fallo en la comunicación:\n{e}")
                self.on_closing()

        threading.Thread(target=communicate, daemon=True).start()

    def on_closing(self):
        try:
            if self.client_socket:
                self.client_socket.send(b"quit")
                self.client_socket.close()
        except:
            pass
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
