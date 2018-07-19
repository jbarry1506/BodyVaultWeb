from database import Database


__author__ = 'jbarry1506'


class Post(object):
    # each post will have the user's updated weight and body fat percentage
    def __init__(self, post_id, weight, bodyfat, user, date, id):
        self.post_id = post_id
        self.weight = weight
        self.bodyfat = bodyfat
        self.user = user
        self.created_date = date
        self.id = id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                            data=self.json())

    def json(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'weight': self.weight,
            'bodyfat': self.bodyfat,
            'user': self.user,
            'created_date': self.created_date
        }

    @staticmethod
    def from_mongo(id):
        # Post.from_mongo('123')
        return Database.find_one(collection='posts', query={'id': id})

    @staticmethod
    def from_bodyVaultWeb(id):
        return Database.find(collection='posts', query={'post_id: id'})
