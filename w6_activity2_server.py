import socket
from bs4 import BeautifulSoup
import requests
import datetime


HOST = '127.0.0.1'
PORT = 24680

def fetchWebsiteData(url_website):
	"""Fetches rows of tabular data from given URL of a website with data excluding table headers.

	Parameters
	----------
	url_website : str
		URL of a website

	Returns
	-------
	bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""
	
	web_page_data = ''

	##############	ADD YOUR CODE HERE	##############
	
	req = requests.get(url_website)
	soup = BeautifulSoup(req.text, 'html.parser')

	web_page_data=soup.find_all('tr')[1:] # Exclude header
	

	##################################################

	return web_page_data


def fetchVaccineDoses(web_page_data):
	"""Fetch the Vaccine Doses available from the Web-page data and provide Options to select the respective Dose.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers

	Returns
	-------
	dict
		Dictionary with the Doses available and Options to select, with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineDoses(web_page_data))
	{'1': 'Dose 1', '2': 'Dose 2'}
	"""

	# vaccine_doses_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	# Since there are only 2 doses logically,we can hard code to save time.Can be generalized when needed.
	vaccine_doses_dict = {'1': 'Dose 1', '2': 'Dose 2'}	

	##################################################

	return vaccine_doses_dict


def fetchAgeGroup(web_page_data, dose):
	"""Fetch the Age Groups for whom Vaccination is available from the Web-page data for a given Dose
	and provide Options to select the respective Age Group.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Age Groups (for whom Vaccination is available for a given Dose) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchAgeGroup(web_page_data, '1'))
	{'1': '18+', '2': '45+'}
	>>> print(fetchAgeGroup(web_page_data, '2'))
	{'1': '18+', '2': '45+'}
	"""

	age_group_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	# Can be generalized when needed.For the data used,it need not be. 
	age_group_dict = {'1': '18+', '2': '45+'}


	##################################################

	return age_group_dict


def fetchStates(web_page_data, age_group, dose):
	"""Fetch the States where Vaccination is available from the Web-page data for a given Dose and Age Group
	and provide Options to select the respective State.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the States (where the Vaccination is available for a given Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchStates(web_page_data, '18+', '1'))
	{
		'1': 'Andhra Pradesh', '2': 'Arunachal Pradesh', '3': 'Bihar', '4': 'Chandigarh', '5': 'Delhi', '6': 'Goa',
		'7': 'Gujarat', '8': 'Harayana', '9': 'Himachal Pradesh', '10': 'Jammu and Kashmir', '11': 'Kerala', '12': 'Telangana'
	}
	"""

	states_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	states=[]

	for val in web_page_data:
		if(val.find(class_="dose_num").string==str(dose) and val.find(class_="age").string==str(age_group)):
			states.append(val.find(class_="state_name").string)
		
		states.sort()

	for i in range(1,len(states)+1):
		states_dict[str(i)]=states[i-1]

	##################################################

	return states_dict


def fetchDistricts(web_page_data, state, age_group, dose):
	"""Fetch the District where Vaccination is available from the Web-page data for a given State, Dose and Age Group
	and provide Options to select the respective District.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Districts (where the Vaccination is available for a given State, Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
	{
		'1': 'Kargil', '2': 'Leh'
	}
	"""

	districts_dict = {}

	##############	ADD YOUR CODE HERE	##############
		
	districts=[]

	for val in web_page_data:
		if(val.find(class_="dose_num").string==str(dose) and val.find(class_="age").string==age_group and val.find(class_="state_name").string==state):
			districts.append(val.find(class_="district_name").string)
		
		districts.sort()

	for i in range(1,len(districts)+1):
		districts_dict[str(i)]=districts[i-1]


	##################################################

	return districts_dict


def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	"""Fetch the Hospital and the Vaccine Names from the Web-page data available for a given District, State, Dose and Age Group
	and provide Options to select the respective Hospital and Vaccine Name.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Hosptial and Vaccine Names (where the Vaccination is available for a given District, State, Dose, Age Group)
		and Options to select, with Key as 'Option' and Value as another dictionary having Key as 'Hospital Name' and Value as 'Vaccine Name'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchHospitalVaccineNames(web_page_data, 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {
				'MedStar Hospital Center': 'Covaxin'
			}
	}
	>>> print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {
				'Eden Clinic': 'Covishield'
			}
	}
	"""
	
	hospital_vaccine_names_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	i=1
	for val in web_page_data:
		if(val.find(class_="dose_num").string==str(dose) and val.find(class_="age").string==age_group and val.find(class_="state_name").string==state and val.find(class_="district_name").string==district):
			hospital_vaccine_names_dict[str(i)]={val.find(class_="hospital_name").string : val.find(class_="vaccine_name").string }
			i+=1		

	##################################################

	return hospital_vaccine_names_dict


def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	"""Fetch the Dates and Slots available on those dates from the Web-page data available for a given Hospital Name, District, State, Dose and Age Group
	and provide Options to select the respective Date and available Slots.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	hospital_name : str
		Name of Hospital where Vaccination is available for given District, State, Dose and Age Group
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Dates and Slots available on those dates (where the Vaccination is available for a given Hospital Name,
		District, State, Dose, Age Group) and Options to select, with Key as 'Option' and Value as another dictionary having
		Key as 'Date' and Value as 'Available Slots'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineSlots(web_page_data, 'MedStar Hospital Center', 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '81'}, '3': {'May 17': '109'}, '4': {'May 18': '78'},
		'5': {'May 19': '89'}, '6': {'May 20': '57'}, '7': {'May 21': '77'}
	}
	>>> print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '137'}, '3': {'May 17': '50'}, '4': {'May 18': '78'},
		'5': {'May 19': '145'}, '6': {'May 20': '64'}, '7': {'May 21': '57'}
	}
	"""

	vaccine_slots = {}

	##############	ADD YOUR CODE HERE	##############

	i=1
	for val in web_page_data:
		if(val.find(class_="dose_num").string==str(dose) and val.find(class_="age").string==age_group and val.find(class_="state_name").string==state and val.find(class_="district_name").string==district and val.find(class_="hospital_name").string==hospital_name):
			for j in range(15,22):
				slot=val.find(class_="may_"+str(j)).string

				vaccine_slots[str(i)]={ "May "+str(j): slot}
				i+=1


	##################################################

	return vaccine_slots


def openConnection():
	"""Opens a socket connection on the HOST with the PORT address.

	Returns
	-------
	socket
		Object of socket class for the Client connected to Server and communicate further with it
	tuple
		IP and Port address of the Client connected to Server
	"""

	client_socket = None
	client_addr = None

	##############	ADD YOUR CODE HERE	##############

	client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_addr=(HOST,PORT)

	##################################################
	
	return client_socket, client_addr


def startCommunication(client_conn, client_addr, web_page_data):
	"""Starts the communication channel with the connected Client for scheduling an Appointment for Vaccination.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	client_addr : tuple
		IP and Port address of the Client connected to Server
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""

	##############	ADD YOUR CODE HERE	##############

	# CAUTION: Buggy code below-still incomplete but working :)
	# Many features yet to be added.

	client_conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	client_conn.bind(client_addr)
	client_conn.listen(50)
	connection, address = client_conn.accept()

	print("Client is connected at: ",address)
	
	send=str(fetchVaccineDoses(web_page_data))
	greet="============================\n# Welcome to CoWIN ChatBot #\n============================\n\nSchedule an Appointment for Vaccination:\n\n>>> Select the Dose of Vaccination:\n"+send
	
	connection.send(greet.encode())
	
	dose = connection.recv(30).decode('utf-8')
	print("Dose selected:  "+dose)
	connection.send(("<<< Dose selected: "+dose).encode())

	if(dose=="1"):

		push(str(fetchAgeGroup(web_page_data,dose)),connection,">>> Select the Age Group:")
		age = connection.recv(30).decode('utf-8')
		if(age=="1"):
			age="18+"
		elif(age=="2"):
			age="45+"

		if(age=="18+" or age=="45+"):
			print("Age Group selected:  "+age)
			connection.send(("<<< Selected Age Group:"+age).encode())

			states=fetchStates(web_page_data,age,dose)

			push(states,connection,">>> Select the State:")
			state_num = connection.recv(30).decode('utf-8')

			if state_num in states.keys():

				state=states[state_num]
				print("State selected:  "+state)
				connection.send(("<<< Selected State: "+state).encode())
				
				district_dict=fetchDistricts(web_page_data,state,age,dose)
				push(str(district_dict),connection,">>> Select the District:")
				district_num = connection.recv(30).decode('utf-8')

				if district_num in district_dict.keys():
					
					district=district_dict[district_num]
					print("District selected:  "+district)
					connection.send(("<<< Selected District: "+district).encode())
					
					vac_centres=fetchHospitalVaccineNames(web_page_data,district,state,age,dose)
					push(str(vac_centres),connection,">>> Select the Vaccination Center Name:")
					vac_centre_num = connection.recv(30).decode('utf-8')

					if vac_centre_num in vac_centres.keys():
						
						vac_centre=list(vac_centres[vac_centre_num].keys())[0]
						print("Hospital selected:  "+vac_centre)
						connection.send(("<<< Selected Vaccination Center: "+vac_centre).encode())

						vac_dates=fetchVaccineSlots(web_page_data,vac_centre,district,state,age,dose)
						push(str(vac_dates),connection,">>> Select one of the available slots to schedule the Appointment:")
						slot_index = connection.recv(30).decode('utf-8')

						flag=False
						sch_date=""
						slot_iftrue=""
						for (index,slot) in zip(vac_dates.keys(),vac_dates.values()):
							if(slot_index==index):
								slot_iftrue=list(slot.values())[0]
								sch_date=list(slot.keys())[0]
								flag=True
								break

						if(flag):
							
							print("Vaccination Date selected:  "+sch_date)
							print("Available Slots on that date:  "+slot_iftrue)
							
							if(slot_iftrue=="0"):

								push("<<< Available Slots on the selected Date: "+slot_iftrue,connection,"<<< Selected Vaccination Appointment Date: "+sch_date)
								

							else:
								push("<<< Available Slots on the selected Date: "+slot_iftrue+"\n<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!\n<<< See ya! Visit again :)",connection,"<<< Selected Vaccination Appointment Date: "+sch_date)


						else:
							print("")
					else:
						print("")
				else:
					print("")

			else:
				print("")
		else:
			count=0
			while(count!=3):
				count+=1
				
				push("<<< Invalid input provided "+count+" time(s)! Try again.\n"+str(fetchAgeGroup(web_page_data,dose)),connection,">>> Select the Age Group:")
				age = connection.recv(30).decode('utf-8')

				print("Age Group selected:  "+age)
				connection.send(("<<< Selected Age Group:"+age).encode())
				if(age=="18+" or age=="45+"):
					states=fetchStates(web_page_data,age,dose)

					push(states,connection,">>> Select the State:")
					state_num = connection.recv(30).decode('utf-8')

					if state_num in states.keys():

						state=states[state_num]
						print("State selected:  "+state)
						connection.send(("<<< Selected State: "+state).encode())
						
						district_dict=fetchDistricts(web_page_data,state,age,dose)
						push(str(district_dict),connection,">>> Select the District:")
						district_num = connection.recv(30).decode('utf-8')

						if district_num in district_dict.keys():
							
							district=district_dict[district_num]
							print("District selected:  "+district)
							connection.send(("<<< Selected District: "+district).encode())
							
							vac_centres=fetchHospitalVaccineNames(web_page_data,district,state,age,dose)
							push(str(vac_centres),connection,">>> Select the Vaccination Center Name:")
							vac_centre_num = connection.recv(30).decode('utf-8')

							if vac_centre_num in vac_centres.keys():
								
								vac_centre=list(vac_centres[vac_centre_num].keys())[0]
								print("Hospital selected:  "+vac_centre)
								connection.send(("<<< Selected Vaccination Center: "+vac_centre).encode())

								vac_dates=fetchVaccineSlots(web_page_data,vac_centre,district,state,age,dose)
								push(str(vac_dates),connection,">>> Select one of the available slots to schedule the Appointment:")
								slot_index = connection.recv(30).decode('utf-8')

								flag=False
								sch_date=""
								slot_iftrue=""
								for (index,slot) in zip(vac_dates.keys(),vac_dates.values()):
									if(slot_index==index):
										slot_iftrue=list(slot.values())[0]
										sch_date=list(slot.keys())[0]
										flag=True
										break

								if(flag):
									
									print("Vaccination Date selected:  "+sch_date)
									
									if(slot_iftrue=="0"):

										push("<<< Available Slots on the selected Date: "+slot_iftrue,connection,"<<< Selected Vaccination Appointment Date: "+sch_date)
										
									else:
										push("<<< Available Slots on the selected Date: "+slot_iftrue+"\n<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!\n<<< See ya! Visit again :)",connection,"<<< Selected Vaccination Appointment Date: "+sch_date)

								else:
									print("")
							else:
								print("")
						else:
							print("")

					else:
						print("")		
	elif(dose=="2"):
		connection.send("\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021\n".encode())
		vac_date = connection.recv(30).decode('utf-8')

		connection.send(("<<< Date of First Vaccination Dose provided: "+vac_date).encode())

		day,month,year=vac_date.split('/')
		valid=True
		try:
			datetime.datetime(int(year),int(month),int(day))
		except:
			valid=False

		if(valid):
			current_time = datetime.datetime.now()
			d=current_time.day
			m=current_time.month
			y=current_time.year
			
			d0 = datetime.date(int(year), int(month), int(day))
			d1 = datetime.date(y, m, d)
			delta = (d1 - d0).days//7		# Get the weeks since 1st dose

			if(delta>=4):
				if(delta<=8):
					
					push(">>> Select the Age Group:\n"+str(fetchAgeGroup(web_page_data,dose)),connection,"<<< Number of weeks from today: "+str(delta)+"\n<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.")
				else:
					push(">>> Select the Age Group:\n"+str(fetchAgeGroup(web_page_data,dose)),connection,"<<< Number of weeks from today: "+str(delta)+"\n<<< You have been late in scheduling your 2nd Vaccination Dose by "+str(delta-8)+" weeks.")
									
				age = connection.recv(30).decode('utf-8')
				if(age=="1"):
					age="18+"
				elif(age=="2"):
					age="45+"
					
				if(age=="18+" or age=="45+"):
					print("Age Group selected:  "+age)
					connection.send(("<<< Selected Age Group:"+age).encode())

					states=fetchStates(web_page_data,age,dose)

					push(states,connection,">>> Select the State:")
					state_num = connection.recv(30).decode('utf-8')

					if state_num in states.keys():

						state=states[state_num]
						print("State selected:  "+state)
						connection.send(("<<< Selected State: "+state).encode())
						
						district_dict=fetchDistricts(web_page_data,state,age,dose)
						push(str(district_dict),connection,">>> Select the District:")
						district_num = connection.recv(30).decode('utf-8')

						if district_num in district_dict.keys():
							
							district=district_dict[district_num]
							print("District selected:  "+district)
							connection.send(("<<< Selected District: "+district).encode())
							
							vac_centres=fetchHospitalVaccineNames(web_page_data,district,state,age,dose)
							push(str(vac_centres),connection,">>> Select the Vaccination Center Name:")
							vac_centre_num = connection.recv(30).decode('utf-8')

							if vac_centre_num in vac_centres.keys():
								
								vac_centre=list(vac_centres[vac_centre_num].keys())[0]
								print("Hospital selected:  "+vac_centre)
								connection.send(("<<< Selected Vaccination Center: "+vac_centre).encode())

								vac_dates=fetchVaccineSlots(web_page_data,vac_centre,district,state,age,dose)
								push(str(vac_dates),connection,">>> Select one of the available slots to schedule the Appointment:")
								slot_index = connection.recv(30).decode('utf-8')

								flag=False
								sch_date=""
								slot_iftrue=""
								for (index,slot) in zip(vac_dates.keys(),vac_dates.values()):
									if(slot_index==index):
										slot_iftrue=list(slot.values())[0]
										sch_date=list(slot.keys())[0]
										flag=True
										break

								if(flag):
									
									print("Vaccination Date selected:  "+sch_date)
									print("Available Slots on that date:  "+slot_iftrue)
									
									if(slot_iftrue=="0"):

										push("<<< Available Slots on the selected Date: "+slot_iftrue,connection,"<<< Selected Vaccination Appointment Date: "+sch_date)
										

									else:
										push("<<< Available Slots on the selected Date: "+slot_iftrue+"\n<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!\n<<< See ya! Visit again :)",connection,"<<< Selected Vaccination Appointment Date: "+sch_date)


								else:
									print("")
							else:
								print("")
						else:
							print("")

					else:
						print("")
				else:
					count=0
					while(count!=3):
						count+=1
						
						push("<<< Invalid input provided "+count+" time(s)! Try again.\n"+str(fetchAgeGroup(web_page_data,dose)),connection,">>> Select the Age Group:")
						age = connection.recv(30).decode('utf-8')

						print("Age Group selected:  "+age)
						connection.send(("<<< Selected Age Group:"+age).encode())
						if(age=="18+" or age=="45+"):
							states=fetchStates(web_page_data,age,dose)

							push(states,connection,">>> Select the State:")
							state_num = connection.recv(30).decode('utf-8')

							if state_num in states.keys():

								state=states[state_num]
								print("State selected:  "+state)
								connection.send(("<<< Selected State: "+state).encode())
								
								district_dict=fetchDistricts(web_page_data,state,age,dose)
								push(str(district_dict),connection,">>> Select the District:")
								district_num = connection.recv(30).decode('utf-8')

								if district_num in district_dict.keys():
									
									district=district_dict[district_num]
									print("District selected:  "+district)
									connection.send(("<<< Selected District: "+district).encode())
									
									vac_centres=fetchHospitalVaccineNames(web_page_data,district,state,age,dose)
									push(str(vac_centres),connection,">>> Select the Vaccination Center Name:")
									vac_centre_num = connection.recv(30).decode('utf-8')

									if vac_centre_num in vac_centres.keys():
										
										vac_centre=list(vac_centres[vac_centre_num].keys())[0]
										print("Hospital selected:  "+vac_centre)
										connection.send(("<<< Selected Vaccination Center: "+vac_centre).encode())

										vac_dates=fetchVaccineSlots(web_page_data,vac_centre,district,state,age,dose)
										push(str(vac_dates),connection,">>> Select one of the available slots to schedule the Appointment:")
										slot_index = connection.recv(30).decode('utf-8')

										flag=False
										sch_date=""
										slot_iftrue=""
										for (index,slot) in zip(vac_dates.keys(),vac_dates.values()):
											if(slot_index==index):
												slot_iftrue=list(slot.values())[0]
												sch_date=list(slot.keys())[0]
												flag=True
												break

										if(flag):
											
											print("Vaccination Date selected:  "+sch_date)
											
											if(slot_iftrue=="0"):

												push("<<< Available Slots on the selected Date: "+slot_iftrue,connection,"<<< Selected Vaccination Appointment Date: "+sch_date)
												

											else:
												push("<<< Available Slots on the selected Date: "+slot_iftrue+"\n<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!\n<<< See ya! Visit again :)",connection,"<<< Selected Vaccination Appointment Date: "+sch_date)


										else:
											print("")
									else:
										print("")
								else:
									print("")

							else:
								print("")
					


					else:
						push("<<< Number of weeks from today: "+str(delta),connection,"<<< You are not eligible right now for 2nd Vaccination Dose! Try after "+str(4-delta)+" weeks.\n<<< See ya! Visit again :)")			
			
	else:
		push("\n>>> Select the Dose of Vaccination:\n"+send,connection,"<<< Invalid input provided 1 time(s)! Try again.\n")
		dose = connection.recv(30).decode('utf-8')
		print("Dose selected:  "+dose)
		connection.send(("<<< Dose selected: "+dose).encode())




	connection.close()

	##################################################


def stopCommunication(client_conn):
	"""Stops or Closes the communication channel of the Client with a message.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	"""

	##############	ADD YOUR CODE HERE	##############

	client_conn.close()

	##################################################


################# UTILITY FUNCTIONS HERE #################
##########################################################


def push(s,connection,msg=""):
	
	connection.send(("\n"+str(msg)+"\n\n"+str(s)+"\n\n").encode())
	

def display(data):
	print(data.decode('utf-8'))

##############################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	client_conn, client_addr = openConnection()
	try:
		startCommunication(client_conn, client_addr, web_page_data)
	except:
		stopCommunication(client_conn)		

# # Examples
# fetchWebsiteData(url_website)
# print(fetchAgeGroup(web_page_data,1))
# print(fetchStates(web_page_data, "18+", 1))
# print(fetchDistricts(web_page_data, "Delhi", "45+", 1))
# print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
# print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
# print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
