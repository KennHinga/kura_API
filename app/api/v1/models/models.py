parties= []

class PartyModel():
    def __init__(self):
         self.parties =parties

    def create_party(self, name, hqAddress, logoUrl):
        """ create party method """
        party = {
            "id": len(parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }
        self.parties.append(party)
        return party

    def get_all_parties(self):
        return self.parties
    
    def parties_get_one(self, id):
        for party in self.parties:
            if party['id'] == id:
                return party

    # def edit_party(self, id, data):
    #     for party in self.parties:
    #         if party['id'] == id:
    #             name= data.get('name')
    #             hqAddress= data.get('hqAddress')
    #             logoUrl= data.get('logoUrl') 
    #             if name:
    #                 party['name'] = name
    #             if hqAddress:
    #                 party['hqAddress'] = hqAddress
    #             if logoUrl:
    #                 party['logoUrl'] = logoUrl
    #             return party

    def party_delete(self, id):
        for party in self.parties:
            if party['id'] == id:
                return self.parties.remove(party) 
   