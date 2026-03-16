import pandas as pd
import numpy as np


### function to build the train and the test sequences for the different window sizes
def build_sequences(df, days, features_to_target) : 

    X, y = [], []

    for i in range(len(df) - days) : 

        X.append(df[features_to_target][i : i + days])
        y.append(df[features_to_target].iloc[i + days])

    X = np.array(X)
    y = np.array(y)

    test_size = int(len(df) * 0.80)
    X_train, X_test = X[ : test_size], X[test_size : ]
    y_train, y_test = y[ : test_size], y[test_size : ]

    print(f"{X_train.shape} :: {y_train.shape} \n{X_test.shape} :: {y_test.shape}")

    return X_train, X_test, y_train, y_test

