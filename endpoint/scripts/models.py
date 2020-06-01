from backend import db


##################################################
#           Define tab that we will use          #
##################################################
class Image(db.Model):

    __tablename__ =  "images"   #tab name


    #tab columns and props
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary())
    infos = db.Column(db.Integer())

    def __init__(self, image, infos):
        self.image = image
        self.infos = infos

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'image': self.image,
            'infos': self.infos,
        }
##################################################


'''
TAB in PLSQL :

CREATE TABLE images(
   id   SERIAL    NOT NULL,
   image           BYTEA    NOT NULL,
   infos            TEXT     NOT NULL
);

'''