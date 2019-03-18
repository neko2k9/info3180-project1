from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired

def validate_gender(form, field):
    if field.data == "":
        raise ValidationError("Please select a gender.")
        
class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired('Please provide a first name')])
    lastname = StringField("Last Name", validators=[InputRequired('Please provide a last name')])
    gender = SelectField("Gender", choices=[("", "---"),('M','Male'), ('F','Female')], validators=[validate_gender])
    email = StringField('Email Address', validators=[Email('This is not a valid email address.'), InputRequired('Please provide an email address')])
    location = StringField('Location', validators=[InputRequired('Please enter a location')])
    bio = TextAreaField('Biography', validators=[InputRequired('Please enter a biography')])
    photo= FileField('images', validators=[FileRequired('Please upload a photo for your profile picture'), FileAllowed(['jpg','png','jpeg'], 'Only jpg, jpeg and png images can be uploaded!')])
