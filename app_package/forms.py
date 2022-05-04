from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, TextAreaField,\
    DateTimeField, MultipleFileField
from wtforms.validators import DataRequired, Length


class OfferPosts(FlaskForm):
    title = TextAreaField('Title of the offer',
                          validators=[DataRequired(), Length(max=100)])
    summary = TextAreaField('Info about the offer',
                            validators=[DataRequired(), Length(max=100)])
    couponCode = TextAreaField('Coupon details', validators=[DataRequired()])
    redeem_link = TextAreaField('Redeem link')
    terms_and_conditions = TextAreaField('Terms and Conditions')
    schedule = DateTimeField('Set dates')
    image = MultipleFileField('Upload photos')
    submit = SubmitField('Submit')


class EditPosts(FlaskForm):
    title = TextAreaField('Title of the offer',
                          validators=[DataRequired(), Length(max=100)])
    summary = TextAreaField('Info about the offer',
                            validators=[DataRequired(), Length(max=100)])
    couponCode = TextAreaField('Coupon details', validators=[DataRequired()])
    redeem_link = TextAreaField('Redeem link')
    terms_and_conditions = TextAreaField('Terms and Conditions')
    schedule = DateTimeField('Set dates')
    image = MultipleFileField('Upload photos')
    submit = SubmitField('Submit')
