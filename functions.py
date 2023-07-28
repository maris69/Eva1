def calculate_payment(hours_worked, hourly_rate):
   if hours_worked < 0 or hourly_rate < 0:
        return -1
    elif hours_worked > 40:
        overtime_hours = hours_worked - 40
        hours_worked = 40
    else:
        overtime_hours = 0

    regular_payment = hours_worked * hourly_rate
    overtime_payment = overtime_hours * (hourly_rate * 1.5)
    total_payment = regular_payment + overtime_payment
    social_benefits_discount = total_payment * 0.06
    total_payment -= social_benefits_discount

    return total_payment
def compare_numbers(num1, num2):
    pass
    
def factorial(num):
    pass


def menu():
    print(15 * "-*-")
    print("\t\tMain Menu\t\t")
    print(15 * "-*-")
    print("1. Calculate payment\n2. Compare two numbers\n3. Calculate the factorial\n4. Exit")
    print(15 * "-*-")
    option = int(input("Please, choose an option: "))
    return option
