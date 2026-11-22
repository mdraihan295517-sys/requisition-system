#Md Raihan_Student iD:20260435
#Purchase Requisition System Prototype -Part 2
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

    #Add requisition
    def add_requisition(self, items):
        self.items = items
        self.total = self.requisitions_details()
        return self.total

    #Requisitions details
    def requisitions_details(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    #Task 2: Requisition Approval
    def approve_requisition(self):
        total = self.requisitions_details()
        if total < 500:
            self.status = "Approved"
            last_three = str(self.requisition_id)[-3:]
            self.approval_reference = self.staff_id + last_three
        else:
            self.status = "Pending"
            self.approval_reference = ""

    #Respond to requisition
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
        for requisition in all_requisitions:
            print("Date:", requisition.date)
            print("Requisition ID:", requisition.requisition_id)
            print("Staff ID:", requisition.staff_id)
            print("Staff Name:", requisition.staff_name)
            if requisition.total == int(requisition.total):
                print("Total: $" + str(int(requisition.total)))
            else:
                print("Total: $" + str(requisition.total))
            print("Status:", requisition.status)
            if requisition.approval_reference != "":
                print("Approval Reference Number:", requisition.approval_reference)
            else:
                print("Approval Reference Number: Not available")
            print()

    #Requisition statistics
    def requisition_statistics(self):
        approved = 0
        pending = 0
        not_approved = 0
        for requisition in all_requisitions:
            if requisition.status == "Approved":
                approved += 1
            elif requisition.status == "Pending":
                pending += 1
            else:
                not_approved += 1

        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:", len(all_requisitions))
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", not_approved)
        return len(all_requisitions), approved, pending, not_approved


print("Purchase Requisition System")

#Step 1: staff enter their requisitions
while True:
    print("\nEnter your information:")
    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")

    requisition = Requisition(date, staff_id, staff_name)
    print("Requisition ID:", requisition.requisition_id)

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

    requisition.add_requisition(items)
    requisition.approve_requisition()
    print("Status:", requisition.status)

    more = input("\nAdd another requisition (yes/no): ")
    if more != "yes":
        break

#Step 2: print the requisitions and the statistics
print("\nPrinting requisitions:")
requisition.display_requisitions()
requisition.requisition_statistics()

#Step 3: the manager answers the pending requisitions
print("\nManager responses:")
found = False
for req in all_requisitions:
    if req.status == "Pending":
        found = True
        if req.total == int(req.total):
            total_text = str(int(req.total))
        else:
            total_text = str(req.total)
        print("\nRequisition", req.requisition_id, "-", req.staff_name, "- Total $" + total_text)
        answer = input("Press A for Approved, N for Not approved or S to skip, then Enter: ")
        if answer == "a" or answer == "A":
            req.respond_to_requisition("Approved")
        elif answer == "n" or answer == "N":
            req.respond_to_requisition("Not approved")
        print("Status:", req.status)

if found == False:
    print("No matches for pendings")

#Step 4: print again after the responses
print("\nPrinting requisitions after the responses:")
requisition.display_requisitions()
requisition.requisition_statistics()