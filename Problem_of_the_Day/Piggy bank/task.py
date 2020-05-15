class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars = self.dollars + deposit_dollars
        if (self.cents + deposit_cents) < 100:
            self.cents = self.cents + deposit_cents
        else:
            self.dollars += (self.cents + deposit_cents) // 100
            self.cents = (self.cents + deposit_cents) % 100