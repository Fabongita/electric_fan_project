
import tkinter as tk
import math
from abc import ABC, abstractmethod
from speed import SPEED

class Drawable(ABC):
    @abstractmethod
    def draw(self, c: tk.Canvas): ...

class Fan(ABC):
    def __init__(self, canvas: tk.Canvas, center, radius):
        self.c, (self.cx, self.cy), self.r = canvas, center, radius
        self.angle = -90
        self.strategy = SPEED[0]
        self.static, self.dynamic = [], []
        self.build()               # fill self.static & self.dynamic
        for comp in self.static:
            comp.draw(self.c)      # draw grill, base, buttons once
        self._bind_buttons()
        self._animate()

    @abstractmethod
    def build(self): ...

    def _bind_buttons(self):
        for i in SPEED:
            # bind any click on tag "btn{i}" → set_speed(i)
            self.c.tag_bind(f"btn{i}", "<Button-1>",
                            lambda e, s=i: self.set_speed(s))

    def set_speed(self, i):
        self.strategy = SPEED.get(i, SPEED[0])
        self._draw_dynamic()      # immediate blade redraw

    def _draw_dynamic(self):
        for comp in self.dynamic:
            comp.draw(self.c)

    def _animate(self):
        # update angle & redraw blades every tick
        self.angle = (self.angle + self.strategy.increment()) % 360
        self._draw_dynamic()
        self.c.after(self.strategy.delay(), self._animate)

class StandingFan(Fan):
    def build(self):
        cx, cy, r = self.cx, self.cy, self.r
        outer = self           # capture for inner classes

        # 1) Grill (static)
        class Grill(Drawable):
            def draw(self, c):
                for k in range(1, 9):
                    span = r * k/8
                    c.create_oval(cx-span, cy-span, cx+span, cy+span,
                                  outline="black", width=1.2)
                for i in range(32):
                    th = math.radians(i * 360 / 32)
                    c.create_line(cx, cy,
                                  cx + r*math.cos(th), cy + r*math.sin(th),
                                  fill="black", width=1.2)

        # 2) Blades (dynamic)
        class Blades(Drawable):
            def draw(self, c):
                c.delete("blades")   # clear old blades
                L, W = r*0.8, 24
                for o in (0, 120, 240):
                    th = math.radians(outer.angle + o)
                    c.create_line(cx, cy,
                                  cx + L*math.cos(th), cy + L*math.sin(th),
                                  fill="gray20", width=W,
                                  capstyle=tk.ROUND, tags="blades")
                c.create_oval(cx-15, cy-15, cx+15, cy+15,
                             fill="black", tags="blades")

        # 3) Neck & Base (static)
        class Base(Drawable):
            def draw(self, c):
                top = cy + r*0.9
                bot = top + 180
                c.create_rectangle(cx-12, top, cx+12, bot,
                                   fill="black")
                c.create_oval(cx-80, bot-10, cx+80, bot+30,
                              fill="black")

        # 4) On‑canvas Buttons (static; both oval & text carry btn tags)
        class Buttons(Drawable):
            def draw(self, c):
                top = cy + r*0.9
                for i, lbl in enumerate(("0","1","2","3")):
                    y = top + 20 + i*40
                    c.create_oval(cx-12, y-12, cx+12, y+12,
                                  fill="lightgray", outline="gray30",
                                  width=1.5, tags=(f"btn{i}",))
                    c.create_text(cx, y, text=lbl,
                                  font=("Arial", 10, "bold"),
                                  tags=(f"btn{i}",))

        # assign lists
        self.static  = [Grill(), Base(), Buttons()]
        self.dynamic = [Blades()]
