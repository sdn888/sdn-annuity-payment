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


# Пример использования
loan_amount = float(input("Введите сумму кредита: "))
annual_rate = float(input("Введите годовую процентную ставку: "))
loan_term_months = int(input("Введите срок кредита в месяцах: "))

monthly_payment = annuity_payment(loan_amount, annual_rate, loan_term_months)
print(f"Ежемесячный платеж: {monthly_payment} руб.")
