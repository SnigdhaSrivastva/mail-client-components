"""Tests for trello_client_api.exceptions coverage."""

from http import HTTPStatus

from trello_client_api.exceptions import (
    TrelloAPIError,
    TrelloAuthenticationError,
    TrelloNotFoundError,
    TrelloRateLimitError,
)


def test_exception_classes_can_be_instantiated() -> None:
    """Each exception carries the expected HTTP status code."""
    api_err = TrelloAPIError("boom", 400)
    assert isinstance(api_err, TrelloAPIError)
    assert api_err.status_code == HTTPStatus.BAD_REQUEST

    auth_err = TrelloAuthenticationError()
    assert isinstance(auth_err, TrelloAuthenticationError)

    nf_err = TrelloNotFoundError("missing")
    assert nf_err.status_code == HTTPStatus.NOT_FOUND

    rl_err = TrelloRateLimitError("slow down")
    assert rl_err.status_code == HTTPStatus.TOO_MANY_REQUESTS
