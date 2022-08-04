import helpers

def process_data():
    # pull the users from a db table
    users = helpers.get_users()

    for _, user in users.iterrows():
        print(f'starting user: {user.user_id}')
        # pull user data from plaid
        user_data = helpers.get_user_data(user)

        # filter user data
        user_data = helpers.filter_user_data(user_data)

        # pull user specifications
        user_specs = helpers.get_user_specs(user)

        # initialize model
        model = helpers.load_model()
        
        # clean data
        user_data = helpers.model_clean(user_data, model)

        # hit validation api
        user_data = helpers.validate(user_data, user)

        # push to db
        helpers.upload(user_data, table_name='clean_data')


if __name__ == "__main__":
    process_data()