# Final solution - after reading Morsels solution
def get_earliest(*args):
    def get_date(arg):
        d, m, y = arg.split("/")
        return y, m, d
    return min(args, key=get_date)


get_earliest("02/24/1946", "01/29/1946", "03/29/1945")



# Only for two arguments - first attempt
'''
def get_earliest(date_a, date_b):
    a, b, c = date_a.split("/")
    a1, b1, c1 = date_b.split("/")

    date_a1 = (c, a, b)
    date_b1 = (c1, a1, b1)

    if date_a1 <= date_b1:
        return date_a
    else:
        return date_b
'''


# Working for multiple arguments but not optimal - second attempt
'''
def get_earliest(*args):    
    arguments = []
    for arg in args:
        a, b, c = arg.split("/")
        arg = (c, a, b)
        arguments.append(arg)

    min_argument = min(arguments)
    result = min_argument[1] + "/" + min_argument[2] + "/" + min_argument[0]
    return result
'''
