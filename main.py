import find_all_squares
import read_meeting_description
import generate_qrcode
import fill_document
import add_questions
import update_people_list
import calc_squares
import add_picture


def calc_square(arr):
    sum_square = 0
    for item in arr:
        sum_square += float(item)
    return sum_square


def find_apart(aparts, target_apart):
    for i, apart in enumerate(aparts):
        if apart[0] == target_apart[0]:
            return i
    return -1


def parse_apart_nums(aparts, parts):
    new_aparts = []
    for i, apart in enumerate(aparts):
        new_apart = [apart, parts[i].split(";")[0], parts[i].split(";")[1]]
        if find_apart(new_aparts, new_apart) == -1:
            new_apart[1] = round(eval(new_apart[1]), 2)
            new_aparts.append(new_apart)
        else:
            new_apart[1] = round(eval(new_apart[1]), 2)
            new_aparts[find_apart(new_aparts, new_apart)][1] += new_apart[1]
            new_aparts[find_apart(new_aparts, new_apart)][2] = new_apart[2]
    aparts_to_str(new_aparts)
    return aparts_to_str(new_aparts)


def aparts_to_str(aparts):
    aparts_strs = []
    for apart in aparts:
        if len(aparts_strs) == 0:
            aparts_strs = [apart[0], apart[1], apart[2]]
        else:
            for i in range(3):
                aparts_strs[i] = f"{aparts_strs[i]}, {apart[i]}"
    return aparts_strs


def create_docs():
    meet_desc = read_meeting_description.read_meeting_description()
    meet_context = dict()

    for item in meet_desc["voting"]:
        meet_context.update({item.replace("-", "_"): meet_desc["voting"][item]})
    people_list = update_people_list.get_update_people_list()
    add_questions.add_questions(meet_context['agenda'])

    for row in people_list:
        part = calc_squares.calc_all_squares(row)
        percent = round(part / find_all_squares.find_all_squares(), 2)
        person_context = dict()
        aparts_data = parse_apart_nums(row[1].split(', '), row[7].split(', '))

        person_context.update({"name": ",".join(set(row[0].split(", ")))})
        person_context.update({"numApart": aparts_data[0]})
        person_context.update({"number": ",".join(set(row[2].split(", ")))})
        person_context.update({"square": round(calc_square(aparts_data[2].split(",")), 2)})
        person_context.update({"document": row[4]})
        person_context.update({"percent": percent})
        person_context.update({"part": part})
        context = person_context | meet_context

        file_name = f"{','.join(set(row[1].split(', '))).replace(' ', '')}_{','.join(set(row[0].split(', ')))}.docx"
        qr_str = f"{meet_context['id']};" \
                 f"{','.join(set(row[0].split(', ')))};" \
                 f"{aparts_data[0]};{aparts_data[2]};" \
                 f"{aparts_data[1]}"
        generate_qrcode.generate_qrcode(qr_str)
        fill_document.fill_document(context, file_name)
        add_picture.add_picture(file_name)


if __name__ == '__main__':
    create_docs()

