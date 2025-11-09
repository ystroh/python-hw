# list=[1,1,2,3,4,5]
#
#
# def creatSet(list):
#     my_set = set()
#     min=1000
#     max=0
#     sum=0
#     for i in list :
#         my_set.add(i)
#         if i>max :
#             max=i
#         if i<min :
#             min=i
#         sum+=i
#     my_set.add(min)
#     my_set.add(max)
#     my_set.add(sum/len(list))
#     return my_set
# print(creatSet(list))
#
d={"a":5,"b":3}

def filter_dict(d, threshold) :
    list=[]
    for k, v in d.items() :
        if v > threshold :
            list.append(k)
    return list
print(filter_dict(d, 4))