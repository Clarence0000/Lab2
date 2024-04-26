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
    min_temp = numsFiltered[0]
    max_temp = numsFiltered[0]
    for i in numsFiltered:
        if min_temp > i:
            min_temp = i
        if max_temp < i:
            max_temp = i  
    return [min_temp,max_temp]

def sort_temperature(numsFiltered):
    numsFiltered.sort()
    return numsFiltered

def calc_median_temperature(numsFiltered):
    if len(numsFiltered) % 2:
        median = numsFiltered[round(len(numsFiltered)/2)]   
    if len(numsFiltered) % 2 == 0:
        median = (((numsFiltered[len(numsFiltered)//2] + numsFiltered[len(numsFiltered)//2 - 1]) / 2))
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    userInputs = get_user_input()
    print("Average temperature = " + str(calc_average_temperature(userInputs)))
    print("Sorted temperature = " + str(sort_temperature(userInputs)))
    print("Minimum and Maximum temperature = " + str(calc_min_max_temperature(userInputs)))
    print("Median = " + str(calc_median_temperature(userInputs)))

if __name__ == "__main__":
    main()