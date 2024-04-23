def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    
def get_user_input():
    nums = input("Enter numbers: ")
    nums = nums.split(",")
    #nums= list(map(float,nums))
    numsFiltered=[float(i) for i in nums]
    print(numsFiltered)
    return numsFiltered

def calc_average_temperature(numsFiltered):
    sum = 0
    for i in numsFiltered:
        sum += i
    avg = sum /len(numsFiltered)
    return avg

def calc_min_max_temperature(numsFiltered):
    min = numsFiltered[0]
    max = numsFiltered[0]
    for i in numsFiltered:
        if min > i:
            min = i
        if max < i:
            max = i  
    return [min,max]

def calc_median_temperature(numsFiltered):
    numsFiltered.sort()
    if len(numsFiltered) % 2:
        median = numsFiltered[round(len(numsFiltered)/2)]   
    if len(numsFiltered) % 2 == 0:
        median = (((numsFiltered[int(len(numsFiltered)/2)] + numsFiltered[int(len(numsFiltered)/2 - 1)]) /2))
    return median

display_main_menu()
userInputs = get_user_input()
print("Average temperature = " + str(calc_average_temperature(userInputs)))
print("Minimum and Maximum temperature = " + str(calc_min_max_temperature(userInputs)))
print("Median = " + str(calc_median_temperature(userInputs)))
