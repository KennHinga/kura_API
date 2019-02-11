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

        if not 'name' in data.keys():
            return jsonify({"message": "name not provided"}), 400

        if not 'hqAddress' in data.keys():
            return jsonify({"message": "hqAddress not provided"}), 400

        if not 'logoUrl' in data.keys():
            return jsonify({"message": "logoUrl not provided"}), 400
        
        name = data['name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']

        if name== "":
            return make_response(jsonify({"message": "party name must be filled"}),400)

        if hqAddress== "":
            return make_response(jsonify({"message": "hqAddress must be filled"}),400)
        
        if logoUrl== "":
            return make_response(jsonify({"message": "logoUrl must be filled"}),400)
        
        if any(party['name'] == name for party in parties):
            return make_response(jsonify({"message": "that party name already exists.Please check again"}),400)

        party = PartyModel().create_party(name, hqAddress, logoUrl)

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
        name = data['name']
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

        if not 'name' in data.keys():
            return jsonify({"message": "name not provided"}),400

        if not 'office_type' in data.keys():
            return jsonify({"message": "office_type not provided"}),400

        name = data['name']
        office_type = data['office_type']

        if name== "":
            return make_response(jsonify({"message": "office name must be filled"}),400)

        if office_type== "":
            return make_response(jsonify({"message": "office_type must be filled"}),400)
        
        if any(office['name'] == name for office in offices):
            return make_response(jsonify({"message": "that office name already exists.Please check again"}),400)
    
        office = OfficeModel().create_office(name, office_type)

        return make_response(jsonify({
            "message": "office posted successfully",
            "data": office
        }))
    
    @version_one.route('/officeList', methods=["GET"])
    def office_get_all():
        """method for getting all offices"""

        partyList = OfficeModel().get_all_offices()
        
        if partyList:
            return make_response(jsonify({
                "message": "this is the partyList",
                "data": partyList
            }), 200) 
        return make_response(jsonify({"message":"no offices found"}),400)

    @version_one.route('/officeList/<int:id>', methods=["GET"])
    def get_one_office(id):
        """method for getting one office by id"""

        office = OfficeModel().offices_get_one(id)

        if office:
            return make_response(jsonify({
                "message": "This is the office",
                "data": office
            }), 200)
        return make_response(jsonify({"message":"no office with such an id"}),400)