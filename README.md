# PHBS_TQFML-Project

## Stock Index Prediction based on Wavelet Transformation and ARIMA-ML Model or TEA-ML Model

* ### Wavelet Transformation
  Stock index data generally has much noise and is non-stationay, which is a huge challenge for us using ML(Machine Learning) methods to  predict the index. However wavelet transformation, an upgraded version of fourier transform, can serve as a very good filter to decrease the noise in stock index and smooth the data, thus helping us to focus more on the main trend of stock index.
  There are two reasons to choose stock index data,
  * Firstly, stock index datas are more synthetic and consecutive than individual stock data;
  * Secondly, by predicting stock index can help to design some trading stategies in stock index futures, which are the only actively trading financial derivative category in China mainland.
  
  
* There are two tryable methods to achieve the goal.
  Firstly, the ARIMA-ML(Autoregressive Integrated Moving Average and Machine Learning) Model
  Secondly, the TEA-ML(Technical Analysis and Machine Learning) Model
  
* ### ARIMA-ML Model 
  After wavelet transformation, there are two types of stock index data, low-frequency and high-frequency. The ARIMA-ML model is trying to  using ARIMA method to predict the high-frequecy data, since high-frequency is stationary, while ML methods, such as SVM(Support Vector Machine)，are trying to predict the low-frequency data. Finally, using the predicted data to reconstruct the stock index. Generally speaking, ARIMA-ML model is trying to complete prediction on the timing series perspective.
  

* ### TEA-ML Model
  On the other hand, TEA-ML model is trying to complete the prediction by finding some correlations between stock index return and technical indicators. By classifying the upward and downward state as '1' and '-1', the problem can be turned into classification problem, to which we can apply the ML methods, then.


## Data Description
  The datas selected are the daily stock index data of 000300.SH representing the large-cap stocks and 000905.SH representing medium-and-small-cap stocks, including,
  * __Open__: Open price
  * __High__: Highest daily price
  * __Low__: Lowest daily price
  * __Volume__: Trading volume
  * __AMT__: Trading amount
  * __Time range__: 2010-01-01 to 2018-03-30
  
  
  
 ## Arangement
* Try best to use both models to make predictions. At least use one of them.
* Try to design a trading strategy based on the stock index prediction result.