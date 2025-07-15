from class_repository import RepositoryHospital


# Пробуем
if __name__ == "__main__":
    repository = RepositoryHospital()

    # тест соединения
    # repository.test_connection()

    # первый запрос EXISTS 
    print("Первый запрос EXISTS:")
    print(repository.request_exists_one())
    print()

    # второй запрос EXISTS
    print("Второй запрос EXISTS:")
    print(repository.request_exists_two())
    print()

    # Запрос ANY 
    print("Запрос ANY:") 
    for i in repository.request_any():
        print(i)
    print()

    # Запрос SOME
    print("Запрос SOME:") 
    for i in repository.request_some():
        print(i)
    print()

    # Запрос ALL
    print("Запрос ALL:") 
    for i in repository.request_all():
        print(i)
    print()

    # Запрос ANY + ALL
    print("Запрос ANY + ALL:") 
    for i in repository.request_any_all():
        print(i)
    print()

    # Запрос UNION
    print("Запрос UNION:") 
    for i in repository.request_union():
        print(i)
    print()

    # Запрос UNION ALL
    print("Запрос UNION ALL:") 
    for i in repository.request_union_all():
        print(i)
    print()

    # Запрос INNER JOIN
    print("Запрос INNER JOIN:") 
    for i in repository.request_inner_join():
        print(i)
    print()

    # Запрос LEFT JOIN
    print("Запрос LEFT JOIN:") 
    for i in repository.request_left_join():
        print(i)
    print()

    # Запрос RIGHT JOIN
    print("Запрос RIGHT JOIN:") 
    for i in repository.request_right_join():
        print(i)
    print()

    # Запрос LEFT RIGHT JOIN
    print("Запрос LEFT RIGHT JOIN:") 
    for i in repository.request_left_right_join():
        print(i)
    print()

    # Запрос FULL JOIN
    print("Запрос FULL JOIN:") 
    for i in repository.request_full_join():
        print(i)
    print()
