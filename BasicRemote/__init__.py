from __future__ import absolute_import, print_function, unicode_literals
from .SmartPerformanceSuite import SmartPerformanceSuite

def create_instance(c_instance):
    return SmartPerformanceSuite(c_instance)