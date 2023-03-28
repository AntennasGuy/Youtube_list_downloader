# Программа создаёт батник (исполняемый файл Windows) для загрузки плей-листов с youtube через утилиту
# yt-dlp. Имеет два режима - запись для скачивания аудио и для скачивания видео.

from selenium import webdriver
from selenium.webdriver.common.by import By


def vvod():
    global text_line, path
    list = input('Введите адрес плей-листа: ')

    url = list
    browser = webdriver.Chrome()
    browser.maximize_window()  # важно максимизировать окно - могут быть проблемы с мобильной версией
    browser.implicitly_wait(10)
    browser.get(url)
    name_of_folder = browser.find_element(By.XPATH, '//*[@id="text"]').text
    name_of_folder = name_of_folder.split()
    name_of_folder = '_'.join(name_of_folder)
    print(name_of_folder)
    path = f'./{name_of_folder}'

    while True:
        vid_or_music = input('Хотите сохранить аудио или видео (1 - аудио, 2 - видео): ')
        if vid_or_music == '1':
            text_line = f' -f m4a {list}'
            break
        elif vid_or_music == '2':
            text_line = f' -f mp4 {list}'
            break
        else:
            print('Неверный выбор. Попробуйте еще раз.')


def write_text():
    with open('download_list.bat', 'a') as file:
        file.write(f'yt-dlp -P {path}{text_line}\n')


if __name__ == '__main__':
    while True:
        vvod()
        write_text()


