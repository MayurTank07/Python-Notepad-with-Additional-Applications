import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Application by Mayur Tank")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.color = "black"
        self.brush_size = 2
        self.old_x = None
        self.old_y = None

        # Menu bar
        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear Canvas", command=self.clear_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)

        color_menu = tk.Menu(menu)
        menu.add_cascade(label="Colors", menu=color_menu)
        color_menu.add_command(label="Choose Color", command=self.choose_color)

        size_menu = tk.Menu(menu)
        menu.add_cascade(label="Brush Size", menu=size_menu)
        size_menu.add_command(label="Small", command=lambda: self.set_brush_size(2))
        size_menu.add_command(label="Medium", command=lambda: self.set_brush_size(5))
        size_menu.add_command(label="Large", command=lambda: self.set_brush_size(10))

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def paint(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            self.canvas.create_line(
                self.old_x,
                self.old_y,
                x,
                y,
                width=self.brush_size,
                fill=self.color,
                capstyle=tk.ROUND,
                smooth=tk.TRUE,
            )
        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = colorchooser.askcolor(initialcolor=self.color)
        if color[1]:
            self.color = color[1]

    def set_brush_size(self, size):
        self.brush_size = size


if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
