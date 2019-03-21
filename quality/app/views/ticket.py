from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Ticket  # 导入工程师模型类
from app.forms import Add_ticket

# 首页的蓝本文件
ticket = Blueprint('ticket', __name__)


@ticket.route('/build_ticket/', methods=['POST', 'GET'])
def build_ticket():
    form = Add_ticket()
    if form.validate_on_submit():
        info = Ticket(number=form.number.data, summary=form.summary.data,
                      ticket_type=form.ticket_type.data, 
                      assinge_date=form.assigne_date.data,
                      assigne_id=form.assigne_id.data)
        info.save()
        # return redirect(url_for('engineer.engineer_manage'))
    return render_template('main/build_ticket.html', form=form)
