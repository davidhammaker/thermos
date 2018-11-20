from flask_wtf import FlaskForm as Form
from wtforms.fields import StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url


class BookmarkForm(Form):
    url = URLField('The URL for your bookmark:', validators=[DataRequired(), url()])
    description = StringField('Add an optional description:')

    def validate(self):
        if not self.url.data.startswith("http://") and not self.url.data.startswith("https://"):
            print("http:// {}".format(self.url.data.startswith("http://")))
            print("https:// {}".format(self.url.data.startswith("https://")))
            self.url.data = "http://" + self.url.data

        if not Form.validate(self):
            return False

        if not self.description.data:
            self.description.data = self.url.data

        return True
