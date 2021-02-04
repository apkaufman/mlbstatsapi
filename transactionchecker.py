import requests
import pprint

print('Transaction Checker')

day_or_days = input('Do you want to check transactions for more than one day? Answer yes or no. ')

if str.lower(day_or_days) == 'no':
    singleyear = input('Please enter the four-digit year you want to check. ')
    singlemonth = input('Please enter the two-digit month you want to check. ')
    singleday = input('Please enter the two-digit day you want to check. ')
    startdate = singleyear + singlemonth + singleday
    enddate = startdate
else:
    startyear = input('Please enter the four-digit starting year. ')
    startmonth = input('Please enter the two-digit starting month. ')
    startday = input('Please enter the two-digit starting day. ')
    startdate = startyear + startmonth + startday
    endyear = input('Please enter the four-digit ending year. ')
    endmonth = input('Please enter the two-digit ending month. ')
    endday = input('Please enter the two-digit ending day. ')
    enddate = endyear + endmonth + endday

transaction_info = requests.get("http://lookup-service-prod.mlb.com/json/named.transaction_all.bam?sport_code='mlb'&start_date='" + startdate + "'&end_date='" + enddate + "'")

pprint.pprint(transaction_info.json())
