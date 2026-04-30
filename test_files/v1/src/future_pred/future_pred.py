import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### function to forecast the future sequence based on the window size given
def gen_future_prices(window_size, last_sequence, model, scaler) : 

    future_pred = []

    current_window = last_sequence.copy()

    for _ in range(window_size) : 

        next_pred = model.predict(current_window, verbose = 0)
        future_pred.append(next_pred[0, : ])

        next_pred_reshaped = np.expand_dims(next_pred, axis = 0)
        
        current_window = np.concatenate(
            (current_window[:, 1 : , :], next_pred_reshaped),
            axis = 1
        )

    future_pred = scaler.inverse_transform(future_pred)

    return future_pred


### function to generate the future business days based on the last date and window size 
def gen_future_dates(last_date, window_size) : 

    future_dates = pd.date_range(
        start = last_date + pd.Timedelta(days = 1),
        periods = window_size,
        freq = 'B'
    )

    return future_dates


### function to plot the graphs of the future prices with respect to old trend
def gen_future_price_graphs(df, df_copy, features_to_target, future_dates, future_preds) : 

    for index,feature in enumerate(features_to_target) :

        print(f"Feature : {feature}")
        plt.figure(figsize=(10,5))
        plt.plot(df['date'], df_copy[feature], label="Historical")
        plt.plot(future_dates, future_preds[:, index], label="Future Forecast")
        plt.legend()
        plt.show()