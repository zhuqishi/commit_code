from django.contrib import admin
from .models import CommitCodeRequest

admin.site.site_header = "提交码管理系统"
admin.site.site_title = "登录提交码管理系统"
admin.site.register(CommitCodeRequest)
