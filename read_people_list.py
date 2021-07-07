import csv


def read_people_list():
    tsv_file = open("./config/owners_record_list.tsv", encoding='utf-8')
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    people_list = list()
    for row in read_tsv:
        people_list.append(row)
    people_list.pop(0)
    tsv_file.close()
    return people_list
