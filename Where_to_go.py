import pandas as pd 
import numpy as np 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df_planets = pd.read_csv("/Users/amir/Downloads/CodeAmir/WhereToGo/Exoplanet_Dataset.csv")
df_stars = pd.read_csv("/Users/amir/Downloads/CodeAmir/WhereToGo/star_classification.csv")

#info about the data (from kaggle)
#obj_ID = Object Identifier, the unique value that identifies the object in the image catalog used by the CAS
#alpha = Right Ascension angle (at J2000 epoch)
#delta = Declination angle (at J2000 epoch)
#u = Ultraviolet filter in the photometric system
#g = Green filter in the photometric system
#r = Red filter in the photometric system
#i = Near Infrared filter in the photometric system
#z = Infrared filter in the photometric system
#run_ID = Run Number used to identify the specific scan
#rereun_ID = Rerun Number to specify how the image was processed
#cam_col = Camera column to identify the scanline within the run
#field_ID = Field number to identify each field
#spec_obj_ID = Unique ID used for optical spectroscopic objects (this means that 2 different observations with the same spec_obj_ID must share the output class)
#class = object class (galaxy, star or quasar object)
#redshift = redshift value based on the increase in wavelength
#plate = plate ID, identifies each plate in SDSS
#MJD = Modified Julian Date, used to indicate when a given piece of SDSS data was taken
#fiber_ID = fiber ID that identifies the fiber that pointed the light at the focal plane in each observation

class_to_code = {item: idx for idx, item in enumerate(df_stars["class"].unique())}

def clean_data(series):
    unique_classes = {item: idx for idx, item in enumerate(series.unique())}
    class_num = series.map(unique_classes).tolist()
    class_str = series.tolist()
    return class_num, class_str #this gives back the enumerated class and what the class is itself

X = np.array(df_stars["redshift"]).reshape(-1, 1)
Y = clean_data(df_stars["class"])[0] #the zero is for the array that holds the enumerated values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, shuffle=True)

rf_model = RandomForestClassifier(n_estimators = 50, n_jobs = 1, random_state= 42)
rf_model.fit(X_train, Y_train)
y_pred = rf_model.predict(X_test)

target_names = list({item: idx for idx, item in enumerate(df_stars["class"].unique())}.keys())
print("RF report 🌳:")
print(classification_report(Y_test, y_pred, target_names=target_names))
