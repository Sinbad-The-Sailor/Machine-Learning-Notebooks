# Machine-Learning-Notebooks

#### 1. Exponential Regression

Modelling bacteria using exponential regression. This is done by transforming the exponential data into linear data using $\ln(\cdot)$, after which regular linear regression techniques can be used. Regressing based on temperature and humidity a $R^2 = 78 \%$ is obtained. An important task of regression is to check the validity of the linear regression assumptions pertaining to the residuals. 

* Residulas have constant variance
* Residulas are independent
* Resiudals are normally distributed

The residual analysis was performed with graphical methods, although, more sophisticated statistical tests for normality and correlation could be useful.

<p align="center">
<img width="1174" alt="image" src="https://user-images.githubusercontent.com/62723280/168441920-6acfe31c-ba63-4501-8ee3-91c51008a3fb.png">
</p>

Next, confidence and prediction bands were calculated for the regression model as shown below. The confidence interval gives a range of possible models that could be fit depending on the sample of the population. The prediction interval gives a range of possible values for a new observation. Note the difference between the two.
<p align="center">
  <img width="600" alt="image" src="https://user-images.githubusercontent.com/62723280/168441948-2614de91-e806-4359-8e53-91305102a746.png">
</p>

 #### 2. Polynomial Regression

Modelling the welding strenght based on the current being used for the welding process can be done with polynomial regression. In this notebook, it is done using varying degrees of polynomials. Using higher degree polynomials leads to less bias but more variance. To counteract this Tikhonov regularization is made, which ameliorates the overfitting of the polynomial to the data. 

<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/62723280/168442268-daa94664-8ac2-425a-b51f-f38e2722f08a.png">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/62723280/168442211-fc9c1b35-8804-40c4-84cf-9a75b5ec05ab.png">
</p>

Also, confidence and perdiction bands were found as shown below.

<p align="center">
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62723280/168442090-7d31bf74-ac5e-48f6-81a0-a730556a3abd.png">
</p>

#### 3. Logistic Regression

Classification of surviving the Titanic is made with a self-impelemnted logistic regression model. Based on features of sex, class and age, the model has a ~ 75 % accuracy. A comparision with sklearn's logistic regression and kNN classifier is made. The logistic regression results are nearly identical (sklearn regularizeses too), and the results are better than kNN. 

#### 4. Softmax Regression

Classification of handwritten digits (MNIST dataset). Uses full gradient decent without batching the model yields an accuracy of ~ 90 %. The confusion matrix is displayed below.

<p align="center">
<img width="223" alt="image" src="https://user-images.githubusercontent.com/62723280/188013601-1fd9866e-7c64-48ca-b8e1-b589f65addc7.png">
</p>


#### 5. Time Series Analysis

Analysing sea-level dataset from NASA. AR, MA and ARMA models are used, in addition to a nonlinear AR model using feed forward neural networks. The results of the network approach are, however, quite disappointing. 

<p align="center">
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62723280/188013403-caa179d3-68eb-4c9a-9b05-607c22500a6e.png">
</p>
