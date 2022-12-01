import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
from matplotlib import font_manager

df_bugs = pd.read_excel(r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\data\beestjes.xlsx')

def bugsvis():
    font_dirs = [r'C:\Users\Verkesfl\OneDrive - Groep Gent\Documenten\Documenten\COGHENT\code\hva-dashboard\dashboard\static\fonts']
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        font_manager.fontManager.addfont(font_file)

    months = ['2022-05', '2022-06', '2022-07', '2022-09']
    types = ['spin', 'mot', 'vlieg', 'kleermot', 'fruitvlieg', 'mug', 'pissebed', 'vliegende mier']
    rooms = ['opstaan', 'geboorte', 'verhuizen', 'rustdag', '(on)geluk', 'rouwen', 'ouder', 'trappenhal', 'jong', 'vakantie', 'school', 'trouw', 'avond', 'huishouden', 'spelen']

    df_bugs['Datum'] = df_bugs['Datum'].astype(str)

    number_month = []
    for month in months:
        df_bugs_months = df_bugs[df_bugs['Datum'].str.contains(month)]
        value = df_bugs_months['Aantal'].sum()
        number_month.append(value)

    plt.style.use("Solarize_Light2")
    plt.rcParams['font.family'] = 'Dosis'
    plt.bar(months, number_month, width=0.4)
    plt.title('Number of bugs / Month')
    plt.tight_layout()
    
    buffermonth = BytesIO()
    plt.savefig(buffermonth, format='png')
    buffermonth.seek(0)
    imagemonth_png = buffermonth.getvalue()
    buffermonth.close()
    graphMonth = base64.b64encode(imagemonth_png)
    graphMonth = graphMonth.decode('utf-8')
    plt.close()

    number_bug = []
    for type in types:
        df_bugs_type = df_bugs[df_bugs['Dier'].str.contains(type)]
        value = df_bugs_type['Aantal'].sum()
        number_bug.append(value)

    plt.bar(types, number_bug, width=0.4)
    plt.title('Number of bugs / Type')
    plt.xticks(rotation=90)
    plt.tight_layout()

    bufferbug = BytesIO()
    plt.savefig(bufferbug, format='png')
    bufferbug.seek(0)
    imagebug_png = bufferbug.getvalue()
    bufferbug.close()
    graphBug = base64.b64encode(imagebug_png)
    graphBug = graphBug.decode('utf-8')
    plt.close()

    number_room = []
    for room in rooms:
        df_bugs_room = df_bugs[df_bugs['Kamer'].str.contains(room)]
        value = df_bugs_room['Aantal'].sum()
        number_room.append(value)

    plt.bar(rooms, number_room, width=0.4)
    plt.title('Number of bugs / Room (5 months)')
    plt.xticks(rotation=90)
    plt.tight_layout()

    bufferroom = BytesIO()
    plt.savefig(bufferroom, format='png')
    bufferroom.seek(0)
    imageroom_png = bufferroom.getvalue()
    bufferroom.close()
    graphRoom = base64.b64encode(imageroom_png)
    graphRoom = graphRoom.decode('utf-8')
    plt.close()

    dict = []
    for month in months:
        df_bugs_months = df_bugs[df_bugs['Datum'].str.contains(month)]
        list = []
        for room in rooms:
            df_bugs_room = df_bugs_months[df_bugs_months['Kamer'].str.contains(room)]
            value = df_bugs_room['Aantal'].sum()
            list.append(value)
        dict.append(list)

    mei = dict[0]
    juni = dict[1]
    juli = dict[2]
    september = dict[3]

    barWidth = 0.25

    bars1 = mei
    bars2 = juni
    bars3 = juli
    bars4 = september

    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

    plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='mei')
    plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='juni')
    plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='juli')
    plt.bar(r4, bars4, color='#d3f4a9', width=barWidth, edgecolor='white', label='september')

    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], rooms)
    plt.xticks(rotation=90)

    plt.legend()
    plt.title('Number of bugs / Month / Room')

    bufferroommonth = BytesIO()
    plt.savefig(bufferroommonth, format='png')
    bufferroommonth.seek(0)
    imageroommonth_png = bufferroommonth.getvalue()
    bufferroommonth.close()
    graphRoommonth = base64.b64encode(imageroommonth_png)
    graphRoommonth = graphRoommonth.decode('utf-8')
    plt.close()

    dict = []
    for type in types:
        df_bugs_type = df_bugs[df_bugs['Dier'].str.contains(type)]
        list = []
        for room in rooms:
            df_bugs_room = df_bugs_type[df_bugs_type['Kamer'].str.contains(room)]
            value = df_bugs_room['Aantal'].sum()
            list.append(value)
        dict.append(list)

    spin = dict[0]
    mot = dict[1]
    vlieg = dict[2]
    kleermot = dict[3]

    barWidth = 0.25

    bars1 = spin
    bars2 = mot
    bars3 = vlieg
    bars4 = kleermot

    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

    plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='spin')
    plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='mot')
    plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='vlieg')
    plt.bar(r4, bars4, color='#d3f4a9', width=barWidth, edgecolor='white', label='kleermot')

    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], rooms)
    plt.xticks(rotation=90)

    plt.legend()
    plt.title('Number of bugs / Type / Room')

    bufferroomtype = BytesIO()
    plt.savefig(bufferroomtype, format='png')
    bufferroomtype.seek(0)
    imageroomtype_png = bufferroomtype.getvalue()
    bufferroomtype.close()
    graphRoomtype = base64.b64encode(imageroomtype_png)
    graphRoomtype = graphRoomtype.decode('utf-8')
    plt.close()

    return(graphMonth, graphBug, graphRoom, graphRoommonth, graphRoomtype)


