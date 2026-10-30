# Q5 - Functions, Parameters and Scope

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


print("Buggy Function:")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))

print("\nCorrect Function:")
print(add_item("Tea"))
print(add_item("Vada"))
print("\nDefault List:")
print(add_item_buggy.__defaults__)
print("\nThree Customers:")

customer1 = add_item("Tea")
customer1 = add_item("Vada", customer1)

customer2 = add_item("Coffee")

customer3 = add_item("Samosa")

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)
def calculate_bill(amount):
    gst = amount * 0.05
    total = amount + gst
    return total, gst


print("\nBill Calculation:")
total, gst = calculate_bill(100)

print("GST:", gst)
print("Total Amount:", total)
print("\nLocal and Global Variables:")

college = "ABC College"

def show_student():
    student = "Aruthra"
    print("Student:", student)
    print("College:", college)

show_student()
print("Outside Function:", college)
print("\nNonlocal Variable:")

def customer_order():
    count = 0

    def add_order():
        nonlocal count
        count += 1
        print("Items Ordered:", count)

    add_order()
    add_order()
    add_order()

customer_order()
print("\nTypes of Parameters:")

def student_details(name, department="CSE"):
    print("Name:", name)
    print("Department:", department)

# Positional arguments
student_details("Aruthra", "CSE")

# Keyword arguments
student_details(name="Anu", department="ECE")

# Default argument
student_details("Ravi")
print("\nGlobal Keyword:")

count = 0

def update_count():
    global count
    count = count + 1
    print("Inside Function:", count)

update_count()
print("Outside Function:", count)