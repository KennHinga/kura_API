parties=[]

class PartyModel():
    def __init__(self):
         self.parties =parties

    def create_party(self, name, hqAddress, logoUrl):
        """ create party method """
        party = {
            "id": len(self.parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }
        self.parties.append(party)
        return party

    # def get_all_party(self):
    #     return selfparties
    
    # def get_one_party(self):
    #     if 

    # def edit_party(self):
    #     pass

    # def delete_party(self):
    #     pass