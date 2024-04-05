class CashMachine():
    def __init__(self):
        self._cash_drawer = []

    def payin_money(self, notes):
        self._cash_drawer.extend(notes)
        self._cash_drawer.sort(reverse=True)

    def withdraw_money(self, amount):
        payout = []
        for note in self._cash_drawer:
            if note + sum(payout) <= amount:
                payout.append(note)

        if sum(payout) == amount:
            for note in payout:
                self._cash_drawer.remove(note)
            return payout
        return []


cash_machine = CashMachine()
cash_machine.payin_money([10,20,100,500,20,20])
withdrawal  = cash_machine.withdraw_money(60)
print(withdrawal) # ==> [100,50]
second_withdrawal = cash_machine.withdraw_money(110)
print(second_withdrawal) # ==> []
#
cs = CashMachine()
cs.payin_money([20,50,50, 100,200,20,20,20])
withdrcs = cs.withdraw_money(460)
print(withdrcs)

