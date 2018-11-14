import requests
from bs4 import BeautifulSoup

def getPrices(companyCode):
    url = "https://finance.naver.com/item/main.nhn?code="+companyCode
    pageCallResult = requests.get(url)
    bs_obj = BeautifulSoup(pageCallResult.content,"html.parser")


    # 가격요소 box
    pricesFactors = bs_obj.find("div", {"class": "rate_info"})


    # 현재가
    todayFactor = pricesFactors.find("p", {"class": "no_today"})
    todayBlind = todayFactor.find("span", {"class": "blind"})


    # 고가
    upFactor = pricesFactors.find_all("em")[4]
    upBlind = upFactor.find("span", {"class": "blind"})


    return {"today": todayBlind.text, "up": upBlind.text}