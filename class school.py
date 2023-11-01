#create a class school,create at least 5 attributes,call those attributes using at least 10 objects.
class School:
    def __init__(self,Fname,Lname,Position,Idno,Work):
        self.Fname=Fname
        self.Lname=Lname
        self.Position=Position
        self.Idno=Idno
        self.Work=Work
    def CommomThings(self):
      print(f"My name is {self.Fname} {self.Lname} \nPosition: {self.Position} \nIdno: {self.Idno} \nWork: {self.Work}")
def main():
   Principal=School("jhone","vaz","Principal",20231954,"Management")
   Sir1=School("Saby","vaz","Teacher",20231954,"Teaching Math")
   Madam1=School("Yamini","Diwakar","Teacher",20231954,"Teaching Science")
   Sir2=School("Sitha","kaki","Teacher",20231954,"Teaching English")
   Madam2=School("Yamini","Kaki","Teacher",20231954,"Teaching Chemistry")
   SportsTeacher=School("Nikitha","karmel","SportsTeacher",20231954,"sports")
   Liberary=School("Pushpa","Mallari","Liberarian",20231954,"Books Maintaince")
   Lab=School("Kavitha","Naik","Laboratry",20231954,"Lab Maintaince")
   Student=School("Shalini","Machani","Student",20231954,"Student")
   Ict=School("Pranesh","Gadagi","Computer Lab",20231954,"Computer Support")
   no1=School.CommomThings(Principal)
   no2=School.CommomThings(Sir1)
   no3=School.CommomThings(Madam1)
   no4=School.CommomThings(Sir2)
   no5=School.CommomThings(Madam2)
   no6=School.CommomThings(SportsTeacher)
   no7=School.CommomThings(Liberary)
   no8=School.CommomThings(Lab)
   no9=School.CommomThings(Student)
   no10=School.CommomThings(Ict)
main()
