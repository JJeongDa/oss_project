# oss_project
## 파이썬 오픈소스 프로젝트 - 노원 음식점 크롤링🍣

### 1. 프로젝트 설명
***
이 프로젝트는 맛집 리스트를 추천해주는 사이트 중 하나인 '망고플레이트🥭'에서 노원구에 있는 음식점에 관한 리뷰수와 조회수를 크롤링한 후 상관관계를 시각화하는 프로젝트이다.

### 2. 사용한 파이썬 오픈소스 라이브러리
***
* 웹 크롤링 - BeautifulSoup4
* HTTP 호출 - Requests
* 데이처 처리 - Pandas
* 데이터 시각화 - Seaborn, Matplotlib

### 3. 프로젝트 진행
***
* 메뉴별 음식점 조회수, 리뷰수 크롤링하기    
메뉴는 한식, 분식, 일식, 중식, 세계음식, 카페, 양식 총 7가지이다.
사이트에서 노원에 있는 각 메뉴의 음식점의 조회수와 리뷰수를 1페이지부터 끝페이지까지 모두 크롤링한 후 csv 파일로 저장한다.
csv 파일에는 메뉴종류, 상호명, 조회수, 리뷰수의 정보가 들어있다.    
<img src="https://github.com/JJeongDa/oss_project/issues/3#issue-1085690486" width=200, height=200>
<img src="https://github.com/JJeongDa/oss_project/issues/4#issue-1085690687" width=300, height=200>

* 모든 데이터 합치기    
각 메뉴별로 저장된 csv 파일의 내용을 하나의 all_data.csv 파일로 데이터를 합친다.

* 데이터 시각화    
main.py에서 각 메뉴별 조회수와 리뷰수, 전체 메뉴에 대한 조회수와 리뷰수의 상관관계, 각 메뉴별 조회수와 리뷰수의 상관관계를 시각화한다. 

### 4. 프로젝트 결과
***
* 각 메뉴에 대한 조회수 그래프    
<img src="https://github.com/JJeongDa/oss_project/issues/2#issue-1085689921" width=300, height=300>    
분식의 조회수가 다른 메뉴의 조회수보다 압도적인 조회수를 가지고 있다. 평소 주변에 카페가 굉장히 많다고 생각하고 분위기 등 고려할게 많을 것이라 생각해서 조회수도 높을 것이라 생각했는데 낮은 조회수를 가지고 있는 것이 의외였다.

* 각 메뉴에 대한 리뷰수 그래프    
<img src="https://github.com/JJeongDa/oss_project/issues/7#issue-1085692324" width=300, height=300>   
분식의 조회수가 압도적으로 높은 것에 비해 리뷰수는 전체적으로 비슷비슷했다. 오히려 조회수는 분식이 제일 높지만 리뷰수는 한식이 제일 높았다.

* 전체 메뉴에 대한 조회수와 리뷰수의 상관관계    
<img src="https://github.com/JJeongDa/oss_project/issues/6#issue-1085691141" width=300, height=300>    
조회수가 많을 수록 당연히 리뷰수도 많을 것이라 생각하지만 그 예외의 경우가 있을까 궁금해서 리뷰수와 조회수의 상관관계를 알아보았다. 예상대로 대부분의 음식점은 조회수가 많을수록 리뷰수도 많았다. 특히 음식점 중 175000회의 압도적인 조회수를 가지는 음식점도 보인다. 하지만 그래프의 선 아래쪽에 있는 리뷰수가 많음에도 조회수는 현저히 낮은 가게들이 있음을 알 수 있었다.

* 각 메뉴에 대한 조회수와 리뷰수의 상관관계    
<img src="https://github.com/JJeongDa/oss_project/issues/5#issue-1085690946" width=1000, height=200>    
조회수와 리뷰수의 상관관계를 각 메뉴별로 시각화한 결과이다.
위에서 봤던 리뷰수는 많지만 조회수가 적은 특징이 한식에서 두드러지게 나타나는 것을 볼 수 있다. 특히 한 음식점은 조회수가 8000 정도로 낮은데 리뷰수가 77회로 엄청 높은 소곱창집이었다. 결과가 신기해서 사이트에 가보니 리뷰에서 '소문듣고 처음왔는데', '친구 추천으로 한번 왔다가' 라는 말이 많았다. 입소문을 탄 음식점이어서 리뷰수만 많은 결과가 나온 게 아닐까 생각했다.