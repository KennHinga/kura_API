parties= []
offices= []

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

class OfficeModel():
    def __init__(self):
         self.offices =offices  
    
    def create_office(self, name, office_type):
        office = {
            "id": len(offices)+1,
            "name": name,
            "type": office_type,
        }
        self.offices.append(office)
        return office
    
    def get_all_offices(self):
        return self.offices

    def offices_get_one(self, id):
        for office in self.offices:
            if office['id'] == id:
                return office
