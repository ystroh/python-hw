str="hjfjf khk 111"

def clearFunc(str):
    new_str = ""
    for c in str:
        if c.isnumeric() or c.isalpha():
            new_str+=c;
    return new_str;
print(clearFunc("abc #666"))

def popolar_func (str):
    list = str.split(" ")
    max = 0;
    prev_ward=""
    for i in list:
        if str.count(i) > max :
            max = str.count(i)
            prev_ward = i
    return prev_ward

print(popolar_func("ab ab s d d"))

def func (str):
    list = str.split(" ")
    str_new = ""
    for i in list:
        str_new += i[0]
    return str_new
print(func("a b"))