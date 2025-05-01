import csv
import sys

def process_transaction(csv_source):
    balance = 0.0
    max_amount = 0.0
    id_max = None
    c_num = 0
    d_num = 0
    
    try:
        with open(csv_source, newline='', encoding='latin-1') as archive:
            reader = csv.DictReader(archive)
            for row in reader:
                transaction_type = row["tipo"]
                amount = float(row["monto"])    
                transaction_id = int(row["id"])
            
                transaction_type = transaction_type.lower().strip()
                if "crédito" in transaction_type or "credito" in transaction_type :
                    balance += amount
                    c_num += 1
                elif "débito" in transaction_type or "debito" in transaction_type:
                    balance -= amount
                    d_num += 1
                
                if amount > max_amount:
                    max_amount = amount
                    id_max = transaction_id
        
        print("Reporte de transacciones")
        print("---------------------------------------")
        print(f"Balance final: {balance:.2f}")
        print(f"Transacción de mayor monto: ID {id_max} - {max_amount:.2f}")
        print(f"Conteo de transacciones: Crédito: {c_num} Débito: {d_num}")
    
    except FileNotFoundError:
        print(f"Archivo no encontrado '{csv_source}'.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Instrucción de uso: 'python main.py <archivo.csv>'")
    else:
        source = sys.argv[1]
        process_transaction(source)
