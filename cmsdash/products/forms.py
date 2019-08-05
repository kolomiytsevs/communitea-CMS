from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, FloatField
from wtforms.validators import DataRequired


class NewProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = FloatField('Price (GBP)', validators=[DataRequired()])
    in_stock = BooleanField('In Stock', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()], id='summernote')
    picture = FileField('Update Main Image', validators=[FileAllowed(['jpg', 'png'])])
    weight = FloatField('Weight (g)')
    submit = SubmitField('Save Product')