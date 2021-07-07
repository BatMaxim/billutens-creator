import update_people_list


def find_all_squares():
    nums_sq = set()
    persons = update_people_list.get_update_people_list()
    for person in persons:
        if person[6].find(", ") == -1:
            nums_sq.add(person[6])
        else:
            nums = person[6].split(", ")
            for num in nums:
                nums_sq.add(num)

    summ = 0
    for item in nums_sq:
        summ += float(item.split(";")[1])
    return summ
