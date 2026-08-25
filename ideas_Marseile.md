# Ejercicios de proyectos con Python (casos reales)

Estos son proyectos chicos pero completos, pensados para que integres archivos, loops, funciones y regex en algo que de verdad podrías usar. Intenta resolver cada uno antes de pedirme la solución.

---

## Bloque 1 — Automatización de archivos

### 1. Organizador de descargas
Un script que recorra una carpeta (la de Descargas, por ejemplo) y mueva los archivos a subcarpetas según su extensión (`pdf/`, `imagenes/`, `instaladores/`, etc.), usando `os.listdir()`, `shutil.move()` y validando con `os.path.splitext()`.
- Extra: detecta y renombra duplicados en vez de sobrescribirlos.

**Concepto:** manejo de archivos y carpetas, `os`, `shutil`.

---

### 2. Buscador de texto en múltiples archivos ("mini-grep")
Un script tipo línea de comandos que reciba una palabra o patrón regex y busque en todos los `.txt` de una carpeta (y subcarpetas, con `os.walk()`), mostrando el archivo y el número de línea donde aparece cada coincidencia.
- Es una versión simplificada de `grep` — buen cierre porque integra casi todo: archivos, loops, funciones y regex.

**Concepto:** `os.walk()`, regex, procesamiento línea por línea.

---

## Bloque 2 — Extracción y limpieza de datos con regex

### 3. Extractor de datos de contacto
Un programa que lea uno o varios archivos `.txt` (recibos de correo, notas, lo que sea) y use regex para extraer todos los teléfonos y correos electrónicos que encuentre, guardándolos en un `.csv` limpio.

**Concepto:** regex sobre archivos reales, escritura de `.csv`.

---

### 4. Validador y limpiador de listas de datos
Toma un archivo con datos "sucios" (por ejemplo una lista de nombres/emails/teléfonos mal formateados, con espacios de más, mayúsculas inconsistentes) y escribe funciones de validación con regex que separen los registros válidos de los inválidos, guardando cada grupo en su propio archivo.

**Concepto:** funciones de validación, regex, separación de datos válidos/inválidos.

---

## Bloque 3 — Reportes a partir de datos

### 5. Generador de reportes de gastos
Partiendo de un `.csv` con transacciones (fecha, categoría, monto), un script que sume los gastos por categoría y por mes usando diccionarios anidados, y escriba un resumen en un `.txt` legible.

**Concepto:** `dict.get()` con valores por defecto, diccionarios anidados, formateo de strings.

