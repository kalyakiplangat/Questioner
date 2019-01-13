'''Global lists'''
meetups = []
questions = []
rsvps = []


class BaseModel(object):
    '''Base class'''
    def __init__(self, db=''):
        self.db = db

    def save(self, data={}):
        db_add = self.check_db()
        self.data = data
        db_add.append(data)

    def check_db(self):
        db_obj = dbconfig[self.db]
        return db_obj

    def return_data(self):
        if self.save:
            return self.data
        return None

    def find(self, id: int):
        db_type = self.check_db()

        for index, item in enumerate(db_type):
            if id == item['id']:
                return index, item
        return None, None

    def update(self, data_update={}):
        '''Update existing data'''
        db = self.check_db()
        index, item = self.find(data_update['id'])
        if item:
            data = db[index]
            data.update(data_update)
            return data

    def delete(self, index: int):
        '''Delete existing data'''
        db = self.check_db()

        if index and isinstance(db, list):
            del db[index]
            return True
        return False

dbconfig = {
    'meetupsdb': meetups,
    'questiondb': questions,
    'rsvpsdb': rsvps
}
