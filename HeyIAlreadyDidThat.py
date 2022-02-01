'''
1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2

For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999.
Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value.
For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and
it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174,
and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.

Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10,
write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with n.
For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3.
If the algorithm reaches a constant, such as 0, then the length is 1.
'''


def sort_num(z):
    y = sorted(z)
    # use x = y[:] in py2
    x = y.copy()
    x.reverse()
    x = int(''.join(x))
    y = int(''.join(y))
    return x, y


def to_decimal(num, b):
    length = len(num)
    new_num = 0
    for s in num:
        length -= 1
        new_num = new_num + int(s) * b ** length
    return new_num


def to_base(num, b):
    num_list = []
    m = 0
    while num != 0:
        m = num % b
        m = str(m)
        num_list.append(m)
        num = num // b
    num_list.reverse()
    value = ''.join(num_list)
    return value


def cal_new_z(x, y, b):
    new_z = 0
    if b == 10:
        new_z = str(x - y)
    else:
        x = to_decimal(str(x), b)
        y = to_decimal(str(y), b)
        new_z = x - y
        new_z = to_base(new_z, b)
    return new_z


def solution(n, b):
    k = len(n)
    list1 = [n]
    z = n
    while True:
        x, y = sort_num(z)
        z = cal_new_z(x, y, b)
        while len(z) < k:
            z = "0" + z
        list1.append(z)
        if list1.count(z) == 2:
            length = len(list1) - list1.index(z) - 1
            return length


print(solution('210011', 3))

