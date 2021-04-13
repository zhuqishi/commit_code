def private_request_commit_code(user, code_path):
    #保留默认值，实际应该使用公司对应的接口#
    return "HIK_TEST12345"+str(code_path)[-3:-1]

def private_login(user, password):
    pass