# Predicting Future Stock Prices

This is a machine learning model predicting future stock prices on a daily basis.
Multiple stocks are read in and the model predicts a probability destribution for the relative gain at the next day.
Then certain thresholds for the mean and standard deviation are used to filter out stocks which most likely will change in a predictable way on the next day. Currently the model is correct in around 55% of all cases. If you would just predict an increase every day, you would be correct in 52% of all cases.

# Problem of Market Predictability

The stock market is a highly volatile system changing in hardly predictable ways. The many different factors such as news, trends or sometimes just random decisions by individuals make the market a highly complex system. However, being able to predict the stock market, even just slightly would be highly profitable and therefore is a goal for many people. Large influences on the market have news headlines and previous stock prices. Evaluating these data in a smart way hence should give some predictability to the market.

# The Dataset

In this project we will use a custom dataset relying on currently 22 stocks defined in the stcok_names.txt. These stocks constist of the open, close, high, low, volume and date data for different time lengths of at least 4 years. These 22 stocks are interchangabele and can be refreshed every day by using the alpha vantage API. The data of all the stocks is read in a numpy array of dimensions [stock, value, timepoint] with sizes [22, 6, 1024] where stock is the number of the stock (order does not matter), value is open, close ... and timepoint is the number of the timepoints (every timepoint is one day).

# Model Architecture

The model consists of an LSTM with self attention mechanism.
