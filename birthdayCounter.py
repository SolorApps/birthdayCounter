import json

def loadDict():
    with open('birthdays.json', 'r') as f:
        birthdays = dict(json.load(f))
        return birthdays

def birthdayCounter(birthdaysDict):
    monthsDict = {
		'01' : 'January',
		'02' : 'February',
	   	'03' : 'March',
		'04' : 'April',
		'05' : 'May',
		'06' : 'June',
		'07' : 'July',
		'08' : 'August',
		'09' : 'September',
		'10' : 'October',
		'11' : 'November',
		'12' : 'December'
	}
    results = dict()

    for key, val in birthdaysDict.items():
        # extracting the month from the date
        numDate = val[:2]
        date = monthsDict[numDate]
        count = results.get(date)
        if count:
            results[date] = count + 1
        else:
            results[date] = 1
    print results

if __name__ == '__main__':
    birthdays = loadDict()
    birthdayCounter(birthdays)