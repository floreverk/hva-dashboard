import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from matplotlib import font_manager

def collections(df_adlib):
    matplotlib.use('SVG')
    font_dirs = [r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\fonts']
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        font_manager.fontManager.addfont(font_file)

    #onderscheidende_kenmerken
    onderscheidende_kenmerken = ["OBJECT", "DIGITALE COLLECTIE", "DOCUMENTAIRE COLLECTIE", "BEELD", "TEXTIEL", "AUDIOVISUELE COLLECTIE"]

    aantal_ok = []
    for ok in onderscheidende_kenmerken:
        aantal = df_adlib['onderscheidende_kenmerken'].str.contains(ok).sum()
        aantal_ok.append(aantal)
    
    plt.style.use("Solarize_Light2")
    plt.rcParams['font.family'] = 'Dosis'
    y_pos = [0, 0.7, 1.4, 2.1, 2.8, 3.5]
    plt.barh(y_pos, aantal_ok, height=0.4)
    plt.yticks(y_pos, onderscheidende_kenmerken)
    plt.title('Number of records / Medium')
    plt.tight_layout()

    bufferok = BytesIO()
    plt.savefig(bufferok, format='png')
    bufferok.seek(0)
    imageok_png = bufferok.getvalue()
    bufferok.close()
    graphOk = base64.b64encode(imageok_png)
    graphOk = graphOk.decode('utf-8')
    plt.close()

    ok = {'drager': onderscheidende_kenmerken, 'aantal': aantal_ok}
    df_ok = pd.DataFrame(ok)
    df_ok['% of collection'] = ((df_ok['aantal'] / df_ok['aantal'].sum())*100).round(2).astype(str) + ' %'
    html_ok = df_ok.to_html()

    #digital collection
    objectnummer = ['FO', 'AU', 'F0', 'TK', 'RE', 'DIA', 'DB', 'VI']

    aantal_on = []
    for on in objectnummer:
        aantal = df_adlib['objectnummer'].str.contains(on).sum()
        aantal_on.append(aantal)
    
    plt.bar(objectnummer, aantal_on, width=0.4)
    plt.title('Number of records / Type / Digital Collection')
    plt.xticks(rotation=90)
    plt.tight_layout()

    bufferon = BytesIO()
    plt.savefig(bufferon, format='png')
    bufferon.seek(0)
    imageon_png = bufferon.getvalue()
    bufferon.close()
    graphOn = base64.b64encode(imageon_png)
    graphOn = graphOn.decode('utf-8')
    plt.close()

    ok = {'type digital collection': objectnummer, 'aantal': aantal_on}
    df_on = pd.DataFrame(ok)
    df_on['% of digital collection'] = ((df_on['aantal'] / df_on['aantal'].sum())*100).round(2).astype(str) + ' %'
    html_on = df_on.to_html()
    
    # of dates present

    date_missing = df_adlib['associatie.periode'].isna().sum()
    date_present = df_adlib['objectnummer'].count()-date_missing

    date_label = ['aanwezig', 'afwezig']
    dates_pm = [date_present, date_missing]

    plt.pie(dates_pm, labels=date_label)
    plt.title('Dates Present / Dates Missing')
    plt.tight_layout()

    bufferDatesPM = BytesIO()
    plt.savefig(bufferDatesPM, format='png')
    bufferDatesPM.seek(0)
    imageDatesPM_png = bufferDatesPM.getvalue()
    bufferDatesPM.close()
    graphDatesPM = base64.b64encode(imageDatesPM_png)
    graphDatesPM = graphDatesPM.decode('utf-8')
    plt.close()

    datespm = {'datering': date_label, 'aantal': dates_pm}
    df_datespm = pd.DataFrame(datespm)
    df_datespm['% of collection'] = ((df_datespm['aantal'] / df_datespm['aantal'].sum())*100).round(2).astype(str) + ' %'
    html_datespm = df_datespm.to_html()

    # of records per deccenia
    periodes = ["19de eeuw", "jaren 1890", "jaren 1900", "jaren 1910", "jaren 1920", "jaren 1930", "jaren 1940", "jaren 1950",
                "jaren 1960", "jaren 1970", "jaren 1980", "jaren 1990", "jaren  2000", "jaren 2010"]
    aantal_records = df_adlib['objectnummer'].value_counts().sum()

    aantal_periode = []
    for periode in periodes:
        aantal = df_adlib['associatie.periode'].str.contains(periode).sum()
        aantal_periode.append(aantal)

    plt.bar(periodes, aantal_periode, width=0.4)
    plt.title('Number of records / Deccenia')
    plt.xticks(rotation=90)
    plt.tight_layout()

    bufferDates = BytesIO()
    plt.savefig(bufferDates, format='png')
    bufferDates.seek(0)
    imageDates_png = bufferDates.getvalue()
    bufferDates.close()
    graphDates = base64.b64encode(imageDates_png)
    graphDates = graphDates.decode('utf-8')
    plt.close()

    dates = {'periodes': periodes, 'aantal': aantal_periode}
    df_dates = pd.DataFrame(dates)
    df_dates['% of collection'] = ((df_dates['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_dates = df_dates.to_html()

    #associations

    # levensfasen
    levensfasen = ["geboorte", "onderwijs", "communie", "huwelijk", "dood"]

    aantal_levensfasen = []
    for levensfase in levensfasen:
        aantal = df_adlib['associatie.onderwerp'].str.contains(levensfase).sum()
        aantal_levensfasen.append(aantal)

    plt.bar(levensfasen, aantal_levensfasen, width=0.4)
    plt.title('Number / Association')
    plt.tight_layout()

    bufferlevensfasen = BytesIO()
    plt.savefig(bufferlevensfasen, format='png')
    bufferlevensfasen.seek(0)
    imagelevensfasen_png = bufferlevensfasen.getvalue()
    bufferlevensfasen.close()
    graphLevensfasen = base64.b64encode(imagelevensfasen_png)
    graphLevensfasen = graphLevensfasen.decode('utf-8')
    plt.close()

    lf = {'associatie': levensfasen, 'aantal': aantal_levensfasen}
    df_lf = pd.DataFrame(lf)
    df_lf['% of collection'] = ((df_lf['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_lf = df_lf.to_html()

    # jaarkalender
    jaarkalender = ["nieuwjaarsdag", "valentijnsdag", "carnaval", "1 april", "Pasen", "Moederdag", "Vaderdag", "Sinterklaas", "Kerstmis", "Driekoningen", "verjaardag"]
    
    aantal_jaarkalender = []
    for jaark in jaarkalender:
        aantal = df_adlib['associatie.onderwerp'].str.contains(jaark).sum()
        aantal_jaarkalender.append(aantal)

    plt.barh(jaarkalender, aantal_jaarkalender, height=0.4)
    plt.title('Number / Association')
    plt.tight_layout()

    bufferjaarkalender = BytesIO()
    plt.savefig(bufferjaarkalender, format='png')
    bufferjaarkalender.seek(0)
    imagejaarkalender_png = bufferjaarkalender.getvalue()
    bufferjaarkalender.close()
    graphJaarkalender = base64.b64encode(imagejaarkalender_png)
    graphJaarkalender = graphJaarkalender.decode('utf-8')
    plt.close()

    jk = {'associatie': jaarkalender, 'aantal': aantal_jaarkalender}
    df_jk = pd.DataFrame(jk)
    df_jk['% of collection'] = ((df_jk['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_jk = df_jk.to_html()

    # vrije tijd
    vrije_tijd = ["circus", "kermis", "speelgoed", "sport", "optocht", "poppenspel", "feest", "vakantie"]

    aantal_vrijetijd = []
    for tijd in vrije_tijd:
        aantal = df_adlib['associatie.onderwerp'].str.contains(tijd).sum()
        aantal_vrijetijd.append(aantal)

    plt.barh(vrije_tijd, aantal_vrijetijd, height=0.4)
    plt.title('Number / Association')
    plt.tight_layout()

    buffervrijetijd = BytesIO()
    plt.savefig(buffervrijetijd, format='png')
    buffervrijetijd.seek(0)
    imagevrijetijd_png = buffervrijetijd.getvalue()
    buffervrijetijd.close()
    graphVrijetijd = base64.b64encode(imagevrijetijd_png)
    graphVrijetijd = graphVrijetijd.decode('utf-8')
    plt.close()

    vt = {'associatie': vrije_tijd, 'aantal': aantal_vrijetijd}
    df_vt = pd.DataFrame(vt)
    df_vt['% of collection'] = ((df_vt['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_vt = df_vt.to_html()

    # dagelijks leven
    dagelijks_leven = ["huishouden", "lichaamsverzorging", "mode", "voedsel", "rookwaren"]

    aantal_dagelijksleven = []
    for leven in dagelijks_leven:
        aantal = df_adlib['associatie.onderwerp'].str.contains(leven).sum()
        aantal_dagelijksleven.append(aantal)

    plt.bar(dagelijks_leven, aantal_dagelijksleven, width=0.4)
    plt.title('Number / Association')
    plt.tight_layout()

    bufferdagelijksleven = BytesIO()
    plt.savefig(bufferdagelijksleven, format='png')
    bufferdagelijksleven.seek(0)
    imagedagelijksleven_png = bufferdagelijksleven.getvalue()
    bufferdagelijksleven.close()
    graphDagelijksleven = base64.b64encode(imagedagelijksleven_png)
    graphDagelijksleven = graphDagelijksleven.decode('utf-8')
    plt.close()

    dl = {'associatie': dagelijks_leven, 'aantal': aantal_dagelijksleven}
    df_dl = pd.DataFrame(dl)
    df_dl['% of collection'] = ((df_dl['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_dl = df_dl.to_html()

    return(aantal_records, graphDates, graphOk, html_dates, html_ok, graphDatesPM, html_datespm, graphOn, html_on, graphLevensfasen, html_lf, 
        graphJaarkalender, html_jk, graphVrijetijd, html_vt, graphDagelijksleven, html_dl)

