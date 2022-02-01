# Level 2 challenge from Google foobar

list1 = ["1.11",
         "2.0.0",
         "1.2",
         "2",
         "0.1",
         "1.2.1",
         "1.1.1",
         "2.0"]

list2 = ["1.1.2",
         "1.0",
         "1.3.3",
         "1.0.12",
         "1.0.2"]

list3 = ["11.12.04",
         "9.88",
         "3.2.1",
         "0.99",
         "1",
         "1.1",
         "1.1.1"]


def sort_elevator_version(l):
    new_list = []
    version = []
    for item in l:
        version = item.split(".")
        x = len(version)
        for i in range(x):
            version[i] = int(version[i])
        new_list.append(version)
    new_list.sort()

    elevator_version = []
    x = len(new_list)
    for i in range(x):
        version = ""
        y = len(new_list[i])
        for j in range(y):
            version += str(new_list[i][j])
            if j + 1 < y:
                version += "."
        elevator_version.append(version)
    return elevator_version


print(sort_elevator_version(list1))
print(sort_elevator_version(list2))
print(sort_elevator_version(list3))
