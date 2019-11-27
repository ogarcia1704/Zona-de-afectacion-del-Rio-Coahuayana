PUNTOS DE INFLUENCIA:

import arcpy
arcpy.env.workspace = "C:/data"
arcpy.Buffer_analysis("roads", "C:/output/majorrdsBuffered", "100 Feet", "FULL", "ROUND", "LIST", "Distance")
# Name: Buffer.py
# Description: Find areas of suitable vegetation which exclude areas heavily impacted by major roads

# import system modules 
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data/Habitat_Analysis.gdb"

# Select suitable vegetation patches from all vegetation
veg = "vegtype"
suitableVeg = "C:/output/Output.gdb/suitable_vegetation"
whereClause = "HABITAT = 1" 
arcpy.Select_analysis(veg, suitableVeg, whereClause)

# Buffer areas of impact around major roads
roads = "majorrds"
roadsBuffer = "C:/output/Output.gdb/buffer_output"
distanceField = "Distance"
sideType = "FULL"
endType = "ROUND"
dissolveType = "LIST"
dissolveField = "Distance"
arcpy.Buffer_analysis(roads, roadsBuffer, distanceField, sideType, endType, dissol-veType, dissolveField)

# Erase areas of impact around major roads from the suitable vegetation patch-es
eraseOutput = "C:/output/Output.gdb/suitable_vegetation_minus_roads"
xyTol = "1 Meters"
arcpy.Erase_analysis(suitableVeg, roads-Buffer, eraseOutput, xyTol)
