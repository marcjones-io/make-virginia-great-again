# make virginia great '''again''' for the first time
from __future__ import division
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

wht_rd_reduced, blk_rd_reduced, ltn_rd_reduced, azn_rd_reduced, ntv_rd_reduced = (0 for i in range(5))
wht_seatbelt_viol, blk_seatbelt_viol, ltn_seatbelt_viol, azn_seatbelt_viol, ntv_seatbelt_viol = (0 for i in range(5))
wht_grand_larceny, blk_grand_larceny, ltn_grand_larceny, azn_grand_larceny, ntv_grand_larceny = (0 for i in range(5))
wht_petty_larceny, blk_petty_larceny, ltn_petty_larceny, azn_petty_larceny, ntv_petty_larceny = (0 for i in range(5))
wht_child_restraint, blk_child_restraint, ltn_child_restraint, azn_child_restraint, ntv_child_restraint = (0 for i in range(5))
wht_poss_ctrl, blk_poss_ctrl, ltn_poss_ctrl, azn_poss_ctrl, ntv_poss_ctrl = (0 for i in range(5))
wht_dwi, blk_dwi, ltn_dwi, azn_dwi, ntv_dwi = (0 for i in range(5))
wht_assault, blk_assault, ltn_assault, azn_assault, ntv_assault = (0 for i in range(5))
wht_susp_license, blk_susp_license, ltn_susp_license, azn_susp_license, ntv_susp_license = (0 for i in range(5))
wht_pub_drunk, blk_pub_drunk, ltn_pub_drunk, azn_pub_drunk, ntv_pub_drunk = (0 for i in range(5))
wht_swear_intox, blk_swear_intox, ltn_swear_intox, azn_swear_intox, ntv_swear_intox = (0 for i in range(5))
wht_mj_poss, blk_mj_poss, ltn_mj_poss, azn_mj_poss, ntv_mj_poss = (0 for i in range(5))
wht_inspect_fail, blk_inspect_fail, ltn_inspect_fail, azn_inspect_fail, ntv_inspect_fail = (0 for i in range(5))
tot_speed, wht_speed, blk_speed, ltn_speed, azn_speed, ntv_speed = (0 for i in range(6))

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
	if entry['Charge'] == 'POSSESSION OF MARIJUANA':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_mj_poss +=1
		elif entry['Race'] == 'Hispanic':
			ltn_mj_poss +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_mj_poss +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_mj_poss +=1
		elif entry['Race'] == 'American Indian':
			ntv_mj_poss +=1
	if entry['Charge'][-2:] == 'SP':
		tot_speed += 1
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_speed +=1
		elif entry['Race'] == 'Hispanic':
			ltn_speed +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_speed +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_speed +=1
		elif entry['Race'] == 'American Indian':
			ntv_speed +=1
	if entry['Charge'] == 'FAIL TO HAVE VEHICLE INSPECTED':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_inspect_fail +=1
		elif entry['Race'] == 'Hispanic':
			ltn_inspect_fail +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_inspect_fail +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_inspect_fail +=1
		elif entry['Race'] == 'American Indian':
			ntv_inspect_fail +=1
	if entry['Charge'] == 'PUBLIC SWEARING/INTOXICATION':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_swear_intox +=1
		elif entry['Race'] == 'Hispanic':
			ltn_swear_intox +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_swear_intox +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_swear_intox +=1
		elif entry['Race'] == 'American Indian':
			ntv_swear_intox +=1
	if entry['Charge'] == 'DRUNK IN PUBLIC':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_pub_drunk +=1
		elif entry['Race'] == 'Hispanic':
			ltn_pub_drunk +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_pub_drunk +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_pub_drunk +=1
		elif entry['Race'] == 'American Indian':
			ntv_pub_drunk +=1
	if entry['Charge'] == 'DRIV UNDER REVO/SUSPENSION':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_susp_license +=1
		elif entry['Race'] == 'Hispanic':
			ltn_susp_license +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_susp_license +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_susp_license +=1
		elif entry['Race'] == 'American Indian':
			ntv_susp_license +=1
	if entry['Charge'] == 'ASSAULT: (MISDEMEANOR)':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_assault +=1
		elif entry['Race'] == 'Hispanic':
			ltn_assault +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_assault +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_assault +=1
		elif entry['Race'] == 'American Indian':
			ntv_assault +=1
	if entry['Charge'] == 'DWI, 1ST':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_dwi +=1
		elif entry['Race'] == 'Hispanic':
			ltn_dwi +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_dwi +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_dwi +=1
		elif entry['Race'] == 'American Indian':
			ntv_dwi +=1
	if entry['Charge'] == 'POSS.OF CONTROLLED SUBSTANCE':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_poss_ctrl +=1
		elif entry['Race'] == 'Hispanic':
			ltn_poss_ctrl +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_poss_ctrl +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_poss_ctrl +=1
		elif entry['Race'] == 'American Indian':
			ntv_poss_ctrl +=1
	if entry['Charge'] == 'CHILD RESTRAINT 7 AND UNDER':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_child_restraint +=1
		elif entry['Race'] == 'Hispanic':
			ltn_child_restraint +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_child_restraint +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_child_restraint +=1
		elif entry['Race'] == 'American Indian':
			ntv_child_restraint +=1
	if entry['Charge'] == 'PETIT LARC <$200 NOT FRM PERSN':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_petty_larceny +=1
		elif entry['Race'] == 'Hispanic':
			ltn_petty_larceny +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_petty_larceny +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_petty_larceny +=1
		elif entry['Race'] == 'American Indian':
			ntv_petty_larceny +=1
if entry['Charge'] == 'GRND LARCENY: >=$200 NOT PERSN':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_grand_larceny +=1
		elif entry['Race'] == 'Hispanic':
			ltn_grand_larceny +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_grand_larceny +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_grand_larceny +=1
		elif entry['Race'] == 'American Indian':
			ntv_grand_larceny +=1
if entry['Charge'] == 'SAFETY BELT VIOLATION':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_seatbelt_viol +=1
		elif entry['Race'] == 'Hispanic':
			ltn_seatbelt_viol +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_seatbelt_viol +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_seatbelt_viol +=1
		elif entry['Race'] == 'American Indian':
			ntv_seatbelt_viol +=1
if entry['Charge'] == 'RD-GENERALLY-MISD':
		if entry['Race'] == 'White Caucasian(Non-Hispanic)':
			wht_rd_reduced +=1
		elif entry['Race'] == 'Hispanic':
			ltn_rd_reduced +=1
		elif entry['Race'] == 'Black(Non-Hispanic)':
			blk_rd_reduced +=1
		elif entry['Race'] ==  'Asian Or Pacific Islander':
			azn_rd_reduced +=1
		elif entry['Race'] == 'American Indian':
			ntv_rd_reduced +=1
	
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

#based om census data
wht_pop_pct = .627
blk_pop_pct = .197
ntv_pop_pct = .005
azn_pop_pct = .065
ltn_pop_pct = .09

charge_porportionality = ctr(race).most_common(5)
output += ' - - -  ETHNICITY BY PORPORTIONALITY: \n'

for each in charge_porportionality:
	if each[0] == 'White Caucasian(Non-Hispanic)':
		output += '		White Caucasian(Non-Hispanic) = ' + str(round(each[1]/len(data)*100,2)) + ' pct of total charged, compared to ' + str(wht_pop_pct*100) + ' pct of total VA population\n'
	elif each[0] == 'Hispanic':
		output += '		Hispanic = ' + str(round(each[1]/len(data)*100,2)) + ' pct of total charged, compared to ' + str(ltn_pop_pct*100) +' pct of total VA population\n'
	elif each[0] == 'Black(Non-Hispanic)':
		output += '		Black(Non-Hispanic) = ' + str(round(each[1]/len(data)*100,2)) + ' pct of total charged, compared to ' + str(blk_pop_pct*100) +' pct of total VA population\n'
	elif each[0] ==  'Asian Or Pacific Islander':
		output += '		Asian Or Pacific Islander = ' + str(round(each[1]/len(data)*100,2)) + ' pct of total charged, compared to ' + str(azn_pop_pct*100) +' pct of total VA population\n'
	elif each[0] == 'American Indian':
		output += '		American Indian = ' + str(round(each[1]/len(data)*100,2)) + ' pct of total charged, compared to ' + str(ntv_pop_pct*100) +' pct of total VA population\n'


output += '\n\n' #str([x[1] in ctr(race).most_common(5)]) + '\n'

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

output += ' - - -  VEHICLE INSPECTION BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_inspect_fail/77941*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_inspect_fail/77941*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_inspect_fail/77941*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_inspect_fail/77941*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_inspect_fail/77941*100,2)) + ' pct of total charged\n\n'

output += ' - - -  DRIV UNDER REVO/SUSPENSION: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_susp_license/44406*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_susp_license/44406*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_susp_license/44406*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_susp_license/44406*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_susp_license/44406*100,2)) + ' pct of total charged\n\n'

output += ' - - -  SPEEDING BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_speed/tot_speed*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_speed/tot_speed*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_speed/tot_speed*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_speed/tot_speed*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_speed/tot_speed*100,2)) + ' pct of total charged\n\n'

output += ' - - -  SAFETY BELT VIOLATION BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_seatbelt_viol/36413*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_seatbelt_viol/36413*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_seatbelt_viol/36413*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_seatbelt_viol/36413*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_seatbelt_viol/36413*100,2)) + ' pct of total charged\n\n'

output += ' - - -  RD-GENERALLY-MISD (RECKLESS DRIVING REDUCED TO MISDEMEANOR) BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_rd_reduced/11174*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_rd_reduced/11174*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_rd_reduced/11174*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_rd_reduced/11174*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_rd_reduced/11174*100,2)) + ' pct of total charged\n\n'

output += ' - - -  POSS OF MARIJUNA BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_mj_poss/27441*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_mj_poss/len(data)*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_mj_poss/27441*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_mj_poss/27441*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_mj_poss/27441*100,2)) + ' pct of total charged\n\n'

output += ' - - -  PUBLIC SWEARING / INTOXICATION: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_swear_intox/17419*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_swear_intox/17419*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_swear_intox/17419*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_swear_intox/17419*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_swear_intox/17419*100,2)) + ' pct of total charged\n\n'

output += ' - - -  DRUNK IN PUBLIC: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_pub_drunk/7617*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_pub_drunk/7617*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_pub_drunk/7617*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_pub_drunk/7617*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_pub_drunk/7617*100,2)) + ' pct of total charged\n\n'

output += ' - - -  ASSAULT: (MISDEMEANOR) BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_assault/12745*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_assault/12745*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_assault/12745*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_assault/12745*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_assault/12745*100,2)) + ' pct of total charged\n\n'

output += ' - - -  1st DWI BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_dwi/15670*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_dwi/15670*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_dwi/15670*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_dwi/15670*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_dwi/15670*100,2)) + ' pct of total charged\n\n'

output += ' - - -  POSS.OF CONTROLLED SUBSTANCE BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_poss_ctrl/12757*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_poss_ctrl/12757*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_poss_ctrl/12757*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_poss_ctrl/12757*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_poss_ctrl/12757*100,2)) + ' pct of total charged\n\n'

output += ' - - -  CHILD RESTRAINT 7 AND UNDER: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_child_restraint/6899*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_child_restraint/6899*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_child_restraint/6899*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_child_restraint/6899*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_child_restraint/6899*100,2)) + ' pct of total charged\n\n'

output += ' - - -  PETIT LARC <$200 NOT FRM PERSN BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_petty_larceny/6333*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_petty_larceny/6333*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_petty_larceny/6333*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_petty_larceny/6333*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_petty_larceny/6333*100,2)) + ' pct of total charged\n\n'

output += ' - - -  GRND LARCENY: >=$200 NOT PERSN BREAKDOWN: \n'
output += '		White Caucasian(Non-Hispanic) = ' + str(round(wht_grand_larceny/10514*100,2)) + ' pct of total charged\n'
output += '		Hispanic = ' + str(round(ltn_grand_larceny/10514*100,2)) + ' pct of total charged\n'
output += '		Black(Non-Hispanic) = ' + str(round(blk_grand_larceny/10514*100,2)) + ' pct of total charged\n'
output += '		Asian Or Pacific Islander = ' + str(round(azn_grand_larceny/10514*100,2)) + ' pct of total charged\n'
output += '		American Indian = ' + str(round(ntv_grand_larceny/10514*100,2)) + ' pct of total charged\n\n'

fips_set = set(court_fips)
output += ' - - -  # COURT_FIPS: ' + str(len(fips_set))+'\n'
output += ' - - -  TOP 25 FIPS: ' + str(ctr(court_fips).most_common(25))+'\n'
# output += ' - - -  COURT FIPS: ' + str(sorted(fips_set))[5:-2] +'\n\n'

code_set = set(codesection)
# output += ' - - -  # CODES VIOLATED: ' + str(len(code_set))+'\n'
output += ' - - -  TOP 25 CODES CITED: ' + str(ctr(codesection).most_common(25))+'\n'
# output += ' - - -  CITATION CODES: ' + str(sorted(code_set))[5:-2] +'\n\n'



filewriter = open('output.txt', 'w')
filewriter.write(output)
filewriter.close
