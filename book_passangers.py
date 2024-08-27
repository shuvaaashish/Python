class flight:
    def __init__(self,capacity):
        self.capacity=capacity 
        self.passanger=[]
    
    def add_passanger(self,name):
        if not self.openseats():
            return False
        self.passanger.append(name)
        return True

    def openseats(self):
        return self.capacity-len(self.passanger)
    
flight=flight(3)
people=[]
a=int(input("Enter the no of passangers"))
for i in range(1,a+1):
    b=input(f'Enter Passanger no {i}')
    people.append(b)
for person in people:
    if flight.add_passanger(person):
        print(f'Added {person} to the flight successully!!')
    else:
        print(f'Sorry, No available seats for {person}')