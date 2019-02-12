from flask import Blueprint, request, make_response, jsonify, Response
from ..models.models import PartyModel, parties
from ..models.models import OfficeModel, offices

version_one = Blueprint('version_one', __name__, url_prefix='/api/v1')


class Party:
    @version_one.route('/partyList', methods=['POST'])
    def post():

        """creating a party method"""

        data = request.get_json()

        if not data:
            return{"message": "please provide required details"}, 400
        
        party_name = data['party_name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']

        if party_name== "":
            return make_response(jsonify({"message": "party name must be filled"}),400)

        if hqAddress== "":
            return make_response(jsonify({"message": "hqAddress must be filled"}),400)
        
        if logoUrl== "":
            return make_response(jsonify({"message": "logoUrl must be filled"}),400)
        
        if any(party['party_name'] == party_name for party in parties):
            return make_response(jsonify({"message": "that party name already exists.Please check again"}),400)

        party = PartyModel().create_party(party_name, hqAddress, logoUrl)

        return make_response(jsonify({
            "message": "party posted successfully",
            "data": party
        }),200)


    @version_one.route('/partyList', methods=["GET"])
    def party_get_all():

        """method for getting all parties"""

        partyList = PartyModel().get_all_parties()

        if partyList:
            return make_response(jsonify({
                "message": "this is the partyList",
                "data": partyList
            }), 200) 
        return make_response(jsonify({"message": "No parties found"}),400)

    @version_one.route('/partyList/<int:id>', methods=["GET"])
    def get_one_party(id):

        """method for getting one party"""

        party = PartyModel().parties_get_one(id)

        if party:
            return make_response(jsonify({
                "status": 200,
                "message": "This is the party",
                "data": party
            }), 200)
        return make_response(jsonify({"message": "No party with that id found"}),400)

    @version_one.route('/partyList/<int:id>', methods=["PATCH"])
    def party_put(id):
        """method for editing party"""

        data = request.get_json()
        party_name = data['party_name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']
        

        party = PartyModel().edit_party(id, data)
        
        return make_response(jsonify({
            "message": "Success:party edited",
            "data": party
        }), 200)

    @version_one.route('/partyList/<int:id>', methods=["DELETE"])
    def delete_party(id):
        """method for deleting a party"""

        party = PartyModel().party_delete(id)
        
        return make_response(jsonify({
            "message": "Deleted"
        }), 200) 

class Office:
    @version_one.route('/officeList', methods=['POST'])
    def post_office():

        """method for creating an office"""

        data = request.get_json()
        if not data:
            return jsonify({"message": "please provide required details"}),400

        office_name = data['office_name']
        office_type = data['office_type']

        if office_name== "":
            return make_response(jsonify({"message": "office name must be filled"}),400)

        if office_type== "":
            return make_response(jsonify({"message": "office_type must be filled"}),400)
        
        if any(office['office_name'] == office_name for office in offices):
            return make_response(jsonify({"message": "that office name already exists.Please check again"}),400)
    
        office = OfficeModel().create_office(office_name, office_type)

        return make_response(jsonify({
            "message": "office posted successfully",
            "data": office
        }))
    
    @version_one.route('/officeList', methods=["GET"])
    def get_all_offices():

        """method for getting all the offices"""

        officeList = OfficeModel().office_get_all()
        
        if officeList:
            return make_response(jsonify({
                "message": "this is the partyList",
                "data": officeList
            }), 200) 
        return make_response(jsonify({"message":"no offices found"}),400)

    @version_one.route('/officeList/<int:id>', methods=["GET"])
    def ofices_get_one(id):

        """method for getting one office by id"""

        office = OfficeModel().get_one_office(id)

        if office:
            return make_response(jsonify({
                "message": "This is the office",
                "data": office
            }), 200)
        return make_response(jsonify({"message":"no office with such an id"}),400)