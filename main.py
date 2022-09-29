#Import reqests module
import requests
#Import json module
import json

#Define the main function
def main():
    #Define the localhost URL
    url = "http://localhost:8000/"
    #Check the status code of the URL
    r = requests.get(url)
    #Print the status code
    print(r.status_code)

#Run the main function
if __name__ == "__main__":
    main()
