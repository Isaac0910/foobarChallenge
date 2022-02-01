def solution(n, b):
    # Your code here
    def sort_num(n):
        y = sorted(n)
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


print(solution('210022', 3))