money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Счетчик месяцев

while money_capital + salary >= spend:
    money_capital += salary - spend
    spend *= (1 + increase)
    months += 1



print("Количество месяцев, которое можно протянуть без долгов:", months)





salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Начальное значение подушки безопасности
current_spend = spend  # Переменная для расчета расходов

for _ in range(months):
    if salary < current_spend:
        money_capital += current_spend - salary
    current_spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))