# temp_conv.py
from flask import Flask
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from converter import c_to_f, f_to_c

temp_conv = Flask(__name__)
temp_conv.config['SECRET_KEY'] = '9jp3jfjdfljasdf9j-23f2f'

class InputForm(FlaskForm):
    celsius = StringField('Celsius')
    fahrenheit = StringField('Fahrenheit')
    convert_to_f = SubmitField('Convert to Fahrenheit')
    convert_to_c = SubmitField('Convert to Celsius')


@temp_conv.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        if 'convert_to_f' in request.form.keys():
            form.fahrenheit.data = c_to_f(float(form.celsius.data))
        else:
            form.celsius.data = f_to_c(float(form.fahrenheit.data))
    return render_template('index.html', form = form )


if __name__ == '__main__':
    temp_conv.run()

