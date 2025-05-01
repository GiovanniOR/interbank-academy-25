# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción:

Este proyecto es un programa de línea de comandos que analiza un archivo CSV de transacciones bancarias y genera un reporte dentro de la terminal.
El archivo debe tener la siguiente estructura
- **Fila 1: Id (Identificador de la transacción).**
- **Fila 2: Tipo (Tipo de transacción, debe ser débito o crédito).**
- **Fila 3: Monto (Cantidad de dinero).**

---

## Instrucciones

1. **Revisar python:**
   - Asegurese que tenga Python instalado en su equipo (Recomendado Python 3.10 o superior)  

2. **Revisar ubicación del archivo:**  
   - Asegurese que el archivo ".csv" se encuentre en la misma carpeta que el archivo "main.py"

3. **Ejecución del programa:**  
   - El programa debe ejecutarse de la siguiente manera:
      `python main.py <nombre_del_archivo>.csv`

---

## Enfoque y Solución:

- ** El programa utiliza Python por su simplicidad para leer datos y archivos ".csv". **
- ** El archivo se procesa con "csv.DictReader" para mayor legibilidad. **
- ** El programa calcula lo siguiente: **
    - Balance final (Entre créditos y débitos).
    - Transacción de mayor monto.
    - Conteo por tipo de transacción.

---

## Estructura del proyecto:

- |
- |-main.py
- |-README.md
- |-<Archivo de datos .csv (1 o +)>
