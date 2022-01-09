# Created by Atlas

from .base import PermissionHandler  # 粒度控制
from stark.service.v1 import StarkHandler, get_choice_text, StarkModelForm, StarkForm, Option


class SaleHandler(PermissionHandler, StarkHandler):
    """
    销售数据管理
    :return:
    """
    list_display = ['title', 'company', 'money', 'time_limit']  # 自定义显示

    # 加上模糊搜索
    search_list = ['title__contains', 'company__contains']
