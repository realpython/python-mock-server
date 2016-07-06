# Third-party imports...
from nose.tools import assert_true
import requests


def test_request_response():
    # Send a request to the real API server and store the response.
    response = requests.get(
        'http://jsonplaceholder.typicode.com/users'
    )

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)
