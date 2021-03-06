
import sys

from flask import Flask
from flask.ext import restful

import factorial007

app = Flask(__name__)
api = restful.Api(app)

class Factorial(restful.Resource):
    def factorial(self, number):
        return factorial007.fact(number)

    def get(self, number):
        return self.factorial(number)

api.add_resource(Factorial, '/factorial/<int:number>')

if __name__ == '__main__':
    if sys.argv[1] == "test":
        factorial = Factorial()
        assert(factorial.factorial(10) == 3628800)
        sys.exit(0)
    app.run(debug=True, host='0.0.0.0')

