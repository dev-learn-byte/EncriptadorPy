# pCrypto - Sistema de Encriptación

![Versión](https://img.shields.io/badge/versión-2.0-blue)
![Python](https://img.shields.io/badge/Python-3.14-green)
![Licencia](https://img.shields.io/badge/licencia-MIT-yellow)

Sistema profesional de encriptación/desencriptación de contraseñas con interfaz gráfica moderna, utilizando algoritmo AES-256-GCM con compatibilidad Java.

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Instalación](#-instalación)
- [Uso de la Aplicación](#-uso-de-la-aplicación)
- [Compilación a Ejecutable](#-compilación-a-ejecutable)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Documentación Técnica](#-documentación-técnica)
- [Changelog](#-changelog)

---

## 🚀 Características

### Funcionalidades Principales
- ✅ **Encriptación AES-256-GCM** - Máxima seguridad con autenticación de datos
- ✅ **Compatibilidad Java** - Tokens encriptados interoperables con sistemas Java
- ✅ **Interfaz Gráfica Moderna** - Diseñada con CustomTkinter (tema claro profesional)
- ✅ **Auto-generación de Llave** - Primera ejecución genera llave automáticamente con splash screen
- ✅ **Gestión de Visibilidad** - Botones para mostrar/ocultar contraseñas
- ✅ **Validación de Entrada** - No permite espacios en contraseñas, confirma coincidencias
- ✅ **Copiar al Portapapeles** - Un clic para copiar resultados
- ✅ **Ejecutable Standalone** - No requiere Python instalado en el equipo final

### Seguridad
- 🔐 Algoritmo: **AES-256-GCM** (256 bits de clave, IV único de 12 bytes por encriptación)
- 🔑 Llave almacenada en: `~/.crypto_keys/as400_key.key` (permisos 400 en Unix)
- 🎲 Cada encriptación genera un token único (IV aleatorio)
- ✅ Formato Base64 para almacenamiento y transporte

---

## 🛠 Tecnologías

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.14.2 | Lenguaje principal |
| **CustomTkinter** | Última | Framework GUI moderno |
| **cryptography** | Última | Librería de encriptación AES-256-GCM |
| **pyperclip** | Última | Copiar al portapapeles |
| **PyInstaller** | 6.18.0 | Compilación a .exe |

### Paleta de Colores
```python
Azul Oscuro:    #1E40AF  # Header principal
Azul:           #3B82F6  # Botones y acciones primarias
Azul Hover:     #2563EB  # Hover en botones
Azul Claro:     #EFF6FF  # Fondos de cards (modo claro)
Azul Medio:     #DBEAFE  # Fondos secundarios
Gris:           #64748B  # Botón salir

# Splash Screen (Tema Oscuro)
Fondo:          #0F172A  # Azul muy oscuro
Card:           #1E293B  # Gris azulado oscuro
Content:        #334155  # Gris medio
Texto:          #F1F5F9  # Blanco cremoso
Progress Bar:   #475569  # Gris para barra vacía
Porcentaje:     #FFFFFF  # Blanco para texto de porcentaje
```

---

## 📥 Instalación

### Opción 1: Usar el Ejecutable (Recomendado para usuarios finales)
```bash
# Simplemente ejecutar:
dist/pCrypto.exe
```

### Opción 2: Ejecutar desde Código Fuente (Desarrollo)
```bash
# 1. Clonar/descargar el proyecto
cd path/to/pCryptoShadow

# 2. Crear entorno virtual
python -m venv .venv

# 3. Activar entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# 4. Instalar dependencias
pip install customtkinter cryptography pyperclip pyinstaller

# 5. Ejecutar aplicación
python crypto_gui.py
```

---

## 🎯 Uso de la Aplicación

### Primera Ejecución
1. La aplicación detecta que no existe llave de encriptación
2. Muestra **splash screen** con barra de progreso animada (0-100%)
3. Genera automáticamente la llave AES-256 en `~/.crypto_keys/as400_key.key`
4. Muestra pantalla de éxito: "✅ ¡Listo! Llave generada exitosamente"
5. Click en "Comenzar" para ir a la interfaz principal

### Encriptar una Contraseña
1. Seleccionar radio button **"Encriptar"**
2. Ingresar contraseña en "Clave a Cifrar"
3. Confirmar la misma contraseña en "Confirmar Clave"
4. Click en botón **"Procesar"**
5. El resultado aparece en el textbox de "Resultado" (solo lectura)
6. Click en **"📋 Copiar"** para copiar al portapapeles

**Validaciones:**
- ❌ No permite espacios en la contraseña
- ❌ Ambos campos deben coincidir
- ❌ No permite campos vacíos

### Desencriptar un Token
1. Seleccionar radio button **"Desencriptar"**
2. Pegar el token encriptado en "Clave a Cifrar" (el campo "Confirmar Clave" se deshabilita automáticamente)
3. Click en botón **"Procesar"**
4. La contraseña original aparece en "Resultado"
5. Click en **"📋 Copiar"** para copiar

### Botones Adicionales
- **Limpiar**: Borra todos los campos y resetea a modo "Encriptar"
- **Salir**: Cierra la aplicación

---

## 🔨 Compilación a Ejecutable

### Comando de Compilación
```bash
# Asegurarse de estar en el directorio del proyecto
cd path/to/pCryptoShadow

# Activar entorno virtual
.venv\Scripts\activate

# Compilar a ejecutable
pyinstaller --onefile --noconsole --name "pCrypto" crypto_gui.py
```

### Parámetros Explicados
| Parámetro | Descripción |
|-----------|-------------|
| `--onefile` | Genera un único archivo .exe (no carpeta con DLLs) |
| `--noconsole` | No muestra ventana de consola negra al ejecutar |
| `--name "pCrypto"` | Nombre del ejecutable resultante |
| `crypto_gui.py` | Archivo Python principal a compilar |

### Resultado de la Compilación
```
pCryptoShadow/
├── dist/
│   └── pCrypto.exe          ← Ejecutable final (~15.7 MB)
├── build/                   ← Archivos temporales (se puede borrar)
├── pCrypto.spec             ← Configuración de PyInstaller (auto-generado)
└── crypto_gui.py            ← Código fuente
```

**⚠️ Importante:**
- El archivo `.spec` se genera automáticamente (no necesita versionarse)
- Solo distribuir el archivo `dist/pCrypto.exe`
- La carpeta `build/` se puede eliminar después de compilar

---

## 📁 Estructura del Proyecto

```
pCryptoShadow/
│
├── crypto_gui.py              # Aplicación principal con GUI (v2.0)
├── encrypt_password.py        # Script CLI para encriptar (validación)
├── decrypt_password.py        # Script CLI para desencriptar (validación)
├── generate_key.py            # Generador manual de llave (obsoleto en v2)
├── README.md                  # Este archivo
│
├── dist/                      # Ejecutables compilados
│   └── pCrypto.exe           # Aplicación standalone
│
├── build/                     # Archivos temporales de PyInstaller
├── pCrypto.spec              # Configuración de PyInstaller (auto-generado)
│
├── .venv/                     # Entorno virtual Python
├── .vscode/                   # Configuración de VS Code
├── .idea/                     # Configuración de PyCharm
└── .history/                  # Historial de ediciones

# En el home del usuario:
~/.crypto_keys/
└── encryption_key.key             # Llave AES-256 (32 bytes en Base64)
```

---

## 📖 Documentación Técnica

### Algoritmo de Encriptación

**AES-256-GCM (Galois/Counter Mode)**
```python
# Proceso de Encriptación
1. Cargar llave de 32 bytes desde ~/.crypto_keys/as400_key.key
2. Generar IV aleatorio de 12 bytes (único por encriptación)
3. Encriptar con AES-256-GCM: plaintext → ciphertext + tag (16 bytes)
4. Concatenar: IV (12) + ciphertext + tag
5. Codificar en Base64 para almacenamiento
6. Retornar token Base64

# Proceso de Desencriptación
1. Decodificar token desde Base64
2. Extraer IV (primeros 12 bytes)
3. Extraer ciphertext + tag (resto)
4. Desencriptar con AES-256-GCM usando IV y llave
5. Retornar plaintext original
```

### Formato del Token Encriptado
```
[IV: 12 bytes][Ciphertext: variable][Auth Tag: 16 bytes]
          ↓ Base64 encoding ↓
"A8fKl3mQ9xP2tY..." (string almacenable)
```

### Compatibilidad Java
Los tokens generados por pCrypto son **100% compatibles** con implementaciones Java estándar de AES-256-GCM, ya que:
- Usa el mismo formato de IV (12 bytes)
- Tag de autenticación de 128 bits (16 bytes)
- Encoding Base64 estándar
- Sin padding (modo GCM no requiere padding)

**Ejemplo Java para desencriptar:**
```java
import javax.crypto.Cipher;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class DecryptPython {
    public static String decrypt(String encryptedBase64, byte[] key) throws Exception {
        byte[] decoded = Base64.getDecoder().decode(encryptedBase64);
        
        byte[] iv = Arrays.copyOfRange(decoded, 0, 12);
        byte[] ciphertext = Arrays.copyOfRange(decoded, 12, decoded.length);
        
        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
        GCMParameterSpec spec = new GCMParameterSpec(128, iv);
        SecretKeySpec keySpec = new SecretKeySpec(key, "AES");
        
        cipher.init(Cipher.DECRYPT_MODE, keySpec, spec);
        byte[] plaintext = cipher.doFinal(ciphertext);
        
        return new String(plaintext, "UTF-8");
    }
}
```

### Validaciones Implementadas

| Validación | Acción | Modo |
|------------|--------|------|
| Espacios en contraseña | ❌ Error | Encriptar/Desencriptar |
| Campo vacío | ⚠️ Advertencia | Ambos |
| Contraseñas no coinciden | ❌ Error | Solo Encriptar |
| Token inválido | ❌ Error en desencriptación | Solo Desencriptar |
| Llave no encontrada | ✅ Auto-genera con splash | Primer inicio |

---

## 📝 Changelog

### Versión 2.0 (2 de febrero de 2026) - **ACTUAL**
#### ✨ Nuevas Características
- **Auto-generación de llave** en primer inicio con splash screen
- **Barra de progreso animada** con porcentaje dentro de la barra (Estilo 4)
- **Tema oscuro** para splash screen (Azul Oscuro Profundo #0F172A)
- Pantalla de éxito después de generar llave
- Animación suave 0→100% con actualización cada 10ms

#### 🎨 Mejoras de UX
- Splash screen profesional con card y header
- Porcentaje visible dentro de la barra de progreso
- Colores optimizados para no cansar la vista
- Transición fluida: Loading → Éxito → Interfaz principal

#### 🐛 Correcciones
- Fix: Reemplazado `self.after(10)` por `time.sleep(0.01)` para animación correcta
- Fix: Actualización sincronizada de barra y porcentaje

---

### Versión 1.0 (26 de enero de 2026)
#### ✨ Características Iniciales
- Encriptación/desencriptación con AES-256-GCM
- Interfaz gráfica con CustomTkinter (Modelo 3: Card con Secciones)
- Radio buttons para cambiar entre Encriptar/Desencriptar
- Botones de visibilidad de contraseñas (👁)
- Validación de entrada (sin espacios, confirmación)
- Textbox de resultado en solo lectura
- Botón copiar al portapapeles
- Focus styling en campos de entrada (border color change)
- Botón "Confirmar Clave" se deshabilita en modo Desencriptar

#### 🎨 Diseño
- Header azul oscuro con título "🔐 pCrypto - Sistema de Encriptación"
- Cards con fondos azul claro
- Botones azul (#3B82F6) con hover (#2563EB)
- Botón salir en gris (#64748B)

#### 📦 Compilación
- Primera compilación exitosa con PyInstaller
- Ejecutable de ~15.7 MB

---

## 🔐 Seguridad y Mejores Prácticas

### Almacenamiento de Llave
- **Ubicación:** `~/.crypto_keys/encryption_key.key` (directorio home del usuario)
- **Permisos:** 0o400 (solo lectura, solo propietario) en sistemas Unix
- **Formato:** 32 bytes aleatorios codificados en Base64
- **Generación:** `os.urandom(32)` - Cryptographically secure random

### Recomendaciones
1. ✅ **No compartir el archivo `.key`** - Es como compartir una contraseña maestra
2. ✅ **Backup de la llave** - Sin ella no se pueden desencriptar tokens antiguos
3. ✅ **No versionar la llave** - Nunca subir `as400_key.key` a Git
4. ✅ **Regenerar llave** - Solo si es necesario (invalida tokens previos)
5. ✅ **Usar HTTPS** - Si se transmiten tokens por red

### Limitaciones Conocidas
- ⚠️ Contraseñas no pueden contener espacios (validación estricta)
- ⚠️ Campo "Confirmar Clave" se deshabilita en modo Desencriptar (puede parecer un bug visualmente)
- ⚠️ En Windows, permisos de archivo no son tan restrictivos como en Unix

---

## 👨‍💻 Desarrollo

### Entorno de Desarrollo
```bash
# Instalar dependencias de desarrollo
pip install customtkinter cryptography pyperclip pyinstaller

# Ejecutar en modo desarrollo
python crypto_gui.py

# Compilar para distribución
pyinstaller --onefile --noconsole --name "pCrypto" crypto_gui.py
```

### Scripts Auxiliares
- `encrypt_password.py` - CLI para pruebas de encriptación
- `decrypt_password.py` - CLI para pruebas de desencriptación
- `generate_key.py` - Generador manual de llave (ya no necesario en v2)

---

## 🤝 Contribución

Este es un proyecto interno de Sprint 5. Para contribuir:
1. Crear branch desde `main`
2. Realizar cambios y testear exhaustivamente
3. Actualizar este README.md si se añaden características
4. Crear Pull Request con descripción detallada

---

## 📄 Licencia

Proyecto interno - Todos los derechos reservados.

---

## 📞 Soporte

Para reportar bugs o solicitar características:
- Crear issue en el repositorio interno
- Contactar al equipo de desarrollo de Sprint 5

---



*Última actualización: 2 de febrero de 2026*
