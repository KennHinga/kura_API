import json
import unittest
from app import create_app
from app.api.v1.models.models import parties

class TestParties(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.data = {
            "name": "yu",
            "hqAddress": "yt",
            "logoUrl": "logoUrl"   
        }

    def test_create_party(self):
        response = self.client().post(path='/partyList', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        

    def test_get_all_parties(self):
        response = self.client().post(path='/partyList', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_parties_get_one(self):
        # response = self.client().post(path='/partyList', data=json.dumps(self.data), content_type='application/json')
        response = self.client().get('/partylist/1', content_type="application/json")
        self.assertEqual(resp.status_code, 200)

    def test_edit_party(self):
        response = self.client().post(path='/partyList', data=json.dumps(edit_party.data), content_type='application/json')
        response = self.client().get('/partyList/1', content_type="application/json")
        self.assertEqual(resp.status_code, 200)

    def test_Party_delete(self):
        response = self.client().post(path= ('/partyList/1'), content_type= "application/json")
        self.assertEqual(resp.status_code, 200)
        


if __name__ == '__main__':
    unnittest.main()


    

   