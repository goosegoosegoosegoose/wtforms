from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPet(FlaskForm):
    """Form for adding new pet"""

    name = StringField("Pet Name", validators=[InputRequired(message="Please enter a name")])
    species = SelectField("Species", choices=[('cat','Cat'), ('dog','Dog'), ('porc','Porcupine')], validators=[InputRequired(message="Please provide pet species")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Please enter valid age")])
    # how do I change field input type to numbers instead of a text input?
    notes = StringField("Notes")
    available = BooleanField("Available?")

class EditPet(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available?")
