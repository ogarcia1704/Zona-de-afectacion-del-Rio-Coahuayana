PENDIENTES:

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# List all TINs in workspace
listTINs = arcpy.ListDatasets("","TIN")

# Determine whether the list contains any TINs
if len(listTINs) > 0:
    for dataset in listTINs:
        print(dataset)
        # Set Local Variables
        aspect = arcpy.CreateUniqueName("Aspect.shp")
        slope = arcpy.CreateUniqueName("Slope.shp")
        outFC = dataset + "_Aspect_Slope.shp"
        #Execute SurfaceAspect
        arcpy.SurfaceAspect_3d(dataset, aspect)
        #Execute SurfaceSlope
        arcpy.SurfaceSlope_3d(dataset, slope)
        #Execute SurfaceSlope
        print("Starting Intersect")
        arcpy.Intersect_analysis(aspect + " #;" + slope + " #", outFC, "ALL")
        print("Completed intersect for " + dataset)
else:
    print("There are no TINs in the " + env.workspace + " directory.")
