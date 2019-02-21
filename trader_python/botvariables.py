import sys, getopt
import datetime
from time import mktime as mktime
import time
from django import forms

class botVariables(object):
    def __init__(self):
        self.strategy_det= {
            'moving_averages': {
                'mov_av_1': forms.IntegerField(initial=12),
                'mov_av_2'   : forms.IntegerField(initial=15),
                },
            'bollinger_bands':{
                'boll_band_1': forms.IntegerField(initial=11),
                'boll_band_2': forms.IntegerField(initial=16),
                },
            'moving_averages_def': {
                'mov_av_1': 12,
                'mov_av_2' : 15,
                },
            'bollinger_bands_def':{
                'boll_band_1': 11,
                'boll_band_2': 16,
                },
        }
