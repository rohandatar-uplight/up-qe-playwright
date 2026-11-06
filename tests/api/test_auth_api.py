
async def test_get_users(api_request_context):
    """Test retrieving a page of users from the ReqRes API."""
    response = await api_request_context.get("/api/users", params={"page": 2})

    assert response.is_success
    assert response.status_code == 200

    response_body = response.json()
    assert response_body["page"] == 2
    assert response_body["data"]
    assert response_body["data"][0]["email"]