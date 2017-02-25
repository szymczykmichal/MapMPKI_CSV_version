import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
from isoweek import Week
import isoweek


#############
df_Tab = pd.read_csv('KPI.csv', sep=';', encoding='cp1250')
df_Tab.columns=['nazwa_interwalu','MBO','ranking','mRegion','regionId', 'Ranking_Grupa', 'Colour']

#############
svg_input = open("Mapa.svg", "r", encoding="utf-8")

tree = ET.parse(svg_input)
root = tree.getroot()
for child in root:
    mRegion_name = child.attrib['id']
    if(mRegion_name in df_Tab['mRegion'].values):
        _row = df_Tab.loc[df_Tab['mRegion'] == mRegion_name]
        s=child.attrib['style']
        d = [ ( elem.split(':')[0], elem.split(':')[1] ) for elem in s.split(';') ]
        child_dict = dict(d)
        # print(_row['mRegion']+': '+child_dict['fill']+' -> '+str(_row['Colour']))
        child.attrib['style'] = child.attrib['style'].replace(child_dict['fill'], _row.iloc[0]['Colour'])
tree.write('Mapa_'+df_Tab.iloc[0]['nazwa_interwalu']+'.svg')

svg_input.closed