from datetime import *

def get_date_diff():
	while True:
		date1 = ''
		date2 = ''
		while True:
			date1 = input('Input date1 (YYYY-mm-dd, "q" to quit):')
			if date1 == 'Q' or date1 == 'q':
				return
			date2 = input('Input date2 (YYYY-mm-dd, "q" to quit):')
			if date2 == 'Q' or date2 == 'q':
				return
			try:
				date1 = datetime.strptime(date1, '%Y-%m-%d')
				date2 = datetime.strptime(date2, '%Y-%m-%d')
				break
			except Exception:
				print('Value error. Please try again.')
		duration = abs(date1 - date2)
		print('The difference between ' + str(date1.year) + '-' + str(date1.month) + '-' + str(date1.day) + ' and ' + str(date2.year) + '-' + str(date2.month) + '-' + str(date2.day) + ' is: ' + str(duration.days) + ' days.')	
