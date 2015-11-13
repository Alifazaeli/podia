__author__ = 'ali'

from project.config import DevelopmentConfig
from project.factory import create_app

application = create_app(DevelopmentConfig)

if '__main__' == __name__:
    application.run(debug=True, host='0.0.0.0')