def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("Please try again")
        return product_idea + "inator"