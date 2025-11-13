# list1 = ["aaaa", "sssss", "fffff", "d"]
# new_list = [i for i in list1 if len(i) > 3]
# print(new_list)
# list2 = [1, 2, 3]
# new_list_number = [i*2 for i in list2 if i % 3 > 0]
# print(new_list_number)
# num_dict = {i:  i*i if i % 2 == 0 else None for i in list2}
# print(num_dict)
# num_dict2 = {i: len(i) for i in list1}
# print(num_dict2)
#
# dict_3 = {"yehudit":18,"michal":19}
# new_dict3 = { }
from modul import create_file, delete_file, creat_file_in_pack, update_file, return_files_from_pack, return_file_place

# create_file("Z:\יד תשפו\סטרו יהודית\python\pack2")
# delete_file("Z:\יד תשפו\סטרו יהודית\python\pack")
creat_file_in_pack("Z:\יד תשפו\סטרו יהודית\python\pack2\ile1")
#update_file("Z:\יד תשפו\סטרו יהודית\python\pack9","somthing")
#delete_file("Z:\יד תשפו\סטרו יהודית\python\pack9")
return_files_from_pack("Z:\יד תשפו\סטרו יהודית\python\pack2")
return_file_place()