import datetime
from os.path import exists
import file

def add_info(path):
    new_note= []
    new_note.append(get_next_id(path))
    title = input('Введите название заметки: ')
    new_note.append(title)
    description = input('Введите описание заметки: ')
    new_note.append(description)
    current_date_time = datetime.datetime.now()
    new_note.append(current_date_time)
    return new_note

def del_note(path, id):
    notes = file.from_file(path)
    del notes[id]
    file.override_notes_scv(notes, path)
    print(f'Запись под номером {id} удалена.')

def change_note(path, id):
    notes = file.from_file(path)
    print(f'Введите новые данные для записи под номером {id}.')
    notes[id][1] = input('Введите новое название заметки: ')
    notes[id][2] = input('Введите новое описание заметки: ')
    notes[id][3] = str(datetime.datetime.now())
    file.override_notes_scv(notes, path)
    print(f'Запись под номером {id} изменена.')

def filter_notes(path, date):
    info = file.from_file(path)
    for i in range(1, len(info)):
        if str(info[i][3][:10]) == date:
            print(f'{info[i][0]}. {info[i][1]}: {info[i][2]}. Дата и время создания: {info[i][3][:-7]}')

def get_next_id(path):
    info = file.from_file(path)
    if info[len(info) - 1][0] == 'id':
        return 1
    return int(info[len(info) - 1][0]) + 1

def view(path):
    info = file.from_file(path)
    for i in range(1, len(info)):
            print(f'{info[i][0]}. {info[i][1]}: {info[i][2]}. Дата и время создания: {info[i][3][:-7]}')


def record_info(path):
    info = add_info(path)
    file.recording_note_scv(info, path)

def choice(path):
    flag = input(
        'Для продолжения работы наберите \'да\', или любой символ для завершения работы... ')
    while (flag.lower() == 'да'):
        valid = exists(path)
        if not valid:
            file.creating(path)
        choice_action = input(
            'Введите 1, чтобы добавить новую заметку \n2 - посмотреть полный список заметок\n3 - посмотреть заметки, созданные или измененные в определенную дату \n4 - изменить заметку, указав ее порядковый номер \n5 - удалить заметку\n')
        if choice_action.lower() == '1':
            record_info(path)
        elif choice_action == '2':
            view(path)
        elif choice_action == '3':
            date = input('Введите дату в формате yyyy-mm-dd: ')
            filter_notes(path, date)
        elif choice_action == '4':
            id = int(input('Введите номер заметки: '))
            change_note(path, id)
        elif choice_action == '5':
            id = int(input('Введите номер заметки: '))
            del_note(path, id)
        flag = input(
            'Для продолжения работы наберите \'да\', или любой символ для завершения работы... ')
    print('Программа завершена.')
