import csv

def creating(path):
    with open(path, 'w', encoding='utf-8') as data:
        fw = csv.writer(data, delimiter=';', lineterminator='\n')
        fw.writerow(['id', 'Название', 'Описание', 'Дата и время создания/изменения'])

def recording_note_scv(info, path):
    with open(path, 'a', encoding='utf-8') as data:
        fw = csv.writer(data, delimiter=';', lineterminator='\n')
        fw.writerow(info)

def override_notes_scv(notes, path):
    with open(path, 'w', encoding='utf-8') as data:
        fw = csv.writer(data, delimiter=';', lineterminator='\n')
        for line in notes:
            fw.writerow(line)
            

def from_file(file):
    lst = []
    with open(file, 'r', encoding='utf-8') as data:
        fr = csv.reader(data, delimiter=';')
        for line in fr:
            lst.append(line)
    return lst