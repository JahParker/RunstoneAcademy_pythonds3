import math

class CollegeOccupant:
    can_attend_campus_events = True
    
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = math.randomInt()

class Student(CollegeOccupant):
    enrolled_classes = []

    def __init__(self, first_name, last_name, credit_hours, in_state) -> None:
        super.__init__(first_name, last_name)
        self.credit_hours = credit_hours
        self.in_state = in_state
        self.tuition = self.calculate_tuition(credit_hours)

    def calculate_tuition(self, credit_hours):
        if self.in_state:
            cost_per_credit_hour = 250
        else:
            cost_per_credit_hour = 650
        
        return cost_per_credit_hour * credit_hours

class Faculty(CollegeOccupant):
    classes_taught = []

    def __init__(self, first_name, last_name, salary) -> None:
        super.__init__(first_name, last_name)
        self.salary = salary
        can_grade = True

class TeachingAssistant(Faculty):
    classes_assisting = []

    def __init__(self, student, salary) -> None:
        first_name = student.first_name
        last_name = student.last_name
        salary = self.salary_per_hour(salary)
        can_grade = False
    
    def salary_per_hour(self, salary):
        total_hours = 120
        return salary // total_hours

class Staff(CollegeOccupant):
    def __init__(self, first_name, last_name, salary) -> None:
        super.__init__(first_name, last_name)
        self.salary = salary




