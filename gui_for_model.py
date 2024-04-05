#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import scrolledtext

# ф-я для генерації тексту
def generate_text(prompt, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(model.device)
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# ф-я для обробки натискання кнопки "Генерувати"
def generate_button_click():
    prompt_text = input_text.get("1.0", tk.END).strip()  # Отримання тексту з поля вводу
    generated_text = generate_text(prompt_text)  # Генерація тексту за допомогою моделі
    output_text.delete("1.0", tk.END)  # Очищення поля виводу
    output_text.insert(tk.END, generated_text)  # Виведення згенерованого тексту

# Створення основного вікна програми
root = tk.Tk()
root.title("Генератор постів GPT-2")

# Створення поля вводу для тексту
input_text = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
input_text.grid(row=0, column=0, padx=10, pady=10)

# Створення кнопки "Генерувати"
generate_button = tk.Button(root, text="Генерувати", command=generate_button_click)
generate_button.grid(row=1, column=0, padx=10, pady=5)

# Створення поля виводу для згенерованого тексту
output_text = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
output_text.grid(row=2, column=0, padx=10, pady=10)

# Запуск головного циклу програми
root.mainloop()

