from typing import TypedDict

class ProductReview(TypedDict):
    product_name: str
    rating: int
    review_text: str
    
    
new_review: ProductReview = {
    "product_name": "Wireless Headphones",
    "rating": 5,
    "review_text": "These headphones have excellent sound quality and battery life."
}

print(new_review)