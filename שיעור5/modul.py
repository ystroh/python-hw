import os
def create_file(place):
    os.mkdir(place)
def delete_packeg(place):
    os.rmdir(place)
def creat_file_in_pack(place):
    with open(place,'w') as file:
        file.write("fff")
def update_file(place,data):
    with open(place,'a') as  file:
        file.write(data)
def delete_file (place):
    os.remove(place)
def return_files_from_pack(place):
    list_files = os.listdir(place)
    print(list_files)
def return_file_place():
  print (os.getcwd())