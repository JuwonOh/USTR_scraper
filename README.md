# USTR_scraper

미국의 미국무역대표부(United States Trade Representative)의 Press Releases를 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py 총 세가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.

```
title : USTR Statement on the EU’s Consultation Request at the WTO ..
time : 01/29/2019 ..
content :  Washington, DC – Today, the United States received from the European Union (EU) a request for consu ..
url : https://ustr.gov/about-us/policy-offices/press-office/press-releases/2019/january/ustr-statement-eu’ ..
scrap_time : 2019-01-30-04 07:17:05 ..


title : Public Hearing on Negotiating Objectives for U.S.-UK Trade Agreement ..
time : 01/28/2019 ..
content :  The Office of the U.S. Trade Representative (USTR) will hold a public hearing from 9:30 AM – 4:00 P ..
url : https://ustr.gov/about-us/policy-offices/press-office/press-releases/2019/january/public-hearing-neg ..
scrap_time : 2019-01-30-04 07:17:06 ..


title : USTR Operating Status ..
time : 01/26/2019 ..
content :  USTR has returned to full operating status. On Monday, January 28, all USTR personnel will resume a ..
url : https://ustr.gov/about-us/policy-offices/press-office/press-releases/2019/january/ustr-operating-sta ..
scrap_time : 2019-01-30-04 07:17:08 ..

```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
