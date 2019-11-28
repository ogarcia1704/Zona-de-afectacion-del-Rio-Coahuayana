import arcpy
arcpy.env.workspace = "C:/E13B64C"
arcpy.Buffer_analysis("Rio1", "C:/Buffer/NewBuffer", "1000 meters", "FULL", "ROUND", "LIST", "Id")
