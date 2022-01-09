# Created by Atlas

from .base import PermissionHandler  # 粒度控制
from stark.service.v1 import StarkHandler, get_choice_text, StarkModelForm, StarkForm, Option


class ProductHandler(PermissionHandler, StarkHandler):
    """
    产品数据管理
    :return:
    """
    list_display = ['title', 'money', 'time']  # 自定义显示

    # 加上模糊搜索
    search_list = ['title__contains']
