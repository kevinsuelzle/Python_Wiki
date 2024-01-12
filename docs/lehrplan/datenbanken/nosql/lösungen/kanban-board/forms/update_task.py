# forms/update_task.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class UpdateTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    status = SelectField('Status', choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')],
                         validators=[DataRequired()])
    submit = SubmitField('Update Task')
