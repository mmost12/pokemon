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
    report = fix(report)
    return render(request, 'evo/fight.html', {'report': report, 'teams': teams})

def evo(request):
    report = [x.split() for x in test.small()]
    report = fix(report)

    return render(request, 'evo/evo.html', {'report': report})

def fix(l):
    for i in range(len(l)):
        l[i] = [x for x in l[i] if not x[len(x)-4:]=='Mega'
                                          and not x[len(x)-6:]=='Primal'
                                          and not x == 'Forme'
                                          and not x == 'Mode'
                                          and not x == 'Size'
                                          and not x == 'Rotom'
                                          and not x == 'Mime'
                                          and not x == 'X'
                                          and not x == 'Y']
        for j in range(len(l[i])):
            l[i][j] = l[i][j].split()[0]
            if l[i][j][len(l[i][j])-3:] == 'Zen':
                l[i][j] = l[i][j][:len(l[i][j])-3] + '-Zen'
            elif l[i][j][len(l[i][j])-3:] == 'Fan':
                l[i][j] = l[i][j][:len(l[i][j])-3] + '-Fan'
            elif l[i][j][len(l[i][j])-3:] == 'Sky':
                l[i][j] = l[i][j][:len(l[i][j])-3] + '-Sky'
            elif l[i][j][len(l[i][j])-4:] == 'Aria':
                l[i][j] = l[i][j][:len(l[i][j])-4] + '-Aria'
            elif l[i][j][len(l[i][j])-5:] == 'Frost':
                l[i][j] = l[i][j][:len(l[i][j])-5] + '-Frost'
            elif l[i][j][len(l[i][j])-7:] == 'Altered':
                l[i][j] = l[i][j][:len(l[i][j])-7] + '-Altered'
            elif l[i][j][len(l[i][j])-7:] == 'Defense':
                l[i][j] = l[i][j][:len(l[i][j])-7] + '-Defense'
            elif l[i][j][len(l[i][j])-5:] == 'Large':
                l[i][j] = l[i][j][:len(l[i][j])-5] + '-Large'
            elif l[i][j][len(l[i][j])-4:] == 'Heat':
                l[i][j] = l[i][j][:len(l[i][j])-4] + '-Heat'
            elif l[i][j][len(l[i][j])-4:] == 'Wash':
                l[i][j] = l[i][j][:len(l[i][j])-4] + '-Wash'
            elif l[i][j][len(l[i][j])-5:] == 'Small':
                l[i][j] = l[i][j][:len(l[i][j])-5] + '-Small'
            elif l[i][j][len(l[i][j])-5:] == 'Trash':
                l[i][j] = l[i][j][:len(l[i][j])-5] + '-Trash'
            elif l[i][j][len(l[i][j])-5:] == 'White':
                l[i][j] = l[i][j][:len(l[i][j])-5] + '-White'
            elif l[i][j][len(l[i][j])-5:] == 'Plant':
                l[i][j] = l[i][j][:len(l[i][j])-5] + '-Plant'
            elif l[i][j][len(l[i][j])-5:] == 'Sandy':
                l[i][j] = l[i][j][:len(l[i][j])-5] + '-Sandy'
            elif l[i][j][len(l[i][j])-5:] == 'Super':
                l[i][j] = l[i][j][:len(l[i][j])-5] + '-Super'
            elif l[i][j][len(l[i][j])-6:] == 'Female':
                l[i][j] = l[i][j][:len(l[i][j])-6] + '-Female'
            elif l[i][j][len(l[i][j])-6:] == 'Normal':
                l[i][j] = l[i][j][:len(l[i][j])-6] + '-Normal'
            elif l[i][j][len(l[i][j])-7:] == 'Average':
                l[i][j] = l[i][j][:len(l[i][j])-7] + '-Average'
            elif l[i][j][len(l[i][j])-6:] == 'Shield':
                l[i][j] = l[i][j][:len(l[i][j])-6] + '-Shield'
            elif l[i][j][len(l[i][j])-7:] == 'Therian':
                l[i][j] = l[i][j][:len(l[i][j])-7] + '-Therian'
            elif l[i][j][len(l[i][j])-8:] == 'Resolute':
                l[i][j] = l[i][j][:len(l[i][j])-8] + '-Resolute'
            elif l[i][j][len(l[i][j])-8:] == 'Standard':
                l[i][j] = l[i][j][:len(l[i][j])-8] + '-Standard'
            elif l[i][j][len(l[i][j])-8:] == 'Ordinary':
                l[i][j] = l[i][j][:len(l[i][j])-8] + '-Ordinary'
            elif l[i][j][len(l[i][j])-4:] == 'Land':
                l[i][j] = l[i][j][:len(l[i][j])-4] + '-Land'
            elif l[i][j][len(l[i][j])-9:] == 'Incarnate':
                l[i][j] = l[i][j][:len(l[i][j])-9] + '-Incarnate'
            elif l[i][j][len(l[i][j])-9:] == 'Pirouette':
                l[i][j] = l[i][j][:len(l[i][j])-9] + '-Pirouette'
            elif l[i][j] == 'Farfetch\'d':
                l[i][j] = 'Farfetchd'
            elif l[i][j] == 'Mr.':
                l[i][j] = 'Mr-Mime'
            elif l[i][j] == 'Jr.':
                l[i][j] = 'Mime-Jr'

    return l
