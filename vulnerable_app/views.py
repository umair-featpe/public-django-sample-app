from django.http import HttpResponse
from django.shortcuts import render
import sqlite3  # Using SQLite for demonstration; vulnerable to SQL injection

def index(request):
    return HttpResponse("Welcome to the Vulnerable Django App!")

def vulnerable_sql(request):
    # Vulnerability: SQL Injection
    user_id = request.GET.get('user_id', '1')  # Input not validated
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Vulnerable query
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return HttpResponse(f"User data: {result}")

def hardcoded_secret(request):
    # Vulnerability: Hardcoded Secret
    api_key = "my-hardcoded-api-key"  # Hardcoded API key
    return HttpResponse(f"Your API Key is: {api_key}")

