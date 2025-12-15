import os
import time
from tabulate import tabulate
from queries_data import get_queries
from db import get_connection  # <--- AQUÍ ESTÁ LA CORRECCIÓN (Importamos desde db.py)

def clear_screen():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Imprime el encabezado del proyecto."""
    print("========================================================")
    print("   PRACTICA BASES DE DATOS - ALGEBRA RELACIONAL")
    print("   Caso Integrador: Tienda de Hardware (E-commerce)")
    print("========================================================\n")

def execute_query(query_data):
    """
    Muestra la equivalencia teórica y ejecuta la consulta SQL.
    """
    # Usamos la función importada de db.py
    conn = get_connection()
    
    if not conn:
        input("(!) No se pudo conectar a la Base de Datos. Presiona ENTER para volver...")
        return

    clear_screen()
    print("\n" + "="*80)
    print(f"CONSULTA {query_data['id']}: {query_data['descripcion']}")
    print("="*80)
    
    # Mostrar las equivalencias teóricas (Requisito clave de la práctica)
    print(f"\n[1] ALGEBRA RELACIONAL:\n    {query_data['algebra']}")
    print(f"\n[2] CALCULO RELACIONAL DE TUPLAS (CRT):\n    {query_data['crt']}")
    print(f"\n[3] CALCULO RELACIONAL DE DOMINIOS (CRD):\n    {query_data['crd']}")
    print(f"\n[4] SQL EQUIVALENTE:\n    {query_data['sql'].strip()}")
    print("-" * 80)
    
    input("\nPresiona ENTER para ejecutar la consulta SQL en la BD...")
    
    try:
        cur = conn.cursor()
        cur.execute(query_data['sql'])
        
        # Obtener nombres de columnas para la tabla
        if cur.description:
            colnames = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            
            print("\nRESULTADOS OBTENIDOS:")
            if len(rows) > 0:
                print(tabulate(rows, headers=colnames, tablefmt="psql"))
                print(f"\nTotal de tuplas: {len(rows)}")
            else:
                print("(!) La consulta se ejecutó correctamente pero no devolvió resultados (Conjunto Vacio).")
        else:
            conn.commit()
            print("\nOperación ejecutada correctamente (sin retorno de datos).")
            
        cur.close()
        conn.close()
    except Exception as e:
        print(f"\n(!) Error SQL durante la ejecución:\n{e}")
    
    input("\nPresiona ENTER para volver al menú principal...")

def main():
    """Bucle principal del menú interactivo."""
    queries = get_queries()
    
    # Pequeña pausa inicial para asegurar que la BD en Docker esté lista
    print("Iniciando sistema...")
    time.sleep(1) 
    
    while True:
        clear_screen()
        print_header()
        
        print(f"{'ID':<4} {'CATEGORIA':<22} {'DESCRIPCION'}")
        print("-" * 80)
        
        # Listar las consultas disponibles
        for q in queries:
            desc_corta = (q['descripcion'][:50] + '..') if len(q['descripcion']) > 50 else q['descripcion']
            print(f"{q['id']:<4} {q['categoria']:<22} {desc_corta}")
            
        print("-" * 80)
        print("[0] Salir del programa")
        
        try:
            opcion_usuario = input("\nSelecciona el ID de la consulta a ejecutar: ")
            
            if not opcion_usuario.isdigit():
                input("(!) Por favor ingresa un número válido. Enter para continuar.")
                continue

            choice = int(opcion_usuario)
            
            if choice == 0:
                print("Saliendo...")
                break
            
            # Buscar la consulta seleccionada en la lista
            selected_query = next((q for q in queries if q['id'] == choice), None)
            
            if selected_query:
                execute_query(selected_query)
            else:
                input("(!) ID no encontrado. Presiona ENTER para intentar de nuevo.")
                
        except Exception as e:
            input(f"(!) Error inesperado: {e}. Enter para continuar.")

if __name__ == "__main__":
    main()