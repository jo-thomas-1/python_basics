# class 'hospital' - department, admin, doctor, nurse
# class 'department' to print all the details of class 'hospital'
# class 'patient' that can collect patient details and also print them

class Hospital:
    def __init__(self):
        self.department = ""
        self.admin = ""
        self.doctor = ""
        self.nurse = ""

    def hosp_get_details(self):
        self.department = input("Enter department: ")
        self.admin = input("Enter admin: ")
        self.doctor = input("Enter patient doctor: ")
        self.nurse = input("Enter patient nurse: ")

class Department(Hospital):
    def dep_print_details(self):
        print("Department", self.department)
        print("Admin", self.admin)
        print("Doctor", self.doctor)
        print("Nurse", self.nurse)

class Patient(Department):
    def __init__(self):
        self.name = ""
        self.age = 0
        self.decease = ""
        self.affected_organ = ""
        self.status = ""

    def get_details(self):
        self.name = input("Enter patient name: ")
        self.age = int(input("Enter patient age: "))
        self.dep_get_details()
        self.decease = input("Enter patient decease: ")
        self.affected_organ = input("Enter affected organ: ")
        self.status = input("Enter patient status/remark: ")

    def print_all(self):
        print("---- Patient Details ----")
        print("Name:", self.name)
        print("Age:", self.age)
        self.dep_print_details()
        print("Decease:", self.decease)
        print("Affected organ:", self.affected_organ)
        print("Patient status/remark:", self.status)


patient_x = Patient()
patient_x.get_details()
patient_x.print_all()
patient_x.dep_print_details()
