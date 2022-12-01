from django.shortcuts import render
from .visualisations import collection, rights, registration, depot, publication, rschijf, thesaurus, bugsvis
from .models import imagerequest, bugs
from .forms import graphForm, Imageform, checkForm, Bugsform, rschijfForm
import pandas as pd
from .qualitychecks import rq, rt

# Create your views here.
def home(request):
    return render(request, 'home.html')

def collectiondash(request):
    df_adlib = pd.read_csv(r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\data\adlib.csv', delimiter=';', low_memory=False)
    if request.method == 'POST':
        form = graphForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['associatie'] == True:
                filter_term = form.cleaned_data['filter_term']
                df_adlib = df_adlib[(df_adlib['associatie.onderwerp'].str.contains(filter_term, na=False))]
                if df_adlib['objectnummer'].value_counts().sum() == 0:
                    return render(request, 'error/asso.html')
                else:
                    aantal_records, graphDates, graphOk, html_dates, html_ok, graphDatesPM, html_datespm, graphOn, html_on, graphLevensfasen, html_lf, graphJaarkalender, html_jk, graphVrijetijd, html_vt, graphDagelijksleven, html_dl = collection.collections(df_adlib)
                    graphMissing, graphFields, html_fm, html_mf = registration.registationdata(df_adlib)
                    graphRights, html_rights, graphRightsPM, html_rightspm = rights.right(df_adlib)
                    graphDepot, html_depot, graphStandplaats, html_standplaats, graphStandplaatsOk, html_standplaatsok = depot.depot(df_adlib)
                    graphPublication, html_publication = publication.publication(df_adlib)

                    return render(request, 'dashboards/assographs.html', {'filter_term': filter_term, 'aantal_records': aantal_records, 'graphDates':graphDates, 'graphOk': graphOk, 'html_dates': html_dates, 'html_ok': html_ok, 'graphDatesPM': graphDatesPM, 'html_datespm': html_datespm, 'graphOn': graphOn, 'html_on': html_on, 'graphLevensfasen': graphLevensfasen, 'html_lf': html_lf, 'graphJaarkalender': graphJaarkalender, 'html_jk': html_jk, 'graphVrijetijd': graphVrijetijd, 'html_vt': html_vt, 'graphDagelijksleven': graphDagelijksleven, 'html_dl': html_dl, 'graphMissing': graphMissing, 'graphFields': graphFields, 'html_fm': html_fm, 'html_mf': html_mf, 'graphRights':graphRights, 'html_rights': html_rights, 'graphRightsPM': graphRightsPM, 'html_rightspm': html_rightspm, 'graphDepot': graphDepot, 'html_depot': html_depot, 'graphStandplaats': graphStandplaats, 'html_standplaats': html_standplaats, 'graphStandplaatsOk': graphStandplaatsOk, 'html_standplaatsok': html_standplaatsok, 'graphPublication': graphPublication, 'html_publication': html_publication})
                
            elif form.cleaned_data['onder_kenm'] == True:
                ok = form.cleaned_data['ok']
                df_adlib = df_adlib[(df_adlib['onderscheidende_kenmerken'] == ok)]
                # add if df_adlib = empty -> error else continue
                aantal_records, graphDates, graphOk, html_dates, html_ok, graphDatesPM, html_datespm, graphOn, html_on, graphLevensfasen, html_lf, graphJaarkalender, html_jk, graphVrijetijd, html_vt, graphDagelijksleven, html_dl = collection.collections(df_adlib)
                graphMissing, graphFields, html_fm, html_mf = registration.registationdata(df_adlib)
                graphRights, html_rights, graphRightsPM, html_rightspm = rights.right(df_adlib)
                graphDepot, html_depot, graphStandplaats, html_standplaats, graphStandplaatsOk, html_standplaatsok = depot.depot(df_adlib)
                graphPublication, html_publication = publication.publication(df_adlib)
            
            #elif 
                #  forms fieldfield or fileinput
                #  df_file = pd_read_csv(form.cleaned_data['csv'])
                # compare with adlib - have new df_adlib continue same as before!
                
                return render(request, 'dashboards/okgraphs.html', {'filter_term': ok, 'aantal_records': aantal_records, 'graphDates':graphDates, 'graphOk': graphOk, 'html_dates': html_dates, 'html_ok': html_ok, 'graphDatesPM': graphDatesPM, 'html_datespm': html_datespm, 'graphOn': graphOn, 'html_on': html_on, 'graphLevensfasen': graphLevensfasen, 'html_lf': html_lf, 'graphJaarkalender': graphJaarkalender, 'html_jk': html_jk, 'graphVrijetijd': graphVrijetijd, 'html_vt': html_vt, 'graphDagelijksleven': graphDagelijksleven, 'html_dl': html_dl, 'graphMissing': graphMissing, 'graphFields': graphFields, 'html_fm': html_fm, 'html_mf': html_mf, 'graphRights':graphRights, 'html_rights': html_rights, 'graphRightsPM': graphRightsPM, 'html_rightspm': html_rightspm, 'graphDepot': graphDepot, 'html_depot': html_depot, 'graphStandplaats': graphStandplaats, 'html_standplaats': html_standplaats, 'graphStandplaatsOk': graphStandplaatsOk, 'html_standplaatsok': html_standplaatsok, 'graphPublication': graphPublication, 'html_publication': html_publication})
            else:
                return render(request, 'error/form.html')

    form = graphForm
    aantal_records, graphDates, graphOk, html_dates, html_ok, graphDatesPM, html_datespm, graphOn, html_on, graphLevensfasen, html_lf, graphJaarkalender, html_jk, graphVrijetijd, html_vt, graphDagelijksleven, html_dl = collection.collections(df_adlib)
    graphMissing, graphFields, html_fm, html_mf = registration.registationdata(df_adlib)
    graphRights, html_rights, graphRightsPM, html_rightspm = rights.right(df_adlib)
    graphDepot, html_depot, graphStandplaats, html_standplaats, graphStandplaatsOk, html_standplaatsok = depot.depot(df_adlib)
    graphPublication, html_publication = publication.publication(df_adlib)

    return render(request, 'dashboards/collection.html', {'form':form, 'aantal_records': aantal_records, 'graphDates':graphDates, 'graphOk': graphOk, 'html_dates': html_dates, 'html_ok': html_ok, 'graphDatesPM': graphDatesPM, 'html_datespm': html_datespm, 'graphOn': graphOn, 'html_on': html_on, 'graphLevensfasen': graphLevensfasen, 'html_lf': html_lf, 'graphJaarkalender': graphJaarkalender, 'html_jk': html_jk, 'graphVrijetijd': graphVrijetijd, 'html_vt': html_vt, 'graphDagelijksleven': graphDagelijksleven, 'html_dl': html_dl, 'graphMissing': graphMissing, 'graphFields': graphFields, 'html_fm': html_fm, 'html_mf': html_mf, 'graphRights':graphRights, 'html_rights': html_rights, 'graphRightsPM': graphRightsPM, 'html_rightspm': html_rightspm, 'graphDepot': graphDepot, 'html_depot': html_depot, 'graphStandplaats': graphStandplaats, 'html_standplaats': html_standplaats, 'graphStandplaatsOk': graphStandplaatsOk, 'html_standplaatsok': html_standplaatsok, 'graphPublication': graphPublication, 'html_publication': html_publication})

def bugsdash(request):
    graphMonth, graphBug, graphRoom, graphRoommonth, graphRoomtype = bugsvis.bugsvis()
    return render(request, 'dashboards/bugs.html', {'graphMonth': graphMonth, 'graphBug': graphBug, 'graphRoom': graphRoom, 'graphRoommonth': graphRoommonth, 'graphRoomtype': graphRoomtype})

def studiodash(request):
    return render(request, 'dashboards/studio.html')

def thesauridash(request):
    aantal_records, graphStatus, html_status, graphEa, html_ea, graphSoort, html_soort = thesaurus.thesaurus()
    return render(request, 'dashboards/thesauri.html', {'aantal_records': aantal_records, 'graphStatus': graphStatus, 'html_status': html_status, 'graphEa': graphEa, 'html_ea': html_ea, 'graphSoort': graphSoort, 'html_soort': html_soort})

def rschijfdash(request):
    number_of_files_on_rschijf, graphExtensions, html_extensies, graphMap, html_map = rschijf.rschijf()
    return render(request, 'dashboards/rschijf.html', {'number_of_files_on_rschijf': number_of_files_on_rschijf, 'graphExtensions': graphExtensions, 'html_extensies': html_extensies, 'graphMap': graphMap, 'html_map': html_map})

def registrationquality(request):
    df_adlib = pd.read_csv(r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\data\adlib.csv', delimiter=';', low_memory=False)
    if request.method == 'POST':
        form = checkForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['association'] == True:
                filter_term = form.cleaned_data['filterterm']
                df_adlib = df_adlib[(df_adlib['associatie.onderwerp'].str.contains(filter_term, na=False))]
                if df_adlib['objectnummer'].value_counts().sum() == 0:
                    return render(request, 'error/registration.html')
                else:
                    filter_term = form.cleaned_data['filterterm']
                    df_adlib = df_adlib[(df_adlib['associatie.onderwerp'].str.contains(filter_term, na=False))]
                    response = rq.rq(df_adlib)
                    return response
            if form.cleaned_data['full_collection'] == True:
                response = rq.rq(df_adlib)
                return response
    form = checkForm
    return render(request, 'qualitychecks/registrationcheck.html', {'form':form})

def rightsquality(request):
    return render(request, 'qualitychecks/rightscheck.html')

def thesauriquality(request):
    return render(request, 'qualitychecks/thesauricheck.html')

def thesauruscheck(request):
    df_thesaurus = pd.read_csv(r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\data\thesaurus.csv', delimiter=';')
    response = rt.rt(df_thesaurus)
    return response

def rschijfquality(request):
    return render(request, 'qualitychecks/rschijfcheck.html')

def registrationmanual(request):
    return render(request, 'manuals/registrationmanual.html')

def rightsmanual(request):
    return render(request, 'manuals/rightsmanual.html')

def faq(request):
    return render(request, 'manuals/faq.html')

def studiodatabase(request):
    all_requests = imagerequest.objects.all
    if request.method == 'POST':
        form = Imageform(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'databases/studio.html', {'all': all_requests, 'form':form})
    else:
        form = Imageform()
    return render(request, 'databases/studio.html', {'all': all_requests, 'form':form})

def bugsdatabase(request):
    all_requests = bugs.objects.all
    if request.method == 'POST':
        form = Bugsform(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'databases/bugs.html', {'all': all_requests, 'form':form})
    else:
        form = Bugsform()
    return render(request, 'databases/bugs.html', {'all': all_requests, 'form':form})

def rschijftool(request):
    df_rschijf = pd.read_excel(r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\data\rschijf.xlsx')
    if request.method == 'POST':
        form = rschijfForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['objectnumber'] == True:
                objectnummer = form.cleaned_data['objectnumber']
                df_rschijf = df_rschijf[df_rschijf['Objectnummer'].str.contains(objectnummer, na=False)]
                if df_rschijf['Objectnummer'].value_counts().sum() == 0:
                    return render(request, 'error/registration.html')
                else:
                    padnaam = df_rschijf['Pad'].iat[0]
                    return render(request, 'tools/rschijf.html', {'form':form, 'padnaam': padnaam})
            else:
                return render(request, 'error/registration.html')
    form = rschijfForm
    return render(request, 'tools/rschijf.html', {'form':form})

def assotool(request):
    return render(request, 'tools/assos.html')