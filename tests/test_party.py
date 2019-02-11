import json
import unittest
from app import create_app
from app.api.v1.models.models import parties

class TestParties(unittest.TestCase):
    """test class for parties"""

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.data = {
            "name": "yu",
            "hqAddress": "yt",
            "logoUrl": "logoUrl"   
        }

    def test_create_party(self):
        """method to test create_party """
        response = self.client().post(path='/api/v1/partyList', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200)  

    def test_get_all_parties(self):
        """method to test getting all_parties"""
        self.client().post(path='/api/v1/partyList', data=json.dumps(self.data), content_type='application/json')
        response = self.client().get(path='/api/v1/partyList', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_parties_get_one(self):
        """method to test get_one_party"""
        self.client().post(path='/api/v1/partyList', data=json.dumps(self.data), content_type='application/json')
        response = self.client().get(path='/api/v1/partyList/1', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_edit_party(self):
        """method to test edit_party"""
        response = self.client().post(path='/api/v1/partyList', data=json.dumps(self.data), content_type='application/json')
        response = self.client().get(path='/api/v1/partyList/1', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_Party_delete(self):
        """method to test delete_party"""
        response = self.client().post(path='/api/v1/partyList/', data=json.dumps(self.data), content_type= "application/json")
        response = self.client().delete(path='/api/v1/partyList/1', content_type="application/json")
        self.assertEqual(response.status_code, 200)
        


if __name__ == '__main__':
    unnittest.main()


    

   