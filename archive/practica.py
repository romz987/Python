class Human:


    def __init__(self):
        self.full_name = ''
        self.dob = ''
        self.phone = ''
        self.town = ''
        self.contry = ''


    def set_data(self, full_name, dob, phone, town, contry):
        self.full_name = full_name
        self.dob = dob
        self.phone = phone
        self.town = town
        self.contry = contry 


    def get_data_dict(self):
        _dict = {
            'full_name': self.full_name,
            'dob': self.dob,
            'phone': self.phone,
            'town': self.town,
            'contry': self.contry
        }

        return _dict


hm = Human()

full_name = input('Введите Ваше имя: ')
dob = input('Введите дату рождения: ')
phone = input('Введите Ваш номер телефона: ')
town = input('Введите Ваш город: ')
contry = input('Введите Вашу страну: ')

hm.set_data(full_name, dob, phone, town, contry)

result = hm.get_data_dict()
print(result)

for key, value in result.items():
    print(f'{key} - {value}')
