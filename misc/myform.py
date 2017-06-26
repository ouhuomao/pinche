# -*- coding: utf-8 -*-
"""
C stand for chinese
"""

from wtforms import Form, validators, fields
from wtforms import BooleanField, StringField, IntegerField

class V_required(validators.DataRequired):
    def __init__(self, message=u"为必填项"):
        super(V_required, self).__init__(message)

class V_len(validators.Length):
    def __init__(self, min=-1, max=-1, message=None):
        m = message 
        if min == -1 and max != -1:
            m = u"长度必须小于%d个字符"%max
        elif min != -1 and max == -1:
            m = u"长度必须大于%d个字符"%min
        elif min != -1 and max != -1:
            m = u"长度必须大于于%d个字符小于%d个字符"%(min, max)
        super(V_len, self).__init__(min, max, m)

class V_range(validators.NumberRange):
    def __init__(self, min=None, max=None, message=None):    
        m = message 
        if min is not None and max is not None:
            m = u"必须大于%d小于%d"%(min, max)
        elif min is not None:
            m = u"必须大于%d"%min
        elif max is not None:
            m = u"必须小于%d"%max
        super(V_range, self).__init__(min, max, m)

class V_phone(object):
    def __call__(self, form, field):
        message = u"请输入11位数字的手机号码"
        if len(field.data) != 11:
            raise validators.ValidationError(message)
        is_ok = False
        prefixs = ["189", "135", "137"]
        for i in prefixs:
            if field.data.startswith(i):
                is_ok = True
                break
        
        if not is_ok:
            raise validators.ValidationError(message)


class F_str(StringField):
    def __init__(self, label="", clabel="-", validators=None, **kwargs):
        super(F_str, self).__init__(label, validators, **kwargs)
        self.clabel = clabel

class F_int(IntegerField):
    def __init__(self, label="", clabel="-", validators=None, **kwargs):
        super(F_int, self).__init__(label, validators, **kwargs)
        self.clabel = clabel

class F_phone(F_str):
    def __init__(self, label="", clabel="-", **kwargs):
        super(F_phone, self).__init__(label, clabel, [V_phone(), ], **kwargs)

class MForm(Form):
    #M stand for message, form with message
    @property
    def error_msg(self):
        msg = []
        for k, error in self.errors.items():
            msg.append("%s: %s"%(getattr(self, k).clabel, ",".join(error)))
        return ";".join(msg)

def get_form(form_config, req):
    class OneForm(MForm):
        pass

    for k, v in form_config.items():
        setattr(OneForm, k, v)
    inputs = req.args if req.method == "GET" else req.form
    return OneForm(inputs)


if __name__ == "__main__":
    class C_form(MForm):
        username = F_str('Username', u"用户名",
            [V_len(max=2), ], 
            default=u'test')
        phone = F_phone('phone', u"手机", default="13523845484")

    form = C_form()
    print "form username.data: ", form.username.data
    print "validate", form.validate()
    for k, error in form.errors.items():
        print "%s: %s"%(getattr(form, k).clabel, ",".join(error)) 
    print "clabel : ", form.username.clabel
    print "all: ", form.error_msg



