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