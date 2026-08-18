### === NUEVO ORDEN DE CONSTRUCCIÓN ===
1. Logging: Empezar con basicConfig(), para cambiar de basicConfig() a dictConfig() no es tan difícil 
2. pyproject.toml, configuración nueva de uv (lo arruiné) y creación inicio básico de main.py - darle un buen putito nombre al proyecto - 
3. Lógica de negocio: ahora sí debuggear la lógica de negocio (el download organizer) que ya tengo 
4. Argparse: Finalizar escribiendo los argumentos de CLI (una versión muy básica), como si fuera una interfaz. 

### ========== CORRECCIÓN DEL ARCHIVO DE PATHLIB, A LO MEJOR TENGO QUE VOLVER A CREAR TODO EL UV DE TODAS FORMAS ========= 
Claro, sin tocar ni corregir el código, te enumero los **casos borde (edge cases)** que veo y que efectivamente harían fallar tu script en distintos escenarios. Van explicados:

---

**1. El `find_directory` y el generador vacío (carpeta inexistente)**  
Tu función usa `while True` y va pidiendo `next()` al generador. Si la carpeta "Downloads" no existe en el home, el generador se queda sin elementos y al llamar a `next()` lanza la excepción `StopIteration`. Como no la atrapas, el programa se rompe de forma abrupta. Es un caso borde clásico: asumes que siempre va a existir.

---

**2. El `temporary_copy` choca con una copia previa**  
Si ya existe una carpeta llamada `Downloads_test` (porque corriste el script antes y no la borraste), `shutil.copytree` lanza un `FileExistsError` y detiene todo. No estás verificando si el destino ya existe.

---

**3. Las subcarpetas que ya existen dentro de la copia**  
Al hacer `shutil.copytree`, estás copiando *todas* las subcarpetas que ya tenga "Downloads" (ej: una carpeta llamada `pdf`). Luego, cuando tu bucle itera sobre los archivos, si encuentra un `archivo.pdf`, calcula `current_dir = directorio / "pdf"` e intenta hacer `mkdir()`. **Pero esa carpeta `pdf` ya existe** (porque la copiaste). Como no usas `exist_ok=True`, el `mkdir()` lanza `FileExistsError`. Es uno de los fallos más seguros que vas a tener.

---

**4. Archivos sin extensión**  
Si tienes un archivo llamado `LICENSE` o `README` (sin punto), `file.suffix` devuelve una cadena vacía (`""`). Al hacer `.lstrip('.')` sigue siendo `""`. Entonces `current_dir = directorio / ""`, que da como resultado la ruta del directorio raíz de prueba. El archivo se moverá a la raíz, pero no se crea ninguna carpeta para él. Además, si ya existe otro archivo sin extensión, se acumulan todos en la raíz, lo cual puede ser confuso y, dependiendo de colisiones de nombres, problemático.

---

**5. Extensiones compuestas (ej: `.tar.gz`, `.log.1`, `.vmdk.bak`)**  
Solo tomas el *último* sufijo (`.gz`, `.1`, `.bak`). Esto descontextualiza completamente los archivos. Un `proyecto.tar.gz` terminará dentro de la carpeta `gz` en lugar de una carpeta `tar` o `tar.gz`. Un `registro.log.1` va a la carpeta `1`. No es un error de ejecución, pero es un fallo lógico de clasificación (pierdes información y mezclas formatos).

---

**6. Colisiones de nombres de archivo al moverlos**  
Dentro de una misma carpeta de destino (ej: la carpeta `pdf`), puede haber dos archivos con exactamente el mismo nombre (ej: `informe.pdf` que vienen de distintas subcarpetas originales, o que ya existía uno previamente movido). `shutil.move` se comporta distinto según el sistema operativo:  
- En **Linux/macOS**, suele sobreescribir el archivo destino sin preguntar (pierdes datos).  
- En **Windows**, suele lanzar un `FileExistsError` y se rompe.  
Como tu script no controla esta situación, el comportamiento es impredecible entre plataformas.

---

**7. El bucle ignora por completo las subcarpetas originales**  
Cuando iteras con `file.is_file()`, estás descartando todos los directorios que se copiaron dentro de `Downloads_test`. Esos directorios se quedan huérfanos y no se mueven a ningún lado, pero además, como vimos en el punto 3, sus nombres pueden chocar con las nuevas carpetas por extensión. Esto genera un estado inconsistente: algunos archivos se mueven a carpetas nuevas y otras carpetas antiguas quedan mezcladas sin ser procesadas.

---

**8. La variable de limpieza final está mal nombrada**  
Esto no es exactamente un caso borde, pero es un error directo: en el `main` declaras `temporary_copy_downloads`, pero en el comentario del `rmtree` usas `temporary_downloads`. Si descomentaras esa línea, te daría un `NameError` porque esa variable no existe.

---

**9. Archivos que empiezan con punto (ocultos) en el directorio de prueba**  
Si dentro de la copia hay un archivo `.bashrc` o `.gitconfig`, `iterdir()` los captura. El sufijo sería `.bashrc` o `.gitconfig`, por lo que los moverías a carpetas llamadas `bashrc` o `gitconfig`. No es un crash, pero cambia completamente el comportamiento esperado (quizá querías ignorarlos o tratarlos de forma especial).

---

**10. Permisos y archivos bloqueados**  
Aunque es más ambiental que lógico, si algún archivo está siendo usado por el sistema o no tienes permisos de escritura/lectura, `shutil.move` o `shutil.copytree` lanzarán excepciones de tipo `PermissionError` que tu script no captura.

---

Resumiendo: los más críticos y seguros de que van a reventar son el **punto 2** (carpeta de prueba ya existente) y el **punto 3** (subcarpetas preexistentes chocando con el `mkdir`). Los demás son fallos lógicos o de pérdida de datos que pueden pasar desapercibidos hasta que te topes con un archivo con extensión compuesta o sin extensión.
