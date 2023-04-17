from src import app

app.config['SECRET_KEY'] = 'hola'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    
