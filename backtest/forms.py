from django import forms
from .models import  BacktestModel


class BacktestForm(forms.ModelForm):
    class Meta:
        model = BacktestModel
        fields = ('pairChosen', 'periodChosen', 'strategy_type', 'strategy_details')
        # widgets = {'backtest_details': forms.HiddenInput()}

    strategy_details = forms.CharField(widget=forms.HiddenInput(), initial="null")



#The backtest details is an empty form given that it will be filled dynamically by the view
class BacktestDetailsForm(forms.Form):
    # strategy_details = forms.CharField()
    pass
