import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        
        # Ползунок длины пароля
        self.length_label = tk.Label(root, text="Длина пароля:")
        self.length_label.pack()

        self.length_slider = tk.Scale(root, from_=8, to=20, orient='horizontal')
        self.length_slider.pack()

        # Чекбоксы для выбора символов
        self.include_digits = tk.BooleanVar(value=True)
        self.include_letters = tk.BooleanVar(value=True)
        self.include_specials = tk.BooleanVar(value=False)

        self.digits_check = tk.Checkbutton(root, text="Цифры", variable=self.include_digits)
        self.digits_check.pack()

        self.letters_check = tk.Checkbutton(root, text="Буквы", variable=self.include_letters)
        self.letters_check.pack()

        self.specials_check = tk.Checkbutton(root, text="Спецсимволы", variable=self.include_specials)
        self.specials_check.pack()

        # Кнопка генерации
        self.generate_button = tk.Button(root, text="Сгенерировать пароль", command=self.generate_password)
        self.generate_button.pack()

        # Таблица истории
        self.history_label = tk.Label(root, text="История паролей:")
        self.history_label.pack()

        self.history_text = tk.Text(root, height=10, width=50)
        self.history_text.pack()

    def generate_password(self):
        length = self.length_slider.get()
        if length < 8 or length > 20:
            messagebox.showerror("Ошибка", "Длина пароля должна быть от 8 до 20 символов.")
            return

        characters = ""
        if self.include_digits.get():
            characters += "0123456789"
        if self.include_letters.get():
            characters += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.include_specials.get():
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/"
        
        if not characters:
            messagebox.showerror("Ошибка", "Выберите хотя бы один тип символов.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.history_text.insert(tk.END, f"{password}\n")
        self.save_history(password)

    def save_history(self, password):
        history = []
        if os.path.exists("history.json"):
            with open("history.json", "r") as f:
                history = json.load(f)
        
        history.append(password)

        with open("history.json", "w") as f:
            json.dump(history, f)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()