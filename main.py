
import tkinter as tk
from fan import StandingFan

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pedestal‑Style Fan")
    W, H = 500, 900

    canvas = tk.Canvas(root, width=W, height=H, bg="white")
    canvas.pack()

    StandingFan(canvas, center=(W//2, 300), radius=200)
    root.mainloop()
