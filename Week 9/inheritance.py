class object:
    pass
class BaseX(object):
    pass
class BaseY(object):
    pass
class BaseZ(object):
    pass
class BaseA(BaseX,BaseY):
    pass
class BaseB(BaseY,BaseZ):
    pass
class BaseM(BaseA, BaseB, BaseZ):
    pass
