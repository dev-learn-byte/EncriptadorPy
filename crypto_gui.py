"""
pCrypto - Sistema de Encriptación
Interfaz gráfica para encriptar/desencriptar contraseñas con AES-256-GCM
Versión 2: Genera llave automáticamente al primer inicio
"""
import customtkinter as ctk
import os
import base64
import pyperclip
import time
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from tkinter import messagebox


class CryptoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración de ventana
        self.title("pCrypto - Sistema de Encriptación")
        self.geometry("700x800")
        self.resizable(True, True)
        self.minsize(650, 700)
        
        # Colores
        self.color_azul_oscuro = "#1E40AF"
        self.color_azul = "#3B82F6"
        self.color_azul_claro = "#EFF6FF"
        self.color_azul_medio = "#DBEAFE"
        self.color_gris = "#64748B"
        
        # Configurar tema
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Variables
        self.show_password1 = False
        self.show_password2 = False
        self.accion_var = ctk.StringVar(value="encriptar")
        
        # Verificar si existe la llave, si no, mostrar pantalla de carga
        if not self.verificar_llave_existe():
            self.mostrar_pantalla_carga()
        else:
            # Crear interfaz
            self.crear_interfaz()
            self.accion_var.trace_add("write", self.on_action_change)
    
    def verificar_llave_existe(self):
        """Verifica si la llave de encriptación ya existe"""
        key_file = Path.home() / '.crypto_keys' / 'encryption_key.key'
        return key_file.exists()
    
    def generar_llave_automatica(self):
        """Genera la llave AES-256 automáticamente"""
        try:
            key_dir = Path.home() / '.crypto_keys'
            key_dir.mkdir(exist_ok=True, mode=0o700)
            
            key_file = key_dir / 'encryption_key.key'
            key = os.urandom(32)
            key_b64 = base64.b64encode(key)
            
            with open(key_file, 'wb') as f:
                f.write(key_b64)
            
            try:
                os.chmod(key_file, 0o400)
            except:
                pass
            
            return True
        except Exception as e:
            print(f"Error al generar llave: {e}")
            return False
    
    def mostrar_pantalla_carga(self):
        """Muestra pantalla de carga con barra de progreso"""
        # Frame principal
        self.geometry("600x400")
        self.resizable(False, False)
        
        main_frame = ctk.CTkFrame(self, fg_color="#0F172A")
        main_frame.pack(fill="both", expand=True)
        
        # Card de carga
        card = ctk.CTkFrame(main_frame, fg_color="#1E293B", corner_radius=15)
        card.pack(expand=True, padx=40, pady=40)
        
        # Header azul
        header_card = ctk.CTkFrame(card, fg_color=self.color_azul, corner_radius=15)
        header_card.pack(fill="x", padx=3, pady=3)
        
        ctk.CTkLabel(
            header_card,
            text="⏳ Inicializando...",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="white"
        ).pack(pady=15)
        
        # Contenido
        content = ctk.CTkFrame(card, fg_color="#334155")
        content.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(
            content,
            text="Generando llave de encriptación...",
            font=ctk.CTkFont(size=14),
            text_color="#F1F5F9"
        ).pack(pady=(0, 30))
        
        # Barra de progreso
        self.progress_bar = ctk.CTkProgressBar(
            content,
            height=22,
            fg_color="#475569",
            progress_color=self.color_azul
        )
        self.progress_bar.pack(fill="x", pady=(0, 10))
        self.progress_bar.set(0)

        self.progress_label = ctk.CTkLabel(
            self.progress_bar,
            text="0%",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="white"
        )
        self.progress_label.place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkLabel(
            content,
            text="(solo se hace una sola vez)",
            font=ctk.CTkFont(size=11),
            text_color="#94A3B8"
        ).pack()
        
        # Iniciar generación de llave
        self.after(500, self.generar_y_mostrar_exito)
    
    def generar_y_mostrar_exito(self):
        """Genera la llave y muestra éxito"""
        # Simular progreso
        for i in range(101):
            self.progress_bar.set(i / 100)
            self.progress_label.configure(text=f"{i}%")
            self.update()
            time.sleep(0.01)  # Esperar 10ms
        
        # Generar llave
        if self.generar_llave_automatica():
            # Mostrar éxito después de 500ms
            self.after(500, self.mostrar_exito)
        else:
            messagebox.showerror("Error", "No se pudo generar la llave")
            self.quit()
    
    def mostrar_exito(self):
        """Muestra pantalla de éxito"""
        # Limpiar
        for widget in self.winfo_children():
            widget.destroy()
        
        # Nueva ventana
        main_frame = ctk.CTkFrame(self, fg_color="#0F172A")
        main_frame.pack(fill="both", expand=True)
        
        # Card de éxito
        card = ctk.CTkFrame(main_frame, fg_color="#1E293B", corner_radius=15)
        card.pack(expand=True, padx=40, pady=40)
        
        # Header azul
        header_card = ctk.CTkFrame(card, fg_color=self.color_azul, corner_radius=15)
        header_card.pack(fill="x", padx=3, pady=3)
        
        ctk.CTkLabel(
            header_card,
            text="✅ ¡Listo!",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="white"
        ).pack(pady=15)
        
        # Contenido
        content = ctk.CTkFrame(card, fg_color="#334155")
        content.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(
            content,
            text="Llave generada exitosamente.",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#F1F5F9"
        ).pack(pady=(0, 10))
        
        ctk.CTkLabel(
            content,
            text="Ya puedes encriptar tus contraseñas.",
            font=ctk.CTkFont(size=12),
            text_color="#E2E8F0"
        ).pack(pady=(0, 30))
        
        # Botón comenzar
        ctk.CTkButton(
            content,
            text="Comenzar",
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=self.color_azul,
            hover_color="#2563EB",
            command=self.ir_a_interfaz_principal
        ).pack(pady=(20, 0))
    
    def ir_a_interfaz_principal(self):
        """Limpia y muestra la interfaz principal"""
        for widget in self.winfo_children():
            widget.destroy()
        
        self.geometry("700x800")
        self.resizable(True, True)
        self.minsize(650, 700)
        
        self.crear_interfaz()
        self.accion_var.trace_add("write", self.on_action_change)
        
    def crear_interfaz(self):
        # Header
        header = ctk.CTkFrame(self, fg_color=self.color_azul_oscuro, height=70, corner_radius=0)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)
        
        titulo = ctk.CTkLabel(
            header,
            text="🔐 pCrypto - Sistema de Encriptación",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="white"
        )
        titulo.pack(pady=20)
        
        # Contenedor principal
        main_container = ctk.CTkFrame(self, fg_color="white")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Card 1: Ingreso de Clave
        card1 = ctk.CTkFrame(main_container, fg_color=self.color_azul_claro, corner_radius=10)
        card1.pack(fill="x", pady=(0, 15))
        
        card1_header = ctk.CTkFrame(card1, fg_color=self.color_azul, corner_radius=10)
        card1_header.pack(fill="x", padx=2, pady=2)
        
        ctk.CTkLabel(
            card1_header,
            text="🔐 Procesamiento de Encriptacion",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="white"
        ).pack(pady=10)
        
        # Campo 1: Clave a Cifrar
        content1 = ctk.CTkFrame(card1, fg_color=self.color_azul_claro)
        content1.pack(fill="x", padx=15, pady=(10, 5))
        
        ctk.CTkLabel(
            content1,
            text="Clave a Cifrar:",
            font=ctk.CTkFont(size=14),
            text_color=self.color_azul_oscuro
        ).pack(anchor="w", pady=(5, 5))
        
        password1_frame = ctk.CTkFrame(content1, fg_color="transparent")
        password1_frame.pack(fill="x")
        
        self.password1_entry = ctk.CTkEntry(
            password1_frame,
            placeholder_text="Ingresa la clave...",
            show="●",
            height=40,
            font=ctk.CTkFont(size=13),
            border_color=self.color_azul,
            border_width=2
        )
        self.password1_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self._add_focus_style(self.password1_entry)
        
        self.toggle_btn1 = ctk.CTkButton(
            password1_frame,
            text="👁",
            width=40,
            height=40,
            fg_color=self.color_azul,
            hover_color="#2563EB",
            command=self.toggle_password1
        )
        self.toggle_btn1.pack(side="right")
        
        # Campo 2: Confirmar Clave
        content2 = ctk.CTkFrame(card1, fg_color=self.color_azul_claro)
        content2.pack(fill="x", padx=15, pady=(10, 15))
        
        ctk.CTkLabel(
            content2,
            text="Confirmar Clave:",
            font=ctk.CTkFont(size=14),
            text_color=self.color_azul_oscuro
        ).pack(anchor="w", pady=(5, 5))
        
        password2_frame = ctk.CTkFrame(content2, fg_color="transparent")
        password2_frame.pack(fill="x")
        
        self.password2_entry = ctk.CTkEntry(
            password2_frame,
            placeholder_text="Confirma la clave...",
            show="●",
            height=40,
            font=ctk.CTkFont(size=13),
            border_color=self.color_azul,
            border_width=2
        )
        self.password2_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self._add_focus_style(self.password2_entry)
        
        self.toggle_btn2 = ctk.CTkButton(
            password2_frame,
            text="👁",
            width=40,
            height=40,
            fg_color=self.color_azul,
            hover_color="#2563EB",
            command=self.toggle_password2
        )
        self.toggle_btn2.pack(side="right")
        
        # Radio buttons
        radio_frame = ctk.CTkFrame(main_container, fg_color="white")
        radio_frame.pack(fill="x", pady=(0, 15))
        
        ctk.CTkLabel(
            radio_frame,
            text="Acción:",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.color_azul_oscuro
        ).pack(side="left", padx=(0, 20))
        
        ctk.CTkRadioButton(
            radio_frame,
            text="Encriptar",
            variable=self.accion_var,
            value="encriptar",
            font=ctk.CTkFont(size=13),
            fg_color=self.color_azul,
            hover_color="#2563EB"
        ).pack(side="left", padx=10)
        
        ctk.CTkRadioButton(
            radio_frame,
            text="Desencriptar",
            variable=self.accion_var,
            value="desencriptar",
            font=ctk.CTkFont(size=13),
            fg_color=self.color_azul,
            hover_color="#2563EB"
        ).pack(side="left", padx=10)
        
        # Card 2: Resultado
        card2 = ctk.CTkFrame(main_container, fg_color=self.color_azul_claro, corner_radius=10)
        card2.pack(fill="both", expand=True, pady=(0, 15))
        
        card2_header = ctk.CTkFrame(card2, fg_color=self.color_azul, corner_radius=10)
        card2_header.pack(fill="x", padx=2, pady=2)
        
        ctk.CTkLabel(
            card2_header,
            text="✅ Resultado",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="white"
        ).pack(pady=10)
        
        result_content = ctk.CTkFrame(card2, fg_color=self.color_azul_claro)
        result_content.pack(fill="both", expand=True, padx=15, pady=(10, 15))
        
        result_frame = ctk.CTkFrame(result_content, fg_color="white")
        result_frame.pack(fill="both", expand=True)
        
        self.result_text = ctk.CTkTextbox(
            result_frame,
            height=80,
            font=ctk.CTkFont(size=12),
            fg_color="white",
            border_color=self.color_azul,
            border_width=2,
            wrap="word"
        )
        self.result_text.pack(fill="both", expand=True, padx=10, pady=10)
        self.result_text.configure(state="disabled")
        
        self.copy_btn = ctk.CTkButton(
            result_frame,
            text="📋 Copiar",
            height=35,
            fg_color=self.color_azul,
            hover_color="#2563EB",
            command=self.copiar_resultado
        )
        self.copy_btn.pack(pady=(0, 10))
        
        # Botones principales
        button_frame = ctk.CTkFrame(main_container, fg_color="white")
        button_frame.pack(fill="x")
        
        ctk.CTkButton(
            button_frame,
            text="Procesar",
            height=45,
            width=180,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.color_azul,
            hover_color="#2563EB",
            command=self.procesar
        ).pack(side="left", expand=True, padx=5)
        
        ctk.CTkButton(
            button_frame,
            text="Limpiar",
            height=45,
            width=180,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#60A5FA",
            hover_color="#3B82F6",
            command=self.limpiar
        ).pack(side="left", expand=True, padx=5)
        
        ctk.CTkButton(
            button_frame,
            text="Salir",
            height=45,
            width=180,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.color_gris,
            hover_color="#475569",
            command=self.quit
        ).pack(side="left", expand=True, padx=5)
    
    def toggle_password1(self):
        self.show_password1 = not self.show_password1
        self.password1_entry.configure(show="" if self.show_password1 else "●")
    
    def toggle_password2(self):
        self.show_password2 = not self.show_password2
        self.password2_entry.configure(show="" if self.show_password2 else "●")
    
    def _add_focus_style(self, entry_widget):
        """Aplica un borde más intenso al enfocar."""
        def on_focus_in(_event):
            entry_widget.configure(border_color="#2563EB")

        def on_focus_out(_event):
            entry_widget.configure(border_color=self.color_azul)

        entry_widget.bind("<FocusIn>", on_focus_in)
        entry_widget.bind("<FocusOut>", on_focus_out)

    def on_action_change(self, *args):
        """Habilita/deshabilita confirmación según acción."""
        if self.accion_var.get() == "desencriptar":
            self.password2_entry.configure(state="disabled")
            self.toggle_btn2.configure(state="disabled")
        else:
            self.password2_entry.configure(state="normal")
            self.toggle_btn2.configure(state="normal")
    
    def cargar_llave(self):
        """Carga la llave AES-256 desde el archivo"""
        key_file = Path.home() / '.crypto_keys' / 'encryption_key.key'
        
        if not key_file.exists():
            messagebox.showerror(
                "Error",
                "No se encuentra la llave de encriptación.\n\n"
                "Primero ejecuta: python generate_key.py"
            )
            return None
        
        try:
            with open(key_file, 'rb') as f:
                key_b64 = f.read()
            return base64.b64decode(key_b64)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer la llave:\n{e}")
            return None
    
    def encriptar_clave(self, password):
        """Encripta una contraseña con AES-256-GCM"""
        key = self.cargar_llave()
        if not key:
            return None
        
        try:
            cipher = AESGCM(key)
            iv = os.urandom(12)
            ciphertext = cipher.encrypt(iv, password.encode(), None)
            encrypted = base64.b64encode(iv + ciphertext).decode()
            return encrypted
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo encriptar:\n{e}")
            return None
    
    def desencriptar_clave(self, encrypted):
        """Desencripta una contraseña con AES-256-GCM"""
        key = self.cargar_llave()
        if not key:
            return None
        
        try:
            cipher = AESGCM(key)
            data = base64.b64decode(encrypted)
            iv = data[:12]
            ciphertext = data[12:]
            decrypted = cipher.decrypt(iv, ciphertext, None)
            return decrypted.decode()
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"No se pudo desencriptar:\n{e}\n\n"
                "Verifica que hayas copiado correctamente la clave encriptada."
            )
            return None
    
    def procesar(self):
        """Procesa la acción seleccionada"""
        password1 = self.password1_entry.get()
        password2 = self.password2_entry.get()
        accion = self.accion_var.get()
        
        # Validaciones
        if not password1:
            messagebox.showwarning("Advertencia", "Debes ingresar una clave")
            return
        
        # Validar espacios
        if any(ch.isspace() for ch in password1):
            messagebox.showerror("Error", "La clave no puede contener espacios")
            return
        
        if accion == "encriptar":
            # Validar confirmación
            if not password2:
                messagebox.showwarning("Advertencia", "Debes confirmar la clave")
                return
            
            if any(ch.isspace() for ch in password2):
                messagebox.showerror("Error", "La confirmación no puede contener espacios")
                return
            
            if password1 != password2:
                messagebox.showerror("Error", "Las claves no coinciden")
                return
            
            # Encriptar
            resultado = self.encriptar_clave(password1)
            if resultado:
                self.result_text.configure(state="normal")
                self.result_text.delete("1.0", "end")
                self.result_text.insert("1.0", resultado)
                self.result_text.configure(state="disabled")
                messagebox.showinfo("Éxito", "Clave encriptada exitosamente")
        
        else:  # desencriptar
            # Desencriptar (password1 contiene el token encriptado)
            resultado = self.desencriptar_clave(password1)
            if resultado:
                self.result_text.configure(state="normal")
                self.result_text.delete("1.0", "end")
                self.result_text.insert("1.0", resultado)
                self.result_text.configure(state="disabled")
                messagebox.showinfo("Éxito", "Clave desencriptada exitosamente")
    
    def limpiar(self):
        """Limpia todos los campos"""
        self.password1_entry.delete(0, "end")
        self.password2_entry.delete(0, "end")
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.configure(state="disabled")
        self.accion_var.set("encriptar")
        self.show_password1 = False
        self.show_password2 = False
        self.password1_entry.configure(show="●")
        self.password2_entry.configure(show="●")
    
    def copiar_resultado(self):
        """Copia el resultado al portapapeles"""
        resultado = self.result_text.get("1.0", "end").strip()
        if resultado:
            pyperclip.copy(resultado)
            messagebox.showinfo("Éxito", "Resultado copiado al portapapeles")
        else:
            messagebox.showwarning("Advertencia", "No hay resultado para copiar")


if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()
