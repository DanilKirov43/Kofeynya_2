from flask import Flask, jsonify, render_template
import psycopg2

app = Flask(__name__)

# Конфигурация базы данных
DB_CONFIG = {
    'dbname': 'coffee_registretion',
    'user': 'postgres',
    'password': '613930',
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, description, price, image_url FROM products')
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    
    product_list = [
        {
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'price': float(row[3]),
            'image_url': row[4]
        }
        for row in products
    ]
    return jsonify(product_list)

if __name__ == '__main__':
    app.run(debug=True)
