'''Define globally accessible lists to store data'''
meetups = []
questions = []
rsvps = []


class BaseModel(object):
    '''Base class model'''
    def __init__(self, db=''):
        '''Initializes the database'''
        self.db = db

    def save(self, data={}):
        '''saves db'''
        db_add = self.check_db()
        self.data = data
        db_add.append(data)

    def check_db(self):
        '''Select a specified db '''
        db_object = db_select[self.db]
        return db_object

    def return_data(self):
        '''Return db data'''
        if self.save:
            return self.data
        return None

    def find(self, id: int):
        '''find a specific data in db'''
        db_type = self.check_db()

        for index, items in enumerate(db_type):
            if id == items['id']:
                return index, items
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
        '''Delete data'''
        db = self.check_db()

        if index and isinstance(db, list):
            del db[index]
            return True
        return False

db_select = {
    'meetupsdb': meetups,
    'questiondb': questions,
    'rsvpsdb': rsvps
}
