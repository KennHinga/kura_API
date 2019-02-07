from flask import Blueprint, request, make_response, jsonify
from ..models.models import PartyModel

version_one = Blueprint('version_one', __name__, url_prefix='/api/v1')



class party:
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
            "message": "you have one aprty now",
            "data": party
        }), 200)


    # @version_one.route('/partyList/<int:id>', methods=["DELETE"])
    # def delete_party(id):
    #     party = PartyModel().delete_party(id)
    #     return make_response(jsonify({
    #         "status": 200,
    #         "message": "Deleted"
    #     }), 200) 