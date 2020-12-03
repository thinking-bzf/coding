import keras
import pandas as pd
import numpy as np
from keras import models
from keras import layers
from keras.utils import plot_model
from keras.callbacks import ModelCheckpoint,TensorBoard,EarlyStopping
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
seed = 7
np.random.seed(seed)

num_epochs = 500
ss_X=preprocessing.StandardScaler()
ss_y=preprocessing.StandardScaler()

log_filepath = 'C:/Users/Fish/Documents/Coding/Python/Cognition Practice/Projects/logs/' 
u_data=pd.read_csv("C:/Users/Fish/Documents/Coding/Python/Cognition Practice/Projects/final_data.csv")
def ps(o_data=u_data):
    data=o_data.drop('URL',axis=1)
    data=data.drop('Unnamed: 0',axis=1)
    data=data.drop('概述',axis=1)
    data=data.drop('健康度',axis=1)
    data=data.drop('厂商',axis=1)

    jb=data['级别']
    f_jb=pd.get_dummies(jb,prefix='级别')
    data=data.drop('级别',axis=1)
        
    pf=data['排放标准']
    f_pf=pd.get_dummies(pf,prefix='排放标准')
    data=data.drop('排放标准',axis=1)
        
    zd=data['自动挡']
    f_zd=pd.get_dummies(zd,prefix='自动挡')
    data=data.drop('自动挡',axis=1)
        
    bx=data['商业险']
    f_bx=pd.get_dummies(bx,prefix='商业险')
    data=data.drop('商业险',axis=1)

    y=data['价格']
    data=data.drop('价格',axis=1)

    feature_names=data.columns


    X=data
    global ss_X
    global ss_y
    X=ss_X.fit_transform(X)
    y=ss_y.fit_transform(y.values.reshape(-1,1))
    f_data=pd.DataFrame(data=X,columns=feature_names,index=o_data.index)
    f_data=pd.concat([f_jb,f_pf,f_zd,f_bx,f_data],axis=1,ignore_index=False)
    X=f_data
    return X,y

X,y=ps()


model=models.Sequential()
model.add(layers.Dense(512, activation='relu',input_shape=(X.shape[1],)))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1))
model.compile(optimizer='Adam',loss='mse',metrics=['mae'])

plot_model(model,to_file='model.png')

filepath="model_weight.hdf5"
filepath2="model_weight2.hdf5"
tensorboard = TensorBoard(log_dir=log_filepath, write_images=1, histogram_freq=1)  
checkpoint = ModelCheckpoint(filepath2, monitor='mean_absolute_error', verbose=1, save_best_only=True,
mode='min')
earlystopping = EarlyStopping(monitor='mean_absolute_error',mode='min',patience=70,verbose=1,restore_best_weights=False)

#回调函数
callbacks_list = [checkpoint,tensorboard,earlystopping]

#训练
model.load_weights(filepath)
history= model.fit(X,y,batch_size=200,epochs=num_epochs,validation_split=0.2,callbacks=callbacks_list)

#保存模型
'''
history= model.fit(X,y,batch_size=200,epochs=num_epochs,validation_split=0.2,callbacks=callbacks_list)
model.save('model.hdf5')
model.save_weights('model_weight.hdf5')
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
r= model.evaluate(X_test,y_test)

print(r)
print(model.metrics_names)

#预测
'''
x_=ss_X.inverse_transform(x0)
y1=model.predict(x0)
y_=ss_y.inverse_transform(y1)
print(x_)
print(y_)

'''

#绘图
'''
mae_history = history.history['val_mean_absolute_error']

plt.plot(range(1, len(mae_history) + 1), mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.savefig("res.png",dpi=200)
'''