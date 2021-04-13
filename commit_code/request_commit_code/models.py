import datetime
from django.db import models
from django.utils import timezone
from .private_method import private_request_commit_code

class CommitCodeRequest(models.Model):
    applicant = models.CharField('申请者', max_length=20)
    users = models.CharField('用户', max_length=100)
    code_path = models.CharField('代码路径', max_length=200)
    commit_code = models.CharField('提交码', max_length=50, default = private_request_commit_code(users,code_path))
    start_time = models.DateTimeField('开始时间', default = timezone.now)
    end_time = models.DateTimeField('结束时间', default = datetime.datetime.now()+datetime.timedelta(weeks=2))
    last_request_time = models.DateTimeField('最近申请时间', default = timezone.now)

    def b_available(self):
        cur_time = timezone.now()
        if cur_time > self.end_time:
            return False
        return cur_time - datetime.timedelta(hours=6) < self.last_request_time
    b_available.boolean = True
    b_available.short_description = "在可用期内"

    def __str__(self):
        return self.code_path
        #return list(self.commit_code,self.users,self.code_path,self.start_time,self.end_time,self.b_expired)
