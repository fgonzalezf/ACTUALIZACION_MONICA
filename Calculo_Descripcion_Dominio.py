__author__ = 'fgonzalezf'
import arcpy,os,sys
Entrada= r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas\enviar18.mdb"
Feat=r"C:\Users\fgonzalezf\Documents\Monica_Forigua\Pruebas\enviar18.mdb\Datos_Extraidos"
FieldName="NEW_FACILITY_TYPE_DESC"
FieldNameCal="FACILITY_TYPE_DESC"
fields = arcpy.ListFields(Feat)
domainName=""
for field in fields:
    if field.name==FieldName:
        print field.name
        domainName= field.domain

print domainName
domains = arcpy.da.ListDomains(Entrada)
with arcpy.da.UpdateCursor(Feat, FieldNameCal) as cursor:
        for row in cursor:
            for domain in domains:
                if domain.name == domainName:
                    coded_values = domain.codedValues
                    for val, desc in coded_values.iteritems():
                        if val == row[0]:
                            row[0] = desc
            cursor.updateRow(row)

