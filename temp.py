import os
from datetime import date 
arr=[]
# We make sure if we alrady have a file or not if not we creat
pp = input("Did you make file before?\nyes or no?\n")
if pp=='no':
    f = open("d://file.txt", "x")
    f.close()
with open("d://file.txt","r") as r:
    l=r.readline()
    while l!="":
        l=l.split()
        arr.append(l)
        l=r.readline()
#we make a class student with getter and setter methods
class student:
#constructor
    def __init__(self,stdnum:int, name:str, surname:str, byear:int, bmonth:int, bday:int, age:int, sex:str, country:str):
        self._stdnum=stdnum
        self._name=name
        self._surname=surname
        self._byear=byear
        self._bmonth=bmonth
        self._bday=bday
        self._sex=sex
        self._country=country
        self._age=age
    def __str__(self):
        return f"{self._stdnum}   {self._name} {self._surname}    { self._sex}    {self._byear} {self._bmonth} {self._bday}    { self._country}    {self._age}"

    def get_stdnum(self):
        return self._stdnum
    
    def set_stdnum(self, stdnum):
        self._stdnum = stdnum
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_surname(self):
        return self._surname
        
    def set_surname(self, surname):
        self._surname = surname
    
    def get_byear(self):
        return self._byear
        
    def get_bmonth(self):
        return self._bmonth
        
    def get_bday(self):
        return self._bday
    
    
    def set_byear(self, year):
        self._byear = year
        
    def set_bmonth(self, month):
        self._bmonth=month
        
    def set_bday(self, day):
        self._bday=day
    
    def get_sex(self):
        return self._sex
    
    def set_sex(self, sex):
        self._sex = sex
    
    def get_country(self):
        return self._country
    
    def set_country(self, country):
        self._country= country
#calculating age
def calculateAge(byear,bday,bmonth):
     today = date.today()
     age = today.year - byear - ((today.month, today.day) < (bmonth, bday))
     return age
 # understanding the requird operation
while True:
    n=int(input("Welcome!\nIf you want to read press 1\nAdd press 2\nSearch press 3\nBirthyear search press 4\nRemove students press 5\nModify students press 6\n leave press Any number\n"))
    if n==2:
        stdnum=int(input("Enter student number:"))
        name=input("Enter name: ") 
        surname=input("Enter surname: ")
        byear=int(input("Enter birth year: ")) 
        bmonth=int(input("Enter birth month: "))
        bday=int(input("Enter birth day: "))
        sex=input("Enter gender: ") 
        country=input("Enter the country of birth:")
        age=calculateAge(byear,bday,bmonth)
        new_student = student(stdnum, name, surname, byear, bmonth, bday, age, sex, country)
        if len(arr)<100: #we limit the array to 100 elements
           arr.append(new_student) # appending the class to array
           with open("d://file.txt","a") as p:
               p.write(str(new_student)+'\n')
        else:
            print("Can't add more dear.")
    elif n==1:
        print("student number"+"    name"+"   surname"+"  sex"+"    birthdate"+"    country of birth"+"  age")
        with open("d://file.txt","r") as r:
            print(r.read())
    elif n==3:
        n=int(input("Give the student number of the targeted student:"))
        n=str(n)
        with open("d://file.txt","r") as r:
            z="w"
            while z!= " ":
                if n in z:
                    print("student number"+" name"+" surname"+"  sex"+"    birthdate"+"   country of birth"+"  age")
                    print(z)
                    break
                else:
                    z=r.readline()
    elif n==4:
        birth_year=input("Give the year u wanna search pretty please? ")
        i=0
        while i<len(arr):
            if birth_year == arr[i][4]:
                print(arr[i][0]+"  "+arr[i][1]+" "+arr[i][2]+"    "+arr[i][3]+"  "+arr[i][4]+"  "+arr[i][5]+"   "+arr[i][6]+"   "+arr[i][7]+"   "+arr[i][8])
            i=i+1
    elif n==5:
        s=int(input("write the student number:"))
        s=str(s)
        with open("d://file.txt","r") as p: # we copy the file to another file 
            with open("d://temp.txt","a") as t:
                x=p.readline()
                while x!='':
                    if s in x:
                        x=p.readline() 
                    t.write(x)
                    x=p.readline()
        with open("d://file.txt","w") as p:# we write from modified file to main file
            with open("d://temp.txt","r") as t:
                for line in t:
                    p.write(line)
        os.remove("d://temp.txt")# we remove file
    elif n==6:
         with open("d://file.txt","r+") as p:
             with open("d://temp.txt","a") as t:
                 student_number = int(input("Enter the student number: "))
                 student_number=str(student_number)
                 x='2'
                 while x!="":
                     x=p.readline()
                     if student_number in x:# understanding what to change
                         f = int(input("Enter the field number to modify (student number=1, first name=2, last name=3, birthday=4, sex=5, country of birth=6): "))
                         print(x)
                         l=x.split()
                         if f == 1:
                             nv=input("Enter the new student number: ")
                             l[0] = nv
                         elif f == 2:
                             nv=input("Enter the new first name: ")
                             l[1] = nv
                             
                         elif f == 3:
                             nv=input("Enter the new last name: ")
                             l[2] = nv
                            
                         elif f == 4:
                                 byear=int(input("enter birthyear: "))
                                 l[4]=byear
                                 bmonth=int(input("enter birthmonth: "))
                                 l[5]=bmonth
                                 bday=int(input("enter birthday: "))
                                 l[6]=bday
                                 l[8]=calculateAge(byear,bday,bmonth)
                                 l[8] = str(l[8])
                                 
                         elif f == 5:
                             nv=input("Enter the new gender: ")
                             l[3] = nv
                         elif f == 6:
                             nv=input("Enter the new country of birth: ")
                             l[7] = nv
                         else:
                             print("Valid number please...")
                             print(l)
                         l = '  '.join(map(str, l))
                         t.write(l + "\n")
                         
                     else:
                         t.write(x)
         with open("d://file.txt","w") as p:# writing to file and deleting decod file
             with open("d://temp.txt","r") as t:
                 for line in t:
                     p.write(line)
         os.remove("d://temp.txt")
    else:
        break
        