# Written by Armen Juhl 5/7/2020
# Break a given array into two arrays without sorting the elements. Each array sum should be equal 
# Sample Input = {5,4,1}
# Sample Output = {5}  {4,1}
# 2 arrays that have the same sum (half of the first array)


def main():
    data = [1, 3, 5, 1, 2, 6, 6, 8, 1, 5, 24, 13, 2, 3, 2, 1]
    data_desc = sorted(data, key=int, reverse=True)

    output = calculate_half_sum_lst(data_desc)
    print(f"sum of list a {sum(output[0])} \nsum of list b {sum(output[1])}")


def calculate_half_sum_lst(data_set):
    half_sum_lst = round(sum(data_set) / 2)
    list_a = list()
    list_b = list()

    for val in data_set:
        if sum(list_a) + val <= half_sum_lst:
            list_a.append(val)
        else:
            list_b.append(val)

    return list_a, list_b


if __name__ == '__main__':
    main()
