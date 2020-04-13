from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV
import joblib

from src.load_data import LoadData
from src.prep_data import PrepData

# Set the name of the file to load, and bring in Loader and Data Prep
loader = LoadData()
prep = PrepData()

df = loader.load_traindata_to_df()

# Set target and get features
y = df['Class']
X = prep.drop_target_column(df)

# Create training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 680
)

# Create a Support Vector Machine model and then Calibrate it using CalibratedClassifierCV
model = SVC(kernel='linear')
model.fit(X_train, y_train)

calibrator = CalibratedClassifierCV(model, cv=10)
calibrator.fit(X_train, y_train)

# Export the model
joblib.dump(calibrator, 'models/cal_model.pkl')