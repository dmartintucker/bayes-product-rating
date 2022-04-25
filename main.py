# Custom methods

from utils import Utils
u = Utils()

sample_dist = u.generate_product_reviews(n_products=10)

from methods import Ratings
r = Ratings(m=3.5, c=10, data=sample_dist)
print(r.compute_rating_metrics())