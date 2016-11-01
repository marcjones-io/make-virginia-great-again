# make virginia great '''again''' for the first time

import csv

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

#variables im interested
num_arrests, num_felonies, num_misdemeanors, jan, feb, mar, apr, may, jun, jul, aug, sep, octb, nov, dec = (0 for i in range(15))

#read data into lists
def efficiently_read(entry):
	# written by:
	# for things in somelist:
	# print str(things).lower()+'.append(entry[\''+str(things)+'\''+'])'
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
	efficiently_read(entry)
	if entry['ArrestDate'] != '':
		num_arrests += 1
	if entry['CaseType'] == 'Felony':
		num_felonies += 1
	elif entry['CaseType'] == 'Misdemeanor':
		num_misdemeanors += 1
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

output = 'Information on VA District Court Data Set\n\n'

output += '# of categories: ' + str(len(categories))+'\n'
output += 'categories: ' + str(categories)[1:-1] + '\n\n'

output += '# of genders: ' + str(len(set(gender)))+'\n'
output += 'genders: ' + str(set(gender))[5:-2] +'\n\n'

output += '# of ethnicities: ' + str(len(set(race)))+'\n'
output += 'ethnicities: ' + str(set(race))[5:-2] +'\n\n'

output += '# of entries/charges: ' + str(len(data)) + '\n'
output += '# of charges by month: \n' + \
		'		jan - '+str(jan)+'\n		feb - '+str(feb)+'\n		mar - '+str(mar)+\
		'\n		apr - '+str(apr)+'\n 		may - '+str(may)+'\n		jun - '+str(jun)+\
		'\n		jul - '+str(jul)+'\n		aug - '+str(aug)+'\n		sep - '+str(sep)+\
		'\n		oct - '+str(octb)+'\n		nov - '+str(nov)+'\n		dec - '+str(dec)+'\n\n'

output += '# of plaintiffs: ' + str(len(set(name)))+'\n'
output += '# of arrests: ' + str(num_arrests)+'\n'
output += '# of complainants: ' + str(len(set(complainant)))+'\n\n'

output += '# of felonies charged: ' + str(num_felonies) +'\n'
output += '# of misdemeanors charged: ' + str(num_misdemeanors)+'\n\n'

output += '# of codes violated: ' + str(len(set(codesection)))+'\n'
output += 'citation codes: ' + str(sorted(set(codesection)))[5:-2] +'\n\n'

filewriter = open('output.txt', 'w')
filewriter.write(output)
filewriter.close
