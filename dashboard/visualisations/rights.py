import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def right(df_adlib):
    matplotlib.use('SVG')
    aantal_records = df_adlib['objectnummer'].value_counts().sum()

    #rights present/missing

    rights_missing = df_adlib['rechten.type'].isna().sum()
    rights_present = aantal_records-rights_missing

    rights_label = ['aanwezig', 'afwezig']
    rights_pm = [rights_present, rights_missing]

    plt.pie(rights_pm, labels=rights_label)
    plt.title('License Present / License Missing')
    plt.tight_layout()

    bufferRightsPM = BytesIO()
    plt.savefig(bufferRightsPM, format='png')
    bufferRightsPM.seek(0)
    imageRightsPM_png = bufferRightsPM.getvalue()
    bufferRightsPM.close()
    graphRightsPM = base64.b64encode(imageRightsPM_png)
    graphRightsPM = graphRightsPM.decode('utf-8')
    plt.close()

    rightspm = {'rechten': rights_label, 'aantal': rights_pm}
    df_rightspm = pd.DataFrame(rightspm)
    df_rightspm['% of collection'] = ((df_rightspm['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_rightspm = df_rightspm.to_html()

    #rights

    licenses = ['PUBLIC DOMAIN', 'CC-BY-NC 4.0', 'CC-BY-SA 4.0', 'CC0', 'IN COPYRIGHT - NON-COMMERCIAL USE PERMITTED', 'IN COPYRIGHT', 'IN COPYRIGHT - UNKNOWN RIGHTSHOLDER']

    aantal_licentie = []
    for licentie in licenses:
        aantal = df_adlib['rechten.type'].str.contains(licentie).sum()
        aantal_licentie.append(aantal)
    
    aantal_licentie[5] = aantal_licentie[5] - aantal_licentie[4] - aantal_licentie[6]
    
    plt.barh(licenses, aantal_licentie, height=0.4)
    plt.title('Number of records / License')
    plt.tight_layout()
    bufferRights = BytesIO()
    plt.savefig(bufferRights, format='png')
    bufferRights.seek(0)
    imageRights_png = bufferRights.getvalue()
    bufferRights.close()
    graphRights = base64.b64encode(imageRights_png)
    graphRights = graphRights.decode('utf-8')
    plt.close()

    rights = {'license': licenses, 'aantal': aantal_licentie}
    df_rights = pd.DataFrame(rights)
    df_rights['% of collection'] = ((df_rights['aantal'] / aantal_records)*100).round(2).astype(str) + ' %'
    html_rights = df_rights.to_html()

    return(graphRights, html_rights, graphRightsPM, html_rightspm)