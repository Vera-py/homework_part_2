from src.widget import get_date, mask_account_card

account_card = "Visa Classic 683198247673765"
"""экспериментальный номер"""
print(mask_account_card(account_card))


date = "2024-03-11T02:26:18.671407"
"""экспериментальная дата"""
print(get_date(date))
