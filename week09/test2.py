def my_map_yield(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)


def my_map_return(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


def testfunc(x, y):
    return x*y


def testfunc2(x, y, z):
    return x*y*z


x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = [1, 3, 4, 5]


list(my_map_yield(testfunc, x, y))
list(my_map_return(testfunc, x, y))


list(my_map_yield(testfunc2, x, y, z))
list(my_map_return(testfunc2, x, y, z))