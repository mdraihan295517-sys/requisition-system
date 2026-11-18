#Md Raihan_ Student ID:-20260435
#Purchase Requisition System Prototype - Part 2
#Task 1: Requisition class.

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