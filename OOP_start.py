class Sunway_student:
    school_name="sunway"
    def __init__(self, firstname, lastname):
        self.first_name=firstname
        self.last_name=lastname

    def get_full_name(self):
            return print(f"{self.first_name} {self.last_name}")

    @classmethod
    def get_school_name(cls):
            print(f"Top 1 college {cls.school_name}")

    @staticmethod
    def print_govt_holidays():
            print("Government holidays 52 days");

s = Sunway_student("ram", "lama" )
print(s.first_name)
Sunway_student.print_govt_holidays()
Sunway_student.get_school_name()
s.get_full_name()