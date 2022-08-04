import pandas as pd
import faker
import time
import random
import datetime

fake = faker.Faker()


class Model:
    def __init__(self):
        """reads from a local file"""
        sleep.time(5)
        print('model initialized')

    def __call__(self, raw):
        """returns the output of a highly sophisticated transaction description cleaner model"""
        return raw.title()

def get_users(num_users=20):
    """returns a dataframe copy of db table
    query = select * from users
    """
    time.sleep(5)
    users = pd.DataFrame({
        'user_id': list(range(num_users)),
        'first_name': [fake.first_name() for _ in range(num_users)],
        'last_name': [fake.last_name() for _ in range(num_users)],
        'zipcode': [fake.zipcode() for _ in range(num_users)],
    })
    print(f'users: {len(users)}')
    return users

def rand_date(max_days_back=30):
    days_back = random.randint(0, max_days_back)
    return (datetime.datetime.today() - pd.Timedelta(f'{days_back}d')).strftime('%Y-%m-%d')

def get_user_data(user, max_transactions=10, max_days_back=30):
    """returns all the transactions from plaid for a given user
    request like {"user": user, "start_date": null, "end_date": null}
    """
    time.sleep(5)
    num_transactions = random.randint(1, max_transactions)
    data = pd.DataFrame({
        'user_id': user.user_id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'merchant': [fake.street_name().lower() for _ in range(num_transactions)],
        'date': [rand_date(max_days_back) for _ in range(num_transactions)],
        'amount': [random.randint(1,250) for _ in range(num_transactions)],
    })
    print(f'recent transactions: {len(data)}')
    return data

def filter_user_data(data, days_back=10):
    """filters for just the past 10 days worth of transactions"""
    min_date = datetime.datetime.today() - pd.Timedelta(f'{days_back}d')
    data['date_dt'] = pd.to_datetime(data['date'])
    data = data[data['date_dt'] >= min_date]
    print(f'transactions: {len(data)}')
    return data

def get_user_specs(user):
    """returns a dict copy of db row
    query = select * from users_specs where user_id = {user.user_id}
    """
    time.sleep(2)
    return {
        'user_id': user.user_id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'work_schedule': random.randint(1, 7),
        'birthday': fake.date(),
    }

def load_model():
    return Model()

def model_clean(data, model):
    """applies highly sophisticated model to clean up merchant"""
    for i, row in data.iterrows():
        data.loc[i, 'merchant'] = model(data.loc[i, 'merchant'])
    return data

def validate(data, user):
    """hits a unreliable third-party api to validate that merchants exist in a given zipcode"""
    time.sleep(1)
    if random.random() < 0.01:
        raise TimeoutError('Validation API timeout')
    print('all merchants are valid')
    return data

def upload(user_data, table_name):
    time.sleep(1)    
    print(f'uploaded transactions: {len(user_data)}')
