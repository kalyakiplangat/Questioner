import json
import datetime

from .base_tests import BaseTest
from app.api.v1.models.meetup_model import Meetups

create_meetup_url = "api/v1/meetups"
get_all_url = "api/v1/meetups/upcoming"
get_one_url = "api/v1/meetups/1"
rsvp_url = "api/v1/meetups/1/rsvps"

class TestMeetups(BaseTest):
  #Test meetup class
    def test_create_meetup(self):
        with self.client:
            meetup_payload = {"location": "Thika", "images": "url", "topic": "topic", "happeningOn": "1-2-2019", "Tags": "python flask"}
            response = self.client.post(create_meetup_url, data=json.dumps(meetup_payload), content_type="application/json")
            result = json.loads(response.data.decode("UTF-8"))
            
            self.assertEqual(result["status"], 201)
            self.assertEqual(result["message"], "New meetup  created successfully")
            self.assertEqual(response.status_code, 201)
            self.assertTrue(response.content_type == "application/json")

    def test_get_all_meetups(self):
        #Get all the record of meetup
        with self.client:
            meetup_payload = {"location": "thika", "images": "url", "topic": "topic", "happeningOn": "1-2-2019", "Tags": "python flask"}
            self.client.post(create_meetup_url, data=json.dumps(meetup_payload), content_type="application/json")

            result1 = self.client.get(get_all_url)
            self.assertEqual(result1.status_code, 200)

    def test_get_specific_meetup(self):
        meetup_payload = {"meetup_id": 1, "location": "thika", "images": "url", "topic": "topic", "happeningOn": "1-2-2019", "Tags": "python flask"}
        self.client.post(create_meetup_url, data = json.dumps(meetup_payload), content_type="application/json")

        result2 = self.client.get(get_one_url)
        self.assertEqual(result2.status_code, 200)

    def test_rsvp_meetup(self):
        #create_meetup
        with self.client:
            meetup_payload = {"location": "gathiga", "images": "url", "topic": "Django", "happeningOn": "2-4-2019", "Tags": "Django"}
            self.client.post(create_meetup_url, data=json.dumps(meetup_payload), content_type="application/json")

            rsvp_payload = {"status": "yes"}
            response8 = self.client.post(rsvp_url, data=json.dumps(rsvp_payload), content_type = "application/json")
            result8 = json.loads(response8.data.decode("UTF-8"))

            self.assertEqual(result8["status"], 201)
            self.assertEqual(response8.status_code, 201)
            self.assertTrue(response8.content_type == "application/json")







