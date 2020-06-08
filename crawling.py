import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseurl =  'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
plusurl = input('검색어를 입력하세요: ')
# plusurl은 한글인 경우 주소창에 들어가기에 문제가 생기기에 ascii코드로 바꾼다. url을 

url = baseurl + urllib.parse.quote_plus(plusurl)


html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser') #뷰티플 숲을 이용해서 url 분석


title = soup.find_all(class_='sh_blog_title') #블로그의 제목 클래스 명

for i in title:
    print(i.attrs['title'])
    print(i['href'])
    print()


 
