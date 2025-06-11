def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Функция формирует новый список банковских операций по заданному параметру"""
    seleсted_operations = []
    for operation in operations:
        if "state" in operation and operation["state"] == state:
            seleсted_operations.append(operation)
    return seleсted_operations


def sort_by_date(operations: list) -> list:
    """Функция сортирует список банковских операций по дате в убывающем порядке"""
    sorted_operations = sorted(operations, key=lambda operation: operation["date"], reverse=True)
    return sorted_operations
