def binaryClassifier():
    import pandas as pd
    import random as rd
    import statistics as st
    data = pd.read_csv("data1/data.csv")
    df = pd.DataFrame(data)
    #print(df)
    actual = df['M']
    #print(actual)
    del df['M']
    accuracy = 0
    for x in range(1000):
        a = rd.randint(0,9)
        while a%2 == 0 :
           a=rd.randint(0,9)
        df1 = df.sample(a, axis=1)
        l = len(df1.columns)
        x = 0
        mode = []
        while x<6 :
            mode.append(st.mode(df1.iloc[x]))
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