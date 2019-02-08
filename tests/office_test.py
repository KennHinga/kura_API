import json
import unittest
from app import create_app
from app.api.v1.models.models import offices

class TestOffices(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.data = {
            "name": "Governor",
            "type": "elective"     
        }

    def test_create_office(self):
        response = self.client().post(path='/officeList', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
    
    
    def test_get_all_offices(self):
        response = self.client().post(path='/officeList', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_offices_get_one(self):
        # response = self.client().post(path='/partyList', data=json.dumps(self.data), content_type='application/json')
        response = self.client().get('/officelist/1', content_type="application/json")
        self.assertEqual(resp.status_code, 200)