# LAB 1.1.1.6
class MobilePhone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return f'mobile phone {self.number} is turned on'

    def turn_off(self):
        return 'mobile phone is turned off'

    def call(self, number):
        return f'calling {number}'


personal_phone = MobilePhone(number=6123456789)
burner_phone = MobilePhone(number=6987654321)

print(personal_phone.turn_on())
print(burner_phone.turn_on())

print(burner_phone.call(personal_phone.number))

print(personal_phone.turn_off())
print(burner_phone.turn_off())
