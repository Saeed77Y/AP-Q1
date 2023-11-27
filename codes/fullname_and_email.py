class Employee:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = '{} {}'.format(firstname, lastname)
        self.email = '{}.{}@company.com'.format(firstname.lower(), lastname.lower())