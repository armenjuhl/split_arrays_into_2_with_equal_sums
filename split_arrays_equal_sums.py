# Written by Armen Juhl 5/7/2020
# Break a given array into two arrays without sorting the elements. Each array sum should be equal 
# Sample Input = {5,4,1}
# Sample Output = {5}  {4,1}
# 2 arrays that have the same sum (half of the first array)


data = [1, 3, 5, 1, 2, 6, 6, 8, 1, 5, 24, 13, 2, 3, 2, 1]

sum_lst = sum(data)
half_sum_lst = round(sum_lst / 2)
data_desc = sorted(data, key=int, reverse=True)


def calculate_half_sum_lst(data_set):
    list_a = list()
    list_b = list()

    for idx, val in enumerate(data_set):
        if sum(list_a) + val <= half_sum_lst:
            list_a.append(val)
        else:
            list_b.append(val)


    return list_a, list_b


output = calculate_half_sum_lst(data_desc)
print(f"sum of list a {sum(output[0])} \nsum of list b {sum(output[1])}")
