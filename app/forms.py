from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, Email

#ContactForm
class ContactForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email',validators = [DataRequired(), Email()])
    subject = StringField('Subject',validators = [DataRequired()])
    message = TextField('Message',validators = [DataRequired(),Length(min=4, max=250)])
    submit = SubmitField('Submit')