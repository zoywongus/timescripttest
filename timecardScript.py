from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from reportlab.lib.units import inch
import datetime
import os.path
dictpeople = {"Dan": {
					"firstname": "Dan",
					"lastname": "Gregatti",
					"phone":"4163067438",
					},
			"Kelly": {
					"firstname":"Kelly",
					"lastname":"Smyth",
					"phone":None
					}
			}
 

date_file = "data.jpg"
sheetimg = 'timecardtest.jpg'
greysheetimg = 'timecardtestbw.jpg'
total_daily_hour_height = 229
date_daily_height = 418
def import_data():
	'''
	personname = input("Enter your name [firstname] [lastname]: ")
	idnum = input("Enter your 6-digit employee number: ")
	firstname = personname.split(' ')[0]
	lastname = personname.split(' ')[1]
	signperson = input("If you want Kelly to sign, enter the answer for (23 * 3), enter any other string if you want Dan the Man who can drive a van to sign:  ")
	if signperson == "69":
		signer = "Kelly"
	else:
		signer = "Dan"
		'''
	firstname = 'hello'
	lastname = 'world'
	signer = "Dan"
	idnum = '1337'
	generate_timesheet(firstname , lastname, idnum, signer)


def generate_timesheet(firstname, lastname, idnum, signer):
	dayofweek = datetime.datetime.today().weekday()
	startday = datetime.datetime.now() - datetime.timedelta(days=(7+dayofweek))
	endday = startday + datetime.timedelta(days=11)
	datestring = str(startday.month).zfill(2) + "/" + str(startday.day).zfill(2) + "/" + str(startday.year)[2:]
	enddatestring = str(endday.month).zfill(2) + "/" + str(endday.day).zfill(2) + "/" + str(endday.year)[2:]
	randomstr = hash(str(datetime.datetime.now().second + datetime.datetime.now().minute + datetime.datetime.now().hour) + 'abcdefg')
	pdf_file_name = firstname + '_' + lastname + '_timesheet' + '_generated-on-' + str(randomstr) + '.pdf'

	c = canvas.Canvas(pdf_file_name,pagesize=landscape(letter))
	c.drawImage(greysheetimg,0,20,width=11*inch,height=7.5*inch)

	c.drawImage("dansigbw.jpg",183,25,width=3.7*inch,height=0.8*inch)

	#name
	c.setFont("Times-Bold", 13, leading=None)
	c.drawString(194,477,lastname + ", " + firstname)
	#employeenum
	c.drawString(642,476,idnum)
	#payendingdate
	c.drawString(198,451,enddatestring)

	c.setFont("Times-Roman", 13, leading=None) #change to normal font
	
	#signaturemyself
	c.drawString(230,96,firstname + ' ' + lastname)


	#dateofmysignature
	c.drawString(642,94,datestring)
	
	#phone number
	c.setFont("Times-Roman", 11, leading=None)
	if (signer == "Dan"):
		c.drawString(500,66,dictpeople['Dan']['phone'])

#samples______________________________________
	#datesample
	c.setFont("Times-Roman", 8, leading=None)
	c.drawString(193,date_daily_height,'06/22/99')

	#hours sample
	c.setFont("Times-Bold", 10, leading=None)
	c.drawString(207,total_daily_hour_height,"8")
	c.drawString(207+36,total_daily_hour_height, "8")

	#regularhoursworked sample
	c.drawString(207,397,'8')

	#totalscolumn test
	c.drawString(755,397,'72')
	c.drawString(755,total_daily_hour_height, '80')


	#TODO DON'T FORGET SPECIAL COLOR FONT FRIDAY
	
	c.showPage()

	c.save()
	print('file ' + str(pdf_file_name) + ' was successfully generated! Do not be a degenerate!')
import_data()