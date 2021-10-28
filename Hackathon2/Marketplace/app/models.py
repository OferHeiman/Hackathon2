from app import db
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired, Email


class Ads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    photo = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(200), nullable=False)
    condition = db.Column(db.String(200), nullable=False)
    phonenumber = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    date_added = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Name %r>' % self.name


class AdForm(FlaskForm):
    name = StringField("Item name", validators=[InputRequired()])
    photo = StringField("Photo URL", validators=[InputRequired()])
    price = StringField("Price", validators=[InputRequired()])
    condition = StringField("Condition", validators=[InputRequired()])
    phonenumber = StringField("Phone Number", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email(message='Please input a valid email')])
    category = SelectField("Category",choices=['Vehicles', 'Real Estate', 'Apparel', 'Electronics', 'Home Goods',
                                               'Musical Instruments', 'Office Supplies', 'Sporting Goods',
                                               'Toys & Games', 'Hobbies', 'Family', 'Entertainment', 'Other'])
    description = TextAreaField("Description", validators=[InputRequired()])
    location = StringField("Location")
    submit = SubmitField("Submit")

    def __repr__(self):
        return '<Name %r>' % self.name
