import tkinter as tk
import random


window = tk.Tk()
window.title("Три сундука")
window.geometry("520x580")
window.resizable(False, False)
window.configure(bg="#f8fafc")

coins = 0
lives = 3
round_number = 1
max_rounds = 6
game_running = True
chosen = False
chests = []


def prepare_chests():
    global chests, chosen
    chests = ["gold", "trap", "empty"]
    random.shuffle(chests)
    chosen = False


def update_stats():
    stats_label.config(
        text=f"Раунд: {round_number}/{max_rounds}   🪙 {coins}   ❤️ {lives}"
    )


def finish_game():
    global game_running
    game_running = False

    if lives == 0:
        message = f"Игра окончена! Ловушки победили. Монет: {coins}"
    else:
        message = f"Все раунды пройдены! Собрано монет: {coins}"

    result_label.config(text=message)
    next_button.config(state="disabled")

    for button in chest_buttons:
        button.config(state="disabled")


def open_chest(index):
    global coins, lives, chosen

    if not game_running or chosen:
        return

    chosen = True
    reward = chests[index]

    if reward == "gold":
        coins += 5
        message = "Ура! Ты нашёл 5 монет!"
        color = "#bbf7d0"
    elif reward == "trap":
        lives -= 1
        message = "Ловушка! Минус одна жизнь."
        color = "#fecaca"
    else:
        message = "Пусто! На этот раз не повезло."
        color = "#e2e8f0"

    chest_buttons[index].config(bg=color)
    result_label.config(text=message)
    update_stats()

    for button in chest_buttons:
        button.config(state="disabled")

    if lives == 0:
        finish_game()
    elif round_number == max_rounds:
        finish_game()
    else:
        next_button.config(state="normal")


def next_round():
    global round_number

    if not game_running or not chosen:
        return

    round_number += 1
    prepare_chests()

    for button in chest_buttons:
        button.config(state="normal", bg="#dbeafe")

    next_button.config(state="disabled")
    result_label.config(text="Новый раунд! Выбирай сундук.")
    update_stats()


def restart_game():
    global coins, lives, round_number, game_running

    coins = 0
    lives = 3
    round_number = 1
    game_running = True
    prepare_chests()

    for button in chest_buttons:
        button.config(state="normal", bg="#dbeafe")

    next_button.config(state="disabled")
    result_label.config(text="Выбирай сундук!")
    update_stats()


title_label = tk.Label(
    window,
    text="🎁 ТРИ СУНДУКА",
    font=("Arial", 24, "bold"),
    bg="#f8fafc"
)
title_label.pack(pady=16)

rules_label = tk.Label(
    window,
    text="В каждом раунде найди сокровище!\nОдин сундук с монетами, один с ловушкой.",
    font=("Arial", 12),
    bg="#f8fafc",
    justify="center"
)
rules_label.pack()

stats_label = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold"),
    bg="#f8fafc"
)
stats_label.pack(pady=18)

chests_frame = tk.Frame(window, bg="#f8fafc")
chests_frame.pack(pady=12)

chest_buttons = []
for index in range(3):
    button = tk.Button(
        chests_frame,
        text=f"🎁\nСундук {index + 1}",
        font=("Arial", 14, "bold"),
        width=11,
        height=4,
        bg="#dbeafe",
        command=lambda i=index: open_chest(i)
    )
    button.grid(row=0, column=index, padx=6)
    chest_buttons.append(button)

result_label = tk.Label(
    window,
    text="Выбирай сундук!",
    font=("Arial", 13),
    bg="#f8fafc",
    wraplength=440
)
result_label.pack(pady=18)

next_button = tk.Button(
    window,
    text="Следующий раунд →",
    font=("Arial", 13, "bold"),
    bg="#bbf7d0",
    state="disabled",
    command=next_round
)
next_button.pack(pady=8)

restart_button = tk.Button(
    window,
    text="↻ Начать заново",
    font=("Arial", 12),
    command=restart_game
)
restart_button.pack(pady=10)

prepare_chests()
update_stats()
window.mainloop()