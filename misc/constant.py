# -*- coding: utf-8 -*-

class USER_TYPE(object):
    DRIVER =1
    PASSENGER = 2
    ALL = {
        DRIVER: "司机",
        PASSENGER: "乘客",
    }

class USER(object):
    class STATUS(object):
        NORMAL = 1
        DEL = 2
      

class ORDER(object):
    class TYPE(object):
        OFFER_SEAT = 1
        FIND_SEAT = 2
        ALL = {
            OFFER_SEAT: "提供座位",
            FIND_SEAT: "求乘",
        }
    class DIRECTION(object):
        GO_OUT = 1
        RETURN = 2
        ALL = {
            GO_OUT: "出城",
            RETURN: "回小区",
        }

    class STATUS(object):
        INIT = 1
        BOOK = 2
        CONFIRM = 3
        CANCEL = 4
        ALL = {
            INIT: "新发布",
            BOOK: "预订",
            CONFIRM: "确定",
            CANCEL: "已取消"
        }
