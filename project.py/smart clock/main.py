# ---------- DIGITAL CLOCK ----------

import tkinter as tk
import time
import random

# For beep sound (Windows)
try:
    import winsound
except:
    winsound = None

# ---------------- WINDOW ----------------

root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x350")
root.configure(bg="black")

# ---------------- VARIABLES ----------------

dark_mode = True
time_format = True      # True = 12 Hour, False = 24 Hour

colors = [
    "cyan",
    "yellow",
    "lime",
    "orange",
    "white",
    "pink",
    "red"
]

last_hour = -1

# ---------------- FUNCTIONS ----------------

def currentTime():

    global last_hour

    # Time Format
    if time_format:
        current_time = time.strftime("%I:%M:%S %p")
    else:
        current_time = time.strftime("%H:%M:%S")

    day = time.strftime("%A")
    date = time.strftime("%d %B %Y")

    # Change time color every second
    time_label.config(
        text=current_time,
        fg=random.choice(colors)
    )

    day_label.config(text=day)
    date_label.config(text=date)

    # Hourly Beep
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    if minute == "00" and second == "00":
        if hour != last_hour:
            last_hour = hour
            if winsound:
                winsound.Beep(1000, 500)

    root.after(1000, currentTime)

# ---------------- LIGHT / DARK MODE ----------------

def change_theme():

    global dark_mode

    if dark_mode:
        root.configure(bg="white")

        title.config(bg="white", fg="black")
        time_label.config(bg="white")
        day_label.config(bg="white", fg="black")
        date_label.config(bg="white", fg="blue")

        dark_mode = False

    else:
        root.configure(bg="black")

        title.config(bg="black", fg="cyan")
        time_label.config(bg="black")
        day_label.config(bg="black", fg="white")
        date_label.config(bg="black", fg="yellow")

        dark_mode = True

# ---------------- 12 / 24 HOUR FORMAT ----------------

def change_format():

    global time_format

    time_format = not time_format

# ---------------- LABELS ----------------

title = tk.Label(
    root,
    text="DIGITAL CLOCK",
    font=("Arial",20,"bold"),
    bg="black",
    fg="cyan"
)
title.pack(pady=10)

time_label = tk.Label(
    root,
    font=("Calibri",45,"bold"),
    bg="black"
)
time_label.pack()

day_label = tk.Label(
    root,
    font=("Arial",18,"bold"),
    bg="black",
    fg="white"
)
day_label.pack()

date_label = tk.Label(
    root,
    font=("Arial",16),
    bg="black",
    fg="yellow"
)
date_label.pack(pady=5)

# ---------------- BUTTONS ----------------

theme_btn = tk.Button(
    root,
    text="🌙 Light / Dark Mode",
    command=change_theme,
    font=("Arial",12)
)
theme_btn.pack(side="left", padx=30, pady=20)

format_btn = tk.Button(
    root,
    text="🕒 12 / 24 Hour",
    command=change_format,
    font=("Arial",12)
)
format_btn.pack(side="right", padx=30, pady=20)

# ---------------- START CLOCK ----------------

currentTime()

root.mainloop()