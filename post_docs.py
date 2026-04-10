# a file to generate random ages for post docs
import random
import pandas as pd

POST_DOCS = [
    "Joe",
    "Moriah",
    "Praachi",
    "Matt",
    "Seungwon",
    "Abby",
    "Claire"
]
FOOD = [
    "plums",
    "pizza",
    "pasta",
    "peanut butter",
    "popsicles"
]


def main():
    """Main execution function"""
    df = []
    # cols: name, age, favorite_food
    for post_doc in POST_DOCS:
        row = {}
        row['name'] = post_doc
        row['age'] = random.randrange(5, 40)
        row['favorite_food'] = random.choice(FOOD)
        df.append(row)
    
    df = pd.DataFrame(df)
    df.to_csv('postdocs.csv', index=False)


if __name__ == '__main__':
    main()