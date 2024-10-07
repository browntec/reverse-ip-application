from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Function to reverse IP
def reverse_ip(ip):
    return '.'.join(reversed(ip.split('.')))

# Connect to the database (SQLite for simplicity)
def store_reverse_ip(reverse_ip):
    conn = sqlite3.connect('ips.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ips (id INTEGER PRIMARY KEY AUTOINCREMENT, reverse_ip TEXT)''')
    cursor.execute('''INSERT INTO ips (reverse_ip) VALUES (?)''', (reverse_ip,))
    conn.commit()
    conn.close()

@app.route('/')
def get_reverse_ip():
    public_ip = request.remote_addr
    reversed_ip = reverse_ip(public_ip)
    store_reverse_ip(reversed_ip)
    return f"Your reversed public IP is: {reversed_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

