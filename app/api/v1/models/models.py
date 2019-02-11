parties= []
offices= []

class PartyModel():
    """creates a PartyModel class"""

    def __init__(self):
         self.parties =parties

    def create_party(self, name, hqAddress, logoUrl):
        """create party model method"""

        party = {
            "id": len(parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }
        self.parties.append(party)
        return party

    def get_all_parties(self):
        """get all parties model method"""

        return self.parties
    
    def parties_get_one(self, id):
        """get one party model method"""

        for party in self.parties:
            if party['id'] == id:
                return party

    def edit_party(self, id, data):
        """edit a party model method"""

        for party in self.parties:
            if party['id'] == id:
                name= data.get('name')
                hqAddress= data.get('hqAddress')
                logoUrl= data.get('logoUrl') 
                if name:
                    party['name'] = name
                if hqAddress:
                    party['hqAddress'] = hqAddress
                if logoUrl:
                    party['logoUrl'] = logoUrl
                return party

    def party_delete(self, id):
        """delete a party model method"""

        for party in self.parties:
            if party['id'] == id:
                return self.parties.remove(party) 

class OfficeModel():
    """creates an OfficeModel class"""

    def __init__(self):
         self.offices =offices  
    
    def create_office(self, name, office_type):
        """create office model method"""

        office = {
            "id": len(offices)+1,
            "name": name,
            "type": office_type,
        }
        self.offices.append(office)
        # print(office)
        return office
    
    def get_all_offices(self):
        """get all offices model method"""

        return self.offices

    def offices_get_one(self, id):
        """get one party model method"""
        for office in self.offices:
            if office['id'] == id:
                return office
