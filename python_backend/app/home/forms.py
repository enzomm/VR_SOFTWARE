from flask_wtf import FlaskForm
from wtforms import TextField, StringField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductForm(FlaskForm):
    class Meta:
        csrf = False

    image = TextField('Image', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(min=10, max=255)])
    cost = DecimalField('Cost', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    type = StringField('Type', validators=[DataRequired(), Length(max=64)])
