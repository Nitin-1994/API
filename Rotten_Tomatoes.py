import requests
from goto import with_goto

@with_goto
def main():
    label .begin
    rotten_value = None

    movie_name=str(input("Enter the search string : ")).strip()
    movie_url = f"http://www.omdbapi.com/?apikey=88deb2b&t={movie_name}"
    r = requests.get(movie_url)

# extracting data in json format

    data = r.json()
    try:
        rating = data['Ratings']
    except:
        print("The is no such movie, Do you want to try again ?")
        output=input("Enter y/n :")
        if output=="y":
            goto .begin
        else:
           goto .end

    for i in range(len(rating)):
        if rating[i]['Source'] == 'Rotten Tomatoes':
            rotten_value = rating[i]['Value']

    print(f"Movie Name : {movie_name} \nRotten Tomatoes : {rotten_value}")

    if rotten_value:
        rotten_value=int(rotten_value[:-1])
        if rotten_value > 30:
            print("Movies has high rating of Rotten Tomatoes, don't watch")
        else:
            print("Movies has low rating of Rotten Tomatoes, you can watch")
    else:
        print("Rotten tomatoes value is not present")

    label .end

main()


