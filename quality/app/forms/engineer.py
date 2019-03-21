from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import Engineer


# 表单注册类
class Add_engineer(FlaskForm):
    itcode = StringField('ITcode', validators=[DataRequired(message='不能为空'),
                                               Length(min=1, max=12, message='不能超过12个字')],
                         render_kw={'placeholder': '请输入ITcode'})
    submit = SubmitField('添加')
