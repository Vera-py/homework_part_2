def get_mask_card_number(account_card: str) -> str:
    """Функция маскирует часть номера банковской карты"""
    card_number_mask = [account_card[-16:-12], account_card[-12:-10] + "**", "****", account_card[-4:]]
    return " ".join(card_number_mask)


def get_mask_account(account_card: str) -> str:
    """Функция берет 4 последние символа банковского счёта"""
    mask_account = account_card[-4:]
    return f"**{mask_account}"