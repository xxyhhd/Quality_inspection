from flask import Blueprint, render_template, request, current_app
from app.models import Ticket  # 导入单据模型类

# 首页的蓝本文件
main = Blueprint('main', __name__)


@main.route('/', methods=['POST', 'GET'])
@main.route('/index/', methods=['POST', 'GET'])
def index():
    # form = Add_engibeer()
    data = Ticket.query.all()
    return render_template('main/index.html', data=data)
