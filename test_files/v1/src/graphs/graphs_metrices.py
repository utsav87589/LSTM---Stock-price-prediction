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
    plt.figure(figsize = (12, 4))

    #----------Plot to see the trend made by model
    plt.subplot(1, 3, 1)
    plt.plot(y_pred, label = 'Predicted')
    plt.plot(y_test, label = 'Actual')

    #----------Actual vs Predicted points
    plt.subplot(1, 3, 2)
    plt.plot(y_test, label='Actual', color='blue', marker='o')
    plt.plot(y_pred, label='Predicted', color='red', marker='x')
    plt.xlabel('Index')
    plt.ylabel('Target Value')
    plt.legend()
    plt.grid(True)

    #--------- Best fit line
    plt.subplot(1, 3, 3)
    plt.scatter(y_test, y_pred, color = 'blue', alpha = 0.5, label = 'Predicted')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
             color = 'red', linewidth = 2, label = 'Best fit line')
    plt.xlabel('Actual Values (y_test)')
    plt.ylabel('Predicted Values (y_pred)')
    plt.legend()
    plt.grid(True)
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