from flatmate import Flatmate
import uuid

class Flat:
    def __init__ (self, direction, landlord, lessor:Flatmate, lessors:list[Flatmate]):
        self.direction = direction
        self.landlord = landlord
        self.lessor = lessor
        self.lessors = lessors
        self.uuid = str(uuid.uuid4())

    def contract(self):
        print(
            f"""
            This contract is between {self.landlord} and {self.lessor.full_name()}.
            The flat is located at {self.direction}.

            current number of flatmates: {len(self.lessors)}
            """
        )
    def add_flatmate(self, flatmate:Flatmate):
        self.lessors.append(flatmate)
    
    def remove_flatmate(self, flatmate:Flatmate):
        self.lessors = [fm for fm in self.lessors if fm.id != flatmate.id]
    
    def get_flatmates(self):
        return self.lessors


        