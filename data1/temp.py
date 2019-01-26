def Classifier():
    import pandas as pd
    import random as rd
    from collections import Counter
    from itertools import groupby 
    data = pd.read_csv("data1/data.csv")
    df = pd.DataFrame(data)
    #print(df)
    actual = df['M']
    #print(actual)
    del df['M']
    num_of_models = len(df.columns)
    accuracy = 0
    for x in range(1000):
        a = rd.randint(0,num_of_models)
        while a%2 == 0 :
            a=rd.randint(0,num_of_models)
        df1 = df.sample(a, axis=1)
        l = len(df1.columns)
        x = 0
        mode = []
        while x<len(df1.index) :
            freqs = groupby(Counter(df1.iloc[x]).most_common(), lambda x:x[1])
            md = [val for val,count in next(freqs)[1]]
            mode.append(md[0])
            x += 1
        res = pd.DataFrame({'col' : mode})
        #print(res)
        y = 0
        count = 0
        while y<6:
            if abs(actual[y] - mode[y]) == 0 :
                count += 1
            y+=1
        le = len(df1.index)
        na = (count/le)*100
        #print('Accuracy is ', na,'%')
        if na>accuracy :
            accuracy = na
            listt = {'Models Used': [list(df1.columns.values)], 'Accuracy': accuracy}
    return listt