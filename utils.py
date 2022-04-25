# Dependencies
import numpy as np 
import pandas as pd 
import warnings, random

warnings.filterwarnings('ignore')

class Utils:

    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_product_reviews(max_reviews_per_product=100, n_products=100) -> pd.DataFrame:

        res = pd.DataFrame()

        # Ratings
        ratings_space =         [1,2,3,4,5]

        # Product type weights
        excellent_product =     [0,1,10,100,1000]
        good_product =          [2,4,8,16,32]
        mediocre_product =      [1,10,100,10,1]
        poor_product =          [32,16,8,4,2]
        terrible_product =      [1000,100,10,1,0]
        divisive_product =      [10,1,0,1,10]
        uniform_product =       [1,1,1,1,1]

        product_space =         [excellent_product, good_product, mediocre_product, poor_product, terrible_product, divisive_product, uniform_product]

        for prod in range(n_products):

            reviews = pd.DataFrame()
            product = random.choice(product_space)
            n_reviews = random.randint(1, max_reviews_per_product)

            reviews['rating'] = random.choices(population=ratings_space, weights=product, k=n_reviews)
            reviews['id'] = [prod] * n_reviews
        
            res = pd.concat([res, reviews], axis=0, sort=True)
        
        return res