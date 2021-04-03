from django.contrib import admin
from .models import CommitCodeRequest


class CommitCodeRequestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('申请者',          {'fields':['applicant']}),
        ('提交码使用者',    {'fields':['users']}),
        ('代码路径',        {'fields':['code_path']}),
        ('开始时间',        {'fields':['start_time'], 'classes':['collapse']}),
        ('结束时间',        {'fields':['end_time'], 'classes':['collapse']}),
    ]

    list_display = ('commit_code', 'applicant', 'users', 'code_path', 'start_time', 'end_time', 'last_request_time', 'b_available')

admin.site.site_header = "提交码管理系统"
admin.site.site_title = "登录提交码管理系统"
admin.site.register(CommitCodeRequest, CommitCodeRequestAdmin)
