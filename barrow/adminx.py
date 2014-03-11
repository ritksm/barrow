#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jack River'

import xadmin

from barrow.models import *


class ApplicationAdmin(object):
    pass


class SpiderAdmin(object):
    list_display = ['application', 'name', 'running']

    def save_models(self):
        self.new_obj.save()

        add_spider_to_scheduler(self.new_obj)


class SpiderTaskAdmin(object):
    list_display = ['spider', 'start_time', 'end_time', 'state']


class SpiderResultAdmin(object):
    list_display = ['hash_value', 'create_time', 'retrieved']


xadmin.site.register(Application, ApplicationAdmin)
xadmin.site.register(Spider, SpiderAdmin)
xadmin.site.register(SpiderTask, SpiderTaskAdmin)
xadmin.site.register(SpiderResult, SpiderResultAdmin)
