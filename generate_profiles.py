from faker import Faker

fake = Faker()

profiles = fake.json(
    num_rows=100,
    data_columns = [
        ("first_name", "first_name"),
        ("last_name", "last_name"),
        ("username", "user_name"),
        ("password", "password"),
        ("id", "uuid4")
    ]
)

with open("profiles.json", "w") as f:
    f.write(profiles)