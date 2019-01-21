
def normalize(array):
    import numpy as np
    mean = np.mean(array)
    std_dev = np.std(array)
    array = (array - mean)/std_dev
    return array

def load_data():
    #Loading Data
    import pandas as pd
    import numpy as np
    df = pd.read_csv("App_Data.csv")
    
    #Converting to Categorical encoding
    df["Type"] = df["Type"].astype('category')
    df["Content Rating"] = df["Content Rating"].astype('category')
    df["Genres"] = df["Genres"].astype('category')
    df["Type"] = df["Type"].cat.codes
    df["Content Rating"] = df["Content Rating"].cat.codes
    df["Genres"] = df["Genres"].cat.codes
    
    #Changing values of Size category
    for i in range(len(df["Size"])):
        if df["Size"][i].find("M") != -1:
            value = df["Size"][i].split('M')
            value[0] = float(value[0])*1000
            df["Size"][i] = value[0]
        elif df["Size"][i].find("k") != -1:
            value = df["Size"][i].split('k')
            value[0] = float(value[0])
            df["Size"][i] = value[0]
        
    #Changing the features to suitable datatype
    df["Reviews"] = df["Reviews"].astype('int64')
    df["Size"] = df["Size"].astype('int64')
    df["Installs"] = df["Installs"].astype('int64')
    df["Type"] = df["Type"].astype('int64')
    df["Price"] = df["Price"].astype('float64')
    df["Content Rating"] = df["Content Rating"].astype('int64')
    df["Genres"] = df["Genres"].astype('int64')
    df["Rating"] = df["Rating"].astype('float64')
    
    #Converting Dataframe to Numpy array
    data = np.array(df)
    
    #Splitting Data into input and labels
    inputs = data[:,0:7]
    
    #Scaling the Data (Dividing by Mean)
    inputs[:,0] = inputs[:,0]/np.mean(inputs[:,0]) 
    inputs[:,1] = inputs[:,1]/np.mean(inputs[:,1])
    inputs[:,2] = inputs[:,2]/np.mean(inputs[:,2])
    
    #Filling null values with mean and Scaling Labels
    labels = np.reshape(np.nan_to_num(data[:,7],copy = False),(data.shape[0],1))
    mean_label = np.mean(labels)
    for i in range(len(labels)):
        if labels[i][0] == 0:
            labels[i][0] = mean_label

    return inputs,labels 

