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

display_main_menu()
userInputs = get_user_input()
print("Average temperature = " + str(calc_average_temperature(userInputs)))
print("Minimum and Maximum temperature = " + str(calc_min_max_temperature(userInputs)))

