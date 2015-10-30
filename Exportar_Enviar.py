import arcpy,os, sys
arcpy.env.overwriteOutput=True
reload(sys)
sys.setdefaultencoding("utf-8")
#featureClassEnt=r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas\Prueba3.mdb\Datos"
#geodatabaseSal=r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas\enviar25.mdb"
featureClassEnt=sys.argv[1]
geodatabaseSal=sys.argv[2]
arcpy.env.workspace = geodatabaseSal

arcpy.CreatePersonalGDB_management(os.path.dirname(geodatabaseSal),os.path.basename(geodatabaseSal),"10.0")

spatial_ref = arcpy.Describe(featureClassEnt).spatialReference
desc = arcpy.Describe(featureClassEnt)
arcpy.AddMessage(desc.catalogPath)
Entrada=""
try:
    Entrada=os.path.dirname(desc.catalogPath)

except:
    Entrada=os.path.dirname(featureClassEnt)

#arcpy.DomainToTable_management(Entrada,"Action","in_memory/table1","Codigo","descripcion")
#arcpy.TableToDomain_management("in_memory/table1","Codigo","descripcion",geodatabaseSal,"Action","Action")

#arcpy.DomainToTable_management(Entrada,"Dom_Chain","in_memory/table2","Codigo","descripcion")
#arcpy.TableToDomain_management("in_memory/table2","Codigo","descripcion",geodatabaseSal,"Dom_Chain","Dom_Chain")

#arcpy.DomainToTable_management(Entrada,"Dom_Contry","in_memory/table3","Codigo","descripcion")
#arcpy.TableToDomain_management("in_memory/table3","Codigo","descripcion",geodatabaseSal,"Dom_Contry","Dom_Contry")

#arcpy.DomainToTable_management(Entrada,"Dom_Facility","in_memory/table4","Codigo","descripcion")
#arcpy.TableToDomain_management("in_memory/table4","Codigo","descripcion",geodatabaseSal,"Dom_Facility","Dom_Facility")

#arcpy.DomainToTable_management(Entrada,"Dom_Food","in_memory/table5","Codigo","descripcion")
#arcpy.TableToDomain_management("in_memory/table5","Codigo","descripcion",geodatabaseSal,"Dom_Food","Dom_Food")

#arcpy.DomainToTable_management(Entrada,"Dom_Subcategoria","in_memory/table6","Codigo","descripcion")
#arcpy.TableToDomain_management("in_memory/table6","Codigo","descripcion",geodatabaseSal,"Dom_Subcategoria","Dom_Subcategoria")

#arcpy.CreateDomain_management(geodatabaseSal, "Dom_Street_Side", "Street Side", "TEXT", "CODED")
#arcpy.AddCodedValueToDomain_management(geodatabaseSal,"Dom_Street_Side","L","L")
#arcpy.AddCodedValueToDomain_management(geodatabaseSal,"Dom_Street_Side","R","R")




Puntos=arcpy.CreateFeatureclass_management(geodatabaseSal,"Datos_Extraidos","POINT","","","",spatial_ref)
if arcpy.TestSchemaLock(Puntos):
    print "Adicionando campos"
    arcpy.AddField_management(Puntos,"Num_Registro","TEXT","","","250","Num_Registro","","","")
    arcpy.AddField_management(Puntos,"POI_Action","TEXT","","","250","POI_Action","","","Action")
    arcpy.AddField_management(Puntos,"FACILITY_TYPE_DESC","TEXT","","","250","FACILITY_TYPE_DESC","","")
    arcpy.AddField_management(Puntos,"NEW_FACILITY_TYPE_DESC","TEXT","","","250","NEW_FACILITY_TYPE_DESC","","","")
    arcpy.AddField_management(Puntos,"SUBCATEGORY","TEXT","","","250","SUBCATEGORY","","","")
    arcpy.AddField_management(Puntos,"NEW_SUBCATEGORY","TEXT","","","250","NEW_SUBCATEGORY","","","")

    arcpy.AddField_management(Puntos,"POI_NAME","TEXT","","","250","POI_NAME","","")
    arcpy.AddField_management(Puntos,"NEW_POI_NAME_FULL_NAME","TEXT","","","250","NEW_POI_NAME_FULL_NAME","","","")
    arcpy.AddField_management(Puntos,"STREET_NAME","TEXT","","","250","STREET_NAME","","","")
    arcpy.AddField_management(Puntos,"NEW_STREET_NAME","TEXT","","","250","NEW_STREET_NAME","","","")
    arcpy.AddField_management(Puntos,"STREET_TYPE","TEXT","","","250","STREET_TYPE","","","")
    arcpy.AddField_management(Puntos,"NEW_STREET_TYPE","TEXT","","","250","NEW_STREET_TYPE","","","")
    arcpy.AddField_management(Puntos,"HOUSE_NUMBER","TEXT","","","250","HOUSE_NUMBER","","","")
    print "Adicionando campos 2"
    arcpy.AddField_management(Puntos,"NEW_HOUSE_NUMBER","TEXT","","","250","NEW_HOUSE_NUMBER","","","")

    arcpy.AddField_management(Puntos,"COUNTRY","TEXT","","","250","COUNTRY","","")
    arcpy.AddField_management(Puntos,"NEW_COUNTRY","TEXT","","","250","NEW_COUNTRY","","","")

    arcpy.AddField_management(Puntos,"Region","TEXT","","","250","Region","","","")
    arcpy.AddField_management(Puntos,"New Region","TEXT","","","250","New Region","","","")
    arcpy.AddField_management(Puntos,"Provincia","TEXT","","","250","Provincia","","","")
    arcpy.AddField_management(Puntos,"New Provincia","TEXT","","","250","New Provincia","","","")
    arcpy.AddField_management(Puntos,"Comuna","TEXT","","","250","Comuna","","","")
    arcpy.AddField_management(Puntos,"New Comuna","TEXT","","","250","New Comuna","","","")
    arcpy.AddField_management(Puntos,"STREET_SIDE","TEXT","","","250","STREET_SIDE","","","")

    arcpy.AddField_management(Puntos,"NEW_STRET_SIDE","TEXT","","","250","NEW_STRET_SIDE","","","")
    arcpy.AddField_management(Puntos,"CHAIN_NAME","TEXT","","","250","CHAIN_NAME","","")
    arcpy.AddField_management(Puntos,"NEW_CHAIN_NAME","TEXT","","","250","NEW_CHAIN_NAME","","","")
    arcpy.AddField_management(Puntos,"FOOD_TYPE","TEXT","","","250","FOOD_TYPE","","")
    arcpy.AddField_management(Puntos,"NEW_FOOD_TYPE","TEXT","","","250","NEW_FOOD_TYPE","","","")

    arcpy.AddField_management(Puntos,"PHONE","TEXT","","","250","PHONE_NUMBER","","","")
    arcpy.AddField_management(Puntos,"NEW_PHONE","TEXT","","","250","NEW_PHONE_NUMBER","","","")
    arcpy.AddField_management(Puntos,"EMAIL","TEXT","","","250","EMAIL","","","")
    arcpy.AddField_management(Puntos,"NEW_EMAIL","TEXT","","","250","NEW_EMAIL","","","")
    arcpy.AddField_management(Puntos,"WEB","TEXT","","","250","WEB","","","")
    arcpy.AddField_management(Puntos,"NEW_WEB","TEXT","","","250","NEW_WEB","","","")
    arcpy.AddField_management(Puntos,"CONTACT_INFO","TEXT","","","250","CONTACT_INFO","","","")
    arcpy.AddField_management(Puntos,"NEW_CONTACT_INFO","TEXT","","","250","NEW_CONTACT_INFO","","","")
    arcpy.AddField_management(Puntos,"POSTAL_CODE","TEXT","","","250","POSTAL_CODE","","","")
    arcpy.AddField_management(Puntos,"NEW_POSTAL_CODE","TEXT","","","250","NEW_POSTAL_CODE","","","")
    arcpy.AddField_management(Puntos,"DATE_INCLUSION","TEXT","","","250","DATE_INCLUSION","","","")
    print "Adicionando campos 3"
    arcpy.AddField_management(Puntos,"DATE_UPDATED","TEXT","","","250","DATE_UPDATED","","","")
    arcpy.AddField_management(Puntos,"LATITUDE","DOUBLE","","","","LATITUDE","","","")
    arcpy.AddField_management(Puntos,"NEW_LATITUDE","DOUBLE","","","","NEW_LATITUDE","","","")
    arcpy.AddField_management(Puntos,"LONGITUDE","DOUBLE","","","","LONGITUDE","","","")
    arcpy.AddField_management(Puntos,"NEW_LONGITUDE","DOUBLE","","","","NEW_LONGITUDE","","","")

    arcpy.AddField_management(Puntos,"NOTES","TEXT","","","250"," NOTES","","","")
    arcpy.AddField_management(Puntos,"VERIFICADO_CAMPO","TEXT","","","250","VERIFICADO_CAMPO","","","")
    arcpy.AddField_management(Puntos,"VIA_PRINCIPAL","TEXT","","","250","VIA_PRINCIPAL","","","")
    arcpy.AddField_management(Puntos,"POI_PRIORI","TEXT","","","250","POI_PRIORI","","","")
    arcpy.AddField_management(Puntos,"POIPVID","TEXT","","","250","POIPVID","","","")
else:
    print("Unable to acquire the necessary schema lock to add the new field")


#Migracion de la Informacion

def Mapa(fieldmappings,FeatEntrada, CampoEntrada , CampoSalida):
        fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex(CampoSalida))
        fieldmap.addInputField(FeatEntrada, CampoEntrada)
        fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex(CampoSalida), fieldmap)
        fieldmappings.removeFieldMap(fieldmappings.findFieldMapIndex(CampoEntrada))
        return fieldmappings

fieldmapping = arcpy.FieldMappings()
fieldmapping.addTable(featureClassEnt)
fieldmapping.addTable(Puntos)
fieldList = arcpy.ListFields(featureClassEnt)
for field in fieldList:
        if field.name=="up2_admin_name":
            fieldmapping= Mapa(fieldmapping,featureClassEnt, "up2_admin_name" ,  "Region")
        elif field.name=="up1_admin_name":
            fieldmapping= Mapa(fieldmapping,featureClassEnt, "up1_admin_name" ,  "Provincia")
        elif field.name=="settlement":
            fieldmapping= Mapa(fieldmapping,featureClassEnt, "settlement" ,  "Comuna")
        elif field.name=="poi_pvid":
            fieldmapping= Mapa(fieldmapping,featureClassEnt, "poi_pvid" ,  "POIPVID")

arcpy.Append_management(featureClassEnt, Puntos, "NO_TEST",fieldmapping)

# Calcular Descripciones en Dominios

print "Calculando campos"

def CalcularDescripcion( Feat, Domain,FieldNameCal):
    #fields = arcpy.ListFields(Feat)
    #domainName=""
    #for field in fields:
        #if field.name==FieldDomain:
            #print field.name
            #domainName= field.domain

    #print domainName
    domains = arcpy.da.ListDomains(Entrada)
    with arcpy.da.UpdateCursor(Feat, FieldNameCal) as cursor:
            for row in cursor:
                for domain in domains:
                    if domain.name == Domain:
                        coded_values = domain.codedValues
                        for val, desc in coded_values.iteritems():
                            if val == row[0]:
                                row[0] = desc
                cursor.updateRow(row)

#CalcularDescripcion(Puntos,"Dom_Facility","FACILITY_TYPE_DESC")
#CalcularDescripcion(Puntos,"Dom_Facility","NEW_FACILITY_TYPE_DESC")
#CalcularDescripcion(Puntos,"Dom_Contry","COUNTRY")
#CalcularDescripcion(Puntos,"Dom_Contry","NEW_COUNTRY")
#CalcularDescripcion(Puntos,"Dom_Chain","CHAIN_NAME")
#CalcularDescripcion(Puntos,"Dom_Chain","NEW_CHAIN_NAME")
#CalcularDescripcion(Puntos,"Dom_Food","FOOD_TYPE")
#CalcularDescripcion(Puntos,"Dom_Food","NEW_FOOD_TYPE")

