import xml.etree.ElementTree as et 
import re
import sys
import pandas 
import pandas as pd 
import json
##from pandas.io.json import json_normalize
import os, sys

# Made by Louis le boss
class ExtendedObject:
    def __init__(self, ext_obj_entry):
        self.PerceivedObjectID = ext_obj_entry.get("PerceivedObjectID")
        self.Xcoordinate = ext_obj_entry.get("Xcoordinate")
        self.Ycoordinate = ext_obj_entry.get("Ycoordinate")
        self.Velocity = ext_obj_entry.get("Velocity")

    def __str__(self):
        return f"PerceivedObjectID: {self.PerceivedObjectID}, X: {self.Xcoordinate}, Y: {self.Ycoordinate}, Velocity: {self.Velocity}"


class DataObject:
    def __init__(self, entry):
        self.id = entry.get("myStationId")
        self.timestamps = entry.get("timestamp")
        self.x = entry.get("Xegosumoposition")
        self.y = entry.get("Yegopsumoposition")
        self.extended_objects = self.extract_extended_objects(entry)

    def extract_extended_objects(self, entry):
        extended_objects = []
        for ext_obj_entry in entry.get("Extended_Perceived_Objects", []):
            ext_obj = ExtendedObject(ext_obj_entry)
            extended_objects.append(ext_obj)
        return extended_objects

    def __str__(self):
        return f"id: {self.id}, Timestamps: {self.timestamps}, X: {self.x}, Y: {self.y}, Extended Objects: {self.extended_objects}"
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

with open('C:\\Users\\Louis\\Downloads\\miiproet_1_2\\ExtendedPerception\\Genuine\\extp_attackrate_0.100000_807.json', 'r') as file:
    data = json.load(file)
result=[]

for entry in data.get("EP", []):
    result+=[DataObject(entry)]



print(str(result[0].extended_objects))