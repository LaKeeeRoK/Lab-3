import tkinter as tk
import pygame
from random import randint, shuffle
import pyperclip


def generate_password():
    global answer
    answer = ""
    for _ in range(4):
        letters = [chr(randint(65, 90)) for _ in range(3)]
        num = str(randint(0, 9))
        answer_lst = letters.copy()
        answer_lst.append(num)
        shuffle(answer_lst)
        answer_str = "".join(answer_lst)
        answer += answer_str + "-"
    answer = answer[:-1]
    canvas.itemconfig(pswd_canvas, text=answer)


def copy_password():
    pyperclip.copy(answer)
    label = tk.Label(root, text="Пароль скопирован!", font=("Arial", 25), fg="red")
    label_window = canvas.create_window(460, 580, window=label)
    root.after(1000, lambda: canvas.delete(label_window))


def OffMusic():
    global off_on_Music
    if off_on_Music:
        off_on_Music = False
        pygame.mixer.music.pause()
        return 0
    off_on_Music = True
    pygame.mixer.music.unpause()


answer = ""
off_on_Music = True
root = tk.Tk()
root.title("Password")
canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack()

image = tk.PhotoImage(file="background.png")
canvas.create_image(0, 0, anchor=tk.NW, image=image)

# button for off/on music
button_OffMusic = tk.Button(root, text="Отключить музыку", command=OffMusic)
button_OffMusic_canvas = canvas.create_window(50, 800, anchor="nw", window=button_OffMusic)

# button for generate password
button_pswd = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
button_pswd_canvas = canvas.create_window(465, 500, anchor="nw", window=button_pswd)

# password output
pswd_canvas = canvas.create_text(460, 450, text="Генерация ключа", fill="white", font=('Arial 30 bold'))

# button for copy password
button_copy = tk.Button(root, text="скопировать пароль", command=copy_password)
button_copy_canvas = canvas.create_window(300, 500, anchor="nw", window=button_copy)

# copy output
copy_canvas = canvas.create_text(530, 650, text="", fill="white", font=('Arial 30 bold'))


canvas.pack(fill="both", expand=True)

# Play music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play(-1)


root.mainloop()