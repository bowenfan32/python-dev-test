"""
Use a mock so that this test still works but no longer makes a HTTP request to example.com

You can test that it is not making HTTP requests by turning off your internet and
checking if it still works.

It should be possible to run the test in this file using PyTest
eg.
    pytest part_4_2.py

"""
from unittest import mock
from checker import check_website_text


@mock.patch("checker.requests.get")
def test_example(mock_request_get):
    """
    Use mocking to rewrite this test so it doesn't make HTTP requests to example.com
    """
    mock_request_get.return_value.text = "Example Domain. asking for permission."
    assert check_website_text("http://example.com/", "Example Domain")
    assert check_website_text("http://example.com/", "asking for permission")
    assert not check_website_text("http://example.com/", "some random text 123 123")
