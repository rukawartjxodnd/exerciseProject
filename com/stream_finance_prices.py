import yy_libs.crawler_finance_prices
import yy_libs.input_data_company_code
# import os

# 종목코드 및 종목명 추출
values = yy_libs.input_data_company_code.getCompanyCodes()

# 결과파일 open
resultFile = open("../data/finance_prices_data.csv", "w+", encoding="euc_kr")

# 파일헤더
resultFile.write("company code"+","+"today price"+","+"high price"+"\n")

# data 쓰기
for value in values[:13]:
    try:
        # 코드 및 코드명 추출
        code = value['code']
        code_name = value['code_name']

        # 가격정보 구하기
        today = yy_libs.crawler_finance_prices.getPrices(code)["today"].replace(",","")
        up = yy_libs.crawler_finance_prices.getPrices(code)["up"].replace(",", "")

        # 파일에 쓰기
        resultFile.write(code_name + "@" + today + "@" + up + "\n")
    except:
        print("error:" + code)
