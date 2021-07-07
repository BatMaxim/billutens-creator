import read_people_list


def add_person_info(person, info):
    new_person = person
    for i, item in enumerate(person):
        new_person[i] = new_person[i] + ", " + info[i]
    return new_person


def change_doc_part(data):
    for item in data:
        item[4] += f", {item[5]}"
        item.append(f"{item[2]};{item[3]}")
        item.append(f"{item[5]};{item[3]}")
    return data


def get_update_people_list():
    data = change_doc_part(read_people_list.read_people_list())
    people = set()
    for item in data:
        people.add(item[0])

    new_people_list = []
    for person in people:
        new_person = []
        for item in data:
            if item[0] == person:
                if len(new_person) == 0:
                    new_person = item
                else:
                    new_person = add_person_info(new_person, item)
        new_people_list.append(new_person)
    return new_people_list
