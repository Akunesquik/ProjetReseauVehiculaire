import xml.etree.ElementTree as et 
import re
import sys
import pandas 
import pandas as pd 
import json
##from pandas.io.json import json_normalize
import os, sys

# Made by Louis
class ExtendedObject:
    def __init__(self, ext_obj_entry):
        self.PerceivedObjectID = ext_obj_entry.get("PerceivedObjectID")
        self.Xcoordinate = ext_obj_entry.get("Xcoordinate")
        self.Ycoordinate = ext_obj_entry.get("Ycoordinate")
        self.Velocity = ext_obj_entry.get("Velocity")

    def __str__(self):
        return f"PerceivedObjectID: {self.PerceivedObjectID}, X: {self.Xcoordinate}, Y: {self.Ycoordinate}, Velocity: {self.Velocity}"


class DataObject:
    def __init__(self, data_entry):
        self.id = data_entry.get("myStationId")
        self.timestamps = [entry.get("timestamp") for entry in data_entry.get("EP", [])]
        self.x = data_entry.get("Xegosumoposition")
        self.y = data_entry.get("Yegopsumoposition")
        self.extended_objects = self.extract_extended_objects(data_entry)

    def extract_extended_objects(self, entry):
        extended_objects = []
        for ext_obj_entry in entry.get("Extended_Perceived_Objects", []):
            ext_obj = ExtendedObject(ext_obj_entry)
            extended_objects.append(ext_obj)
        return extended_objects

    def __str__(self):
        return f"Classe: {self.id}, Timestamps: {self.timestamps}, X: {self.x}, Y: {self.y}, Extended Objects: {self.extended_objects}"
# Il a crée deux classes

""" xtree = et.parse('IRTSystemX.net.xml')
root = xtree.getroot()

df_cols = ["idjunc", "typejunc", "xjunc", "yjunc", "incLanes", "intLanes"]
rows = []

for element in root.iter(tag='junction'):
    
    idjunc = element.attrib['id']
        
    typejunc = element.attrib['type']
    posx = element.attrib['x']
    posy = element.attrib['y']
    inclanejunc = element.attrib['incLanes']
    inclanejunc = list(inclanejunc.split())
    intlanejunc = element.attrib['intLanes']
    intlanejunc = list(intlanejunc.split())
    rows.append({"idjunc": idjunc, "typejunc": typejunc, "xjunc":posx , "yjunc":posy,
                 "incLanes": inclanejunc, "intLanes": intlanejunc})
    junction_df = pd.DataFrame(rows, columns = df_cols)

        #juncID = junction.text
        #print (juncID, end=' ')
        #for junction in element.iter():
            #junctionID = junction.text
            #if (junction.tag=='junction'):
                #print (junction.text)
print (junction_df) """

###################################################################################################################################
"""
with open('C:\\Users\\Louis\\Downloads\\miiproet_1_2\\ExtendedPerception\\Genuine\\extp_attackrate_0.100000_807.json', 'r') as file:
    data = json.load(file)

result=[]

# Vérifier si la clé "EP" existe dans le JSON
if "EP" in data:
    # Parcourir chaque objet dans la liste "EP"
    for entry in data["EP"]:
        # Vérifier si la clé "timestamp" existe dans l'objet
        timestamps.append(entry["timestamp"])


print(timestamps)"""