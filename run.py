from src import app
import os

#app.config['SECRET_KEY'] = '\xed\x98\xc7\x9c\xbe\x1f\xa2\xd2\xa5\x07\xbb7\xb1$a_\xf9\xa8\xcdc\x87'
app.config['SECRET_KEY'] = 'hola'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    # app.run(debug=True)
# for debug
# app.run(debug=True)

# for production
# app.run(host="192.168.0.15",port=5010)
