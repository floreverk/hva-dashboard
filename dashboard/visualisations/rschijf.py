import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from matplotlib import font_manager

df_rschijf = pd.read_excel(r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\data\rschijf.xlsx')
df_adlib = pd.read_csv(r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\data\adlib.csv', delimiter=';', low_memory=False)


def rschijf():

    number_of_files_on_rschijf = df_rschijf['Bestandsnaam'].value_counts().sum()

    extensies = ['.tif', '.jpg', '.wav', '.aif', '.mp3', '.aiff', '.mp4', '.png', '.mov', '.jpeg', '.tiff', '.avi', '.dng']

    aantal_extensie1 = []
    for extensie in extensies:
        aantal = df_rschijf['Extensie'].str.contains(extensie).sum()
        aantal_extensie1.append(aantal)

    extensies2 = ['.TIF', '.JPG', '.WAV', '.AIF', '.MP3', '.AIFF', '.MP4', '.PNG', '.MOV', '.JPEG', '.TIFF', '.AVI', '.DNG']

    aantal_extensie2 = []
    for extensie in extensies2:
        aantal = df_rschijf['Extensie'].str.contains(extensie).sum()
        aantal_extensie2.append(aantal)
    
    aantal_extensie = [x + y for (x, y) in zip(aantal_extensie1, aantal_extensie2)] 

    plt.bar(extensies, aantal_extensie, width=0.4)
    plt.title('Number of files / Extension')
    plt.tight_layout()

    bufferextensions = BytesIO()
    plt.savefig(bufferextensions, format='png')
    bufferextensions.seek(0)
    imageextensions_png = bufferextensions.getvalue()
    bufferextensions.close()
    graphExtensions = base64.b64encode(imageextensions_png)
    graphExtensions = graphExtensions.decode('utf-8')
    plt.close()

    extensions = {'extensions': extensies, 'aantal': aantal_extensie}
    df_extensies = pd.DataFrame(extensions)
    df_extensies['%'] = ((df_extensies['aantal'] / df_extensies['aantal'].sum())*100).round(2).astype(str) + ' %'
    html_extensies = df_extensies.to_html()

    mappen = ['WERKMAP', 'OBJECTCOLLECTIE', 'FOTOCOLLECTIE', 'EXTERNE SCHIJVEN', 'DOCUMENTAIRE COLLECTIE', 'DIGITALE COLLECTIE', 'AUDIOVISUELE DRAGERS']

    aantal_map = []
    for map in mappen:
        aantal = df_rschijf['Pad'].str.contains(map).sum()
        aantal_map.append(aantal)

    plt.bar(mappen, aantal_map, width=0.4)
    plt.title('Number of files / directory')
    plt.xticks(rotation=90)
    plt.tight_layout()

    buffermap = BytesIO()
    plt.savefig(buffermap, format='png')
    buffermap.seek(0)
    imagemap_png = buffermap.getvalue()
    buffermap.close()
    graphMap = base64.b64encode(imagemap_png)
    graphMap = graphMap.decode('utf-8')
    plt.close()

    maps = {'Directory': mappen, 'aantal': aantal_map}
    df_map = pd.DataFrame(maps)
    df_map['%'] = ((df_map['aantal'] / df_map['aantal'].sum())*100).round(2).astype(str) + ' %'
    html_map = df_map.to_html()

    return(number_of_files_on_rschijf, graphExtensions, html_extensies, graphMap, html_map)