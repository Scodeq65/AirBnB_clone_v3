#!/usr/bin/python3
"""
Index file for API views
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['Get'], strict_slashes=False)
def stats():
    """Endpoint that retrives the nos of each objects by type:"""
    return jsonify(amenity=storage.count('Amenity')
                   cities=storage.count("city")
                   places=storage.count("Place")
                   reviews=storage.count("Review")
                   states=storage.count("State")
                   users=storage.count("User"))
