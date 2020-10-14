import itertools
import arcpy
import sys


xetler = dict([(l[0],l[1]) for l in arcpy.da.SearchCursor("line",["OBJECTID","SHAPE@"])])

noqteler = dict([(p[0],p[1]) for p in arcpy.da.SearchCursor("Entrans",["OBJECTID","SHAPE@"])])

for i in itertools.product(noqteler,xetler):
    noqteID = i[0]
    xettID = i[1]
    cixis = xetler[xettID].queryPointAndDistance(noqteler[noqteID])



nearest_line = {}
# { <noqteID>: { xettID: <xettID>, distance:<distance> } }

    if distance(noqteler,xetler) < nearest_line[noqteID].distance:
    
        nearest_line[noqteID].xettID = xettID 
        nearest_line[noqteID].xettID = distance(noqteler,xetler) 


for point in nearest_line.keys():

    print(noqteler)
    print(noqteler.xettID)
    print(noqteler.distance)
