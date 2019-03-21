from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, DateField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import Process


# 表单注册类
class Add_process(FlaskForm):
    engineer_id = StringField('处理者', validators=[DataRequired(message='处理工程师不能为空')])
    time = DateField('处理日期', format='%Y-%m-%d', render_kw={'placeholder': '2019-01-01'})
    process_one = SelectField('是否完全更新：', choices=[
        ('合格', '合格'),
        ('不合格', '不合格')])
    process_two = SelectField('是否符合规范：', choices=[
        ('合格', '合格'),
        ('不合格', '不合格')])
    submit = SubmitField('添加')
