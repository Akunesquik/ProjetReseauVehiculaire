import xml.etree.ElementTree as et 
import re
import sys
import pandas 
import pandas as pd 
import json
##from pandas.io.json import json_normalize
import os, sys, json

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
        self.timestamps = data_entry.get("timestamp")
        self.x = data_entry.get("Xegosumoposition")
        self.y = data_entry.get("Yegopsumoposition")
        self.orientation = data_entry.get("orientationangle")
        self.longaccelleration = data_entry.get("longacceleration")
        self.longspeed  = data_entry.get("longspeed")
        self.extended_objects = self.extract_extended_objects(data_entry)

    def extract_extended_objects(self, entry):
        extended_objects = []
        for ext_obj_entry in entry.get("Extended_Perceived_Objects", []):
            ext_obj = ExtendedObject(ext_obj_entry)
            extended_objects.append(ext_obj)
        return extended_objects

    def __str__(self):
        extended_objects_str = f",\n ".join([str(obj) for obj in self.extended_objects])
        return f"\nClasse: {self.id}, Timestamp: {self.timestamps}, X: {self.x}, Y: {self.y},orientation {self.orientation},longaccelleration {self.longaccelleration},longspeed  {self.longspeed }, Extended Objects:\n {extended_objects_str}"


###################################################################################################################################
def traitement_ext_obj(entry):
        extended_objects = []
        for ext_obj_entry in entry.get("Extended_Perceived_Objects", []):
            ext_obj = ExtendedObject(ext_obj_entry)
            extended_objects.append(ext_obj)
        return extended_objects


with open('ExtendedPerception\\Genuine\\extp_attackrate_0.100000_807.json', 'r') as file:
    json_data = json.load(file)

data_objects= []
for entry in json_data.get("EP", []):
    data_objects.append(DataObject(entry)) 

# Afficher le résultat
for obj in data_objects:
    print(str(obj))
