from django.shortcuts import render
from trader_python.botvariables import botVariables

from backtest.forms import BacktestForm, BacktestDetailsForm

from django.http import JsonResponse
from django.template.loader import render_to_string

# Basic form that will be displayed
def dynamic(request):

    #When request happens, an empty dict is generatedn
    context = {}

    #In case the user has clicked the submit button
    if request.method == "POST":
        backtestForm = BacktestForm(request.POST)
        if backtestForm.is_valid():
            #Check if the user had changed the strategy_details from the deffault
            if request.POST.get('strategy_details')=="null":
                #Use default values stored in botVariables object
                vars=botVariables()
                new_fields=vars.strategy_det[request.POST.get('strategy_type')+"_def"]
                backtest= backtestForm.save(commit=False)
                backtest.strategy_details=new_fields
                backtest.save()
                print ("default values saved")
            else:
                backtestForm.save()
        else:
            print ("not valid form")

    #insert the backtestForm within the context
    context['backtest_form'] = BacktestForm(request.POST or None,)
    # print (context)
    return render(request, "backtest/dynamic.html", context)




def strategy_specify(request):
    if request.method == 'POST':
        DetailForm = BacktestDetailsForm(request.POST)
    else:
        if 'strategy_type' in request.GET:
            strat_type= str(request.GET['strategy_type'])
            vars=botVariables()
            new_fields=vars.strategy_det[strat_type]
            DynamicDetailsForm = type('DynamicDetailsForm', (BacktestDetailsForm,), new_fields)

            DetailForm = DynamicDetailsForm()


    return save_strategy_details(request, DetailForm, 'backtest/show_details_strategy.html')



def save_strategy_details(request, form, template_name):
    data = dict()
    content={}
    if request.method == 'POST':
        if form.is_valid():
            for key in request.POST.keys():
                if key != 'csrfmiddlewaretoken':
                    content[key] = request.POST[key]
            data['strategy_details']=content
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    print (form)
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
