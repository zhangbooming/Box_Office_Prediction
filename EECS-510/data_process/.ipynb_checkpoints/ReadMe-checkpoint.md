## Update 2019/0526
***数据清洗已经OK了***,清洗好的数据为cleaned/clean_result.csv,同一文件夹下的py文件即为用来清洗的代码.暴力的用两层循环找title名字相同且发行年份不超过2年的(为了处理系列电影的重复问题).

### Work has been done

1. 数据简单清洗

   - Why: imdb.csv和boxoffice.csv两张表对于电影名字的定义不同,一部可能是Avengers, 一部可能是Avengers(2012),所以需要对数据进行简单的清洗,然后才能做拼接操作

   - How:对csv的title项进行字符串过滤,去除除字母以外所有字符(空格,括号等,同时去除括号之间的字符—为例避免干扰).这样在清洗后的数据里面,只要发现两个电影的title相同,即可认为这是一部电影

   - details

     ```python
     a=r'\(.*?\)'
     for i in range(len(df_1['title'])):
         pre = df_1['title'][i]
         res = re.sub(a, '', pre)
         df_1['title'][i] = ''.join(list(filter(str.isalpha, res))).lower()
         # print(i)
     ```

     

   - 

2. csv文件拼接

   - How: Pandas.merge, how = 'inner'表示取交集, on = 'title'表示根据两个csv文件的title列进行交运算,如果两个csv文件没有同一名字的列,则可以用left_on和right_on来指定key

     ```python
     pd.merge(df_1, df_2, how='inner', on = 'title')
     ```

     

   - 优势:速度很快

   - 不足:对于系列电影,会出现错误,比方说imdb.csv有复仇者1,2,3三部的数据,boxoffice.csv也有复仇者1,2,3.如果仅仅根据merge进行合并,会得到九条数据

   - 改进

     两个csv文件都有year,所以可以用year进行辅助判断

3. 结合year进行过滤

   - 遇到的问题

     不会抽出单行数据然后进行拼接

   - 代码

     ```python
     df_1 = pd.read_csv("imdb_test.csv",error_bad_lines=False)
     df_2 = pd.read_csv("boxoffice_test.csv",error_bad_lines=False)
     
     df = pd.DataFrame(columns = ["fn", "tid", "title", "wordsInTitle","url","imdbRating","ratingCount","duration","year_x","type","nrOfWins","nrOfNominations","nrOfPhotos","nrOfNewsArticles","nrOfUserReviews","nrOfGenre","Action","Adult","Adventure","Animation","Biography","Comedy","Crime","Documentary","Drama","Family","Fantasy","FilmNoir","GameShow","History","Horror","Music","Musical","Mystery","News","RealityTV","Romance","SciFi","Short","Sport","TalkShow","Thriller","War","Western","lifetime_gross"]) #创建一个空的dataframe
     
     for i in range(len(df_1['title'])):
         for j in range(len(df_2['title'])):
             title_1 = df_1['title'][i]
             year_1 = int(df_1['year'][i])
     
             title_2 = df_2['title'][j]
             year_2 = int(df_2['year'][j])
     
             # print("title 1 = %s, title 2 = %s" %(title_1, title_2))
             if title_1 == title_2:
                 print("year 1 = %d, year 2 = %d" %(year_1, year_2))
                 if year_1 == year_2:
                     print('title ----> %s' % title_2)
                     
                     # 这里就不会了,不知道怎么做拼接
                     df = df.append([df_1['title'].loc[title_1],df_2['lifetime_gross'][j]], ignore_index= True)
     
     
     ```

     
