import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def publication(df_adlib):
    matplotlib.use('SVG')
    aantal_records = df_adlib['objectnummer'].value_counts().sum()

    aantal_europeana = df_adlib['webpublicatie'].str.contains('Europeana').sum()
    aantal_erfgoedinzicht = df_adlib['webpublicatie'].str.contains('Erfgoedinzicht').sum()
    aantal_afdeling = df_adlib['afdeling'].value_counts().sum()
    aantal_afvoer = df_adlib['afdeling'].str.contains('afvoer').sum()
    aantal_website = aantal_afdeling-aantal_afvoer

    aantal_publicatie = [aantal_website, aantal_erfgoedinzicht, aantal_europeana]
    labels = ['Website', 'Erfgoedinzicht', 'CoGent']

    plt.bar(labels, aantal_publicatie, width=0.4)
    plt.title('Number of records / Publication')
    plt.xticks(rotation=90)
    plt.tight_layout()

    bufferpublication = BytesIO()
    plt.savefig(bufferpublication, format='png')
    bufferpublication.seek(0)
    imagepublication_png = bufferpublication.getvalue()
    bufferpublication.close()
    graphPublication = base64.b64encode(imagepublication_png)
    graphPublication = graphPublication.decode('utf-8')
    plt.close()

    publications = {'Type Publication': labels, 'aantal': aantal_publicatie}
    df_publication = pd.DataFrame(publications)
    df_publication['% of collection'] = ((df_publication['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_publication = df_publication.to_html()

    return(graphPublication, html_publication)


