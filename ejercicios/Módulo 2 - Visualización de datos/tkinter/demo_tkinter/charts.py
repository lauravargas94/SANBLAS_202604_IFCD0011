import enum
from tkinter import messagebox

class ChartType(enum.Enum):
    BAR = 1
    SCATTER = 2
    PLOT = 3    
    PIE = 4 

def draw_chart(canvas, ax, df, chart_type):
    if (df is None) or (df.empty):
        messagebox.showerror(title='Error', message='No data to display')   
        return
    ax.clear()
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    if chart_type == ChartType.BAR:
        ax.bar(df[0], df[1], color='#2a7fb8')
        ax.set_title('Bar chart')    
        ax.set_aspect('auto')
    elif chart_type == ChartType.SCATTER:
        ax.scatter(df[0], df[1], color="#b72048")
        ax.set_title('Scatter chart')
        ax.set_aspect('auto')
    elif chart_type == ChartType.PLOT:
        ax.plot(df[0], df[1], color="#b82aaa")
        ax.set_title('Plot chart')
        ax.set_aspect('auto')
    elif chart_type == ChartType.PIE:
        ax.pie(df[1], labels=df[0], autopct='%1.1f%%')
        ax.set_title('Pie chart')
        ax.set_aspect('equal')
    canvas.draw()
