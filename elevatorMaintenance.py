# This is a level 2 challenge from Google foobar

list1 = [
    "1.11",
    "2.0.0",
    "1.2",
    "2",
    "0.1",
    "1.2.1",
    "1.1.1",
    "2.0"]

list2 = [
    "1.1.2",
    "1.0",
    "1.3.3",
    "1.0.12",
    "1.0.2"]


def deplicate_list(list):
    new_list1 = []
    new_list2 = []
    for item in list:
        new_list2.clear()
        new_item = ""
        x = 0
        for character in item:
            x += 1
            if character.isnumeric():
                new_item += character
                if x == len(item):
                    new_list2.extend(new_item)
            else:
                new_list2.extend(new_item)
                new_item = ""
        new_list1.append(new_list2)
    return new_list1


list3 = deplicate_list(list2)
print(list3)
