class Detail:
    def __init__(self, fName, lName, dob, po):
        self.fName = fName
        self.lName = lName
        self.dob = dob
        self.po = po

    def printDetail(self):
        print("My Name is---- ", self.fName, self.lName,"Date of Birth ---",self.dob,'Post Office----',self.po, )


class StudentOne(Detail):
    def __init__(self, fName, lName, dob, po,year):
        super().__init__(fName, lName, dob, po)
        self.graduationYear=year


x = StudentOne('Farhan', 'Shafiq', 20, 60,2026)
x.printDetail()
