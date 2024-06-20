# Task 1: Vehicle Registration System

class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def get_detail(self):
              print(f"This are the details of the car, plate: {self.registration_number}, car type: {self.type}, owner: {self.owner}")

        
        def update_owner(self, new_owner):
               self.owner = new_owner
               print(f"This are the details of the car with new owner, plate: {self.registration_number}, car type: {self.type}, owner: {self.owner}")


acura = Vehicle('ceh6741', 'tsx', 'dare')
toyota = Vehicle('gfd5874', 'camry', 'joy')
honda = Vehicle('yth4567', 'pilot', 'kemi')
nissan = Vehicle('lye8542', 'passat', 'josh')

acura.get_detail()
honda.get_detail()

print('='*75)

# Change owners
acura.update_owner('Mike')
honda.update_owner('Blake')


# Task 2: Event Management System Enhancement

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.num_participants = 0


        def add_participant(self):
              self.num_participants += 1


        def get_participant_count(self, name):
              print('Current number of participants is: ', self.num_participants)
        

event = Event('Birthday', "Nov 25")

print('='*75)

event.get_participant_count()

event.add_participant()
event.add_participant()
event.add_participant()
event.add_participant()

print('='*75)

event.get_participant_count()
                  