import tkinter as tk
from tkinter import ttk

def get_basketball_tactics(tactic_type):
    # Создаем главное окно
    basketball_tactics_window = tk.Toplevel()
    basketball_tactics_window.title("Тактики баскетбола")

    # Создаем виджет Notebook
    notebook = ttk.Notebook(basketball_tactics_window)
    notebook.pack(fill="both", expand=True)

    # Создаем две вкладки для разделения на "Атаку" и "Защиту"
    offense_tab = ttk.Frame(notebook)
    defense_tab = ttk.Frame(notebook)

    # Добавляем вкладки в Notebook
    notebook.add(offense_tab, text='Атака')
    notebook.add(defense_tab, text='Защита')

    # Создаем функции для отображения тактик
    def show_offense_tactics():
        basketball_tactics_label.config(text=get_basketball_tactics.offense_tactics)

    def show_defense_tactics():
        basketball_tactics_label.config(text=get_basketball_tactics.defense_tactics)

    # Создаем кнопки для переключения между вкладками "Атака" и "Защита"
    offense_button = ttk.Button(offense_tab, text="Атака", command=show_offense_tactics)
    defense_button = ttk.Button(defense_tab, text="Защита", command=show_defense_tactics)

    # Добавляем кнопки на соответствующие вкладки
    offense_button.pack(padx=10, pady=10)
    defense_button.pack(padx=10, pady=10)

    # Создаем метку для отображения тактик
    basketball_tactics_label = tk.Label(offense_tab, text="", wraplength=400, justify=tk.LEFT, font=("Helvetica", 14), padx=10, pady=10)
    basketball_tactics_label.pack()

    # Определяем, какую тактику нужно показать
    if tactic_type == "Атака":
        basketball_tactics_label.config(text=get_basketball_tactics.offense_tactics)
    elif tactic_type == "Защита":
        basketball_tactics_label.config(text=get_basketball_tactics.defense_tactics)

    # Запускаем главный цикл обработки событий
    basketball_tactics_window.mainloop()
