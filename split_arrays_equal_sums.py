# Written by Armen Juhl 5/7/2020
# Break a given array into two arrays without sorting the elements. Each array sum should be equal 
# Input = {5,4,1}
# Output = {5}  {4,1}

# 2 arrays that have the same sum (half of the first array)

data = [1,3,5,1,2,6,6,8,1,5,24,13,2,3,2,1]

sum_lst = sum(data)
half_sum_lst = round(sum_lst / 2)
data_desc = sorted(data, key=int, reverse=True)

print(data)
print('data desc', data_desc)

def calculate_half_sum_lst(data):
    list_a = list()
    list_b = list()

    for i in data_desc:
        if sum(list_a) + i <= half_sum_lst:
            list_a.append(i)
        else:
            list_b.append(i)
    return(list_a, list_b)

output = calculate_half_sum_lst(data)
print(f"list a {output[0]} \nlist b {output[1]}")
print('sum of list a ', sum(output[0]), '\nsum of list b ', sum(output[1]))


