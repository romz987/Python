1. Установил odbc:  

        sudo emerge --ask dev-db/unixODBC

2. Установил alien (в @world)

3. Конвертировал пакет для ubuntu в .tgz

4. Распаковал его:  

        tar -xvzf <package_name> -C / 

5. Создал /etc/odbcinst.ini (похоже, что зря)

6. Установил драйвер:  

        sudo odbcinst -i -d -f /etc/odbcinst.ini
        похоже, что не совсем правильно, ну ладно... 

7. Проверил, что как:  

        odbcinst -j
        odbcinst -q -d

8. Как потом все это удалять? - 
С помощью tar посмотреть содержимое архива без распаковки и будет видно, куда он что собрался разложить.
