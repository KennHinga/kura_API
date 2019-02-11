import json
import unittest
from run import app
from app.api.v1.models.models import offices

class TestOffices(unittest.TestCase):
    """class to test officeModel"""
    def setUp(self):
        self.app = app
        self.client= self.app.test_client
        self.data = {
            "name": "Governor",
            "office_type": "elective"     
        }

    def test_create_office(self):
        """method to test create_office"""
        response = self.client().post(path='/api/v1/officeList', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["message"],"office posted successfully" )
    
    def test_get_all_offices(self):
        """method to test get_all_offices"""
        self.client().post(path='/api/v1/officeList', data=json.dumps(self.data), content_type='application/json')
        response = self.client().get(path='/api/v1/officeList', content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["message"],"this is the partyList" )

    def test_ofices_get_one(self):
        """method testing get_one office"""
        self.client().post(path='/api/v1/officeList', data=json.dumps(self.data), content_type='application/json')
        response = self.client().get(path='/api/v1/officeList/1', content_type="application/json")
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unnittest.main()

