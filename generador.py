import tkinter as tk
from tkinter import ttk

def agregar_columna():
    columnas_text.insert(tk.END, columna_entry.get() + ',\n')
    columna_entry.delete(0, tk.END)

def agregar_valor():
    valores_text.insert(tk.END, valor_entry.get() + ',\n')
    valor_entry.delete(0, tk.END)

def generar_sql():
    tabla = tabla_entry.get()
    columnas = columnas_text.get(1.0, tk.END).strip().replace('\n', ' ')
    valores = valores_text.get(1.0, tk.END).strip().replace('\n', ' ')

    query = f"INSERT INTO {tabla} ({columnas}) VALUES ({valores});"
    sql_text.delete(1.0, tk.END)
    sql_text.insert(tk.INSERT, query)

def copiar_sql():
    ventana.clipboard_clear()
    ventana.clipboard_append(sql_text.get(1.0, tk.END))
    
def limpiar_pantalla():
    tabla_entry.delete(0, tk.END)
    columna_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)
    columnas_text.delete(1.0, tk.END)
    valores_text.delete(1.0, tk.END)
    sql_text.delete(1.0, tk.END)
    

ventana = tk.Tk()
ventana.title("Generador de SQL INSERT")

ttk.Label(ventana, text="Tabla:").grid(column=0, row=0, sticky=tk.W)
tabla_entry = ttk.Entry(ventana)
tabla_entry.grid(column=1, row=0)

ttk.Label(ventana, text="Columna:").grid(column=0, row=1, sticky=tk.W)
columna_entry = ttk.Entry(ventana)
columna_entry.grid(column=1, row=1)
agregar_columna_btn = ttk.Button(ventana, text="Agregar Columna", command=agregar_columna)
agregar_columna_btn.grid(column=2, row=1)

columnas_text = tk.Text(ventana, wrap=tk.WORD, width=40, height=4)
columnas_text.grid(column=0, row=2, columnspan=3)

ttk.Label(ventana, text="Valor:").grid(column=0, row=3, sticky=tk.W)
valor_entry = ttk.Entry(ventana)
valor_entry.grid(column=1, row=3)
agregar_valor_btn = ttk.Button(ventana, text="Agregar Valor", command=agregar_valor)
agregar_valor_btn.grid(column=2, row=3)

valores_text = tk.Text(ventana, wrap=tk.WORD, width=40, height=4)
valores_text.grid(column=0, row=4, columnspan=3)

generar_btn = ttk.Button(ventana, text="Generar", command=generar_sql)
generar_btn.grid(column=0, row=5, columnspan=3)

sql_text = tk.Text(ventana, wrap=tk.WORD, width=40, height=10)
sql_text.grid(column=0, row=6, columnspan=3)

copiar_btn = ttk.Button(ventana, text="Copiar", command=copiar_sql)
copiar_btn.grid(column=0, row=7, columnspan=3)

limpiar_btn = ttk.Button(ventana, text="Limpiar", command=limpiar_pantalla)
limpiar_btn.grid(column=0, row=8, columnspan=3)


ventana.mainloop()
