parties= []
offices= []

class PartyModel():

    """creates a PartyModel class"""

    def __init__(self):
         self.parties =parties

    def create_party(self, party_name, hqAddress, logoUrl):

        """create party model method"""

        party = {
            "party_id": len(parties)+1,
            "party_name": party_name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }
        self.parties.append(party)
        return party

    def get_all_parties(self):

        """get all parties model method"""

        return self.parties
    
    def parties_get_one(self, party_id):

        """get one party model method"""

        for party in self.parties:
            if party['party_id'] == party_id:
                return party

    def edit_party(self, party_id, data):

        """edit a party model method"""

        for party in self.parties:
            if party['party_id'] == party_id:
                party_name= data.get('party_name')
                hqAddress= data.get('hqAddress')
                logoUrl= data.get('logoUrl') 
                if party_name:
                    party['party_name'] = party_name
                if hqAddress:
                    party['hqAddress'] = hqAddress
                if logoUrl:
                    party['logoUrl'] = logoUrl
                return party

    def party_delete(self, party_id):

        """delete a party model method"""

        for party in self.parties:
            if party['party_id'] == party_id:
                return self.parties.remove(party) 

class OfficeModel():

    """creates an OfficeModel class"""

    def __init__(self):
         self.offices =offices  
    
    def create_office(self, office_name, office_type):

        """create office model method"""

        office = {
            "office_id": len(offices)+1,
            "office_name": office_name,
            "type": office_type,
        }
        self.offices.append(office)
        # print(office)
        return office
    
    def get_all_offices(self):

        """get all offices model method"""

        return self.offices

    def offices_get_one(self, office_id):

        """get one office model method"""

        for office in self.offices:
            if office['office_id'] == office_id:
                return office
