from flask import Blueprint, render_template, request, current_app
from app.models import Ticket, Process  # 导入单据模型类

# 首页的蓝本文件
main = Blueprint('main', __name__)


# 展示所有单据
@main.route('/', methods=['POST', 'GET'])
@main.route('/index/', methods=['POST', 'GET'])
def index():
    try:
        page = int(request.args.get('page', 1))
    except:
        page = 1
    pagination = Ticket.query.filter().order_by(Ticket.death_date.desc()).paginate(page, current_app.config['PAGE_NUM'], False)
    data = pagination.items
    process = Process.query.all()
    return render_template('main/index.html', data=data, process=process, pagination=pagination)


# 展示所有SR单据
@main.route('/show_SR/', methods=['POST', 'GET'])
def show_SR():
    try:
        page = int(request.args.get('page', 1))
    except:
        page = 1
    pagination = Ticket.query.filter(Ticket.ticket_type=='SR').order_by(Ticket.death_date.desc()).paginate(page, current_app.config['PAGE_NUM'], False)
    data = pagination.items
    process = Process.query.filter(Process.ticket_id.in_([x.id for x in data]))
    return render_template('main/index.html', data=data, process=process, pagination=pagination)


# 展示所有INC单据
@main.route('/show_INC/', methods=['POST', 'GET'])
def show_INC():
    try:
        page = int(request.args.get('page', 1))
    except:
        page = 1
    pagination = Ticket.query.filter(Ticket.ticket_type=='INC').order_by(Ticket.death_date.desc()).paginate(page, current_app.config['PAGE_NUM'], False)
    data = pagination.items
    process = Process.query.filter(Process.ticket_id.in_([x.id for x in data]))
    return render_template('main/index.html', data=data, process=process, pagination=pagination)


# 展示所有MONITOR单据
@main.route('/show_MONITOR/', methods=['POST', 'GET'])
def show_MONITOR():
    try:
        page = int(request.args.get('page', 1))
    except:
        page = 1
    pagination = Ticket.query.filter(Ticket.ticket_type=='MONITOR').order_by(Ticket.death_date.desc()).paginate(page, current_app.config['PAGE_NUM'], False)
    data = pagination.items
    process = Process.query.filter(Process.ticket_id.in_([x.id for x in data]))
    return render_template('main/index.html', data=data, process=process, pagination=pagination)