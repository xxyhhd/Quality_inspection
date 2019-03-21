from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from app.models import Ticket, Process  # 导入工程师模型类
from app.forms import Add_ticket, Add_process
from sqlalchemy import or_  #导入或操作

# 首页的蓝本文件
ticket = Blueprint('ticket', __name__)


# 建单方法
@ticket.route('/build_ticket/', methods=['POST', 'GET'])
def build_ticket():
    form = Add_ticket()
    if form.validate_on_submit():
        info = Ticket(number=form.number.data, summary=form.summary.data,
                      ticket_type=form.ticket_type.data,
                      assinge_date=form.assigne_date.data,
                      assigne_id=form.assigne_id.data)
        info.save()
        return redirect(url_for('main.index'))
    return render_template('main/build_ticket.html', form=form)


# 添加处理工程师方法
@ticket.route('/build_process/<int:id>/', methods=['POST', 'GET'])
def build_process(id):
    form = Add_process()
    if form.validate_on_submit():
        info = Process(engineer_id=form.engineer_id.data, 
                        time=form.time.data, 
                        process_one=form.process_one.data, 
                        process_two=form.process_two.data, ticket_id=id)
        info.save()
        return redirect(url_for('main.index'))
    return render_template('main/build_process.html', form=form)


# 添加删除单据方法
@ticket.route('/delete_ticket/<int:id>/')
def delete_ticket(id):
    print(id)
    Ticket.query.get(id).delete()
    flash('已删除')
    return redirect(url_for('main.index'))



# 搜索方法
@ticket.route('/search/', methods=['POST', 'GET'])
def search():
    search_info = request.form.get('search', '')
    if not search_info:
        search_info = request.args.get('search', '')
    try:
        page = int(request.arges.get('search', 1))
    except:
        page = 1
    pagination = Ticket.query.filter(or_(Ticket.number.contains(search_info), Ticket.summary.contains(search_info))).order_by(Ticket.death_date.desc()).paginate(page, current_app.config['PAGE_NUM'], False)
    data = pagination.items
    process = Process.query.filter(Process.ticket_id.in_([x.id for x in data]))
    return render_template('main/index.html', data=data, process=process, pagination=pagination)


