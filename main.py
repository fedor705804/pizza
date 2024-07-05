import tkinter as tk
from tkinter import ttk

# Функции для обновления заказа
def update_order():
    selected_items = "Пицца: " + pizza_var.get()
    selected_items += "\nДополнения: " + ", ".join([topping for topping, var in toppings_vars.items() if var.get()])
    selected_items += "\nНапиток: " + drink_var.get()
    selected_items += "\nСоус: " + sauce_var.get()
    # Добавление выбранного комбо в заказ
    if combo_var.get():
        selected_items += "\nКомбо: " + combo_var.get()
    order_details.config(text=selected_items)

# Создание главного окна
root = tk.Tk()
root.title("Заказ пиццы")

# Установка минимального размера окна
root.minsize(500, 400)

# Создание рамки для содержимого с возможностью прокрутки
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Канвас для прокрутки
canvas = tk.Canvas(main_frame)
canvas.pack(side="left", fill="both", expand=True)

# Добавление бегунка
scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Конфигурация канваса
canvas.configure(yscrollcommand=scrollbar.set)

# Создание другой рамки внутри канваса для элементов интерфейса
second_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Привязка функции к изменению размера канваса
def on_canvas_resize(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
canvas.bind('<Configure>', on_canvas_resize)

# Стилизация виджетов
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TRadiobutton', font=('Helvetica', 10))

# Переменные для хранения выбора пользователя
pizza_var = tk.StringVar()
drink_var = tk.StringVar()
sauce_var = tk.StringVar()
combo_var = tk.StringVar()
toppings_vars = {}

# Меню пицц
pizza_label = ttk.Label(second_frame, text="Выберите пиццу:", style='TLabel')
pizza_label.pack()
pizzas = ["Пепперони", "Маргарита", "Гавайская", "Четыре сыра", "С ветчиной и грибами"]
for pizza in pizzas:
    pizza_rb = ttk.Radiobutton(second_frame, text=pizza, variable=pizza_var, value=pizza, command=update_order, style='TRadiobutton')
    pizza_rb.pack()

# Меню дополнений
toppings_label = ttk.Label(second_frame, text="Выберите дополнения:", style='TLabel')
toppings_label.pack()
toppings = ["Оливки", "Помидоры", "Сыр", "Грибы", "Ветчина", "Бекон", "Курица", "Ананасы"]
for topping in toppings:
    var = tk.BooleanVar()
    toppings_vars[topping] = var
    topping_cb = ttk.Checkbutton(second_frame, text=topping, variable=var, onvalue=True, offvalue=False, command=update_order)
    topping_cb.pack()

# Меню напитков
drink_label = ttk.Label(second_frame, text="Выберите напиток:", style='TLabel')
drink_label.pack()
drinks = ["Кола", "Спрайт", "Фанта", "Лимонад", "Вода"]
for drink in drinks:
    drink_rb = ttk.Radiobutton(second_frame, text=drink, variable=drink_var, value=drink, command=update_order, style='TRadiobutton')
    drink_rb.pack()

# Меню соусов
sauce_label = ttk.Label(second_frame, text="Выберите соус:", style='TLabel')
sauce_label.pack()
sauces = ["Кетчуп", "Майонез", "Барбекю", "Чесночный", "Томатный"]
for sauce in sauces:
    sauce_rb = ttk.Radiobutton(second_frame, text=sauce, variable=sauce_var, value=sauce, command=update_order, style='TRadiobutton')
    sauce_rb.pack()

# Меню комбо
combo_label = ttk.Label(second_frame, text="Выберите комбо:", style='TLabel')
combo_label.pack()
combos = {
    "Комбо 1": "Пепперони + Кола + Кетчуп",
    "Комбо 2": "Маргарита + Фанта + Майонез",
    "Комбо 3": "Гавайская + Лимонад + Барбекю"
}
for combo_name, combo_content in combos.items():
    combo_rb = ttk.Radiobutton(second_frame, text=f"{combo_name} ({combo_content})", variable=combo_var, value=combo_name, command=update_order, style='TRadiobutton')
    combo_rb.pack()

# Место для отображения деталей заказа
order_details = ttk.Label(second_frame, text="Ваш заказ будет отображаться здесь.", style='TLabel')
order_details.pack()

# Запуск главного цикла
root.mainloop()