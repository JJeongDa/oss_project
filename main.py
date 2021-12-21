import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("./data/all_data.csv")

# 메뉴별 조회수
sns.barplot(data=df, x="메뉴종류", y="조회수", ci=None)
plt.show()
# 메뉴별 리뷰수
sns.barplot(data=df, x="메뉴종류", y="리뷰수", ci=None)
plt.show()
# 전체메뉴에 대한 리뷰수-조회수 관계
sns.regplot(data=df, x="리뷰수", y="조회수")
plt.show()
# 메뉴별 리뷰수-조회수 관계
sns.lmplot(data=df, x="리뷰수", y="조회수", hue="메뉴종류", col="메뉴종류", truncate=False, size=3)
plt.show()