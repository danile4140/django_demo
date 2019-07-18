from rest_framework import pagination


class MyCursorPagination(pagination.CursorPagination):
    """
    Cursor 光标分页 性能高，安全
    """
    page_size = 9
    ordering = '-id'
    page_size_query_param = "pages"
    max_page_size = 20


class MyPageNumberPagination(pagination.PageNumberPagination):
    """
    普通分页，数据量越大性能越差
    """
    # 指定每一页的个数
    page_size = 11
    # 可以让前端来设置page_szie参数来指定每页个数
    page_size_query_param = 'size'
    # 设置页码的参数
    page_query_param = 'page'
    # 一页最大20个
    max_page_size = 20


