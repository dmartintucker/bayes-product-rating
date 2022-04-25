# Dependencies
import numpy as np 
import pandas as pd 

class Ratings(object):

    def __init__(self, m, c, data) -> None:
        self.prior = m 
        self.confidence = c
        self.data = data
    
    def compute_m(self):
        pass 

    def compute_c(self):
        pass 

    def compute_bayesian_mean(self, ratings_array):
        """
        Computes the Bayesian mean given an array of ratings, a prior, and a confidence value.
        """

        if not self.prior or not self.confidence:
            raise TypeError("Must specify prior (m) and confidence (c).")

        return (self.confidence * self.prior + np.nansum(ratings_array)) / (self.confidence + ratings_array.count())

    @property
    def ratings(self):
        data = self.data
        data = data[['id', 'rating']]
        return data

    def compute_rating_metrics(self):
        return self.ratings.groupby('id').agg(['count', 'mean', self.compute_bayesian_mean])