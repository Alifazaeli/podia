__author__ = 'ali'

from project.config import DeploymentConfig
from project.factory import create_app

application = create_app(DeploymentConfig)

if '__main__' == __name__:
    application.run(debug=False, host='0.0.0.0')