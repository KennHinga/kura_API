import os
import datetime
import jwt
from app.api.v2.Models.user_models import UserModel 
from flask import Blueprint, request, jsonify, abort, make_response

version_two = Blueprint('version_two', __name__, url_prefix= '/api/v2' )

class Register:
    """class for signing up to become a user"""

    @version_two.route('/register', methods=['POST'])
    def post_user():
        data = request.get_json()
        firstName = data['firstName']
        lastName = data['lastName']
        otherName = data['otherName']
        email = data['email']
        phoneNumber = data['phoneNumber']
        passportUrl = data['passportUrl']
        isAdmin = data['isAdmin']
        isCandidate = data['isCandidate']
        password = data['password']

        user= UserModel().create_new_user(firstName, lastName, otherName, email, phoneNumber, passportUrl, isAdmin, isCandidate, password)
        
        return make_response(jsonify({
            "message": "user created successfully",
            "data": user
        }),201)