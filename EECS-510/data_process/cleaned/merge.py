import pandas as pd
import re

df_1 = pd.read_csv("imdb_res.csv",error_bad_lines=False)
df_2 = pd.read_csv("boxoffice_res.csv",error_bad_lines=False)

df_1 = pd.DataFrame(df_1)
df_2 = pd.DataFrame(df_2)
# fn,tid,title,wordsInTitle,url,imdbRating,ratingCount,duration,year_x,type,nrOfWins,nrOfNominations,nrOfPhotos,nrOfNewsArticles,nrOfUserReviews,nrOfGenre,Action,Adult,Adventure,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,FilmNoir,GameShow,History,Horror,Music,Musical,Mystery,News,RealityTV,Romance,SciFi,Short,Sport,TalkShow,Thriller,War,Western,rank,studio,lifetime_gross,year_y
df = pd.DataFrame(columns = ["tid", "title", "wordsInTitle","url","imdbRating","ratingCount","duration","year_x","type","nrOfWins","nrOfNominations","nrOfPhotos","nrOfNewsArticles","nrOfUserReviews","nrOfGenre","Action","Adult","Adventure","Animation","Biography","Comedy","Crime","Documentary","Drama","Family","Fantasy","FilmNoir","GameShow","History","Horror","Music","Musical","Mystery","News","RealityTV","Romance","SciFi","Short","Sport","TalkShow","Thriller","War","Western","lifetime_gross"]) #创建一个空的dataframe

for row1 in df_1.itertuples(index=False, name='Pandas'):
    for row2 in df_2.itertuples(index=False, name='Pandas'):
        try:
            title_1 = getattr(row1, "title")
            year_1 = int(getattr(row1, "year"))
            # print(title_1, year_1)

            title_2 = getattr(row2, "title")
            year_2 = int(getattr(row2, "year"))
            # print(title_2, year_2)

            if title_1 == title_2:
                # print("year 1 = %d, year 2 = %d" %(year_1, year_2))
                if abs(year_1 - year_2) <= 2 :
                    # print('title : %s' % title_2)
                    res = pd.DataFrame(row1).T
                    # print(type(res))
                    res['lifetime_gross'] = getattr(row2, "lifetime_gross")
                    # df = df.append(res)
                    # print(res)
                    res.to_csv('clean_result.csv', mode='a', header=False, index = False)
        except Exception as e:
            print(e)




# for i in range(0,len(df_1)):
#     for j in range(0,len(df_2)):
#         title_1 = df_1.iloc[[i]]['title']
#         year_1 = int(df_1.iloc[[i]]['year'])

#         title_2 = df_2.iloc[[j]]['title']
#         year_2 = int(df_2.iloc[[j]]['year'])

#         print("title 1 = %s, title 2 = %s" %(title_1, title_2))
#         if title_1 == title_2:
#             print("year 1 = %d, year 2 = %d" %(year_1, year_2))
#             if abs(year_1 - year_2) <= 2 :
#                 print('title ----> %s' % title_2)
#                 print("i = " + str(i))
#                 print("j = " + str(j))
#                 temp = df_1.iloc[[i]]

#                 df = df.append(temp, ignore_index= True)
                # print((df_1.iloc[i:i+1,:]))
                # print('df_1 %s' %df_1[i])
                # print('df_1 %s' % df_2[i])
                # df = df.append([df_1['title'].loc[title_1],df_2['lifetime_gross'][j]], ignore_index= True)


#
# result = pd.merge(df_1, df_2, how='inner', on = 'title')
# print(result)

# a=r'\(.*?\)'
# for i in range(len(df_1['title'])):
#     pre = df_1['title'][i]
#     res = re.sub(a, '', pre)
#     df_1['title'][i] = ''.join(list(filter(str.isalpha, res))).lower()
#     # print(i)
#
# print(df)
df.to_csv("header.csv",index=False)
# result.to_csv("res.csv",index=False)