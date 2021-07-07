def calc_all_person_s(person):
    sum_square = 0
    if person[7].find(",") == -1:
        nums = person[7].split(";")
        sum_square = eval(nums[0]) * float(nums[1])
    else:
        nums_parts = person[7].split(",")
        for item in nums_parts:
            nums = item.split(";")
            sum_square += eval(nums[0]) * float(nums[1])
    return sum_square


def calc_all_squares(person):
    return round(calc_all_person_s(person), 2)


