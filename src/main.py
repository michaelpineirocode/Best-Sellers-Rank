import pygsheets
import pandas as pd
from requests_html import  HTMLSession
import settings
import time

def getSellerRank(url): # returns integer value
    # setup of a lightweight chromium browser
    sesh = HTMLSession()
    r = sesh.get(url)
    r.html.render(sleep=1) # renders the page's html and sleeps for a second
    
    best_sellers_rank = r.html.xpath('//*[@id="detailBulletsWrapper_feature_div"]/ul[1]/li/span', first=True).text.split(" ")[3][1:].replace(",", "")
    return int(best_sellers_rank)

def update_spreadsheet(rank):
    #authorization
    gc = pygsheets.authorize(service_file=settings.json_title)

    # Create empty dataframe
    df = pd.DataFrame()

    # Create a column
    df['name'] = [str(rank), 'Steve', 'Sarah']

    #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    ## print(settings.spreadsheet_title)
    sh = gc.open(settings.spreadsheet_title)

    #select the first sheet 
    wks = sh[settings.sheet_number]

    #update the first sheet with df, starting at cell B2. 
    wks.set_dataframe(df,(1,1))

def main():
    start_time = time.time()
    while True:
        if (time.time() - start_time) % 1800 == 0:
            print("UPDATING")
            rank = getSellerRank(settings.url)
            update_spreadsheet(rank)
            start_time = time.time()

if __name__ == "__main__":
    main()
