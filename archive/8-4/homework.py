class PCPowerBlock:

    power = '650Wt'

    def switch_on(self):
        print('Блок питания включен')


class PCMotherboard:

    chipset = 'AMD B550'

    def distrib_voltage(self):
        print('Материнская плата распределяет напряжение')

class PCCPU:

    cpu_frequency = '3.9GHz'
    cores_count = 6 

    def activate_turbo_mode(self):
        print('Турбо-режим активирован')


class PCRam:

    ram_capacity = '32Gb'
    ram_frequency = '5600Mhz'

    def upload_data(self):
        print('данные загружены в оперативную память')

    def download_data(self):
        print('данные выгружены из оперативной памяти')


class PCSSD:

    ssd_capacity = '1Tb'

    def save_data(self):
        print('данные записаны на ssd диск')

    def erase_data(self):
        print('данные удалены из ssd диска')


class PSGraphicsCard:

    graphic_card_model = 'Radeon RX 7800XT'
    graphic_card_memory = '16Gb'

    def start_casting(self):
        print('Видеокарта начала выводить изображение на экран')


# Множественное наследование
class ComputerOne(PCPowerBlock, PCMotherboard, PCCPU, PCRam, PCSSD, PSGraphicsCard):

    def __init__(self):
        pass

    def start_computer(self):
        self.switch_on()
        self.distrib_voltage()
        self.activate_turbo_mode()
        self.upload_data()
        self.save_data()
        self.start_casting()


# Композиция
class ComputerTwo:
    def __init__(self):
        self.power_block = PCPowerBlock()
        self.motherboard = PCMotherboard()
        self.cpu = PCCPU()
        self.ram = PCRam()
        self.ssd = PCSSD()
        self.graphics_card = PSGraphicsCard()

    def start_computer(self):
        self.power_block.switch_on()
        self.motherboard.distrib_voltage()
        self.cpu.activate_turbo_mode()
        self.ram.upload_data()
        self.ssd.save_data()
        self.graphics_card.start_casting()


# Тест
computer = ComputerOne()
computer.start_computer()
print('\n\n')
computer = ComputerTwo()
computer.start_computer()
