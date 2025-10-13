#machine leraning
# dataset -- Training --- Testing---deploy
#labelled---supervised , unlabelled--unsupervised , mix--- semi supervised
#reinforcement learning -- it's like cycle(agent,enviroment,policy,reward(positive,negative),state) 
#nlp -- natural language processing
# mean,mode,covaraince,coeficient,intercept

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Corrected dataset
data = pd.DataFrame({
    'yearsexperience': [1.0, 1.3, 1.5, 2.0, 2.2, 3.0, 3.2, 3.3, 3.6, 4.0, 5.0],
    'salary': [900, 8777, 566, 889, 4555, 6000, 5444, 3323, 8889, 6677, 67799]
})
 
x = data[['yearsexperience']].values
y = data['salary'].values

x_train, x_test,y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

sgd_model = SGDRgressor(max_iter=1, tol=none,eta=0.01, random_state=42)

epochs = 5
print("epoch\tTrain MsE\tTest MSE")
for epoch in range(1,epochs+1):
    sgd_model.partial_fit(x_train,y_train)
 
y_train_pred = sgd_model.predict(x_train)
y_train_pred = sgd_model.predict(x_test)

print(f"{epoch}\{train_mse:.2f}\t\t{test_mse:.2f}")
print("\nfinal model coefficient:", sgd_model.coef_)
print("final model intercept:",sgd_model.intercept_)

plt.scatter(x_test,y)
