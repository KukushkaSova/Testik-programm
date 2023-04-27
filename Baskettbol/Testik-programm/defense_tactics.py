import tkinter as tk

def show_defense_tactics():
    defense_tactics_window = tk.Toplevel()
    defense_tactics_window.title("Defense Tactics")

    # ваш код для отображения тактик защиты
import tkinter as tk

def show_defense_tactics():
    defense_tactics_window = tk.Toplevel()
    defense_tactics_window.title("Defense Tactics")

    # создаем фрейм для отображения текста с тактиками
    tactics_frame = tk.Frame(defense_tactics_window, padx=10, pady=10)
    tactics_frame.pack()

    # добавляем текст с тактиками
    tactics_label = tk.Label(tactics_frame, text="Тактики защиты:\n\n"
                                                  "1. Ман-ту-ман: защитник назначается на отдельного игрока и следит за ним по всей площадке.\n\n"
                                                  "2. Зональная защита: игроки защиты отводят зоны площадки и защищают их от противника.\n\n"
                                                  "3. Подрезание паса: защитник прерывает передачу мяча к другому игроку, пытаясь перехватить мяч.\n\n"
                                                  "4. Нажим на игрока: защитник находится вблизи противника, не давая ему много пространства для маневра.")
    tactics_label.pack()
