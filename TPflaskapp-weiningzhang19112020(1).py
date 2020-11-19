from flask import Flask 
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello DC'
if __name__ == '__main__':
    app.run()

book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
@app.route('/api/<books>')
def get_json(books):
    return 'get json {}'.format(books)
