class Repair: 
    def __init__(self, customer, device, technician, repair_status): 
        self._customer = customer 
        self._device = device 
        self._technician = technician 
        self.repair_status = repair_status 
        self.payments = 0 
     
    @property 
    def customer(self): 
        return self._customer 
     
    @property 
    def device(self): 
        return self._device 
     
    @property 
    def technician(self): 
        return self._technician 
 
    def add_payment(self, amount): 
        self.payments += amount 
     
    def show_details(self): 
        print(f"Customer: {self.customer.name} | Device: {self.device} | Technician: {self.technician.name} | Status: {self.repair_status} | Payments: {self.payments}") 
     
    @staticmethod 
    def repair_in_progress(status): 
        return status.lower() == "in progress" 
 
class Technician: 
    def __init__(self, name, experience): 
        self.name = name 
        self.experience = experience 
 
    def show_info(self): 
        print(f"Technician: {self.name}, Experience: {self.experience} years") 
 
class Customer: 
    def __init__(self, name, email): 
        self.name = name 
        self.email = email 
 
class Feedback: 
    def __init__(self, customer, rating, comment): 
        self.customer = customer 
        self.rating = rating 
        self.comment = comment 
 
    def show_feedback(self): 
        print(f"Feedback from {self.customer.name}: | Rating: {self.rating} | Comment: {self.comment}") 
 
class StandartRepair(Repair): 
    def __init__(self, customer, device, technician, repair_status, part_needed=None): 
        super().__init__(customer, device, technician, repair_status) 
        self.part_needed = part_needed 
     
    def show_details(self): 
        super().show_details() 
        print(f"Part Needed: {self.part_needed}") 
 
class PremiumService: 
    def __init__(self, premium_level): 
        self.premium_level = premium_level 
     
    def show_premium(self): 
        print(f"Premium Level: {self.premium_level}") 
 
class AdvancedRepair(Repair, PremiumService): 
    def __init__(self, customer, device, technician, premium_level, repair_status): 
        Repair.__init__(self, customer, device, technician, repair_status) 
        PremiumService.__init__(self, premium_level) 
     
    def show_details(self): 
        Repair.show_details(self) 
        self.show_premium() 
 
tech1 = Technician("Petro", 5) 
tech2 = Technician("Igor", 25) 
 
cust1 = Customer("Alice", "alice@gmail.com") 
cust2 = Customer("Maksym", "maksym@gmail.com") 
cust3 = Customer("Dmytro", "Dmytro22@gmail.com") 
 
repair1 = Repair(cust1, "Laptop", tech1, "In progress") 
repair2 = StandartRepair(cust2, "Smartphone", tech2, 'In progress', part_needed="Screen") 
repair3 = AdvancedRepair(cust3, "AirPods", tech2, "Platinum", "Completed") 
 
feedback1 = Feedback(cust1, 4, "Great service!") 
feedback2 = Feedback(cust2, 4, "Good") 
feedback3 = Feedback(cust3, 5, "Perfect!") 
 
repair1.add_payment(1000) 
repair1.show_details() 
tech1.show_info() 
print() 
 
repair2.add_payment(850) 
repair2.show_details() 
tech2.show_info() 
print() 
 
repair3.add_payment(10000) 
repair3.show_details() 
tech2.show_info() 
print() 
 
 
feedback1.show_feedback() 
feedback2.show_feedback() 
feedback3.show_feedback() 
 
print("\nIs repair in progress?", Repair.repair_in_progress(repair1.repair_status))