import os
from class_note_manager import NoteManager
from class_note import Note
from class_command import AddNoteCommand


if __name__ == "__main__":
    nmanager = NoteManager()

    while True:
        os.system('clear')
        print("Менеджер записок")
        print("1. Создать записку")
        print("2. Отменить создание последней записки")
        print("3. Показать все записки")
        print()
        print("0. Выход")
        print("\n")
        choice = input("Выберите опцию: ")

        # Создать записку
        if choice == "1":
            os.system('clear')
            try: 
                title = str(input("Введите заголовок записки: "))
                text = str(input("Введите текст записки: "))
                date = str(input("Введите текущую дату: "))
                print()
                note = Note(title, text, date)
                command = AddNoteCommand(nmanager, note)
                command.execute()
                 
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        # Отменить создание последней записки
        elif choice == "2":
            os.system('clear')
            try: 
                command.undo()
                print("Последняя записка удалена!")

            except NameError:
                print("Записки еще не добавлялись!")
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        # Показать все записки
        elif choice == "3":
            os.system('clear')
            try: 
                notes_list = nmanager.get_notes_list()
                if notes_list:
                    for note in notes_list:
                        print(note.__str__())
                else:
                    print("Записок нет")
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        # Выход
        elif choice == "0":
            os.system('clear')
            exit()
