# def find_common_int(file1, file2):

with open("file1.txt", "r") as file_1:
    file_1_list = file_1.read().split()  # read().split() is superior to .readlines()
    print(file_1_list)
with open("file2.txt", "r") as file_2:
    file_2_list = file_2.read().split()
    print(file_2_list)
    int_file_1 = [int(number) for number in file_1_list]
    int_file_2 = [int(number) for number in file_2_list]
    result = [number for number in int_file_1 if number == number in int_file_2]
print(result)


# function method
def return_int_list(file):
    with open(file, "r") as file:
        file_list = file.read().split()
        int_file_list = [int(number) for number in file_list]
        return int_file_list


def return_same_values(list1, list2):
    result = [number for number in list1 if number == number in list2]
    return result


print(return_same_values(return_int_list("file1.txt"), return_int_list("file2.txt")))
