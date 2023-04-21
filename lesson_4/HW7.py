
class CourtCase:
    def __init__(self, case_number):
        self.case_number = case_number
        self.case_participants = []
        self.listening_datetimes = []
        self.if_finished = False
        self.verdict = ''

    def set_a_listening_datetime(self, date, time):
        self.listening_datetimes.append({date: time})

    def add_participant(self, INN):
        self.case_participants.append(INN)

    def remove_participants(self, INN):
        self.case_participants.remove(INN)

    def make_a_decision(self, verdict):
        self.verdict += verdict
        if verdict != '':
            self.if_finished = True


# Проверка работоспособности программы
x = CourtCase('A-123456')
x.set_a_listening_datetime('12.12.2022', '10:00')

print(x.listening_datetimes)

x.set_a_listening_datetime('17.12.2022', '14:00')

print(x.listening_datetimes)

x.add_participant('214652134765')

print(x.case_participants)

x.make_a_decision('Полностью оправдан.')

print(x.verdict)

b = CourtCase('А-1233217')

print(b.verdict, b.case_number, b.case_participants, b.listening_datetimes)
print(x.verdict, x.case_number, x.case_participants, x.listening_datetimes)

b.make_a_decision('Штраф 5000 рублей.')
print(b.verdict, b.case_number, b.case_participants, b.listening_datetimes)