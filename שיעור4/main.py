
with open('file.txt', 'w') as file_right:
    file_right.write("this text\nis so short")


def num_wards(file):
    count = 1
    with open(file, 'r') as file_read:
        for line in file_read:
            count += 1
            count += line.count(' ')
    return count
print(num_wards('file.txt'))

#2

import csv
def wright_csv(list):
    with open('csv.txt', 'w') as file_wright:
        writer = csv.writer(file_wright)
        for i in list:
            writer.writerow(i)

list= [["sara", "cohen", 2, "modiin"],["chani","gotlib",3,"Bnay-Brak"]]
wright_csv(list)

#3
import json
def wright_json(dic):
    with open('data.json', 'w') as file_wright:
        for i in dic:
             json.dump(i,file_wright)
    with open('data.json', 'r') as file_read:
            print(json.load(file_read))

dic= {"name":"sara","name":"tamar"}
wright_json(dic)