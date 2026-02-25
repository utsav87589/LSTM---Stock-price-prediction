import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error


### function to print the metrices
def metrices(y_test, y_pred) : 
    print(f"MAE : {mean_absolute_error(y_test, y_pred)}")
    print(f"MSE : {mean_squared_error(y_test, y_pred)}")
    print(f"RMSE : {root_mean_squared_error(y_test, y_pred)}")


### function to plot for the y_pred vs the y_test
def plot_predictions(y_test, y_pred) : 
    plt.figure(figsize = (8, 4))
    plt.subplot(1, 2, 1)
    plt.plot(y_pred)
    plt.plot(y_test)
    plt.subplot(1, 2, 2)
    plt.scatter(y_pred, y_test)
    plt.scatter(y_test, y_pred, edgecolors = 'r')
    plt.show()


### function to plot the graphs pre_and_post scaling
def plot_graphs_post_scaling(df, df_copy, cols) : 

    for col in cols : 

        print(f"feature : {col}")

        plt.figure(figsize = (8, 4))
        plt.subplot(1, 2, 1)
        plt.title('Boxplot : df')
        sns.boxplot(df[col])
        plt.xlabel("")
        plt.ylabel("")

        plt.subplot(1, 2, 2)
        plt.title('Boxplot : df_copy')
        sns.boxplot(df_copy[col])
        plt.xlabel("")
        plt.ylabel("")


        plt.show()