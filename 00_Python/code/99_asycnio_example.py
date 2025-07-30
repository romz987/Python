import asyncio  
from datetime import datetime 


# async def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         await asyncio.sleep(1)
#
#
# async def main():
#     await print_numbers() 


files_list = [
    ('comedy.mpeg', 5),
    ('good_book.djvu', 4),
    ('music.mp3', 7)
]


async def download_file(file_data: tuple):
    """ Функция загрузки файла """
    print(f'starting download {file_data[0]}')
    await asyncio.sleep(file_data[1])
    print(f'{file_data[0]} downloaded')


async def main(files_list):
    tasks_list = [
        asyncio.create_task(download_file(file)) for file in files_list
    ]
    for task in tasks_list:
        await task


if __name__ == "__main__":
    print(datetime.now())
    asyncio.run(main(files_list))
    print(datetime.now())
