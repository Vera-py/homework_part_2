def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует часть номера банковской карты"""
    blocks = (
        card_number[:4],
        card_number[4:6] + "**",
        "****",
        card_number[-4:],
    )
    return " ".join(blocks)


def get_mask_account(account_number: str) -> str:
    """Функция берет 4 последние символа банковского счёта"""
    mask_account = account_number[-4:]
    return f"**{mask_account}"
