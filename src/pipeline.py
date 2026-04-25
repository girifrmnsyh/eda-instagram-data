from sklearn.base import BaseEstimator, TransformerMixin
from preprocessing import preprocess_data
from feature_engineering import feature_engineering


class PreprocessingTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return preprocess_data(X)


class FeatureEngineeringTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return feature_engineering(X)