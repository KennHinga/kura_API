import json
import unittest
from run import app
from app.api.v1.models.models import offices

class TestOffices(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client= self.app.test_client
        self.data = {
            "name": "Governor",
            "office_type": "elective"     
        }

    def test_create_office(self):
        response = self.client().post(path='/api/v1/officeList', data=json.dumps(self.data), content_type='application/json')
        resp = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
    
    def test_get_all_offices(self):
        self.client().post(path='/api/v1/officeList', data=json.dumps(self.data), content_type='application/json')
        response = self.client().get(path='/api/v1/officeList', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_ofices_get_one(self):
        self.client().post(path='/api/v1/officeList', data=json.dumps(self.data), content_type='application/json')
        response = self.client().get(path='/api/v1/officeList/1', content_type="application/json")
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unnittest.main()

