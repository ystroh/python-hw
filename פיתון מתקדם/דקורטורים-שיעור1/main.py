# import datetime
#
#
# def dec(function):
#     def in_dec():
#         print(datetime.datetime.now())
#         function()
#         print(datetime.datetime.now())
#     return in_dec
#
# @dec
# def long():
#     for _ in range(9999999):
#         count = 0
#
# @dec
# def short():
#     for _ in range(1):
#         count = 0
#
# long()
# short()
dict = {}

def dec2(func):
    def new_func(*arg):
        for k,v in dict:
            if(k == func.__name__):
                for k2,v2 in v:
                    if(k2==arg):
                        return v2
                    else:
                        resalt = func(*arg)
                        dict[k][len]={arg,resalt}
                        return resalt
            else:
                resalt = func(*arg)
                dict[len] = {func.__name__, {arg,resalt}}
                return resalt
    return new_func
@dec2
def f(x):
    return x+1

print(f(1))