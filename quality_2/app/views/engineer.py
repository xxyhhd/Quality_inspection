from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Engineer  # 导入工程师模型类
from app.forms import Add_engineer

# 首页的蓝本文件
eng = Blueprint('engineer', __name__)


# 展示所有工程师
@eng.route('/engineer_manage/')
def engineer_manage():
    data = Engineer.query.filter(Engineer.status == True)
    return render_template('main/engineer.html', data=data)


# 工程师离职
@eng.route('/engineer_departure/<int:id>/')
def departure(id):
    a = Engineer.query.get(id)
    a.status = False
    a.save()
    flash('%s已离职' % (a.itcode))
    return redirect(url_for('engineer.engineer_manage'))


# 入职工程师
@eng.route('/add_engineer/', methods=['POST', 'GET'])
def add_engineer():
    form = Add_engineer()
    if form.validate_on_submit():
        info = Engineer(itcode=form.itcode.data)
        info.save()
        flash('%s已入职' % (form.itcode.data))
        return redirect(url_for('engineer.engineer_manage'))
    return render_template('main/add_engineer.html', form=form)
