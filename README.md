# 🌀 Pedestal‑Style Fan Simulator (OOP Implementation)

A simple interactive fan simulation built with Python and Tkinter. Click the on‑canvas buttons (0–3) on the fan’s neck to turn it off or set speeds Low (1) → High (3). Blades spin smoothly, and the static grill, base, and controls remain responsive. This project demonstrates how to apply core OOP principles to a GUI animation.

---

## 🛠️ OOP Principles Applied

✅ **Encapsulation**  
- All fan state (canvas, position, radius, angle, speed strategy) is held inside the `Fan` class.  
- Internal data (`angle`, `strategy`, component lists) is managed via methods (`set_speed`, `_animate`) rather than global variables.

✅ **Abstraction**  
- The `Drawable` interface hides drawing details behind a single `draw(c)` method.  
- The `Speed` interface abstracts timing and rotation logic behind `.delay()` and `.increment()`.

✅ **Inheritance**  
- `StandingFan` subclasses the abstract `Fan` class, reusing its animation loop, button-binding, and speed logic.  
- Only a single `build()` method in `StandingFan` defines grill, blades, base, and buttons.

✅ **Polymorphism**  
- **Speed strategies** (`Off`, `Low`, `Med`, `High`) all implement the `Speed` interface—`Fan` doesn’t care which one is active.  
- **Drawable components** (`Grill`, `Blades`, `Base`, `Buttons`) all implement `Drawable` so the `Fan` can iterate over “all drawables” without knowing their specifics.

---

## 🎮 Features

➥ **Smooth animation** of three chunky blades that occupy 80% of the guard’s radius  
➥ **On‑canvas controls** (buttons 0–3) embedded in the fan’s neck—no external widgets needed  
➥ **Immediate response**: speed changes redraw blades instantly, no waiting for the next tick  
➥ **Static vs. dynamic rendering**: only blades are redrawn each frame for maximum performance  
➥ **Pedestal‑style design**: tall neck and sturdy base for a realistic standing fan look  
➥ **Clean, modular code**: easily extendable to add new fan types or speed behaviors

---

## 🖋️ Credits

- **Project idea** by: Me  
- **Code implementation** by: ChatGPT(OpenAI)

---

## 📝 Notes

This project was created primarily to demonstrate the Four Fundamental Principles of OOP in Python with a fun, graphical simulation. Feel free to fork, tweak blade sizes, colors, or even add new fan models (ceiling fan, desk fan) by subclassing `Fan` and providing your own `build()` logic!
