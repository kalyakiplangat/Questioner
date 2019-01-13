import datetime

from .basemodel import BaseModel, meetups, rsvps


class Meetups(BaseModel):
    '''Meetup model'''
    def __init__(self):
        super().__init__('meetupsdb')

    def create_meetup(self, location: str, images: list, topic: str,
                      happeningOn: str, tags: list):
        '''creates meetup'''
        meetup = {
            'id': len(meetups)+1,
            'createdOn': str(datetime.date.today()),
            'topic': topic,
            'location': location,
            'images': images,
            'happeningOn': happeningOn,
            'tags': tags
        }
        self.save(meetup)

    def get_all(self):
        '''All the meetup'''
        return meetups


class RSVPS(BaseModel):
    '''RSVP model'''
    def __init__(self):
        super().__init__('rsvpsdb')

    def create_rsvp(self, userid: int, meetupid: int):
        '''Adds a RSVP'''
        rsvp = {
            'userid': userid,
            'meetupid': meetupid,
            'isScheduled': True
        }
        self.save(rsvp)
