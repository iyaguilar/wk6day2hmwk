from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, equal_to


class CreatePostForm(FlaskForm):
    img_url = StringField('Image URL:', validators=[DataRequired()])
    submit = SubmitField('Create Post')