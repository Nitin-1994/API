# importing the requests library 
import requests 
movie_name=str(input("Enter the search string : "))
cmd=str(f"http://www.omdbapi.com/?apikey=88deb2b&t={movie_name}")
print(cmd)
#exit()  
# api-endpoint 


  
# location given here 
#location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
#PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
#r = requests.get(url = URL, params = PARAMS) 
r = requests.get(url = cmd) 
# extracting data in json format 
data = r.json()
#print(data)
try:
	rotten=data["Ratings"][1]
	print(rotten['Source']+" : "+rotten['Value'])
except:
	print("No ratings found")
#for i in rotten:
#	print(i.value(),end="")
