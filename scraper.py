# a bot that goes to a https://fred.stlouisfed.org/series/{CA}STHPI for every state acronym and downloads the data for the chart by clicking button with class "download-button" and downloading a csv of the data into ./data from the cwd  */
# imports required libraries
import requests
import os
import time

url1 = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id="
url2 = "STHPI&scale=left&cosd=1975-01-01&coed=2022-04-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Quarterly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2022-11-02&revision_date=2022-11-02&nd=1975-01-01"

# creates a list of all the state abbreviations
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"];


# for each state in states downloads the csv data from fred.stlouisfed.org and saves it to ./data/{state}.csv
for state in states:
    url = url1 + state + url2
    r = requests.get(url, allow_redirects=True)
    open('./data/' + state + '.csv', 'wb').write(r.content)
    time.sleep(1)




# for state in states:
#     print("Downloading data for " + state)
#     url = url1 + state + url2
#     r = requests.get(url, allow_redirects=True)
#     open('./data/' + state + '.csv', 'wb').write(r.content)
#     time.sleep(1)

# for url in urls:
#     driver.get(url)
#     driver.find_element_by_class_name("download-button").click()
#     time.sleep(5)
#     driver.find_element_by_class_name("download-csv").click()
#     time.sleep(5)
#     driver.find_element_by_class_name("download-close").click()
#     time.sleep(5)

#driver.quit()

#/* I have a feeling that the issue is with the way I am downloading the csvs. I am using the selenium module to click the download button and then click the download csv button. I am not sure if the issue is with the way I am downloading the csvs or if the issue is with the way I am iterating through the urls. I am not sure if I am doing something wrong with the way I am iterating through the urls or if I am doing something wrong with the way I am downloading the csvs. Any help would be greatly appreciated. Thank you. */
