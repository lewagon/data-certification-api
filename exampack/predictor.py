
import pandas as pd

import joblib

from sklearn.preprocessing import StandardScaler

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression


class Trainer():

    def load_data(self):

        # read data
        url = "https://wagon-public-datasets.s3.amazonaws.com/certification_paris_2021Q1/spotify_popularity_train.csv"

        data = pd.read_csv(url)

        # clean data
        data = data.drop_duplicates()
        data.dropna(inplace=True)

        # extract target
        y = data.popularity
        X = data.drop("popularity", axis=1)

        return X, y

    def create_pipeline(self):

        column_transformer = ColumnTransformer([
            ("year_pipeline", StandardScaler(), ["acousticness"]),
        ])

        pipeline = Pipeline(steps=[
            ("column_transformer", column_transformer),
            ("model", LinearRegression())
        ])

        return pipeline

    def train(self):

        # load data
        X, y = self.load_data()

        # create pipeline
        pipeline = self.create_pipeline()

        # fit pipeline
        pipeline.fit(X, y)

        # save pipeline
        joblib.dump(pipeline, "model.joblib")


if __name__ == '__main__':
    trainer = Trainer()
    trainer.train()
