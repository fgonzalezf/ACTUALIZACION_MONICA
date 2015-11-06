import arcpy, os, sys
arcpy.env.overwriteOutput=True
reload(sys)
sys.setdefaultencoding("utf-8")
#FeatEntrada= r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas\enviar25.mdb\Datos_Extraidos"
#Excel_Salida = r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas_NBS\prueba8.xls"
#Geodatabase_Base = r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas\Prueba3.mdb"
FeatEntrada= sys.argv[1]
Excel_Salida =sys.argv[2]
Geodatabase_Base =sys.argv[3]


tabla=arcpy.CreateTable_management ("in_memory", "tabla")


#Campos

fields =["ACTION_CODE","POI_PVID","PS3_BLEND_POI_ID","FACILITY_CODE_",
         "POI_NAME_LANG_CODE","POI_NAME_","POI_ADDRESS_LANG_CODE","ADDRESS_NUMBER",
         "COUNTRY_","LATITUDE_","LONGITUDE_","PHONE_NUMBER_","CHAIN_ID_","CUISINE_ID","BUILDING_TYPE",
         "SUPPLIER_POI_ID","STREET_BASE_NAME","POSTAL_CODE_","PROTECTED_ID","CALL_REVIEW_DATE",
         "SOURCE_CODE","NUMBER","STREET_SIDE_","WEB","EMAIL"]

for field in fields:
    arcpy.AddField_management("in_memory/tabla", field, "TEXT", "","","250","")


tablaFeat=arcpy.TableToTable_conversion(FeatEntrada, "in_memory", "feat")

def Mapa(fieldmappings,FeatEntrada, CampoEntrada , CampoSalida):
        fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex(CampoSalida))
        fieldmap.addInputField(FeatEntrada, CampoEntrada)
        fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex(CampoSalida), fieldmap)
        fieldmappings.removeFieldMap(fieldmappings.findFieldMapIndex(CampoEntrada))
        return fieldmappings

fieldmapping = arcpy.FieldMappings()
fieldmapping.addTable("in_memory/feat")
fieldmapping.addTable("in_memory/tabla")
fieldList = arcpy.ListFields("in_memory/feat")
for field in fieldList:
        if field.name=="NEW_FACILITY_TYPE_DESC":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_FACILITY_TYPE_DESC" ,  "FACILITY_CODE_")
        elif field.name=="NEW_POI_NAME_FULL_NAME":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_POI_NAME_FULL_NAME" ,  "POI_NAME_")
        if field.name=="NEW_COUNTRY":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_COUNTRY" ,  "COUNTRY_")
        elif field.name=="NEW_LATITUDE":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_LATITUDE" ,  "LATITUDE_")
        if field.name=="NEW_LONGITUDE":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_LONGITUDE" ,  "LONGITUDE_")
        elif field.name=="NEW_PHONE_NUMBER":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_PHONE" ,  "PHONE_NUMBER_")
        if field.name=="NEW_CHAIN_NAME":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_CHAIN_NAME" ,  "CHAIN_ID_")
        elif field.name=="NEW_FOOD_TYPE":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_FOOD_TYPE" ,  "CUISINE_ID")
        elif field.name=="NEW_STRET_SIDE":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_STRET_SIDE" ,  "STREET_SIDE_")
        elif field.name=="NEW_POSTAL_CODE":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_POSTAL_CODE" ,  "POSTAL_CODE_")
        elif field.name=="POIPVID":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "POIPVID" ,  "POI_PVID")
        elif field.name=="NEW_STREET_NAME":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_STREET_NAME" ,  "STREET_BASE_NAME")
        elif field.name=="POI_Action":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "POI_Action" ,  "ACTION_CODE")
        elif field.name=="NEW_WEB":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_WEB" ,  "WEB")
        elif field.name=="NEW_EMAIL":
            fieldmapping= Mapa(fieldmapping,"in_memory/feat", "NEW_EMAIL" ,  "EMAIL")




arcpy.Append_management("in_memory/feat", "in_memory/tabla", "NO_TEST",fieldmapping)
print "Exportando Excel"

#def CalcularDescripcion( Feat, Domain,FieldNameCal):

    #domains = arcpy.da.ListDomains(Geodatabase_Base)
    #with arcpy.da.UpdateCursor(Feat, FieldNameCal) as cursor:
            #for row in cursor:
                #for domain in domains:
                    #if domain.name == Domain:
                        #coded_values = domain.codedValues
                        #for val, desc in coded_values.iteritems():
                            #if str(desc).upper() == str(row[0]).upper():
                                #row[0] = val
                #cursor.updateRow(row)

def CalcularDescripcion(Feat,Tabla,FieldNameCal):
    try:
        Tabla= Geodatabase_Base+os.sep+Tabla
        campos=["Codigo","Descripcion"]
        if arcpy.Exists(Tabla):
            with arcpy.da.UpdateCursor(Feat, FieldNameCal) as cursor:
                for row in cursor:
                    with arcpy.da.SearchCursor(Tabla,campos ) as cursor2:
                        for row2 in cursor2:
                            if str(row[0]).upper()==str(row2[0]).upper():
                                row[0]=row2[1]
                    cursor.updateRow(row)
        del cursor
        del cursor2
    except Exception as e:
        arcpy.AddMessage("Error calculando dominios "+ e.message+ str(row[0])+ str(row2[1]))





CalcularDescripcion("in_memory/tabla","Dom_Contry","COUNTRY_")
CalcularDescripcion("in_memory/tabla","Dom_Facility","FACILITY_CODE_")
CalcularDescripcion("in_memory/tabla","Dom_Chain","CHAIN_ID_")
CalcularDescripcion("in_memory/tabla","Dom_Food","CUISINE_ID")
arcpy.CalculateField_management("in_memory/tabla","POI_NAME_LANG_CODE",'"SPA"',"VB")
arcpy.CalculateField_management("in_memory/tabla","POI_ADDRESS_LANG_CODE",'"SPA"',"VB")
arcpy.CalculateField_management("in_memory/tabla","NUMBER",'"#"',"VB")





exp=None
try:
   TABLEEXPORT= arcpy.TableToTable_conversion("in_memory/tabla",os.path.dirname(FeatEntrada),"Tablaexp")

except:
    arcpy.AddMessage("Error Exportando Tabla Geodatabase Bloqueada")

fields=arcpy.ListFields(TABLEEXPORT)

for field1 in fields:
    if field1.name[-1:]=="_":
        arcpy.AlterField_management(TABLEEXPORT,field1.name,field1.name[:-1])

arcpy.TableToExcel_conversion(TABLEEXPORT, Excel_Salida,"true")

arcpy.Delete_management("in_memory/tabla")
arcpy.Delete_management("in_memory/feat")
arcpy.Delete_management(TABLEEXPORT)
arcpy.Delete_management("TablaExp2")
