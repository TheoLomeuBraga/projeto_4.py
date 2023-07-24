import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_graph(points):
    x = []
    y = []

    for p in points:
        x.append(p[0])
        y.append(p[1])

    # Create a Figure and Axes
    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)

    # Plot the data
    ax.plot(x, y, marker='o')

    # Set labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Simple Graph')

    # Create a canvas to display the plot
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the main window
window = tk.Tk()
window.title("Simple Graphic with Matplotlib and Tkinter")
window.geometry("400x300")

# Create a button to generate the graph
graphc_points = [[1,2],[2,4],[3,6]]
create_graph(graphc_points)

# Start the main event loop
window.mainloop()
