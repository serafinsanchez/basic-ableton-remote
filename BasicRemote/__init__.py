from __future__ import absolute_import, print_function, unicode_literals
from .BasicRemote import BasicRemote

def create_instance(c_instance):
    return BasicRemote(c_instance)