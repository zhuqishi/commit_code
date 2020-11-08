import datetime
from django.db import models
from django.utils import timezone

class CommitCodeRequest(models.Model):
    commit_code = models.CharField('提交码', max_length=200, default="HIKTest_0102335")
    applicant = models.CharField('申请者', max_length=20)
    users = models.CharField('用户', max_length=100)
    code_path = models.CharField('代码路径', max_length=200)
    start_time = models.DateTimeField('开始时间',default = timezone.now)
    end_time = models.DateTimeField('结束时间',default = timezone.now)
    b_expired = models.BooleanField('是否过期', default=0)

    def __str__(self):
        return self.commit_code

    '''
    def __init__(self):
        self.init_end_time()

    def init_end_time(self):
        self.end_time = self.start_time + datetime.timedelta(weeks=1)
        '''