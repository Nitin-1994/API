# importing the requests library 
import requests 
def MovieTitle():
	movie_name=str(input("Enter the search string : "))
	
	cmd=str(f"http://www.omdbapi.com/?apikey=88deb2b&t={movie_name}")
	#print(cmd)
	return cmd

#MovieTitle()
########################################################################
#exit()  
# api-endpoint 
# location given here 
#location = "delhi technological university"
# defining a params dict for the parameters to be sent to the API 
#PARAMS = {'address':location} 
# sending get request and saving the response as response object 
#r = requests.get(url = URL, params = PARAMS) 
###############################################################################

def main():
	while True:
		cmd=MovieTitle()
		r = requests.get(url = cmd) 
# extracting data in json format 
		data = r.json()
		if 'Error' in data:
			print("Wrong Input,try again")

			truth_value=input("Do you want to retype ? : ")
			if truth_value != 'y':
				exit()
			continue
		
			
		else:
			try:
				Ratings=data["Ratings"]
				for i in Ratings:
					if 'Rotten Tomatoes' in i['Source']:
						rotten=i
					
				Percent=rotten['Value']
				if int(Percent[:len(Percent)-1]) <30:
					print("You can watch movie as rotten tomatoes is only",rotten['Value'])
				else:
					print("Don't watch as it does not seems to be good movie and rootem tomatoes value is",rotten['Value'])

			except:
				print("No ratings found")
			exit()


if __name__== "__main__":
	main()
