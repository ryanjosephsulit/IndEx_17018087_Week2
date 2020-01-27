"""
Provide Python code to create either a SQLite database or a MySQL database and insert sample data.
Your solution may make use of any appropriate Python package e.g. sqlite3, mysql-connector, sqlalchemy.
The structure of the database must be as follows:

Database name: rain

Table names: user, forecast, city

Columns for user table: user_id (INTEGER PRIMARY KEY), username (TEXT NOT NULL), email (TEXT NOT NULL)

Columns for city table: city_id (INTEGER PRIMARY KEY), city (TEXT NOT NULL)

Columns for forecast table: forecast_id (INTEGER PRIMARY KEY), city_id (INTEGER, Foreign Key), user_id (INTEGER, Foreign Key), forecast_datetime (TEXT NOT NULL), forecast (text not null), comment (TEXT)

Note: SQLite does not have a datetime data type, use TEXT and enter dates as YYYY-MM-DD HH:MM:SS

Insert the following records into each table:
    [user: user_id, username, email]
        1, weatherman, jo@bloggs.com
        2, itrains, itrains@alot.co.uk
        3, sunny, sunny_grl@sunshine.co.uk
    [city: city_id, city]
        1, London
        2, Manchester
        3, Birmingham
        4, Edinburgh
        5, Belfast
        6, Cardiff
    [forecast: forecast_id, city_id, user_id, forecast_datetime, forecast, comment]
        1, 2, 2, 2020-01-27 09:00:00, 'Moderate rain', 'It is really likely to rain today, sorry folks'
        2, 6, 1, 2020-01-27 09:00:00, 'Heavy rain', 'Don't leave home without full waterproofs today!'
        3, 1, 3, 2020-01-27 09:00:00, 'No rain', 'No umbrella required.'

"""
import sqlite3

sqlite_file = 'rain.db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('''
            CREATE TABLE IF NOT EXISTS user 
            (user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL)
            ''')

c.execute('''
            CREATE TABLE IF NOT EXISTS city 
            (city_id INTEGER PRIMARY KEY,
            city TEXT NOT NULL)
            ''')

c.execute('''
            CREATE TABLE IF NOT EXISTS forecast
            (forecast_id INTEGER PRIMARY KEY, 
            city_id INTEGER, 
            user_id INTEGER, 
            forecast_datetime TEXT NOT NULL, 
            forecast TEXT NOT NULL, 
            comment TEXT,
            FOREIGN KEY (city_id) REFERENCES user(user_id),
            FOREIGN KEY (user_id) REFERENCES city(city_id))''')

user_data = [(1, 'weatherman', 'jo@bloggs.com'),
            (2, 'itrains', 'itrains@alot.co.uk'),
            (3, 'sunny', 'sunny_grl@sunshine.co.uk')]
city_data = [(1, 'London'), (2, 'Manchester'), (3, 'Birmingham'), (4, 'Edinburgh'), (5, 'Belfast'), (6, 'Cardiff')]
forecast_data = [(1, 2, 2, '2020-01-27 09:00:00', 'Moderate rain', 'It is really likely to rain today, sorry folks'),
                 (2, 6, 1, '2020-01-27 09:00:00', 'Heavy rain', 'Dont leave home without full waterproofs today!'),
                 (3, 1, 3, '2020-01-27 09:00:00', 'No rain', 'No umbrella required.')]


c.executemany('INSERT INTO user (user_id, username, email) VALUES (?,?,?)', user_data)
c.executemany('INSERT INTO city (city_id, city) VALUES (?,?)', city_data)
c.executemany(''' INSERT INTO forecast (forecast_id, city_id, user_id, forecast_datetime, forecast, comment) 
                VALUES (?,?,?,?,?,?)''', forecast_data)

conn.commit()
conn.close()
