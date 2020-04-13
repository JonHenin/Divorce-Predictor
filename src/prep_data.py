class PrepData():
    def __init__(self):
        pass

    def drop_target_column(self, df):
        return df.drop(['Class'], axis=1)
