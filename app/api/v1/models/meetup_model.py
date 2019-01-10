from ...v1.utils.validators import Validations
import datetime

from ...v1.models import user_models


meetup = []

meetup_id = 1



class Meetups(Validations):
    """A meetup model"""

    def create_meetup(self, createdOn, location, images, topic, happeningOn, tags):
        """add a meetup to the meetup"""
        new_meetup = dict(
            meetup_id=len(meetup) + 1,
            createdOn=datetime.datetime.now().strftime("%H:%M%P %A %d %B %Y"),
            location=location,
            images=images,
            topic=topic,
            happeningOn=happeningOn,
            tags=tags,
        )

        checks = location, topic, happeningOn, tags
        strings = location, images, topic, tags
        if self.is_empty(checks) is True:
            return {"error": "Please fill out all fields"}, 406
        elif self.is_whitespace(checks) is True:
            return {"error": "Data cannot contain white strings"}, 406
        elif self.is_string(strings) is False:
            return {"error": "Input must be of type string"}, 406
        elif self.is_valid_date(happeningOn) is False:
            return {"error": "Date must be in this format DD-MM-YYYY"}
        else:
            meetup.append(new_meetup)
            return new_meetup

    def get_all_meetups(self):
        if len(meetup) == 0:
            return False
        else:
            return meetup


    @staticmethod
    def get_specific_meetup(meetup_id):
        meetup_item = [meet for meet in meetup if meet["meetup_method to id"] == meetup_id]
        if meetup_item:
            return meetup_item[0]
        return {"message": "Meetup record not found"}

    




