from src.masks import get_mask_account, get_mask_card_number


card_number = "7000792289606361"
"""экспериментальный номер карты"""
mask_card_resalt = get_mask_card_number(card_number)
print(mask_card_resalt)


account_number = "7000792289606361"
"""экспериментальный номер счета"""
mask_account_resalt = get_mask_account(card_number)
print(mask_account_resalt)
