class Employee:
    def __init__(self, fullname, **kwargs) -> None:
        self.fullname = fullname
        splittedlist = list(self.fullname.split())
        self.name = splittedlist[0]
        self.lastname = splittedlist[1]
        for key, value in kwargs.items():
            setattr(self, key, value)