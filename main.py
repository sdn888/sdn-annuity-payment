import pandas as pd
import matplotlib.pyplot as plt


def annuity_payment(loan_amount, annual_rate, loan_term_months):
    """
    Рассчитывает ежемесячный аннуитетный платеж по кредиту.
    :param loan_amount: Сумма кредита (основной долг)
    :param annual_rate: Годовая процентная ставка (в процентах)
    :param loan_term_months: Срок кредита в месяцах
    :return: Ежемесячный аннуитетный платеж
    """
    monthly_rate = annual_rate / 100 / 12  # Преобразуем годовую ставку в месячную

    if monthly_rate == 0:
        return loan_amount / loan_term_months  # Если ставка 0%, просто делим долг на количество месяцев

    annuity_coefficient = (monthly_rate * (1 + monthly_rate) ** loan_term_months) / \
                          ((1 + monthly_rate) ** loan_term_months - 1)

    monthly_payment = loan_amount * annuity_coefficient
    return round(monthly_payment, 2)


def generate_amortization_schedule(loan_amount, annual_rate, loan_term_months):
    """
    Генерирует график погашения кредита.
    :param loan_amount: Сумма кредита
    :param annual_rate: Годовая процентная ставка (в процентах)
    :param loan_term_months: Срок кредита в месяцах
    :return: DataFrame с графиком платежей
    """
    monthly_payment = annuity_payment(loan_amount, annual_rate, loan_term_months)
    monthly_rate = annual_rate / 100 / 12
    balance = loan_amount
    schedule = []

    for month in range(1, loan_term_months + 1):
        interest_payment = balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment
        schedule.append([month, round(monthly_payment, 2), round(interest_payment, 2), round(principal_payment, 2),
                         round(balance, 2)])

    return pd.DataFrame(schedule, columns=["Месяц", "Платеж", "Проценты", "Основной долг", "Остаток долга"])


def plot_amortization_schedule(schedule):
    """
    Визуализирует график погашения кредита.
    :param schedule: DataFrame с графиком платежей
    """
    plt.figure(figsize=(10, 5))
    plt.plot(schedule["Месяц"], schedule["Проценты"], label="Процентные выплаты", color='r')
    plt.plot(schedule["Месяц"], schedule["Основной долг"], label="Погашение основного долга", color='b')
    plt.xlabel("Месяц")
    plt.ylabel("Сумма в рублях")
    plt.title("График погашения кредита")
    plt.legend()
    plt.grid()
    plt.show()


# Пример использования
loan_amount = float(input("Введите сумму кредита: "))
annual_rate = float(input("Введите годовую процентную ставку: "))
loan_term_months = int(input("Введите срок кредита в месяцах: "))

monthly_payment = annuity_payment(loan_amount, annual_rate, loan_term_months)
schedule = generate_amortization_schedule(loan_amount, annual_rate, loan_term_months)
print(schedule)
plot_amortization_schedule(schedule)
