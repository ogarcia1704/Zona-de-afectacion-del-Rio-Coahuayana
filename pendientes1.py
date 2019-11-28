import arcpy
arcpy.env.workspace = "C:/CDV E13B64C"
listTINs = arcpy.ListDatasets("","TIN")
if len(listTINs) > 0:
    for dataset in listTINs:
    print(dataset)
    aspect = arcpy.CreateUniqueName("E13B64C.shp", "C:\E13B64C")
    slope = arcpy.CreateUniqueName("Pendientes.shp", "C:\E13B64C ")
    outFC = dataset + "_E13B64C_Pendientes.shp"
    arcpy.SurfaceAspect_3d(dataset, aspect)
    arcpy.SurfaceSlope_3d(dataset, slope)
    print("Starting Intersect")
    arcpy.Intersect_analysis(aspect + " #;" + slope + " #", outFC, "ALL")
    print("Completed intersect for " + dataset)
else:
    print("There are no TINs in the " + env.workspace + " directory.")
