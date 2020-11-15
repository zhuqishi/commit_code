import datetime
from django.db import models
from django.utils import timezone

class CommitCodeRequest(models.Model):
    commit_code = models.CharField('提交码', max_length=50)
    applicant = models.CharField('申请者', max_length=20)
    users = models.CharField('用户', max_length=100)
    code_path = models.CharField('代码路径', max_length=200)
    start_time = models.DateTimeField('开始时间',default = timezone.now)
    end_time = models.DateTimeField('结束时间',default = datetime.datetime.now()+datetime.timedelta(weeks=1))
    b_available = models.BooleanField('在可用期内', default=True)

    def __str__(self):
        return self.code_path
        #return list(self.commit_code,self.users,self.code_path,self.start_time,self.end_time,self.b_expired)
