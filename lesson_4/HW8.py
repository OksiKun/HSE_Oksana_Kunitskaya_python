class Contract:

    def __init__(self, date, contractor, subject, price, validity_period):
        self.date = date
        self.contractor = contractor
        self.subject = subject
        self.price = price
        self.currency = 'Руб'
        self.validity_period = validity_period
        self.active = True

    def change_the_price(self, price):
        self.price = price

    def terminate_the_contract(self):
        print('Договор расторгнут.')
        self.active = False

    def extend_the_contract(self):
        if active == False:
            print('Договор уже расторгнут.')
        else:
            print('Договор продлен.')


a = Contract('12.12.2022', 'ООО "Ромашка"', 'Поставка', '1000000', '6 месяцев')

print(a)
print(a.date, a.contractor, a.subject, a.price, a.validity_period)

a.change_the_price('1200000')
print(a.date, a.contractor, a.subject, a.price, a.validity_period)

a.terminate_the_contract()
print(a.active)

