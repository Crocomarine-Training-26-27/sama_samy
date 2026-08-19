                            #Task 2 part 2 OOP
                        #member: Sama Samy Ameen

class EmergencyVehicles:
    def __init__(self):
        self.name=input('Enter the name of the vehicle: ')
        try:  #in case the input is not a float
            self._fuel=float(input(f'Enter the amount of fuel in this {self.name}: '))
            self.maxfuel=float(input(f'Enter the amount of max fuel in this {self.name}: '))
            #repeating the input until it is valid
            while self._fuel<0  or self.maxfuel <0 or self._fuel> self.maxfuel :
                self._fuel=float(input(f'Enter a valid amount of fuel in this {self.name}: '))
                self.maxfuel=float(input(f'Enter a valid amount of max fuel in this {self.name}: '))
               
        except:
            print('Enter a valid amount')


    def respond(self): # each subclass should implement its own method
        raise NotImplementedError("Subclasses must implement this method.")


    def refuel(self):   #restoring fuel to the max fuel 
        self._fuel=self.maxfuel
        print('fuel set to max')

#subclasses:

# note: in every subclass , no constructor was made because the inputs taken from the super class are already enough     'as far as i understand :)'

class Ambulance(EmergencyVehicles):
    #overriding the inherited function to avoid raising error
    def respond(self):
        self._fuel-=10

    def treat_patient(self):
        print('patient treated')


class PoliceCar(EmergencyVehicles):
    #overriding the inherited function to avoid raising error
        def respond(self):
            self._fuel-=5
        def arrest_suspect(self):
            print('criminal arrested')

class FireFighterCar(EmergencyVehicles):
    #overriding the inherited function
    def respond(self):
                self._fuel-=15

    def rescue_civilians(self):
        print('rescuing civilians...')
    def prepare(self):
        print('preparing...')
    def extinguish(self):
        print('extinguishing fire...')

    def extinguish_fire(self):
        self.rescue_civilians()
        self.prepare()
        self.extinguish()
        print('Fire extinguished successfully')

