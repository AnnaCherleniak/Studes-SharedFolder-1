class TransactionError(Exception):
    def __str__(self) -> str:
        return 'Недостаточно средств для снятия!'


class ActionError(Exception):
    def __str__(self) -> str:
        return 'Ошибка! Действие не определено'
