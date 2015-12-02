__author__ = 'ali'

from project.models.podcast import Podcast
from . import api

@api.route('/podcast', methods=['GET'])
def podcast():
    return Podcast.get(), 200