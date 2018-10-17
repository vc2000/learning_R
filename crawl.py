#crawl data

from bs4 import BeautifulSoup
import requests


r = requests.get("https://www.investing.com/indices/investing.com-us-500-components")
c = r.content
soup = BeautifulSoup(c, "html.parser")

for i in soup:
    print(i)

#print(all)

"""
largest_companies <- read_html("https://www.investing.com/indices/us-spx-500-components")   
companies<-largest_companies%>%
html_nodes("#cr1")%
%html_table(header=1) -> sp500
sp500 <- sp500[[1]] 
sp500
"""