import tkinter as tk

def show_attack_tactics():
    attack_tactics_window = tk.Toplevel()
    attack_tactics_window.title("Attack Tactics")

    # создаем фрейм для отображения текста с тактиками
    tactics_frame = tk.Frame(attack_tactics_window, padx=10, pady=10)
    tactics_frame.pack()

    # добавляем текст с тактиками
    tactics_label = tk.Label(tactics_frame, text="Атакующие тактики:\n\n"
                                                  "1. Прорыв: игроки нападают на защиту, прорываясь к кольцу и пытаясь забросить мяч.\n\n"
                                                  "2. Постановка блока: один из игроков ставит блок, чтобы создать пространство для другого игрока для заброса мяча.\n\n"
                                                  "3. Разворот: игрок, имеющий мяч, быстро разворачивается и пытается забросить мяч в кольцо, пока защитник не успевает закрыть доступ.\n\n"
                                                  "4. Развивающаяся атака: команда быстро передвигается по площадке, пытаясь найти свободного игрока для заброса мяча.")
    tactics_label.pack()
