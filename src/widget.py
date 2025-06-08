from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card: str) ->str:
    """Функция определяет введен номер счета или карты и маскирует соответственно данным"""
    if "Счет" in account_card:
        account_card_mask = f"Счет {get_mask_account(account_card)}"
    else:
        account_card_mask = f"{account_card[:-17]} {get_mask_card_number(account_card)}"
    return account_card_mask


def get_date(date: str) -> str:
    """Функция преобразует дату в формат дд.мм.гггг"""
    date_format = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return date_format