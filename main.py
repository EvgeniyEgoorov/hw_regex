from pprint import pprint
import csv
import re
import pandas as pd

pd.set_option('display.max_columns', None)


def read(file):
    with open(file, encoding='utf-8') as f:
        rows = csv.reader(f)
        contacts_list = list(rows)
        text(contacts_list)


def text(data):
    revised_text = []
    for item in data:
        string = ','.join(item)
        pattern = r'^([А-ЯЁа-яё]+)[\s,]*([А-ЯЁа-яё]+)[\s,]*([А-ЯЁа-яё]*)[\s,]*([А-ЯЁа-яё]*)[\s,]*' \
                  r'((?<=,)\D*?(?=,))*[\s,]*((?<=,).*?(?=,))*,*([A-Za-z0-9@.]*)'
        repl = r'\1, \2, \3, \4, \5, \6, \7'
        result = re.sub(pattern, repl, string)
        revised_text.append(result)
    phones(revised_text)


def phones(data):
    revised_phones = []
    for item in data:
        pattern2 = r'(\+7|8)[\s-]*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})([\s-]*\(*(доб\.\s\d+)\)*)*'
        repl2 = r' +7(\2)\3-\4-\5'
        result = re.sub(pattern2, repl2, item)
        revised_phones.append(result.split())
    write_draft(revised_phones)


def grouped():
    content = pd.read_csv('draft.csv')
    group = content.groupby('lastname').first()
    print(pd.DataFrame(group))


def write_draft(data):
    with open('draft.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=" ")
        writer.writerows(data)


def write_dict():
    pass


read('phonebook_raw.csv')
grouped()

