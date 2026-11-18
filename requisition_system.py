#Md Raihan - Student ID: 20260435
#Purchase Requisition System Prototype - Part 2
#Task 1: Requisition class

requisition_counter = 0
all_requisitions = []


class Requisition:

    #Task 1: Staff Info
    def __init__(self, date, staff_id, staff_name):
        global requisition_counter
        requisition_counter += 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = requisition_counter + 10000
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = ""

        all_requisitions.append(self)

    #Add Requisition
    def add_requisition(self, items):
        total = 0
        for item in items:
            total += item["price"]
        self.items = items
        self.total = total
        return total

    #Task 2: Requisition Approval
    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            last_three = str(self.requisition_id)[-3:]
            self.approval_reference = self.staff_id + last_three
        else:
            self.status = "Pending"
            self.approval_reference = ""

    #Respond to Requisition
    def respond_to_requisition(self, decision):
        if self.status == "Pending":
            if decision == "Approved":
                self.status = "Approved"
                last_three = str(self.requisition_id)[-3:]
                self.approval_reference = self.staff_id + last_three
            elif decision == "Not approved":
                self.status = "Not approved"

    #Task 3: Display Requisitions
    def display_requisitions(self):
        for r in all_requisitions:
            print("Date:", r.date)
            print("Requisition ID:", r.requisition_id)
            print("Staff ID:", r.staff_id)
            print("Staff Name:", r.staff_name)
            if r.total == int(r.total):
                print("Total: $" + str(int(r.total)))
            else:
                print("Total: $" + str(r.total))
            print("Status:", r.status)
            if r.approval_reference != "":
                print("Approval Reference Number:", r.approval_reference)
            else:
                print("Approval Reference Number: Not available")
            print()

    #Requisition Statistics
    def requisition_statistics(self):
        approved = 0
        pending = 0
        not_approved = 0
        for r in all_requisitions:
            if r.status == "Approved":
                approved += 1
            elif r.status == "Pending":
                pending += 1
            else:
                not_approved += 1

        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:", len(all_requisitions))
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", not_approved)


#Staff Info input
def enter_requisition():
    print("Enter your information:")
    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")

    items = []
    print("\nAdd items:")
    while True:
        item_name = input("Item Name: ")
        item_price = float(input("Item Price ($): "))

        item = {
            "name": item_name,
            "price": item_price
        }
        items.append(item)

        again = input("Add another item (yes/no): ")
        if again != "yes":
            break

    r = Requisition(date, staff_id, staff_name)
    r.add_requisition(items)
    r.approve_requisition()
    return r


#Testing
r1 = Requisition("03/04/2024", "FN19", "John Paul")
r1.add_requisition([{"name": "Keyboard", "price": 150}, {"name": "Monitor", "price": 300}])
r1.approve_requisition()

r2 = Requisition("05/04/2024", "FN20", "Tracy Brown")
r2.add_requisition([{"name": "Laptop", "price": 1000}])
r2.approve_requisition()

r3 = Requisition("07/05/2024", "FN15", "Emma Wellington")
r3.add_requisition([{"name": "Server", "price": 3000}, {"name": "Switch", "price": 500}])
r3.approve_requisition()

r4 = Requisition("03/05/2024", "FN02", "Catlin White")
r4.add_requisition([{"name": "Chair", "price": 490}])
r4.approve_requisition()

r5 = Requisition("09/05/2024", "FN08", "Sam Lee")
r5.add_requisition([{"name": "Printer", "price": 500}])
r5.approve_requisition()

print("Before manager responses")
print()
r1.display_requisitions()
r1.requisition_statistics()

r2.respond_to_requisition("Approved")
r3.respond_to_requisition("Not approved")

print()
print("After manager responses")
print()
r1.display_requisitions()
r1.requisition_statistics()

extra = input("Enter another requisition? (yes/no): ")
if extra == "yes":
    new_r = enter_requisition()
    print()
    new_r.display_requisitions()
    new_r.requisition_statistics()