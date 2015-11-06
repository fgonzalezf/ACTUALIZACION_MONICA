#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# Name:        Actualización de Puntos Interes CRUD
# Purpose:
#
# Author:      fernando gonzalez
#
# Created:     14/09/2015
# Copyright:   (c) fgonzalezf 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy,os,sys
reload(sys)
sys.setdefaultencoding("utf-8")
#PuntosEntradaOr=r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas_CRUD\enviar30.mdb\Datos_Extraidos"
#PutosSalida=r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas_CRUD\Totales.mdb\Puntos_Totales"
#excel= r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas_CRUD\prueba10.xls"
#Actualizacion="true"
PuntosEntradaOr=sys.argv[1]
PutosSalida=sys.argv[2]
excel= sys.argv[3]
Actualizacion= sys.argv[4]


workspace= os.path.dirname(PutosSalida)


def Mapa(fieldmappings,FeatEntrada, CampoEntrada , CampoSalida):
        fieldmap = fieldmappings.getFieldMap(fieldmappings.findFieldMapIndex(CampoSalida))
        fieldmap.addInputField(FeatEntrada, CampoEntrada)
        fieldmappings.replaceFieldMap(fieldmappings.findFieldMapIndex(CampoSalida), fieldmap)
        fieldmappings.removeFieldMap(fieldmappings.findFieldMapIndex(CampoEntrada))
        return fieldmappings

PuntosEntrada=arcpy.FeatureClassToFeatureClass_conversion(PuntosEntradaOr,"in_memory","PuntosEnt")


def CalcularDescripcion( Feat, Domain,FieldNameCal):

    domains = arcpy.da.ListDomains(os.path.dirname(PutosSalida))
    with arcpy.da.UpdateCursor(Feat, FieldNameCal) as cursor:
            for row in cursor:
                for domain in domains:
                    if domain.name == Domain:
                        coded_values = domain.codedValues
                        for val, desc in coded_values.iteritems():
                            if str(desc).upper() == str(row[0]).upper():
                                row[0] = val
                cursor.updateRow(row)

CalcularDescripcion(PuntosEntrada,"Dom_Contry","NEW_COUNTRY")
CalcularDescripcion(PuntosEntrada,"Dom_Facility","NEW_FACILITY_TYPE_DESC")
CalcularDescripcion(PuntosEntrada,"Dom_Chain","NEW_CHAIN_NAME")
CalcularDescripcion(PuntosEntrada,"Dom_Food","NEW_FOOD_TYPE")


fieldmapping = arcpy.FieldMappings()
fieldmapping.addTable(PuntosEntrada)
fieldmapping.addTable(PutosSalida)
fieldList = arcpy.ListFields(PuntosEntrada)
for field in fieldList:
        if field.name=="POIPVID":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "POIPVID" , "poi_pvid")
        elif field.name=="NEW_FACILITY_TYPE_DESC":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_FACILITY_TYPE_DESC" ,  "facility_type_desc")
        elif field.name=="NEW_SUBCATEGORY":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_SUBCATEGORY" ,  "subcategory")
        elif field.name=="NEW_POI_NAME_FULL_NAME":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_POI_NAME_FULL_NAME" ,  "poi_name")
        elif field.name=="NEW_STREET_NAME":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_STREET_NAME" ,  "street_name")
        elif field.name=="NEW_STREET_TYPE":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_STREET_TYPE" ,  "street_type")
        elif field.name=="NEW_HOUSE_NUMBER":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_HOUSE_NUMBER" ,  "house_number")
        elif field.name=="NEW_COUNTRY":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_COUNTRY" ,  "country")
        elif field.name=="New_Region":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "New_Region" ,  "up2_admin_name")
        elif field.name=="New_Provincia":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "New_Provincia" ,  "up1_admin_name")
        elif field.name=="New_Comuna":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "New_Comuna" ,  "settlement")
        elif field.name=="NEW_STRET_SIDE":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_STRET_SIDE" ,  "street_side")
        elif field.name=="NEW_CHAIN_NAME":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_CHAIN_NAME" ,  "chain_name")
        elif field.name=="NEW_FOOD_TYPE":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_FOOD_TYPE" ,  "food_type")
        elif field.name=="NEW_CONTACT_INFO":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_CONTACT_INFO" ,  "contact_info")
        elif field.name=="NEW_PHONE":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_PHONE" ,  "Phone")
        elif field.name=="NEW_EMAIL":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_EMAIL" ,  "Email")
        elif field.name=="NEW_WEB":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_WEB" ,  "Web")
        elif field.name=="NEW_POSTAL_CODE":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_POSTAL_CODE" ,  "postal_code")
        elif field.name=="NEW_LATITUDE":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_LATITUDE" ,  "latitude")
        elif field.name=="NEW_LONGITUDE":
            fieldmapping= Mapa(fieldmapping,PuntosEntrada, "NEW_LONGITUDE" ,  "longitude")



fieldsEnt = ["POIPVID","NEW_FACILITY_TYPE_DESC","NEW_SUBCATEGORY","NEW_POI_NAME_FULL_NAME","NEW_STREET_NAME","NEW_STREET_TYPE",
             "NEW_HOUSE_NUMBER","NEW_COUNTRY","New_Region","New_Provincia","New_Comuna","NEW_STRET_SIDE","NEW_CHAIN_NAME","NEW_FOOD_TYPE"
             ,"NEW_CONTACT_INFO","NEW_PHONE","NEW_EMAIL","NEW_WEB","NEW_POSTAL_CODE","NEW_LATITUDE","NEW_LONGITUDE","SHAPE@XY"]

fieldsSal = ["poi_pvid","facility_type_desc","subcategory","poi_name","street_name","street_type","house_number",
             "country","up2_admin_name","up1_admin_name","settlement","street_side","chain_name","food_type",
             "contact_info","Phone","Email","Web","postal_code","latitude","longitude","SHAPE@XY"]

fieldsTablaExp= ["ESTADO","poi_pvid","POIPVID","facility_type_desc","NEW_FACILITY_TYPE_DESC","subcategory","NEW_SUBCATEGORY","poi_name","NEW_POI_NAME_FULL_NAME","street_name","NEW_STREET_NAME",
                 "street_type","NEW_STREET_TYPE","house_number","NEW_HOUSE_NUMBER","country","NEW_COUNTRY","up2_admin_name","New_Region","up1_admin_name","New_Provincia","settlement","New_Comuna",
                 "street_side","NEW_STRET_SIDE","chain_name","NEW_CHAIN_NAME","food_type","NEW_FOOD_TYPE","contact_info","NEW_CONTACT_INFO","Phone","NEW_PHONE","Email","NEW_EMAIL","Web","NEW_WEB","postal_code","NEW_POSTAL_CODE","latitude","NEW_LATITUDE",
                 "longitude","NEW_LONGITUDE"]
tabla= arcpy.CreateTable_management ("in_memory","tabla")
for filetab in fieldsTablaExp:
    arcpy.AddField_management("in_memory/tabla",filetab,"TEXT","","","250")

tablaFeat=arcpy.TableToTable_conversion(PuntosEntrada, "in_memory", "feat")

Y=0

if Actualizacion=="true":
    edit = arcpy.da.Editor(workspace)
    edit.startEditing(False, True)
    edit.startOperation()
    cursorIns = arcpy.da.InsertCursor("in_memory/tabla",fieldsTablaExp)
    with arcpy.da.UpdateCursor(PuntosEntrada, fieldsEnt) as cursor1:
        for row1 in cursor1:
            Y=Y+1
            rowexpresion= "[poi_pvid]="+str(row1[0])
            rowexpresionEnt= sql_exp = """{0} = {1}""".format(arcpy.AddFieldDelimiters(os.path.dirname(PuntosEntradaOr),"POIPVID"),"'"+str(row1[0])+"'")

            #print rowexpresion
            with arcpy.da.UpdateCursor(PutosSalida, fieldsSal, rowexpresion) as cursor2:
                X=0
                for row2 in cursor2:
                    X=X+1
                    print X
                    try:
                       if row2[0]== int(row1[0]):
                            cursorIns.insertRow(("Actualizado",str(row2[0]),row1[0],row2[1],row1[1],row2[2],row1[2],row2[3],
                                                 row1[3],row2[4],row1[4],row2[5],row1[5],row2[6],row1[6],row2[7],row1[7],row2[8],row1[8],
                                                 row2[9],row1[9],row2[10],row1[10],row2[11],row1[11],row2[12],
                                                 row1[12],row2[13],row1[13],row2[14],row1[14],row2[15],row1[15],row2[16],row1[16],
                                                 row2[17],row1[17],row2[18],row1[18],str(row2[19]),str(row1[19]),str(row2[20]),str(row1[20])))
                            if row2[1]==row1[1] or row1[1] is None :
                                pass

                            else:

                                row2[1]=row1[1]if row1[1] else None

                            if row2[2]==row1[2] or row1[2] is None:
                               pass
                            else:
                                row2[2]=row1[2]if row1[2] else None

                            if row2[3]==row1[3] or row1[3] is None:
                               pass
                            else:
                                row2[3]=row1[3]if row1[3] else None

                            if row2[4]==row1[4]or row1[4] is None:
                                pass
                            else:
                                row2[4]=row1[4]if row1[4] else None

                            if row2[5]==row1[5]or row1[5] is None:
                               pass
                            else:
                                row2[5]=row1[5]if row1[5] else None

                            if row2[6]==row1[6]or row1[6] is None:
                               pass
                            else:
                                row2[6]=row1[6]if row1[6] else None

                            if row2[7]==row1[7]or row1[7] is None:
                               pass
                            else:
                                row2[7]=row1[7]if row1[7] else None

                            if row2[8]==row1[8]or row1[8] is None:
                               pass
                            else:
                                row2[8]=row1[8]if row1[8] else None

                            if row2[9]==row1[9]or row1[9] is None:
                               pass
                            else:
                                row2[9]=row1[9]if row1[9] else None

                            if row2[10]==row1[10]or row1[10] is None:
                               pass
                            else:
                                row2[10]=row1[10]if row1[10] else None

                            if row2[11]==row1[11]or row1[11] is None:
                               pass
                            else:
                                row2[11]=row1[11]if row1[11] else None

                            if row2[12]==row1[12]or row1[12] is None:
                               pass
                            else:
                                row2[12]=row1[12]if row1[12] else None

                            if row2[13]==row1[13]or row1[13] is None:
                               pass
                            else:
                                row2[13]=row1[13]

                            if row2[14]==row1[14]or row1[14] is None:
                                pass
                            else:
                                row2[14]=row1[14]

                            if row2[15]==row1[15]or row1[15] is None:
                               pass
                            else:
                                row2[15]=row1[15]if row1[15] else None

                            if row2[16]==row1[16]or row1[16] is None:
                               pass
                            else:
                                row2[16]=row1[16]if row1[16] else None

                            if row2[17]==row1[17]or row1[17] is None:
                               pass
                            else:
                                row2[17]=row1[17]

                            if row2[18]==row1[18]or row1[18] is None:
                               pass
                            else:
                                row2[18]=row1[18]
                            if row2[19]==row1[19]or row1[19] is None:
                               pass
                            else:
                                row2[19]=row1[19]
                            if row2[20]==row1[20]or row1[20] is None:
                               pass
                            else:
                                row2[20]=row1[20]
                            if row2[21]==row1[21]or row1[21] is None:
                               pass
                            else:
                                row2[21]=row1[21]


                            cursor2.updateRow(row2)



                    except Exception as e:
                        #print e.message

                        print "Error en Actualizando:  " + rowexpresion
                        pass
                if X==0:
                    try:
                        #Insercion de Puntos Nuevos
                        print X
                        arcpy.AddMessage(rowexpresionEnt)
                        arcpy.MakeFeatureLayer_management(PuntosEntradaOr,"NuevoLayer",rowexpresionEnt.strip())
                        arcpy.Append_management("NuevoLayer",PutosSalida,"NO_TEST",fieldmapping)
                        with arcpy.da.SearchCursor("NuevoLayer", "*") as cursor5:
                            for row5 in cursor5:
                                cursorIns.insertRow(("Nuevo",row2[0],"Nuevo",row2[1],"**Nuevo**",row2[2],"**Nuevo**",row2[3],
                                                 "**Nuevo**",row2[4],"**Nuevo**",row2[5],"**Nuevo**",row2[6],"**Nuevo**",row2[7],"**Nuevo**",
                                                     row2[8],"**Nuevo**",
                                                 row2[9],"**Nuevo**",row2[10],"**Nuevo**",row2[11],"**Nuevo**",row2[12],
                                                 "**Nuevo**",str(row2[13]),"**Nuevo**",str(row2[14]),"**Nuevo**",row2[15],"**Nuevo**",
                                                 row2[16],"**Nuevo**",row2[17],"**Nuevo**",row2[18],"**Nuevo**",row2[19],"**Nuevo**",row2[20],"**Nuevo**"))

                        arcpy.Delete_management("NuevoLayer")
                    except Exception as e:
                        print e.message
                        arcpy.AddMessage("Error en Insertando:  " + rowexpresionEnt +"  "+ e.message)

                        pass

    edit.stopOperation()
    edit.stopEditing(True)
else:
    cursorIns = arcpy.da.InsertCursor("in_memory/tabla",fieldsTablaExp)
    with arcpy.da.SearchCursor(PuntosEntrada, fieldsEnt) as cursor1:
        for row1 in cursor1:
            Y=Y+1
            rowexpresion= "[poi_pvid]="+str(row1[0])
            rowexpresionEnt= sql_exp = """{0} = {1}""".format(arcpy.AddFieldDelimiters(os.path.dirname(PuntosEntradaOr),"POIPVID"),"'"+str(row1[0])+"'")

            #print rowexpresion
            with arcpy.da.SearchCursor(PutosSalida, fieldsSal, rowexpresion) as cursor2:
                X=0
                for row2 in cursor2:
                    X=X+1
                    print X
                    try:
                        if row2[0]== int(row1[0]):
                            print row2[1]
                            print row1[1]
                            cursorIns.insertRow(("Actualizado",str(row2[0]),row1[0],row2[1],row1[1],row2[2],row1[2],row2[3],
                                                 row1[3],row2[4],row1[4],row2[5],row1[5],row2[6],row1[6],row2[7],row1[7],row2[8],row1[8],
                                                 row2[9],row1[9],row2[10],row1[10],row2[11],row1[11],row2[12],
                                                 row1[12],row2[13],row1[13],row2[14],row1[14],row2[15],row1[15],row2[16],row1[16],
                                                 row2[17],row1[17],row2[18],row1[18],str(row2[19]),str(row1[19]),str(row2[20]),str(row1[20])))

                    except Exception as e:
                        #print e.message

                        print "Error en Recorriendo 1:  " + rowexpresion
                        pass
                if X==0:
                    try:
                        cursorIns.insertRow(("Nuevo",row2[0],"Nuevo",row2[1],"**Nuevo**",row2[2],"**Nuevo**",row2[3],
                                                 "**Nuevo**",row2[4],"**Nuevo**",row2[5],"**Nuevo**",row2[6],"**Nuevo**",row2[7],"**Nuevo**",
                                                     row2[8],"**Nuevo**",
                                                 row2[9],"**Nuevo**",row2[10],"**Nuevo**",row2[11],"**Nuevo**",row2[12],
                                                 "**Nuevo**",str(row2[13]),"**Nuevo**",str(row2[14]),"**Nuevo**",row2[15],"**Nuevo**",
                                                 row2[16],"**Nuevo**",row2[17],"**Nuevo**",row2[18],"**Nuevo**",row2[19],"**Nuevo**",row2[20],"**Nuevo**"))


                    except Exception as e:
                        print e.message
                        arcpy.AddMessage("Error en Recorriendo:  " + rowexpresionEnt +"  "+ e.message)

                        pass


import xlwt

try:
    tabla="in_memory/tabla"

    style = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['orange']
    style.pattern = pattern

    styleHeader = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['gray25']
    styleHeader.pattern = pattern

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    #Encabezado
    i=0
    for nom in fieldsTablaExp:
        ws.write(0, i, nom, styleHeader)
        i=i+1
    Z=1
    with arcpy.da.SearchCursor(tabla, fieldsTablaExp) as cursor:
            for row in cursor:
                ws.write(Z, 0, row[0])
                for x in range(0, (len(fieldsTablaExp)-1)/2):
                    if row[2*x+1]==row[2*x+2] or(row[2*x+1]=="" and row[2*x+2]== None ) or (row[2*x+1]==None and row[2*x+2]== "" ) :
                        ws.write(Z, 2*x+1, row[2*x+1])
                        ws.write(Z, 2*x+2, row[2*x+2])
                    else:
                        ws.write(Z, 2*x+1, row[2*x+1],style)
                        ws.write(Z, 2*x+2, row[2*x+2],style)
                Z=Z+1

    wb.save(excel)

    #arcpy.TableToExcel_conversion("in_memory/tabla",excel)
    arcpy.Delete_management("in_memory/tabla")
    arcpy.Delete_management("LayerPuntos")
except Exception as e:
    arcpy.AddMessage("Error Exportando Tabla: "+ e.message)

