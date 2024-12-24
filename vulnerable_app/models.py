from django.db import connection

class DummyModel:
    unused_variable = "This variable is not used anywhere"

def execute_raw_query(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Unsafe query
    with connection.cursor() as cursor:
        cursor.execute(query)
