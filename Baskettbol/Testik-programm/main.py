import tkinter as tk
import attack_tactics
import defense_tactics
from PIL import ImageTk, Image
from rules import get_rules_by_location
from history import get_basketball_history
from russia_history import get_russia_basketball_history
from tactics import get_basketball_tactics
from inventory import get_inventory



def create_image_button(text, image_path, action):
    button_image = ImageTk.PhotoImage(Image.open(image_path))
    button = tk.Button(root, text=text, image=button_image, compound="top", command=action)
    button.image = button_image
    return button


def show_inventory():
    inventory_window = tk.Tk()
    inventory_window.title("Инвентарь и площадка")

    inventory_label = tk.Label(inventory_window, text=get_inventory(), wraplength=400, justify=tk.LEFT, font=("Helvetica", 14), padx=10, pady=10)
    inventory_label.pack(side=tk.LEFT)

    image1 = Image.open("D:/Sportt/Baskettbol/Оборудование/Разметка.png").resize((200,200), resample=Image.LANCZOS)
    photo1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("D:/Sportt/Baskettbol/Оборудование/Оборудование.png").resize((200,200), resample=Image.LANCZOS)
    photo2 = ImageTk.PhotoImage(image2)

    canvas = tk.Canvas(inventory_window, width=1500, height=1000)
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=photo1)
    canvas.create_image(200, 0, anchor=tk.NW, image=photo2)

    inventory_label.config(state=tk.DISABLED)
    inventory_window.photo1 = photo1
    inventory_window.photo2 = photo2

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("История баскетбола")

    history_label = tk.Label(history_window, text=get_basketball_history(), wraplength=400, justify=tk.LEFT, font=("Helvetica", 14), padx=10, pady=10)
    history_label.pack()

    image1 = Image.open("image1.jpg").resize((200, 200), Image.LANCZOS)
    photo1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("image2.jpg").resize((200, 200), Image.LANCZOS)
    photo2 = ImageTk.PhotoImage(image2)

    canvas = tk.Canvas(history_window, width=400, height=200)
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=photo1)
    canvas.create_image(200, 0, anchor=tk.NW, image=photo2)

    history_label.config(state=tk.DISABLED)
    history_window.image1 = photo1
    history_window.image2 = photo2

def show_russia_basketball_history():
    russia_history_window = tk.Toplevel(root)
    russia_history_window.title("История баскетбола в России")

    russia_history_label = tk.Label(russia_history_window, text=get_russia_basketball_history(), wraplength=400, justify=tk.LEFT, font=("Helvetica", 14), padx=10, pady=10)
    russia_history_label.pack()

    russia_history_label.config(state=tk.DISABLED)

def show_basketball_rules():
    basketball_rules_window = tk.Toplevel(root)
    basketball_rules_window.title("Правила игры в баскетбол")

    basketball_rules_label = tk.Label(basketball_rules_window, text=get_rules_by_location('world'), wraplength=400, justify=tk.LEFT, font=("Helvetica", 14), padx=10, pady=10)
    basketball_rules_label.pack()

    image = Image.open("basketball_rules.jpg").resize((400, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    canvas = tk.Canvas(basketball_rules_window, width=400, height=200)
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    basketball_rules_label.config(state=tk.DISABLED)
    basketball_rules_window.photo = photo

def show_basketball_tactics():
    basketball_tactics_window = tk.Toplevel(root)
    basketball_tactics_window.title("Basketball Tactics")

    # разместите две кнопки в одном фрейме
    buttons_frame = tk.Frame(basketball_tactics_window)
    buttons_frame.pack(side="top", padx=10, pady=10)

    # кнопка "Атака"
    attack_tactics_button = tk.Button(buttons_frame, text="Атака", command=attack_tactics.show_attack_tactics)
    attack_tactics_button.pack(side="left")

    # кнопка "Защита"
    defense_tactics_button = tk.Button(buttons_frame, text="Защита", command=defense_tactics.show_defense_tactics)
    defense_tactics_button.pack(side="left")

def show_media():
    media_window = tk.Toplevel(root)
    media_window.title("Фото и видео")

    media_label = tk.Label(media_window, text="Текст с описанием фото и видео", wraplength=400, justify=tk.LEFT, font=("Helvetica", 14), padx=10, pady=10)
    media_label.pack()

    image = Image.open("your_image.jpg").resize((400, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    
    canvas = tk.Canvas(media_window, width=400, height=200)
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    media_label.config(state=tk.DISABLED)
    media_window.photo = photo

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Баскетбол")
root.geometry("1500x900")

# Создание кнопок
history_button = create_image_button("История баскетбола", "D:/Sportt/Baskettbol/images/history.png", show_history)
russia_history_button = create_image_button("История баскетбола в России", "D:/Sportt/Baskettbol/images/russia.png", show_russia_basketball_history)
rules_button = create_image_button("Правила баскетбола", "D:/Sportt/Baskettbol/images/rules.png", show_basketball_rules)
tactics_button = create_image_button("Тактики игры в баскетбол", "D:/Sportt/Baskettbol/images/tactics.png", show_basketball_tactics)
inventory_button = create_image_button("Инвентарь и площадка", "D:/Sportt/Baskettbol/images/inventory.png", show_inventory)
media_button = create_image_button("Фото и видео", "D:/Sportt/Baskettbol/images/media.png", show_media)
exit_button = create_image_button("Выход", "D:/Sportt/Baskettbol/images/exit.png", exit_program)

# Отображение кнопок
history_button.pack(side="left", padx=10, pady=10)
russia_history_button.pack(side="left", padx=10, pady=10)
rules_button.pack(side="left", padx=10, pady=10)
tactics_button.pack(side="left", padx=10, pady=10)
inventory_button.pack(side="left", padx=10, pady=10)
media_button.pack(side="left", padx=10, pady=10)
exit_button.pack(side="right", padx=10, pady=10)


root.mainloop()