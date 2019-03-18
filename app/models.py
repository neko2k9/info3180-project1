from . import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email=db.Column(db.String(80),unique=True)
    location=db.Column(db.String(80))
    bio = db.Column(db.String(255))
    filename = db.Column(db.String(80))
    date_joined = db.Column(db.DateTime)
    
    def __init__(self,firstname,lastname,gender,email,location,biography,filename,date_joined):
        self.firstname=firstname
        self.lastname =lastname
        self.gender=gender
        self.email=email
        self.location=location
        self.bio=biography
        self.filename=filename
        self.date_joined=date_joined

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)