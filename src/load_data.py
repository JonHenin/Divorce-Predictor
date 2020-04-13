import pandas as pd
import joblib
from pathlib import Path

class LoadData():
    def __init__(self):
        self.datapath = Path('./data/')
        #self.questions = pd.read_excel(self.datapath, sheet_name='questions')
        #self.answers = pd.read_excel(self.datapath, sheet_name='answers')
        self.questions = pd.read_csv(self.datapath / 'questions.csv')
        self.answers = pd.read_csv(self.datapath / 'answers.csv')

    def load_traindata_to_df(self):
        df = pd.read_csv(self.datapath / 'responses.csv')

        return df

    def load_model(self, path):
        return joblib.load(path)

    def userdata_to_df(self, json):
        df = pd.DataFrame(json, index=[0])

        return df