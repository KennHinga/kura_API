from flask import Blueprint, request, make_response, jsonify
from ..models.models import PartyModel

version_one = Blueprint('version_one', __name__, url_prefix='/api/v1')

@version_one.route('/parties', methods=['POST'])

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

    
    # @api.route('/partyList', methods=["GET"])
    # def party_get_all():
    #     partyList = Party().get_all_parties()
    #     return make_response(jsonify({
    #         "status": 200,
    #         "message": "this is the partyList",
    #         "data": partyList
    #     }), 200) 

    # def party_get_one():
    #     pass

    # def party_put():
    #     pass
    
    # def party_delete():
    #     pass