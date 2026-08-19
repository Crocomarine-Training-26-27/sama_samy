                              #oop task 2 
                           #member: sama samy


class Student:
    #basic info for students 'attributes'
    def __init__(self):
        self.name=input('Enter your name: ')
        #in case that the input is not an integer
        try:
            self._id=float(input('Enter your id: ')) #id info is protected
        except:
            print('invalid form of id')
        self._grades=[]
        #a dictionary with all the info of the students for display info function later
        self.info={'name':self.name,'grades':self._grades}
        print('student added')


    #method for adding grades
    def add_grade(self):
        #checking the id of the user for adding grades
        try:
            checkid=float(input('Enter your id: '))
        except:
            print('invalid form of id')
        if checkid==self._id:
            grade=input('Enter your grade:')
            self._grades.append(float(grade))
            print('grade added')
        else:
            print('incorrect id')

    def get_average(self):
        sum=0
        for i in self._grades:
            sum+=i
        if len(self._grades)!=0:  #to avoid dividing by zero
            print('average of grades is: ',sum/len(self._grades))
        #adding the 'average' key to the info dictionary
        self.info['average']=sum/len(self._grades)

    def display_info(self):
        #checking the id first
        checkid=float(input('Enter your id: '))
        if checkid==self._id:
            print(self.info)


s1=Student()
s1.add_grade()
s1.add_grade()
s1.get_average()
s1.display_info()