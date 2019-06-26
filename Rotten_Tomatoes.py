import requests
from goto import with_goto
import sys

@with_goto
def main():
    rotten_value = None

    movie_name=sys.argv[1:]
    movie_url = f"http://www.omdbapi.com/?apikey=88deb2b&t={movie_name}"
    r = requests.get(movie_url)

# extracting data in json format

    data = r.json()
    try:
        rating = data['Ratings']
    except:
        print("The is no such movie, Try again")
        goto .end

    for i in range(len(rating)):
        if rating[i]['Source'] == 'Rotten Tomatoes':
            rotten_value = rating[i]['Value']

    print(f"Movie Name : {movie_name} \nRotten Tomatoes : {rotten_value}")

    if rotten_value:
        rotten_value=int(rotten_value[:-1])
        if rotten_value > 30:
            print("Movies has high rating on Rotten Tomatoes, so it could be good movie to watch")
        else:
            print("Movies has low rating on Rotten Tomatoes, you can ignore this movie")
    else:
        print("Rotten tomatoes value is not present")

    label .end

main()
