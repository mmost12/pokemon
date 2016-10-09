from django.shortcuts import render
from django.http import HttpResponseRedirect
import test

app_name = 'evo'
# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get("script") == "evolution":
            return HttpResponseRedirect('evo/')
        else:
            return HttpResponseRedirect('fight/')
    else:
        return render(request, 'evo/index.html', {})

def fight(request):
    report = test.show_fight()
    teams  = report[:2]
    report = report[2:]
    return render(request, 'evo/fight.html', {'report': report, 'teams': teams})

def evo(request):
    report = [x.split() for x in test.small()]
    for i in range(len(report)):
        report[i] = [x for x in report[i] if not x[len(x)-4:]=='Mega'
                                          and not x[len(x)-6:]=='Primal'
                                          and not x == 'Forme'
                                          and not x == 'Mode'
                                          and not x == 'Size'
                                          and not x == 'Rotom'
                                          and not x == 'Mime'
                                          and not x == 'X'
                                          and not x == 'Y']
        for j in range(len(report[i])):
            if report[i][j][len(report[i][j])-3:] == 'Zen':
                report[i][j] = report[i][j][:len(report[i][j])-3] + '-Zen'
            elif report[i][j][len(report[i][j])-3:] == 'Fan':
                report[i][j] = report[i][j][:len(report[i][j])-3] + '-Fan'
            elif report[i][j][len(report[i][j])-3:] == 'Sky':
                report[i][j] = report[i][j][:len(report[i][j])-3] + '-Sky'
            elif report[i][j][len(report[i][j])-4:] == 'Aria':
                report[i][j] = report[i][j][:len(report[i][j])-4] + '-Aria'
            elif report[i][j][len(report[i][j])-5:] == 'Frost':
                report[i][j] = report[i][j][:len(report[i][j])-5] + '-Frost'
            elif report[i][j][len(report[i][j])-7:] == 'Altered':
                report[i][j] = report[i][j][:len(report[i][j])-7] + '-Altered'
            elif report[i][j][len(report[i][j])-7:] == 'Defense':
                report[i][j] = report[i][j][:len(report[i][j])-7] + '-Defense'
            elif report[i][j][len(report[i][j])-5:] == 'Large':
                report[i][j] = report[i][j][:len(report[i][j])-5] + '-Large'
            elif report[i][j][len(report[i][j])-4:] == 'Heat':
                report[i][j] = report[i][j][:len(report[i][j])-4] + '-Heat'
            elif report[i][j][len(report[i][j])-4:] == 'Wash':
                report[i][j] = report[i][j][:len(report[i][j])-4] + '-Wash'
            elif report[i][j][len(report[i][j])-5:] == 'Small':
                report[i][j] = report[i][j][:len(report[i][j])-5] + '-Small'
            elif report[i][j][len(report[i][j])-5:] == 'Trash':
                report[i][j] = report[i][j][:len(report[i][j])-5] + '-Trash'
            elif report[i][j][len(report[i][j])-5:] == 'White':
                report[i][j] = report[i][j][:len(report[i][j])-5] + '-White'
            elif report[i][j][len(report[i][j])-5:] == 'Plant':
                report[i][j] = report[i][j][:len(report[i][j])-5] + '-Plant'
            elif report[i][j][len(report[i][j])-5:] == 'Sandy':
                report[i][j] = report[i][j][:len(report[i][j])-5] + '-Sandy'
            elif report[i][j][len(report[i][j])-5:] == 'Super':
                report[i][j] = report[i][j][:len(report[i][j])-5] + '-Super'
            elif report[i][j][len(report[i][j])-6:] == 'Female':
                report[i][j] = report[i][j][:len(report[i][j])-6] + '-Female'
            elif report[i][j][len(report[i][j])-6:] == 'Normal':
                report[i][j] = report[i][j][:len(report[i][j])-6] + '-Normal'
            elif report[i][j][len(report[i][j])-7:] == 'Average':
                report[i][j] = report[i][j][:len(report[i][j])-7] + '-Average'
            elif report[i][j][len(report[i][j])-6:] == 'Shield':
                report[i][j] = report[i][j][:len(report[i][j])-6] + '-Shield'
            elif report[i][j][len(report[i][j])-7:] == 'Therian':
                report[i][j] = report[i][j][:len(report[i][j])-7] + '-Therian'
            elif report[i][j][len(report[i][j])-8:] == 'Resolute':
                report[i][j] = report[i][j][:len(report[i][j])-8] + '-Resolute'
            elif report[i][j][len(report[i][j])-8:] == 'Standard':
                report[i][j] = report[i][j][:len(report[i][j])-8] + '-Standard'
            elif report[i][j][len(report[i][j])-8:] == 'Ordinary':
                report[i][j] = report[i][j][:len(report[i][j])-8] + '-Ordinary'
            elif report[i][j][len(report[i][j])-4:] == 'Land':
                report[i][j] = report[i][j][:len(report[i][j])-4] + '-Land'
            elif report[i][j][len(report[i][j])-9:] == 'Incarnate':
                report[i][j] = report[i][j][:len(report[i][j])-9] + '-Incarnate'
            elif report[i][j][len(report[i][j])-9:] == 'Pirouette':
                report[i][j] = report[i][j][:len(report[i][j])-9] + '-Pirouette'
            elif report[i][j] == 'Farfetch\'d':
                report[i][j] = 'Farfetchd'
            elif report[i][j] == 'Mr.':
                report[i][j] = 'Mr-Mime'
            elif report[i][j] == 'Jr.':
                report[i][j] = 'Mime-Jr'

    return render(request, 'evo/evo.html', {'report': report})
