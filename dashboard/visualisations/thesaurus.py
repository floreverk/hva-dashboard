import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from matplotlib import font_manager

df_thesaurus = pd.read_csv(r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\data\thesaurus.csv', delimiter=';')

def thesaurus():
    aantal_records = df_thesaurus['term'].value_counts().sum()
    status = ['descriptor', 'non-descriptor', 'niet gedefinieerd']

    descriptor = df_thesaurus['term.status'].str.contains('descriptor').sum() - df_thesaurus['term.status'].str.contains('non-descriptor').sum()
    nondescriptor = df_thesaurus['term.status'].str.contains('non-descriptor').sum()
    nietgedefinieerd = df_thesaurus['term.status'].str.contains('niet gedefinieerd').sum()

    aantal_status = [descriptor, nondescriptor, nietgedefinieerd]

    font_dirs = [r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\fonts']
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        font_manager.fontManager.addfont(font_file)
    plt.style.use("Solarize_Light2")
    plt.rcParams['font.family'] = 'Dosis'
    plt.bar(status, aantal_status, width=0.4)
    plt.title('Number / Status')
    plt.tight_layout()

    bufferstatus = BytesIO()
    plt.savefig(bufferstatus, format='png')
    bufferstatus.seek(0)
    imagestatus_png = bufferstatus.getvalue()
    bufferstatus.close()
    graphStatus = base64.b64encode(imagestatus_png)
    graphStatus = graphStatus.decode('utf-8')
    plt.close()

    statussen = {'status': status, 'aantal': aantal_status}
    df_status = pd.DataFrame(statussen)
    df_status['% of thesaurus'] = ((df_status['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_status = df_status.to_html()

    external_authority = ['wikidata', 'erfgoed', 'aat', 'tgn']
    aantal_ea = []
    for authority in external_authority:
        aantal = df_thesaurus['bron'].str.contains(authority).sum()
        aantal_ea.append(aantal)
    ontbrekende_ea = aantal_records - sum(aantal_ea)
    external_authority.append('geen externe authoriteit')
    aantal_ea.append(ontbrekende_ea)

    plt.barh(external_authority, aantal_ea, height=0.4)
    plt.title('Number / External Authority')
    plt.xticks(rotation=90)
    plt.tight_layout()

    bufferea = BytesIO()
    plt.savefig(bufferea, format='png')
    bufferea.seek(0)
    imageea_png = bufferea.getvalue()
    bufferea.close()
    graphEa = base64.b64encode(imageea_png)
    graphEa = graphEa.decode('utf-8')
    plt.close()

    ea = {'External Authority': external_authority, 'aantal': aantal_ea}
    df_ea = pd.DataFrame(ea)
    df_ea['% of thesaurus'] = ((df_ea['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_ea = df_ea.to_html()

    soort_term = ['afmeting', 'collectie', 'eenheid', 'gebeurtenis', 'geografisch trefwoord', 'materiaal', 'objectcategorie', 'objectnaam', 'onderwerp', 'periode', 'plaats', 'rechten', 'rol', 'techniek', 'toestand', 'type objectnaam', 'verwervingsmethode']

    aantal_soort = []
    for soort in soort_term:
        aantal = df_thesaurus['term.soort'].str.contains(soort).sum()
        aantal_soort.append(aantal)

    plt.barh(soort_term, aantal_soort, height=0.4)
    plt.title('Number / Type')
    plt.xticks(rotation=90)
    plt.tight_layout()

    buffersoort = BytesIO()
    plt.savefig(buffersoort, format='png')
    buffersoort.seek(0)
    imagesoort_png = buffersoort.getvalue()
    buffersoort.close()
    graphSoort = base64.b64encode(imagesoort_png)
    graphSoort = graphSoort.decode('utf-8')
    plt.close()

    st = {'Type of term': soort_term, 'aantal': aantal_soort}
    df_soort = pd.DataFrame(st)
    df_soort['% of thesaurus'] = ((df_soort['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_soort = df_soort.to_html()

    return(aantal_records, graphStatus, html_status, graphEa, html_ea, graphSoort, html_soort)
