from flask import Flask, request, redirect, render_template, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)

app.config['SECRET_KEY'] = "whatnow"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def homepage():
    """Pets list homepage"""

    pets = Pet.query.all()

    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Form to add a new pet"""
    form = AddPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        if form.photo_url.data == '':
            photo_url = None
        else:
            photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')    
    else:
        return render_template("pet_form.html", form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_info(pet_id):
    """Pet info page"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPet(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        return redirect('/')
    else:
        return render_template('pet_display_edit.html', pet=pet, form=form)

