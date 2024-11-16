from TransactionError import TransactionError, ActionError


class ATM:

    MULTIPLICITY = 50
    PERCENT_WITHDRAWAL = 1.5
    MIN_SUM_PERCENT = 30
    MAX_SUM_PERCENT = 600
    LIMIT_TRANSACTION = 3
    PERCENT_FOR_TRANSACTION = 3
    SUM_WEALTH = 5_000_000
    TAX_ON_WEALTH = 10

    def __init__(self, state: bool = True) -> None:
        self.state = state
        self.summ = 0
        self.count = 0

    def action(self) -> str:
        result = input('Ваше действие?:\n'
                       'Нажмите п - если хотите ПОПОЛНИТЬ,\n'
                       'Нажмите с - если хотите СНЯТЬ,\n'
                       'Нажмите в - если хотите ВЫЙТИ,\n')
        return result

    def refill(self) -> int:
        result = int(input(f'сумма пополнения, кратно {self.MULTIPLICITY}: '))
        return result

    def withdrawal(self) -> int:
        result = int(input(f'сумма снятия, кратно {self.MULTIPLICITY}: '))
        return result

    def sum_str(self) -> str:
        return f'Остаток денег на счету - {self.summ}'

    def sum_for_transaction(self, value: int) -> int:
        result = round(value * self.PERCENT_FOR_TRANSACTION / 100)
        return result

    def sum_tax_wealth(self, value: int) -> int:
        result = round(value * self.TAX_ON_WEALTH / 100)
        return result

    def sum_percent_withdrawal(self, value: int) -> int:
        result = round(value * self.PERCENT_WITHDRAWAL / 100)
        return result


atm = ATM()
while atm.state:
    action = atm.action()
    if action == 'п':
        temp = atm.refill()

        if atm.summ > atm.SUM_WEALTH:
            sum_tax_wealth = atm.sum_tax_wealth(atm.summ)
            atm.summ -= sum_tax_wealth

        if temp % atm.MULTIPLICITY != 0:
            continue

        sum_for_transaction = 0
        atm.count += 1
        if atm.count == atm.LIMIT_TRANSACTION:
            atm.count = 0
            sum_for_transaction = atm.sum_for_transaction(temp)
        atm.summ += (temp - sum_for_transaction)
        print(atm.sum_str())
    elif action == 'с':
        temp = atm.withdrawal()

        if atm.summ > atm.SUM_WEALTH:
            sum_tax_wealth = atm.sum_tax_wealth(atm.summ)
            atm.summ -= sum_tax_wealth

        if temp % atm.MULTIPLICITY != 0:
            continue

        sum_percent_withdrawal = atm.sum_percent_withdrawal(temp)
        if sum_percent_withdrawal < atm.MIN_SUM_PERCENT:
            sum_percent_withdrawal = atm.MIN_SUM_PERCENT
        elif sum_percent_withdrawal > atm.MAX_SUM_PERCENT:
            sum_percent_withdrawal = atm.MAX_SUM_PERCENT

        sum_for_transaction = 0
        atm.count += 1
        if atm.count == atm.LIMIT_TRANSACTION:
            atm.count = 0
            sum_for_transaction = atm.sum_for_transaction(temp)

        if (temp + sum_percent_withdrawal + sum_for_transaction) > atm.summ:
            raise TransactionError

        atm.summ -= (temp + sum_percent_withdrawal + sum_for_transaction)
        print(atm.sum_str())
    elif action == 'в':
        print(atm.sum_str())
        atm.state = False

    else:
        raise ActionError
