#Import reqests module
import requests


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

main()
