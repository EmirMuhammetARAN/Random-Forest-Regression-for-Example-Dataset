import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

data=pd.read_csv("example.csv")
x=data.iloc[:,0].values.reshape(-1,1)
y=data.iloc[:,1].values.reshape(-1,1)

rf=RandomForestRegressor(n_estimators=500 ,random_state=0)

rf.fit(x,y)

x2=np.arange(min(x),max(x),0.01).reshape(-1,1)
y_pred=rf.predict(x2)

print(y_pred)

plt.plot(x2,y_pred,color='b')
plt.scatter(x,y,color='red')
plt.show()