from flask_wtf import FlaskForm
import wtforms as wf
from wtforms import validators
from app.models import Transactons


class TransactionForm(FlaskForm):
    period = wf.StringField('Период', validators=[wf.validators.DataRequired()])
    value = wf.IntegerField('Сумма', validators=[wf.validators.DataRequired()])
    status = wf.SelectField('Статус', choices=[('Activate'), ( 'Deactivate')])
    unit = wf.SelectField('Валюта', choices=[('Кыргызские сомы'), ('Доллары США')])
    subject = wf.StringField('Комментарии')
    submit = wf.SubmitField(label='Добавить')


