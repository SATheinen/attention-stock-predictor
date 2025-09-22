import json
import requests
import os

# File containing stock names
txt_file = "stock_names"

# Where to drop the stock data
#!!! The folder should be empty before downloading the files !!!
folder_name = "data_dump"

with open("../api_key.txt") as file:
    text = file.read()
    api_key = text.split(" ")[-1]

def fetch_data(stock_name, api_key=api_key, output_size='full'):
    # download data
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&outputsize={output_size}&apikey={api_key}&datatype=json'
    r = requests.get(url)
    data = r.json()

    # save data
    with open(f'./{folder_name}/{stock_name}.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    
    # Create Folder if not exist
    if not os.path.isdir(f"{folder_name}"):
        os.mkdir(f"{folder_name}")
    
    if not os.listdir(f'./{folder_name}/'):
        print(f"Get Data \n Always be check your daily Alpha Vantage API limit!")
    else:
        raise Exception(f"Target folder NOT empty! \n Clear folder before running this script again!")

    with open(f'./{txt_file}.txt', 'r') as file:
        stock_list = [line.strip() for line in file.readlines()]
    print(f"Open {txt_file}.txt")
    
    # only 25 api requests per day
    counter = 0
    for stock in stock_list:
        if not os.path.exists(f'./{folder_name}/{stock}.json'):
            if counter < 25:
                print(f'get {folder_name}/{stock}.json')
                fetch_data(stock)
                counter+=1
            else:
                print(f'API limit reached')
                break
