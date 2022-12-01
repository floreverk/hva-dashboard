import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def registationdata(df_adlib):
    matplotlib.use('SVG')

    #aantal ontbrekende velden
    missing_objectname = df_adlib['objectnaam'].isna().sum()
    missing_titel = df_adlib['titel'].isna().sum()
    missing_associatie = df_adlib['associatie.onderwerp'].isna().sum()
    missing_image = df_adlib['reproductie.referentie'].isna().sum()
    aantal_records = df_adlib['objectnummer'].value_counts().sum()

    labels = ['objectnaam', 'titel', 'associatie', 'afbeelding']
    missing = [missing_objectname, missing_titel, missing_associatie, missing_image]
    
    plt.bar(labels, missing, width=0.4)
    plt.title('Number of records missing / Field')
    plt.xticks(rotation=90)

    plt.tight_layout()
    bufferMissing = BytesIO()
    plt.savefig(bufferMissing, format='png')
    bufferMissing.seek(0)
    imageMissing_png = bufferMissing.getvalue()
    bufferMissing.close()
    graphMissing = base64.b64encode(imageMissing_png)
    graphMissing = graphMissing.decode('utf-8')
    plt.close()

    fieldsmissing = {'veld': labels, 'aantal ontbrekende': missing}
    df_ok = pd.DataFrame(fieldsmissing)
    df_ok['% of collection'] = ((df_ok['aantal ontbrekende'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_fm = df_ok.to_html()

    #aantal ontbrekende velden basisregistratie per record (0-4)
    #reproductie referentie
    aantalvelden = []
    columns = ['associatie.onderwerp', 'titel', 'objectnaam', 'reproductie.referentie']
    df_aantal = df_adlib[columns]
    df_aantal = df_aantal.fillna(0)
    for index, row in df_aantal.iterrows():
        if row['objectnaam'] == 0:
            value = 1
        else:
            value = 0
        
        if row['titel'] == 0:
            value1 = 1
        else:
            value1 = 0

        if row['associatie.onderwerp'] == 0:
            value2 = 1
        else:
            value2 = 0
        
        if row['reproductie.referentie'] == 0:
            value3 = 1
        else:
            value3 = 0

        aantal = value + value1 + value2 + value3
        aantalvelden.append(aantal)

    ontbrekende_velden = [aantalvelden.count(1), aantalvelden.count(2), aantalvelden.count(3), aantalvelden.count(4)]
    labelsmissing = ['een veld', 'twee velden', 'drie velden', 'vier velden'] 

    plt.bar(labelsmissing, ontbrekende_velden, width=0.4)
    plt.title('Number of records / Number of Fields (basisregistratie) missing')
    plt.xticks(rotation=90)

    plt.tight_layout()
    bufferFields = BytesIO()
    plt.savefig(bufferFields, format='png')
    bufferFields.seek(0)
    imageFields_png = bufferFields.getvalue()
    bufferFields.close()
    graphFields = base64.b64encode(imageFields_png)
    graphFields = graphFields.decode('utf-8')
    plt.close()

    fieldsmissing = {'ontbrekende velden': labelsmissing, 'aantal': ontbrekende_velden}
    df_mf = pd.DataFrame(fieldsmissing)
    df_mf['% of collection'] = ((df_mf['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_mf = df_mf.to_html()

    return(graphMissing, graphFields, html_fm, html_mf)