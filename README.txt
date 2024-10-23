#Archivo 'Ventas_tienda_por_departamento.csv'
# Este archivo es para el análisis de los datos de ventas

## Instrucciones para la configuración del entorno usando venv

### 1. Crear y activar el entorno virtual

# 1.1. Crear el entorno virtual
# Ejecuta el siguiente comando para crear un entorno virtual en la carpeta actual del proyecto:
```bash
python -m venv venv

# 1.2. Activar el entorno virtual
# Para activar el entorno virtual, sigue los pasos según el sistema operativo que estés usando:
# 
# En Windows (desde PowerShell como administrador):
```bash
.\venv\Scripts\activate
# 
# En macOS/Linux:
```bash
source venv/bin/activate
#
# Nota: Si estás usando PowerShell y encuentras problemas de permisos, es posible que necesites cambiar la política de ejecución 
# para scripts con el siguiente comando:
```bash
Set-ExecutionPolicy RemoteSigned -Scope Process
# Luego, presiona Y para confirmar.

# Una vez activado, verás que el prompt de tu terminal cambia, indicando que estás dentro del entorno virtual.

### 2. Instalar las dependencias del proyecto

# Con el entorno virtual activado, instala las dependencias ejecutando el siguiente comando:
```bash
pip install -r requirements.txt
# 
# Este comando instalará todas las bibliotecas necesarias para ejecutar el proyecto.

### 3. Ejecutar el script

# Una vez que las dependencias estén instaladas, puedes ejecutar el archivo principal index.py con el siguiente comando:
```bash
python index.py
# 
# Este comando ejecutará el análisis de datos y generará los archivos necesarios.

### 4. Desactivar el entorno virtual

# Cuando termines de trabajar, puedes desactivar el entorno virtual ejecutando el siguiente comando:
```bash
deactivate
# 
# Esto te devolverá al entorno principal de tu sistema y desactivará el entorno virtual.

---

## Instrucciones para ejecutar el proyecto sin un entorno virtual

### 1. Instalar las dependencias del proyecto
# Si no estás usando un entorno virtual, deberás instalar las bibliotecas necesarias en el entorno global de Python.
# Para instalar las dependencias, ejecuta el siguiente comando desde la carpeta del proyecto:
```bash
pip install -r requirements.txt
# 
# Esto instalará todas las bibliotecas mencionadas en el archivo `requirements.txt` globalmente en tu sistema.

### 2. Ejecutar el script
# Después de que las dependencias estén instaladas, puedes ejecutar el archivo principal `index.py` usando el siguiente comando:
```bash
python index.py
# 
# En algunos sistemas operativos, como macOS o Linux, también puedes usar:
```bash
python3 index.py
# 
# Este comando ejecutará el análisis de datos y generará los archivos necesarios.

### 3. Consideraciones finales
# Si no utilizas un entorno virtual, todas las bibliotecas que instales se guardarán globalmente en tu sistema.
# Esto puede provocar conflictos si trabajas en múltiples proyectos que requieren diferentes versiones de las mismas bibliotecas.
# Por esta razón, es recomendable usar un entorno virtual para proyectos que requieran varias dependencias.


---

## Desactivar la política de ejecución en PowerShell

### 1. ¿Por qué se cambia la política de ejecución?
# En algunos sistemas, PowerShell no permite ejecutar scripts por motivos de seguridad.
# Cambiamos la política de ejecución con el siguiente comando:
```bash
Set-ExecutionPolicy RemoteSigned -Scope Process
# 
# Esto permite ejecutar scripts locales que están firmados digitalmente y scripts remotos sin firmar en la sesión actual de PowerShell.

### 2. ¿Cuándo se desactiva la política de ejecución?
# La política de ejecución que se activa en PowerShell permanece solo durante la sesión actual.
# Si cierras la ventana de PowerShell o reinicias tu sistema, la política vuelve a su valor por defecto.

### 3. Desactivación manual (opcional)
# Si deseas restablecer la política de ejecución a su valor predeterminado dentro de la misma sesión de PowerShell, 
# puedes hacerlo con el siguiente comando:
```bash
Set-ExecutionPolicy Restricted -Scope Process
# 
# Este comando restablece la política de ejecución a la configuración que bloquea la ejecución de scripts.
# Alternativamente, puedes usar:
```bash
Set-ExecutionPolicy Default -Scope Process
# 
# Esto restaurará la política de ejecución a la que esté definida por el sistema o la configuración del usuario.

### 4. Consideraciones finales
# No es necesario ejecutar estos comandos si solo planeas cerrar PowerShell después de trabajar con el entorno virtual.
# Al abrir una nueva sesión, PowerShell volverá automáticamente a su política de ejecución predeterminada.
