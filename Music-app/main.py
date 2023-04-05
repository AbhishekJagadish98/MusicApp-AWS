
import boto3
from boto3.dynamodb.conditions import Key, Attr

from flask import Flask, render_template, request, flash, url_for, redirect, session
import json

app = Flask(__name__)
app.secret_key = 'etretrgrvfevgrerer'

dynamodb = boto3.resource('dynamodb',
                          region_name = 'us-east-1',
                          aws_access_key_id='ASIAX6ND5WK3BZW4W2F7',
                          aws_secret_access_key='DTRFIdUUGV9OG8yxS0YxYl9sfmpowRlomKHuQfkW',
                          aws_session_token='FwoGZXIvYXdzECYaDJVaRtL67NlnLMx1OCLNAXxQeVbbT/PmhGk1sfd4p/aRdlwr8cy3JDcH1XcpITYD602CHH1NGcuTEjjnHgoT3o0dI3HAx/SfiN6jPzSw87CWebKmfusTFwGNxADJt8q0CfN6oAYA0jBOVBy6vsMPfplXyMzKPAbt+gGZDjx9+cdCDgtm60znHVD7BYW5sXb7sGlMqhG+nSpf1/38sOxenLNOQ2Q+ri/ptddhmaU/27YZHztTUQZIX4Mw57YMWdTqaIAaz7QfKRQlYCfyHHUBU0nnYXik+B3wbMpKO/Aop7KwoQYyLWfqCX0EjN/nvAGOpf6Qs/r/7+fKVytCFT1uEzzTuZcf3CJJMiGSN+MhW9fjlA==')


def sessionset(name,items):
    session['user'] = name
    session['subscribe'] = items

def subscribenew(name):
    table = dynamodb.Table('subscribe')
    session.clear()
    response = table.scan(
        FilterExpression=Attr('user_name').contains(name)
        )
    items = response['Items']
    for item in items:
        item['year'] = int(item['year'])
        item['user_name'] = list(item['user_name'])
    sessionset(name,items)
    return list(items)
    
@app.route('/')
def root():
    session.clear()
    return render_template('login.html')

@app.route('/verify', methods = ['POST'])
def verify():
    if request.method == 'POST':
        userid = request.form['email']
        password = request.form['password']

        table = dynamodb.Table('login')
        response = table.query(KeyConditionExpression = Key('email').eq(userid))
        items = response['Items']
        name = items[0]['user_name']
        if(password == items[0]['password']):
            err = ''
            table = dynamodb.Table('subscribe')
            response = table.scan(
            FilterExpression=Attr('user_name').contains(name)
            )
            items = response['Items']
            for item in items:
                item['year'] = int(item['year'])
                item['user_name'] = list(item['user_name'])
            sessionset(name,items)
            return render_template("index.html",name = name,items=list(items))
        else:
            err = "Invalid Credentials Please Check"
            return render_template('login.html',err = err)
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['fname']
        password = request.form['password']

        table = dynamodb.Table('login')
        response = table.scan(
            FilterExpression=Attr('email').contains(email)
            )
        items = response['Items']
        if items:
            err = "Email Already exists"
            return render_template("signup.html", err=err)
        else:
            table.put_item(
                Item = {
                    'email':email,
                    'user_name':name,
                    'password':password
                    }
                )
            return render_template('login.html')
        return render_template('index.html')

@app.route('/query', methods = ['POST'])
def musicquery():
    result = None
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        year = request.form['year']
        
        table = dynamodb.Table('music')
        
        filter_expression = None
        if title:
            filter_expression = Attr('title').contains(title)
        if year:
            filter_expression = Attr('year').contains(year)
        if artist:
            filter_expression = Attr('artist').contains(artist)
        if title and year:
            filter_expression = Attr('title').contains(title)
            filter_expression &= Attr('year').contains(year)
        if title and artist:
            filter_expression = Attr('title').contains(title)
            filter_expression &= Attr('artist').contains(artist)
        if year and artist:
            filter_expression = Attr('year').contains(year)
            filter_expression &= Attr('artist').contains(artist)
        if title and year and artist:
            filter_expression &= Attr('title').contains(title)
            filter_expression &= Attr('year').contains(year)
            filter_expression &= Attr('artist').contains(artist)
            
        if filter_expression:
            response = table.scan(FilterExpression=filter_expression)
            items = response['Items']
            if len(items) == 0:
                result = "No result. Please try again."
            else:
                result = items
        else:
            result = "No result. Please try again."

    return render_template('index.html', result=result)

@app.route('/unsubscribe/<title>/<artist>')
def unsubscribe(title,artist):
    name = session['user']
    tableName = dynamodb.Table('subscribe')
    response = tableName.update_item(
        Key={
        'title': title,
        'artist':artist
        },
        UpdateExpression='DELETE #user_name :name',
        ExpressionAttributeNames={
            '#user_name': 'user_name'
        },
        ExpressionAttributeValues={':name': set([name])}
    )
    items = subscribenew(name)
    return render_template("index.html", name=name, items=items)

@app.route('/subscribe/<title>/<artist>/<year>')
def subscribe(title, artist, year):
    name = session['user']
    tableName = dynamodb.Table('subscribe')
    response = tableName.scan(
        FilterExpression=Attr('title').eq(title)
    )
    items = response['Items']
    for item in items:
        item['year'] = int(item['year'])
        if 'user_name' in item:
            item['user_name'] = list(item['user_name'])
    if items:
        response = tableName.update_item(
            Key={
                'title': title,
                'artist': artist
            },
            UpdateExpression='ADD #user_name :name',
            ExpressionAttributeNames={
                '#user_name': 'user_name'
            },
            ExpressionAttributeValues={':name': set([name])}
        )
        items = subscribenew(name)
        return render_template("index.html", name=name, items=items)
    else:
        item = {
            'title': str(title),
            'artist': artist,
            'user_name': set([name]),
            'year': year
        }
        response = tableName.put_item(Item=item)
        items = subscribenew(name)
        return render_template("index.html", name=name, items=items)

 
if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)
