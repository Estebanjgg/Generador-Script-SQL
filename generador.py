import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox




def agregar_columna():
    columnas_text.insert(tk.END, columna_entry.get() + ',\n')
    columna_entry.delete(0, tk.END)

def eliminar_ultima_columna():
    columnas = columnas_text.get(1.0, tk.END).strip().split('\n')
    columnas.pop()
    columnas_text.delete(1.0, tk.END)
    columnas_text.insert(tk.END, ',\n'.join(columnas) + '\n')

def agregar_valor():
    valores_text.insert(tk.END, valor_entry.get() + ',\n')
    valor_entry.delete(0, tk.END)

def eliminar_ultimo_valor():
    valores = valores_text.get(1.0, tk.END).strip().split('\n')
    valores.pop()
    valores_text.delete(1.0, tk.END)
    valores_text.insert(tk.END, ',\n'.join(valores) + '\n')

def generar_sql_insert():
    if mode == 'INSERT':
        tabla = tabla_entry.get()
        columnas = columnas_text.get(1.0, tk.END).strip().replace('\n', ' ')
        valores = valores_text.get(1.0, tk.END).strip().replace('\n', ' ')
        query = f"INSERT INTO {tabla} ({columnas}) VALUES ({valores});"

        sql_text.delete(1.0, tk.END)
        sql_text.insert(tk.INSERT, query)



def copiar_sql():
    ventana.clipboard_clear()
    ventana.clipboard_append(sql_text.get(1.0, tk.END))
    messagebox.showinfo("Copied", "Text copied to clipboard.")

    
def limpiar_pantalla():
    tabla_entry.delete(0, tk.END)
    columna_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)
    columnas_text.delete(1.0, tk.END)
    valores_text.delete(1.0, tk.END)
    sql_text.delete(1.0, tk.END)
    
    
def generar_sql_delete_single():
    tabla = tabla_entry.get()
    id_value = id_entry.get()

    query = f"DELETE FROM {tabla} WHERE ID = {id_value};"
    sql_text.delete(1.0, tk.END)
    sql_text.insert(tk.INSERT, query)


def generar_sql_delete_multiple():
    tabla = tabla_entry.get()
    id_values = id_entry.get().split('-')
    start_id = id_values[0].strip()
    end_id = id_values[1].strip()

    query = f"DELETE FROM {tabla} WHERE ID BETWEEN {start_id} AND {end_id};"
    sql_text.delete(1.0, tk.END)
    sql_text.insert(tk.INSERT, query)
    
def generar_sql_update():
    tabla = tabla_entry.get()
    columnas = columnas_text.get(1.0, tk.END).strip().split('\n')
    valores = valores_text.get(1.0, tk.END).strip().split('\n')
    id_value = id_entry.get()

    set_statements = []
    for columna, valor in zip(columnas, valores):
        set_statements.append(f"{columna} = {valor}")

    set_string = ', '.join(set_statements)

    query = f"UPDATE {tabla} SET {set_string} WHERE ID = {id_value};"

    sql_text.delete(1.0, tk.END)
    sql_text.insert(tk.INSERT, query)


    
def toggle_mode():
    global mode

    if mode == 'INSERT':
        mode = 'DELETE'
        toggle_mode_btn.config(text='Mode: DELETE')
        agregar_columna_btn.grid_remove()
        eliminar_ultima_columna_btn.grid_remove()
        agregar_valor_btn.grid_remove()
        eliminar_ultimo_valor_btn.grid_remove()
        columnas_text.grid_remove()
        valores_text.grid_remove()
        columna_label.grid_remove()
        valor_label.grid_remove()
        id_label.grid()
        id_entry.grid()
        delete_single_btn.grid()
        delete_multiple_btn.grid()
        generar_btn.config(command=generar_sql_delete_single)  

    elif mode == 'DELETE':
        mode = 'UPDATE'
        toggle_mode_btn.config(text='Mode: UPDATE')
        id_label.grid()
        id_entry.grid()
        delete_single_btn.grid_remove()
        delete_multiple_btn.grid_remove()
        columna_label.grid(column=0, row=1, sticky=tk.W)
        valor_label.grid(column=0, row=3, sticky=tk.W)
        columnas_text.grid()
        valores_text.grid()
        agregar_columna_btn.grid()
        eliminar_ultima_columna_btn.grid()
        agregar_valor_btn.grid()
        eliminar_ultimo_valor_btn.grid()
        generar_btn.config(command=generar_sql_update)  

    else:
        mode = 'INSERT'
        toggle_mode_btn.config(text='Mode: INSERT')
        id_label.grid_remove()
        id_entry.grid_remove()
        delete_single_btn.grid_remove()
        delete_multiple_btn.grid_remove()
        columna_label.grid(column=0, row=1, sticky=tk.W)
        valor_label.grid(column=0, row=3, sticky=tk.W)
        columnas_text.grid()
        valores_text.grid()
        agregar_columna_btn.grid()
        eliminar_ultima_columna_btn.grid()
        agregar_valor_btn.grid()
        eliminar_ultimo_valor_btn.grid()
        generar_btn.config(command=generar_sql_insert)  


    

ventana = tk.Tk()
ventana.title("SQL INSERT Generator by Esteban Gonzalez")

ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_rowconfigure(4, weight=1)
ventana.grid_rowconfigure(6, weight=1)
columna_label = ttk.Label(ventana, text="Columna:")
columna_label.grid(column=0, row=1, sticky=tk.W)

valor_label = ttk.Label(ventana, text="Value:")
valor_label.grid(column=0, row=3, sticky=tk.W)

ttk.Label(ventana, text="Table Name:").grid(column=0, row=0, sticky=tk.W)
tabla_entry = ttk.Entry(ventana)
tabla_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=5, pady=5)

ttk.Label(ventana, text="Columna:").grid(column=0, row=1, sticky=tk.W)
columna_entry = ttk.Entry(ventana)
columna_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=5)
agregar_columna_btn = ttk.Button(ventana, text="Add Column", command=agregar_columna)
agregar_columna_btn.grid(column=2, row=1, padx=5)
eliminar_ultima_columna_btn = ttk.Button(ventana, text="Delete last column", command=eliminar_ultima_columna)
eliminar_ultima_columna_btn.grid(column=3, row=1, padx=5)
columnas_text = tk.Text(ventana, wrap=tk.WORD, width=40, height=4)
columnas_text.grid(column=0, row=2, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

ttk.Label(ventana, text="Value:").grid(column=0, row=3, sticky=tk.W)
valor_entry = ttk.Entry(ventana)
valor_entry.grid(column=1, row=3, sticky=(tk.W, tk.E), padx=5)
agregar_valor_btn = ttk.Button(ventana, text="Adding Value", command=agregar_valor)
agregar_valor_btn.grid(column=2, row=3, padx=5)
eliminar_ultimo_valor_btn = ttk.Button(ventana, text="Delete last value", command=eliminar_ultimo_valor)
eliminar_ultimo_valor_btn.grid(column=3, row=3, padx=5)

valores_text = tk.Text(ventana, wrap=tk.WORD, width=40, height=4)
valores_text.grid(column=0, row=4, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

generar_btn = ttk.Button(ventana, text="Generate", command=generar_sql_insert)
generar_btn.grid(column=0, row=5, columnspan=3, padx=5, pady=5)

sql_text = tk.Text(ventana, wrap=tk.WORD, width=40, height=10)
sql_text.grid(column=0, row=6, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

copiar_btn = ttk.Button(ventana, text="Copy", command=copiar_sql)
copiar_btn.grid(column=0, row=7, columnspan=2, padx=5, pady=5)

limpiar_btn = ttk.Button(ventana, text="Clean", command=limpiar_pantalla)
limpiar_btn.grid(column=2, row=7, columnspan=2, padx=5, pady=5)

ttk.Label(ventana, text="").grid(column=1, row=0, sticky=tk.W)
id_label = ttk.Label(ventana, text="ID(s):")
id_label.grid(column=2, row=0, sticky=tk.W)
id_label.grid_remove()

id_entry = ttk.Entry(ventana)
id_entry.grid(column=3, row=0, sticky=(tk.W, tk.E), padx=5)
id_entry.grid_remove()

delete_single_btn = ttk.Button(ventana, text="Delete by ID", command=generar_sql_delete_single)
delete_single_btn.grid(column=2, row=4, padx=5)
delete_single_btn.grid_remove()

delete_multiple_btn = ttk.Button(ventana, text="Delete multiple IDs exemplo (1 - 4)", command=generar_sql_delete_multiple)
delete_multiple_btn.grid(column=3, row=4, padx=5)
delete_multiple_btn.grid_remove()


mode = 'INSERT'

toggle_mode_btn = ttk.Button(ventana, text="Mode: INSERT", command=toggle_mode)
toggle_mode_btn.grid(column=4, row=0, padx=5, pady=5)



ventana.mainloop()



