#Import reqests module
import requests
#Import json module
import json

#Define the main function
def main():
    #Define the localhost URL
    url = "http://0.0.0.0:8000/"
    #Check the status code of the URL
    r = requests.get(url)
    #Print the status code
    print(r.status_code)

    #get the json data
    data = r.json()
    #Print the json data
    print(data)
    # zsh script get my local IP address
    # ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
    

#Run the main function
if __name__ == "__main__":
    main()
