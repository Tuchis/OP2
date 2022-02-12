"""
LAB 2 1
Parser of the json file
"""
import json


def parse_kved(class_code: str) -> None:
    """
    The main function that parses the file and finds the required class
    Then writes it into the file
    >>> parse_kved("01.30")

    >>> parse_kved("02.10")

    """
    with open("kved.json", encoding="utf-8") as file:
        data = json.load(file)

    # nest = ["section", "division", "group", "class"]
    # search = [None, class_code[0:2], class_code[0:4], class_code]
    for first in range(len(data['sections'][0])):
        first_wave = data['sections'][0][first]
        for second in range(len(first_wave['divisions'])):
            second_wave = first_wave['divisions'][second]
            for triple in range(len(second_wave['groups'])):
                # print(data['sections'][0][first]['divisions'][second]['groups'])
                triple_wave = second_wave['groups'][triple]
                for forth in range(len(triple_wave['classes'])):
                    if triple_wave['classes'][forth]['classCode'] == class_code:
                        info = (first_wave['sectionName'], len(first_wave['divisions']),\
second_wave['divisionName'], len(second_wave['groups']), triple_wave['groupName'],\
len(triple_wave['classes']), triple_wave['classes'][forth]['className'])
    write_kved(info)


def write_kved(info: list) -> None:
    """
    Function, that writes information into file
    Writes into kved_results.json
    """
    types = ["section", "division", "group", "class"]

    for num in range(4):
        temper_dict = {}
        temper_dict["name"] = info[0 + num * 2]
        temper_dict["type"] = types[num]
        if num != 3:
            temper_dict["num_children"] = info[1 + num * 2]
        if num != 0:
            temper_dict["parent"] = temp_dict
        temp_dict = temper_dict

    with open("kved_results.json", "w", encoding="utf-8") as file:
        json.dump(temp_dict, file, indent=2, ensure_ascii = False)


def main(code: str) -> None:
    """
    MAIN function, that calls parser
    """
    parse_kved(code)


# if __name__ == "__main__":
#     main("02.10")
