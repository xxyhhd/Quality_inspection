from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, DateField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import Ticket


# 表单注册类
class Add_ticket(FlaskForm):
    number = StringField('单号', validators=[DataRequired(message='单号不能为空'),
                                           Length(min=1, max=50, message='单号不能超过50字')],
                         render_kw={'placeholder': '请输入单号'})
    summary = TextAreaField('概述', validators=[DataRequired(
        message='概述不能为空')], render_kw={'placeholder': '请输入概述'})
    ticket_type = SelectField('类型：', choices=[
        ('INC', 'INC'),
        ('SR', 'SR'),
        ('MONITOR', 'MONITOR')])
    assigne_date = DateField('到组日期', format='%Y-%m-%d', render_kw={'placeholder': '2019-01-01'})
    assigne_id = StringField('接单者', validators=[DataRequired(message='接单工程师不能为空')])
    submit = SubmitField('添加')
