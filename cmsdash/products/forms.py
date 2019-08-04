from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cmsdash.models import Product


class NewProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = FloatField('Price (GBP)', validators=[DataRequired()])
    in_stock = BooleanField('In Stock', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()], id='summernote')
    picture = FileField('Upload main product image', validators=[FileAllowed(['jpg', 'png'])])
    weight = FloatField('Weight (g)')
    submit = SubmitField('Create Product')