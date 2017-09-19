from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError
from .models import User

class LoginForm(Form):
    user_id = StringField('user_id', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class RegistrationForm(Form):
    user_id = StringField('user_id', validators=[DataRequired(), Length(1, 50), Regexp('^[A-Za-z0-9_.]*$', 0,
                                                                                       'User is must have only letters, '
                                                                                       'numbers, dots or underscores')])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('password2', message='password must match')])
    password2 = PasswordField('confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_user_id(self, field):
        if User.query.filter_by(user_id=field.data).first():
            raise ValidationError('User id already in use')

class PostForm(Form):
    body = TextAreaField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')
