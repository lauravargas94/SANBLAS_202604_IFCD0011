import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from charts import ChartType, draw_chart

ANCHO = 640
ALTO = 480

df = None

def finish_app():
    sys.exit(0)

def show_credits():
    messagebox.showinfo(title='Autor', message='By Fernando Paniagua (2026)')

def set_file_name():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files","*.csv*"),))
    entry_path.delete(0, tk.END)
    entry_path.insert(0, filename)

def process_data():
    global df
    nombre_fichero = entry_path.get()
    try:
        df = pd.read_csv(nombre_fichero, header=None)
        text_data.delete("1.0", tk.END)
        text_data.insert("1.0", str(df.head()))
        messagebox.showinfo('Success', 'Data loaded successfully. Select a chart type to visualize the data.')
    except FileNotFoundError as fne:
        messagebox.showerror('Error', 'El archivo no ha sido encontrado')
    except UnicodeDecodeError as ude:
        messagebox.showerror('Error', 'El formato del archivo no es válido')
    except Exception as exception:
        print(exception)
        messagebox.showerror('Error', 'Ha ocurrido un error inexperado')

if __name__=='__main__':
    # VENTANA PRINCIPAL
    main_window = tk.Tk()
    main_window.title('Visualizador de datos')
    # DIMENSIONES
    main_window.geometry(f'{ANCHO}x{ALTO}')
    main_window.minsize(width=ANCHO, height=ALTO)
    # MENÚ PRINCIPAL
    main_menu = tk.Menu()
    main_window.config(menu=main_menu)

    # MENÚ FILE
    file_menu=tk.Menu(tearoff=0) # tearoff -> Elimina la línea discontínua
    file_menu.add_command(label='Open', command=set_file_name)
    file_menu.add_command(label='Exit', command=finish_app)
    main_menu.add_cascade(label='File', menu=file_menu)
    
    # MENÚ TIPOS DE GRÁFICOS
    types_menu=tk.Menu(tearoff=0)
    types_menu.add_command(label='Bars', command=lambda: draw_chart(canvas, ax, df, ChartType.BAR))
    types_menu.add_command(label='Scatter', command=lambda: draw_chart(canvas, ax, df, ChartType.SCATTER))
    types_menu.add_command(label='Lines', command=lambda: draw_chart(canvas, ax, df, ChartType.PLOT))
    types_menu.add_command(label='Pie', command=lambda: draw_chart(canvas, ax, df, ChartType.PIE))
    main_menu.add_cascade(label='Chart type', menu=types_menu)

    # MENÚ HELP
    help_menu=tk.Menu(tearoff=0)
    help_menu.add_command(label='About...', command=show_credits)
    main_menu.add_cascade(label='Help', menu=help_menu)

    # FORMULARIO DE BÚSQUEDA
    label_path = tk.Label(text='Path')
    label_path.grid(row=0, column=0)

    entry_path = tk.Entry(width=80)
    entry_path.insert(0, './data.csv') # TODO Eliminar
    entry_path.grid(row=0, column=1, padx=10, pady=10)

    button_load = tk.Button(text='Load', background='#00AA00', foreground='white', command=process_data)
    button_load.grid(row=0, column=2)

    # VISUALIZADOR DE DATOS
    text_data = tk.Text(height=8)
    text_data.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky='nsew')

    # GRÁFICO EMBEBIDO
    graph_frame = tk.Frame(main_window, background='white')
    graph_frame.grid(row=2, column=0, columnspan=3, sticky='nsew', padx=10, pady=(0, 10))
    main_window.grid_rowconfigure(2, weight=1)
    main_window.grid_columnconfigure(1, weight=1)

    figure = plt.Figure(figsize=(6, 3), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, master=graph_frame)
    canvas.get_tk_widget().pack(fill='both', expand=True)

    main_window.mainloop()


