# addprov.py
# Indivica OSCAR Configuration SQL Generator
# by Mike
# based on code by David Daley
#
# Last updated: 2014-04-17


#!/usr/bin/python
import calendar
import re
import sys

# script to add new users

# bill centre codes
# G stands for Hamilton
# J - Kingston
# P - London
# E - Mississauga
# F - Oshawa
# D - Ottawa
# R - Sudbury
# U - Thunder Bay
# N - Toronto      


# Default clinic information.
# NOTE: DO NOT USE APOSTROPHES EVER BECAUSE eOSCAR SUCKS
clinic_name = "Bay College Medical Centre"
clinic_address = "C216-777 Bay St."
clinic_city = "Toronto"
clinic_postal = "McG 2C8"
clinic_phone = "416-977-8877"
clinic_fax ="416-977-0118"

# clinic array for multi-office set up
# For Single Office, you can leave these fields alone.
# Addprov weighs the values in the following order:
#   doctor['address'] > clinic['address'] > clinic_address
#   doctor['phone'] > clinic['phone'] > clinic_phone
#   doctor['fax'] > clinic['fax'] > clinic_fax
#
# NOTE: DO NOT USE APOSTROPHES EVER BECAUSE OSCAR SUCKS
# NOTE:  10 CHARACTER LIMIT FOR myGroupName
# NOTE:  20 CHARACTER LIMIT FOR messengerGroupAndTeamName
clinic={}
clinic['messengerGroupAndTeamName'] = ['']
clinic['myGroupName'] = ['Doctors']
clinic['address'] = ['']
clinic['phone'] = ['']
clinic['fax'] = ['']

# NOTE: 40 CHARACTER LIMIT FOR ADDRESS IN PROVIDER RECORDS:
# You can leave the address, phone number and fax number fields blank.
#   If: blank then: use clinic value
#
# NOTE: PLEASE PLEASE PLEASE BE SURE TO NUMBER CLINICS IN INCREASING ORDER.
#   ALSO USE THE STRING VALUE FOR THE NUMBER.


# doctor user accounts
# each array in doctor[] must be the same length
doctor = {}
doctor['clinic'] = ['1', '1', '1', '1']
doctor['last_nm'] =  ['Wong', 'Lee', 'Wong', 'Siu']
doctor['first_nm'] = ['Albert', 'Winnie', 'Angela', 'King Fun']
doctor['login_nm'] = ['wongal', 'lee', 'wongan', 'siu']
doctor['prov_no'] = ['106724', '000001', '000002', '000003']
doctor['group_no'] = ['0000', '0000', '0000', '0000']
doctor['cpso'] = ['60871', '68146', '69873', '74220']
doctor['spec'] = ['00', '00', '00', '00']
doctor['billcentre'] = ['N', 'N', 'N', 'N']
doctor['address'] = ['', '', '', '']
doctor['phone'] = ['', '', '', '']
doctor['fax'] = ['', '', '', '']

# staff user accounts
# each array in staff[] must be the same length
staff = {}
staff['clinic'] =['1', '1']
staff['last_nm'] =  ['Yau', 'Yau']
staff['first_nm'] = ['Liza', 'Queenie']
staff['login_nm'] = ['yaul', 'yauq']
staff['prov_no'] = ['999901', '999902']


###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
#
#
#                              NO CHANGES BELOW HERE
#
#
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################





# check the maximum size of messengerGroupAndTeamNAme: 20
# check the maximum size of myGroupName: 10
# check the maximum size of the doctor['address'] field: 40

i=0
while i < len(clinic['messengerGroupAndTeamName']):
    if len(clinic['messengerGroupAndTeamName'][i]) > 20:
        raise NameError('@messengerGroupAndTeamName is too long. 20 Character limit.')
    if len(clinic['myGroupName'][i]) > 10:
        raise NameError('@myGroupName is too long. 10 Character Limit.')
    i += 1
i=0
while i < len(doctor['address']):
    if len(doctor['address'][i]) > 40:
        raise NameError('@doctor[address] is too long. 40 Character Limit.')
    i += 1

# Update external providers service types.

print "###########################################################################"
print "#     INSERT into consultationServices: external provider service types."
print "###########################################################################"
print "insert into consultationServices(serviceId,serviceDesc,active) values (58, 'Family Practice', '1'), (59, 'Anaesthesia', '1'), (60, 'General Surgery', '1'), (61, 'Neurosurgery Surgery', '1'), (62, 'Community Medicine', '1'), (63, 'Orthopaedic Surgery', '1'), (64, 'Geriatrics', '1'), (65, 'Plastic Surgery', '1'), (66, 'Cardiovascular Surgery', '1'), (67, 'Emergency Medicine', '1'), (68, 'Internal Medicine', '1'), (69, 'Psychiatry', '1'), (70, 'Obstetrics & Gynaecology', '1'), (71, 'Genetics', '1'), (72, 'Ophthalmology', '1'), (73, 'Otolaryngology', '1'), (74, 'Paediatrics', '1'), (75, 'Pathology', '1'), (76, 'Microbiology', '1'), (77, 'Clinical Biochemistry', '1'), (78, 'Physical Medicine', '1'), (79, 'Diagnostic Radiology', '1'), (80, 'Therapeutic Radiology', '1'), (81, 'Urology', '1'), (82, 'Gastroenterology', '1'), (83, 'Respirology', '1'), (84, 'Rheumatology', '1'), (85, 'Haematology', '1'), (86, 'Clinical Immunology', '1'), (87, 'Nuclear Medicine', '1'), (88, 'Thoracic Surgery', '1'), (89, 'Dental Surgery', '1'), (90, 'Oral Surgery', '1'), (91, 'Orthodontics', '1'), (92, 'Paedodontics', '1'), (93, 'Periodontics', '1'), (94, 'Oral Pathology', '1'), (95, 'Endocrinology', '1'), (96, 'Oral Radiology', '1'), (97, 'Prosthodontics', '1'), (98, 'Optometry', '1'), (99, 'Osteopathy', '1'), (100, 'Chiropody (Podiatry)', '1'), (101, 'Chiropractics', '1'), (102, 'Midwife', '1'), (103, 'Sports Medicine', '1'), (104, 'Physiotherapy', '1'), (105, 'Nurse Practitioner', '1'), (106, 'Alternate Health Care Profession', '1'), (107, 'Allergist', '1'), (108, 'Infectious Diseases', '1'), (109, 'Intensive Care Unit', '1'), (110, 'Laboratory Medicine', '1'), (111, 'Nephrology', '1'), (112, 'Registered Nurse', '1'), (113, 'Surgical Assistant', '1');"

# Update the Clinic Information.

print "###########################################################################"
print "#     UPDATE clinic with: clinic information."
print "###########################################################################"
print "update clinic set clinic_name='"+clinic_name+"' where clinic_no='1234';"
print "update clinic set clinic_address ='"+ clinic_address+"' where clinic_no='1234';"
print "update clinic set clinic_city ='"+ clinic_city+"' where clinic_no='1234';"
print "update clinic set clinic_postal ='"+ clinic_postal+"' where clinic_no='1234';"
print "update clinic set clinic_phone='"+ clinic_phone+"' where clinic_no='1234';"
print "update clinic set clinic_fax='"+ clinic_fax+"' where clinic_no='1234';"
print "update clinic set clinic_location_code='' where clinic_no='1234';"



print "###########################################################################"
print "#     UPDATE encounterForm: turn off old forms, turn on new forms."
print "###########################################################################"
# Disable the T2Diabetes, Lab Req 2007 form from the form list.
print "update encounterForm set hidden='0' where form_name='T2Diabetes';"
print "update encounterForm set hidden='0' where form_name='Lab Req 2007';"

# Enable the Lab Req 2010 form in the form list.
print "update encounterForm set hidden='25' where form_name='Lab Req 2010';"


# scheduleInsert generates the inserts for a provider's schedule
# provider is the provider number, it doesn't actually use this yet - thank you closures
# start year is the starting year.
months = range(1, 13)
def printYear(start):
    k = 0
    for month in months:
        for day in range(1, 32):
            try:
                weekday = calendar.weekday(start, month, day)
            except ValueError:
                continue
            if weekday < calendar.SATURDAY:
                k += 1
                #print "%d-%02d-%02d" % (start, month, day)
                print "insert into scheduledate(sdate, provider_no,available,priority,reason,hour,creator,status) values('%d-%02d-%02d" % (start, month, day)+"', '"+doctor['prov_no'][i]+"', '1', 'b', '', '', 'z_indivica,ithream', 'A');"

def scheduleInsert(provider, startyear):
    startdate = str(startyear)+"-01-01"
    enddate = str(startyear+1)+"-12-31"
    print "insert into rschedule(provider_no,sdate,edate,available,day_of_week,avail_hourB,avail_hour,creator,status) values('"+doctor['prov_no'][i]+"', '"+startdate+"', '"+enddate+"', '1', '2 3 4 5 6', '', '<MON></MON><TUE></TUE><WED></WED><THU></THU><FRI></FRI>', 'z_indivica,ithream', 'A');"
    
    # print out all the workdays (Mon - Fri) of a month
    # tested with Python24    vegaseat     01feb2007
    # source: http://www.daniweb.com/software-development/python/code/216867
    
    printYear(startyear)
    printYear(startyear+1)


# Address Book for OSCAR Messenger: Messenger Group Admin
addressbookStart = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><addressBook><group>"
addressbookEnd = "</group></addressBook>"
addressbookUsers = []


print "###########################################################################"
print "#     BEGIN PRINTING DOCTOR ACCOUNTS"
print "###########################################################################"
i=0
while i < len(doctor['last_nm']):
    
    
    doctor['clinic'][i] = int(doctor['clinic'][i])
    
    # if the doctor's address field is null
    # then: if the doctor has a clinic id, use the clinic's address
    # else: use the default clinic address
    if not doctor['address'][i]:
        if doctor['clinic'][i]:
            if clinic['address'][doctor['clinic'][i]-1]:
                doctor['address'][i] = clinic['address'][doctor['clinic'][i]-1]
            else:
                doctor['address'][i] = clinic_address+", "+clinic_city+" "+clinic_postal

    # if the doctor's phone field is null
    # then: if the doctor has a clinic id, use the clinic's phone
    # else: use the default clinic phone
    if not doctor['phone'][i]:
        if doctor['clinic'][i]:
            if clinic['phone'][doctor['clinic'][i]-1]:
                doctor['phone'][i] = clinic['phone'][doctor['clinic'][i]-1]
            else:
                doctor['phone'][i] = clinic_phone

    # if the doctor's fax field is null
    # then: if the doctor has a clinic id, use the clinic's fax
    # else: use the default clinic fax
    if not doctor['fax'][i]:
        if doctor['clinic'][i]:
            if clinic['fax'][doctor['clinic'][i]-1]:
                doctor['fax'][i] = clinic['fax'][doctor['clinic'][i]-1]
            else:
                doctor['fax'][i] = clinic_fax

    # if the doctor has a clinic
    # then: assign the doctor to the clinic's team
    # else: make the clinic team null
    if doctor['clinic'][i]:
        doctor_team = clinic['messengerGroupAndTeamName'][doctor['clinic'][i]-1]
    else:
        doctor_team = ''


    # Add doctor account into provider table with values from doctor[][].
    #   provider_no: provider number
    #   last_name: lastname
    #   first_name: firstname
    #   provider_type: 'doctor'
    #   speciality: 'Doctors'
    #   team: doctor_team
    #   sex: ''
    #   dob: 'null'
    #   address: ''
    #   phone: ''
    #   work_phone: ''
    #   email: ''
    #   ohip_no: doctor['prov_no'][i]
    #   rma_no: doctor['prov_no'][i]
    #   billing_no: doctor['prov_no'][i]
    #   hso_no: doctor['prov_no'][i]
    #   status: '1'
    #   comments: '<xml_p_fax>"+clinic_fax+"</xml_p_fax><xml_p_specialty_code>"+doctor['spec'][i]+"</xml_p_specialty_code><xml_p_billinggroup_no>"+doctor['group_no'][i]+"</xml_p_billinggroup_no>'
    ##      adds clinic fax, specialty code & group billing number.
    #   provider_activity: ''
    #   practictionerNo: doctor['cpso'][i]

    print "###########################################################################"
    print "#     Printing DOCTOR account for:"+doctor['first_nm'][i]+" "+doctor['last_nm'][i]
    print "###########################################################################"

    print "insert into provider (provider_no,last_name,first_name,provider_type,specialty,team,sex,dob,address,phone,work_phone,email,ohip_no,rma_no,billing_no,hso_no,status,comments,provider_activity,practitionerNo) values ('"+doctor['prov_no'][i]+"','"+doctor['last_nm'][i]+"','"+doctor['first_nm'][i]+"','doctor','Doctors','"+doctor_team+"','',null,'"+doctor['address'][i]+"','','"+doctor['phone'][i]+"','','"+doctor['prov_no'][i]+"','"+doctor['prov_no'][i]+"','"+doctor['prov_no'][i]+"','"+doctor['prov_no'][i]+"','1','<xml_p_fax>"+doctor['fax'][i]+"</xml_p_fax><xml_p_specialty_code>"+doctor['spec'][i]+"</xml_p_specialty_code><xml_p_billinggroup_no>"+doctor['group_no'][i]+"</xml_p_billinggroup_no>','','"+doctor['cpso'][i]+"');"
    
    # Add provider billing centre information.
    print "insert into  providerbillcenter (provider_no,billcenter_code) values ('"+doctor['prov_no'][i]+"','"+doctor['billcentre'][i]+"');"
    
    # Add individual doctor group.
    print "insert into mygroup(mygroup_no,provider_no,last_name,first_name,vieworder) values ('', '"+doctor['prov_no'][i]+"','"+doctor['last_nm'][i]+"','"+doctor['first_nm'][i]+"',NULL);"
    
    # Add clinic doctor group.
    if not doctor['clinic'][i]:
        if clinic['myGroupName'][doctor['clinic'][i]-1]:
            print "insert into mygroup(mygroup_no,provider_no,last_name,first_name,vieworder) values ('"+clinic['myGroupName'][doctor['clinic'][i]-1]+"', '"+doctor['prov_no'][i]+"','"+doctor['last_nm'][i]+"','"+doctor['first_nm'][i]+"',NULL);"

    # Add provider preferences.
    print "insert into ProviderPreference (providerNo,startHour,endHour,everyMin,myGroupNo,defaultServiceType,colourTemplate) values('"+doctor['prov_no'][i]+"','8','20','15','Doctors','MFP','deepblue');"
        
    # Add login username and password.
    print "insert into security (user_name,password,provider_no,pin,b_ExpireSet,date_ExpireDate,b_LocalLockSet,b_RemoteLockSet) values('"+doctor['login_nm'][i]+"','96-6838-103-11254-95-6856-9856126-59432-43-1197-9873','"+doctor['prov_no'][i]+"','1320','0',null,'1','1');"
        
    # Add admin roles: 'admin', 'doctor'.
    print "insert into secUserRole(provider_no, role_name, activeyn) values('"+doctor['prov_no'][i]+"', 'admin',1);"
    print "insert into secUserRole(provider_no, role_name, activeyn) values('"+doctor['prov_no'][i]+"', 'doctor',1);"
        
    # Add program_provider: something for accessing notes?
    # Add groupMembers_tbl: something something dark side.
    print "insert into program_provider (program_id,provider_no,role_id) Values('10016','"+doctor['prov_no'][i]+"',2);"
    print "insert into groupMembers_tbl (groupID,provider_No) values ('0','"+doctor['prov_no'][i]+"');"
        
    # Add property: use RX3.
    print "insert into property(name,value,provider_no) values ('rx_use_rx3','yes','"+doctor['prov_no'][i]+"');"
        
    
    # Add default doctor signature 'Dr. [first_name] [last_name].
    print "insert into providerExt(provider_no,signature) values ('"+doctor['prov_no'][i]+"','Dr. "+doctor['first_nm'][i]+" "+doctor['last_nm'][i]+"');"
    

    #add user to address book for future sorting
    # if the doctor's fax field is null
    # then: if the doctor has a clinic id, use the clinic's fax
    # else: use the default clinic fax
    if doctor['clinic'][i]:
        addressbookUsers.append(("<address desc=\""+doctor['last_nm'][i]+","+doctor['first_nm'][i]+"\" id=\""+doctor['prov_no'][i]+"\"/>",doctor['clinic'][i]-1))
    else:
        addressbookUsers.append(("<address desc=\""+doctor['last_nm'][i]+","+doctor['first_nm'][i]+"\" id=\""+doctor['prov_no'][i]+"\"/>", ''))
    
        
    # generate calendar for scheduling.
    scheduleInsert(doctor['prov_no'],2013)
    
    i += 1
                    
print "###########################################################################"
print "#     BEGIN PRINTING STAFF ACCOUNTS"
print "###########################################################################"

i=0
while i < len(staff['last_nm']):
    
    staff['clinic'][i] = int(staff['clinic'][i])
    
    print "###########################################################################"
    print "#     Printing STAFF account for:"+staff['first_nm'][i]+" "+staff['last_nm'][i]
    print "###########################################################################"
    
    # Add nurse account into provider table with values from staff[][].
    print "insert into provider (provider_no,last_name,first_name,provider_type,specialty,team,sex,dob,address,phone,work_phone,email,ohip_no,rma_no,billing_no,hso_no,status,comments,provider_activity,practitionerNo) values ('"+staff['prov_no'][i]+"','"+staff['last_nm'][i]+"','"+staff['first_nm'][i]+"','nurse','Doctors','','',null,'','','','','','','','','1','<xml_p_specialty_code></xml_p_specialty_code><xml_p_billinggroup_no></xml_p_billinggroup_no>','','');"
        
    # Add provider preferences.
    print "insert into ProviderPreference (providerNo,startHour,endHour,everyMin,myGroupNo,defaultServiceType,colourTemplate) values('"+staff['prov_no'][i]+"','8','20','15','Doctors','MFP','deepblue');"
        
    # Add login username and password.
    print "insert into security (user_name,password,provider_no,pin,b_ExpireSet,date_ExpireDate,b_LocalLockSet,b_RemoteLockSet) values('"+staff['login_nm'][i]+"','96-6838-103-11254-95-6856-9856126-59432-43-1197-9873','"+staff['prov_no'][i]+"','1320','0',null,'1','1');"
        
    # Add admin roles: 'admin', 'nurse'.
    print "insert into secUserRole(provider_no, role_name, activeyn) values('"+staff['prov_no'][i]+"', 'admin',1);"
    print "insert into secUserRole(provider_no, role_name, activeyn) values('"+staff['prov_no'][i]+"', 'nurse',1);"
        
    # Add program_provider: something for accessing notes?
    # Add groupMembers_tbl: something something dark side.
    print "insert into program_provider (program_id,provider_no,role_id) Values('10016','"+staff['prov_no'][i]+"',2);"
    print "insert into groupMembers_tbl (groupID,provider_No) values ('0','"+staff['prov_no'][i]+"');"
        

    print "insert into property(name,value,provider_no) values ('rx_use_rx3','yes','"+staff['prov_no'][i]+"');"
    
    print "insert into groupMembers_tbl(groupID,provider_no) values ('0','"+staff['prov_no'][i]+"');"

    #add user to address book for future sorting
    # if the doctor's fax field is null
    # then: if the doctor has a clinic id, use the clinic's fax
    # else: use the default clinic fax
    if staff['clinic'][i]:
        addressbookUsers.append(("<address desc=\""+staff['last_nm'][i]+","+staff['first_nm'][i]+"\" id=\""+staff['prov_no'][i]+"\"/>",staff['clinic'][i]-1))
    else:
        addressbookUsers.append(("<address desc=\""+staff['last_nm'][i]+","+staff['first_nm'][i]+"\" id=\""+staff['prov_no'][i]+"\"/>", ''))

    i += 1

print "###########################################################################"
print "#     BEGIN PRINTING FINAL CHANGES"
print "###########################################################################"

# sort addressbook
addressbookUsers = sorted(addressbookUsers, key=lambda x: (x[1], x[0]))
addressbookFinal = []

#if: clinic['messengerGroupAndTeamName'][0], ie first clinic messengerGroupAndTeamName is null:
#then: assume single doctor clinic, do not appeend separate group

# THIS IS CODE IMPROVMENTS YOU WANT TO MAKE IN PYTHON
# i = 0
# areClinicNamesEmpty = true
# (while (not areCliniNamesEmpty?)
#   (null? clinic['messengerGroupAndTeamName'][i])
#   (+ i 1)
# (if areClinicNamesEmpty
#   addressbookFinal.append("<group desc=\""+re.sub('[!@#$\']', '', clinic['messengerGroupAndTeamName'][0])+"\" id=\"18\">")

if clinic['messengerGroupAndTeamName'][0] != '':
    addressbookFinal.append("<group desc=\""+re.sub('[!@#$\']', '', clinic['messengerGroupAndTeamName'][0])+"\" id=\"18\">")

# THIS IS CODE YOU NEED TO COMMENT ABOUT SO YOU CAN UNDERSTAND IT IN THE FUTURE WHEN YOU ARE TIRED WITH MINIMAL WORK
i =0
while i < len(addressbookUsers):
    addressbookFinal.append(addressbookUsers[i][0])
    if i+1 < len(addressbookUsers):
        if addressbookUsers[i][1] != addressbookUsers[i+1][1]:
            addressbookFinal.append("</group><group desc=\""+re.sub('[!@#$\\\']', '', clinic['messengerGroupAndTeamName'][addressbookUsers[i][1]+1])+"\" id=\""+str(addressbookUsers[i+1][1]+17)+"\">")
    i += 1

# if areClinicNamesEmpty
if clinic['messengerGroupAndTeamName'][0] != '':
    addressbookFinal.append("</group>")

# print groups_tbl for group names.
i=0
while i < len(clinic['messengerGroupAndTeamName']):
    print "insert into groups_tbl (parentID, groupDesc) values ('0', '"+re.sub('[!@#$\']', '', clinic['messengerGroupAndTeamName'][i])+"');"
    i += 1

# update OSCAR Messenger Addressbook.
print "update oscarcommlocations set addressbook='"+addressbookStart+"".join(addressbookFinal)+addressbookEnd+"'"
