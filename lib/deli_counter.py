def line(customers):
    if not customers:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently:"
        for index, person in enumerate(customers, start= 1):
            line_status += f" {index}. {person}"
        print(line_status)
        

def take_a_number(customers, name):
    customers.append(name)
    position = len(customers)
    print(f"Welcome, {name}. You are number {position} in line.")
    

def now_serving(customers):
    if not customers:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {customers[0]}.")
        del(customers[0])
