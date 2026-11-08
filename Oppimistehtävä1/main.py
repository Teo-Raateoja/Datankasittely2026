from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.fetch_data import fetch_data
from config import API_URL, DATABASE_URL
from data_analysis.analyze_data import analyze_users
from data_protection.anonymization import anonymize
from data_protection.masking import mask
from db.models import User


def main():
    api_users = fetch_data(API_URL)
    if not isinstance(api_users, list):
        raise RuntimeError("The API request failed or returned unexpected data.")

    users = [
        {
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "city": user["address"]["city"],
            "company_name": user["company"]["name"],
            "phone": user["phone"],
            "website": user["website"],
        }
        for user in api_users
    ]

    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    try:
        with Session.begin() as session:
            for user in users:
                session.merge(User(**user))
    finally:
        engine.dispose()

    print(f"Saved {len(users)} users.")

    protected_users = [user.copy() for user in users]
    anonymize(protected_users)
    mask(protected_users)
    analyze_users(protected_users)


if __name__ == "__main__":
    main()