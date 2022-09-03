
def average_of_time():
    """
    :return: average of numbers in a list excluding the max and min numbers
    """
    list = []
    list.append(float(input("Enter the time for performance 1: ")))
    list.append(float(input("Enter the time for performance 2: ")))
    list.append(float(input("Enter the time for performance 3: ")))
    list.append(float(input("Enter the time for performance 4: ")))
    list.append(float(input("Enter the time for performance 5: ")))
    list.remove(max(list))
    list.remove(min(list))
    average = sum(list)/len(list)
    print(f"The official competition score is {average:.2f} seconds.")

def main():

    average_of_time()

main()