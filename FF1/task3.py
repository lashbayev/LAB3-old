def filter_prime(*list):
    list1 = list()
    for x in range(len(list) + 1):
        for i in range(1, x + 1):
            if (x % i != 0) and ((i == 1 and x % i == 0) and (i == x and x % i == 0)):
                list1.append(x)
    return list1

    

filter_prime([1,3,7,9,11,23,24,64,16,81,100])
                 