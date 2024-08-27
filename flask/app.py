from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL connection configuration
MYSQL_HOST = os.getenv('MYSQL_HOST', 'mysql')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'root')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'music_app')

def get_db_connection():
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    return connection

@app.route('/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT users.id, users.username, users.email, GROUP_CONCAT(genres.genre_name) as preferences '
                   'FROM users '
                   'JOIN user_genre_preferencebuis ON users.id = user_genre_preferences.user_id '
                   'JOIN genres ON user_genre_preferences.genre_id = genres.id '
                   'GROUP BY users.id')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
