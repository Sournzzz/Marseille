import logging

logging.basicConfig(
    filename="organizer.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%H:%M:%S" #I can edit this later if I want to add year, month, etc.    
)

name = "Pedro Páramo"

"""

Con el % nativo de logging, la interpolación del mensaje se hace cuando el registro necesita ser formateado,
no cuando escribo la llamada a logging. Esto no aplica para la basicConfig()

"""

logging.warning("Sálvenme auxilio - %s", name) 

#Ejemplo de stack traces en logging

donuts = 0
people = 5

try:
    people / donuts
except ZeroDivisionError:
    logging.error("DonutCalculationError", exc_info=True)   
