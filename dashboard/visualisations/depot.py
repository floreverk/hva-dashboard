import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64
from matplotlib import font_manager

def depot(df_adlib):
    matplotlib.use('SVG')
    font_dirs = [r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\fonts']
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

    aantal_records = df_adlib['objectnummer'].value_counts().sum()
    digitale_collectie = df_adlib['onderscheidende_kenmerken'].str.contains('DIGITALE COLLECTIE').sum()

    #rights present/missing

    depot_missing = df_adlib['huidige_standplaats'].isna().sum()-digitale_collectie
    depot_present = aantal_records-depot_missing

    depot_label = ['aanwezig', 'afwezig']
    depot_pm = [depot_present, depot_missing]

    plt.pie(depot_pm, labels=depot_label)
    plt.title('Standplaats Present / Standplaats Missing')
    plt.tight_layout()

    bufferDepot = BytesIO()
    plt.savefig(bufferDepot, format='png')
    bufferDepot.seek(0)
    imageDepot_png = bufferDepot.getvalue()
    bufferDepot.close()
    graphDepot = base64.b64encode(imageDepot_png)
    graphDepot = graphDepot.decode('utf-8')
    plt.close()

    depotpm = {'standplaats': depot_label, 'aantal': depot_pm}
    df_depot = pd.DataFrame(depotpm)
    df_depot['% of collection'] = ((df_depot['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_depot = df_depot.to_html()

    # ok van missing standplaatsen
    df_adlib['huidige_standplaats']=df_adlib['huidige_standplaats'].fillna(0)
    df_missing = df_adlib[(df_adlib['huidige_standplaats'] == 0)]
    
    onderscheidende_kenmerken = ["OBJECT", "DOCUMENTAIRE COLLECTIE", "BEELD", "TEXTIEL", "AUDIOVISUELE COLLECTIE"]

    aantal_ok = []
    for ok in onderscheidende_kenmerken:
        aantal = df_missing['onderscheidende_kenmerken'].str.contains(ok).sum()
        aantal_ok.append(aantal)
    
    plt.style.use("Solarize_Light2")
    plt.rcParams['font.family'] = 'Dosis'
    y_pos = [0, 0.7, 1.4, 2.1, 2.8]
    plt.barh(y_pos, aantal_ok, height=0.4)
    plt.yticks(y_pos, onderscheidende_kenmerken)
    plt.title('Number of records / Missing standplaats / Medium')
    plt.tight_layout()

    bufferokmissing = BytesIO()
    plt.savefig(bufferokmissing, format='png')
    bufferokmissing.seek(0)
    imagestandplaatsok_png = bufferokmissing.getvalue()
    bufferokmissing.close()
    graphStandplaatsOk = base64.b64encode(imagestandplaatsok_png)
    graphStandplaatsOk = graphStandplaatsOk.decode('utf-8')
    plt.close()

    standplaatsok = {'drager': onderscheidende_kenmerken, 'aantal': aantal_ok}
    df_standplaatsok = pd.DataFrame(standplaatsok)
    df_standplaatsok['% of collection'] = (((df_standplaatsok['aantal'] / aantal_records)*100).round(2).astype(str) + ' %')
    html_standplaatsok = df_standplaatsok.to_html()

    # standplaatsen

    standplaats = ['Ghe_', 'ALIJN_']
    df_adlib['huidige_standplaats'] = df_adlib['huidige_standplaats'].replace([0],'0')

    aantal_standplaats = []
    for plaats in standplaats:
        aantal = df_adlib['huidige_standplaats'].str.contains(plaats).sum()
        aantal_standplaats.append(aantal)

    standplaats.append('Andere')
    andere = depot_present-aantal_standplaats[0]-aantal_standplaats[1]
    aantal_standplaats.append(andere)

       
    plt.barh(standplaats, aantal_standplaats, height=0.4)
    plt.title('Number of records / Standplaats')
    plt.tight_layout()
    bufferStandplaats = BytesIO()
    plt.savefig(bufferStandplaats, format='png')
    bufferStandplaats.seek(0)
    imageStandplaats_png = bufferStandplaats.getvalue()
    bufferStandplaats.close()
    graphStandplaats = base64.b64encode(imageStandplaats_png)
    graphStandplaats = graphStandplaats.decode('utf-8')
    plt.close()

    standplaatsen = {'standplaats': standplaats, 'aantal': aantal_standplaats}
    df_standplaats = pd.DataFrame(standplaatsen)
    df_standplaats['% of collection'] = ((df_standplaats['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_standplaats = df_standplaats.to_html()

    return(graphDepot, html_depot, graphStandplaats, html_standplaats, graphStandplaatsOk, html_standplaatsok)