from flask import Blueprint, request, make_response, jsonify, Response
from ..models.models import PartyModel
from ..models.models import OfficeModel

version_one = Blueprint('version_one', __name__, url_prefix='/api/v1')



class Party:
    @version_one.route('/partyList', methods=['POST'])
    def post():
        data = request.get_json()
        name = data['name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']

        party = PartyModel().create_party(name, hqAddress, logoUrl)

        return make_response(jsonify({
            "status": 201,
            "data": party
        }))


    @version_one.route('/partyList', methods=["GET"])
    def party_get_all():
        partyList = PartyModel().get_all_parties()
        return make_response(jsonify({
            "status": 200,
            "message": "this is the partyList",
            "data": partyList
        }), 200) 

    @version_one.route('/partyList/<int:id>', methods=["GET"])
    def get_one_party(id):
        party = PartyModel().parties_get_one(id)
        return make_response(jsonify({
            "status": 200,
            "message": "This is the party",
            "data": party
        }), 200)

    @version_one.route('/partyList/<int:id>', methods=["PATCH"])
    def party_put(id):
        data = request.get_json()
        name = data['name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']
        

        party = PartyModel().edit_party(id, data)
        
        return make_response(jsonify({
            "status": 200,
            "message": "Success:party edited",
            "data": party
        }), 200)

    @version_one.route('/partyList/<int:id>', methods=["DELETE"])
    def delete_party(id):
        party = PartyModel().party_delete(id)
        return make_response(jsonify({
            "status": 200,
            "message": "Deleted"
        }), 200) 


class Office:
    @version_one.route('/officeList', methods=['POST'])
    def post_office():
        data = request.get_json()
        name = data['name']
        office_type = data['office_type']

        office = OfficeModel().create_office(name, office_type)

        return make_response(jsonify({
            "status": 201,
            "data": office
        }))

    
    @version_one.route('/officeList', methods=["GET"])
    def office_get_all():
        partyList = OfficeModel().get_all_offices()
        
        return make_response(jsonify({
            "status": 200,
            "message": "this is the partyList",
            "data": partyList
        }), 200) 

    @version_one.route('/officeList/<int:id>', methods=["GET"])
    def get_one_office(id):
        office = OfficeModel().offices_get_one(id)
        return make_response(jsonify({
            "status": 200,
            "message": "This is the office",
            "data": office
        }), 200)