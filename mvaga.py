# make virginia great '''again''' for the first time

import csv
from collections import Counter as ctr

#open csv files
data = []
filename = 'court_data/criminal_district_court_cases_2015_'
for i in range(1,13):
	data += list(csv.DictReader(open(filename+str(i)+'.csv')))

#init std categories to lists
aka1,aka2,address,amendedcasetype,amendedcharge,amendedcode,arrestdate,casenumber,casestatus,casetype,charge,\
classs,codesection,complainant,costs,dob,defenseattorney,fileddate,finaldisposition,fine,finecostsdue,\
finecostspaid,finecostspaiddate,gender,locality,name,offensedate,operatorlicenserestrictioncodes,\
operatorlicensesuspensiontimedays,probationstarts,probationtimedays,probationtype,race,restrictionenddate,\
restrictionstartdate,sentencesuspendedtimedays,sentencetimedays,status,vasap,court_fips = ([] for i in range(40))

#variables im interested in
finescost_revenue, num_arrests, num_felonies, num_misdemeanors, num_amended, jan, feb, mar, apr, may, \
jun, jul, aug, sep, octb, nov, dec = (0 for i in range(17))

#read data into lists
def read_entries(entry):
	amendedcode.append(entry['AmendedCode'])
	complainant.append(entry['Complainant'])
	locality.append(entry['Locality'])
	dob.append(entry['DOB'])
	charge.append(entry['Charge'])
	probationtimedays.append(entry['ProbationTimeDays'])
	arrestdate.append(entry['ArrestDate'])
	name.append(entry['Name'])
	status.append(entry['Status'])
	amendedcasetype.append(entry['AmendedCaseType'])
	casenumber.append(entry['CaseNumber'])
	restrictionenddate.append(entry['RestrictionEndDate'])
	casestatus.append(entry['CaseStatus'])
	operatorlicensesuspensiontimedays.append(entry['OperatorLicenseSuspensionTimeDays'])
	finaldisposition.append(entry['FinalDisposition'])
	address.append(entry['Address'])
	defenseattorney.append(entry['DefenseAttorney'])
	operatorlicenserestrictioncodes.append(entry['OperatorLicenseRestrictionCodes'])
	classs.append(entry['Class'])
	aka1.append(entry['AKA1'])
	codesection.append(entry['CodeSection'])
	offensedate.append(entry['OffenseDate'])
	casetype.append(entry['CaseType'])
	finecostspaid.append(entry['FineCostsPaid'])
	aka2.append(entry['AKA2'])
	restrictionstartdate.append(entry['RestrictionStartDate'])
	probationstarts.append(entry['ProbationStarts'])
	gender.append(entry['Gender'])
	costs.append(entry['Costs'])
	sentencetimedays.append(entry['SentenceTimeDays'])
	finecostspaiddate.append(entry['FineCostsPaidDate'])
	probationtype.append(entry['ProbationType'])
	amendedcharge.append(entry['AmendedCharge'])
	race.append(entry['Race'])
	finecostsdue.append(entry['FineCostsDue'])
	court_fips.append(entry['court_fips'])
	vasap.append(entry['VASAP'])
	fine.append(entry['Fine'])
	sentencesuspendedtimedays.append(entry['SentenceSuspendedTimeDays'])
	fileddate.append(entry['FiledDate'])
	
for entry in data:
	read_entries(entry)
	# if entry['FineCostsPaid'] == 'Paid':
	# 	finescost_revenue += float(str(entry['Fine']).strip().strip('$').strip()) + float(str(entry['Costs']).strip().strip('$').strip())
	if entry['ArrestDate'] != '':
		num_arrests += 1
	if entry['CaseType'] == 'Felony':
		num_felonies += 1
	elif entry['CaseType'] == 'Misdemeanor':
		num_misdemeanors += 1
	if entry['AmendedCharge'] != '':
		num_amended += 1
	if str(entry['FiledDate'])[:2] == '01':
		jan += 1
	elif str(entry['FiledDate'])[:2] == '02':
		feb += 1
	elif str(entry['FiledDate'])[:2] == '03':
		mar += 1
	elif str(entry['FiledDate'])[:2] == '04':
		apr += 1
	elif str(entry['FiledDate'])[:2] == '05':
		may += 1
	elif str(entry['FiledDate'])[:2] == '06':
		jun += 1
	elif str(entry['FiledDate'])[:2] == '07':
		jul += 1
	elif str(entry['FiledDate'])[:2] == '08':
		aug += 1
	elif str(entry['FiledDate'])[:2] == '09':
		sep += 1
	elif str(entry['FiledDate'])[:2] == '10':
		octb += 1
	elif str(entry['FiledDate'])[:2] == '11':
		nov += 1
	elif str(entry['FiledDate'])[:2] == '12':
		dec += 1
	
#identify all the keys in the dict and 
categories = ([x for x in data[0].keys()])

output = 'Univestigated Summary VA District Court Data Set 			by Marc Jones\n\n'

output += ' - - -  # CATEGORIES: ' + str(len(categories))+'\n'
output += ' - - -  CATEGORIES: ' + str(categories)[1:-1] + '\n\n'

#do we respect lgbtq people?
gender_set =  set(gender)
output += ' - - -  # GENDERS: ' + str(len(gender_set))+'\n'
output += ' - - -  GENDERS: ' + str(gender_set)[5:-2] +'\n\n'

#find top 5-1000 or so of following categories
ethnic_set = set(race)
output += ' - - -  # ETHNICITIES: ' + str(len(ethnic_set))+'\n'
output += ' - - -  ETHNICITIES: ' + str(ethnic_set)[5:-2] +'\n'
output += ' - - -  TOP 5 ETHNICITIES: ' + str(ctr(race).most_common(5))+'\n\n'
#perhaps more defined ethnic categories can help us identify who needs better serves

#why some months over others
output += ' - - -  # ENTRIES/CHARGES: ' + str(len(data)) + '\n'
output += ' - - -  # CHARGES BY MONTH: \n' + \
		'		jan - '+str(jan)+'\n		feb - '+str(feb)+'\n		mar - '+str(mar)+\
		'\n		apr - '+str(apr)+'\n 		may - '+str(may)+'\n		jun - '+str(jun)+\
		'\n		jul - '+str(jul)+'\n		aug - '+str(aug)+'\n		sep - '+str(sep)+\
		'\n		oct - '+str(octb)+'\n		nov - '+str(nov)+'\n		dec - '+str(dec)+'\n\n'
# output += ' - - -  $ REVENUE GENERATED: $' + str(finescost_revenue) + '\n\n'


output += ' - - -  # PLAINTIFFS: ' + str(len(set(name)))+'\n'
output += ' - - -  # ARRESTS: ' + str(num_arrests)+'\n'
output += ' - - -  # COMPLAINANTS: ' + str(len(set(complainant)))+'\n'
output += ' - - -  TOP 25 COMPLAINANTS: ' + str(ctr(complainant).most_common(25))+'\n\n'

output += ' - - -  # FELONIES CHARGED: ' + str(num_felonies) +'\n'
output += ' - - -  # MISDEMEANORS CHARGED: ' + str(num_misdemeanors)+'\n'
output += ' - - -  # AMENDED CHARGES: ' + str(num_amended)+'\n'
output += ' - - -  TOP 50 CHARGES: ' + str(ctr(charge).most_common(50))+'\n\n'

fips_set = set(court_fips)
output += ' - - -  # COURT_FIPS: ' + str(len(fips_set))+'\n'
output += ' - - -  TOP 25 FIPS: ' + str(ctr(court_fips).most_common(25))+'\n'
output += ' - - -  COURT FIPS: ' + str(sorted(fips_set))[5:-2] +'\n\n'

code_set = set(codesection)
output += ' - - -  # CODES VIOLATED: ' + str(len(code_set))+'\n'
output += ' - - -  TOP 25 CODES CITED: ' + str(ctr(codesection).most_common(25))+'\n'
output += ' - - -  CITATION CODES: ' + str(sorted(code_set))[5:-2] +'\n\n'

filewriter = open('output.txt', 'w')
filewriter.write(output)
filewriter.close
