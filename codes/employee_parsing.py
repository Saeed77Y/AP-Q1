class Employee:
    def __init__(self, firstname, lastname, salary) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.salary =  salary

    @classmethod
    def from_string(cls, string):
        splitted = list(string.split('-'))
        return cls(splitted[0], splitted[1], int(splitted[2]))