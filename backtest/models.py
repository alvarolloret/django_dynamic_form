from django.db import models

# Create your models here.

class BacktestModel(models.Model):
    BacktestModel = (
            ('moving_averages', 'Moving Averages'),
            ('bollinger_bands', 'Bollinger Bands'))
    Period_CHOICES= [
            ('KLINE_INTERVAL_4HOUR', '4h'),
            ('others', 'Others'),
            ]
    Pair_CHOICES= [
        ('ETHUSDT', 'USDT_ETH'),
        ('others', 'Others'),
        ]

    pairChosen= models.CharField(default='ETHUSDT', choices=Pair_CHOICES, max_length=1024)
    periodChosen= models.CharField(default='KLINE_INTERVAL_4HOUR', choices=Period_CHOICES, max_length=1024)
    strategy_type = models.CharField(default='moving_averages',
            choices=BacktestModel, max_length=1024)
    strategy_details = models.CharField(max_length=1024)
