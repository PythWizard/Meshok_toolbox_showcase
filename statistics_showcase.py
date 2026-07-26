import json
from collections import Counter
from datetime import datetime


def analyze_dataset(filename):
    """
    Analyze Meshok users dataset.
    """

    with open(filename, "r", encoding="utf-8") as f:
        users = json.load(f)

    if not isinstance(users, list):
        raise ValueError("JSON must contain a list of users")


    # Geography analysis
    cities = [
        user.get("city", "Unknown")
        for user in users
    ]

    top_cities = Counter(cities).most_common(10)


    # Registration analysis
    years = []

    for user in users:
        date = user.get("registrationDate")

        if date:
            try:
                year = datetime.fromisoformat(
                    date.replace("Z", "")
                ).year

                years.append(year)

            except:
                pass

    registration_years = Counter(years)


    # Review statistics
    avg_reviews = sum(
        user.get("reviews_from_sellers_total", 0)
        +
        user.get("reviews_from_buyers_total", 0)
        for user in users
    ) / len(users)


    return {
        "users": len(users),
        "top_cities": top_cities,
        "registration_years": registration_years,
        "average_reviews": round(avg_reviews, 2)
    }


if __name__ == "__main__":

    report = analyze_dataset("results.json")

    print(json.dumps(
        report,
        indent=4,
        ensure_ascii=False
    ))
