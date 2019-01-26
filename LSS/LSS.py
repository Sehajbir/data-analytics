def leastSumOfSquares(): 
    import random as rd
    import pandas as pd
    data = pd.read_csv('LSS/data.csv')
    df = pd.DataFrame(data)
    c = df['C']
    del df['C']
    weights = []
    minimum = 999999
    final_weights = []
    for p in range(1000):
        for i in range(len(df.columns)):
            weights.append(rd.random())
        #print(df.head)
        su = 0
        for x in range(len(df.index)):
            s = 0
            for y in range(len(df.columns)):
                s = s + df.iloc[x][y]*weights[y]
            su = su + abs(c[x]-s)
        if su < minimum :
            minimum = su
            final_weights.clear()
            final_weights = weights.copy()
        weights.clear()
    res = {'Least Sum Of Squares :': minimum, 'Weights Used :': final_weights}
    return res