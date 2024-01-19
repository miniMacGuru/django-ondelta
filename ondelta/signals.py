# -*- coding: utf-8 -*-
from django.dispatch import Signal

post_ondelta_signal = Signal(['fields_changed', 'instance'])
