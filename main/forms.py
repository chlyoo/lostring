from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    querysrtring = StringField('Input US stock symbol ex) AAPL, GOOG, MSFT', validators=[DataRequired()])
    search = SubmitField('Search')
