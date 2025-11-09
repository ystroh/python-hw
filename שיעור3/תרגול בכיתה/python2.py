# def revers_list (list):
#     return list[::-1]
# l1=[1,2,3]
# print (revers_list(l1))
#
# def calculate_average(list):
#     count=0
#     for i in list:
#         count+=i
#     return count/len(list)
#
# print (calculate_average(l1))
#
# def in_prime(num):
#     for i in range(2,num-1):
#         if num % i == 0:
#             return False
#     return True
# print (in_prime(7))
#
# def fib_eq (n):
#     prev=0
#     now=1
#     list=[0,1]
#     for i in range (2,n) :
#         list.append(prev+now)
#         prev,now=prev+now,now
#     return list
# print (fib_eq(5))
#
# def pr(*args, **kwargs):
#     for i in args:
#         print (i)
#     for key, value in kwargs.items():
#         print (key, value)
#
# pr("aa","bb",a=3,b=2)

def finf(key_get,dict):
    for i in dict:
        for k,v in i.items():
            if k==key_get:
                print (v)
                return
    print("not found")


dict=[{'k':1},{'k':2}]

finf('k',dict)