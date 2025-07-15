class Note:

    def __init__(self, title: str, text: str, date: str):
        self.title = title
        self.text = text
        self.date = date

    def __str__(self):
        """ Информация о записке """
        return (
            f"{self.title}\n{self.text}\n\t{self.date}"
        )




