import csv


class CsvManager:

    def get_data_from_csv(self, filename: str) -> list:
        """ Получить данные из csv """
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            result = []
            next(reader, None)
            for row in reader:
                result.append(row)
            return result

    def get_customers_data(self) -> list:
        """ Получить данные из таблицы customers """        
        return self.get_data_from_csv("files/customers_data.csv")

    def get_employees_data(self) -> list:
        """ Получить данные из таблицы employees """
        return self.get_data_from_csv("files/employees_data.csv")

    def get_orders_data(self) -> list:
        """ Получить данные из таблицы orders """
        return self.get_data_from_csv("files/orders_data.csv")




csvman = CsvManager()
print(csvman.get_employees_data())

