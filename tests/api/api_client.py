
# import pytest
# import httpx
# from typing import Optional, Dict, Any

# class APIClient:
#     def __init__(self, base_url: str):
#         self.base_url = base_url
#         self.token = None
#         self.headers = {"Content-Type": "application/json"}
#         self.client = httpx.AsyncClient(base_url=base_url, timeout=10.0)

#     async def login(self, username, password):
#         """Login and set authentication token."""
#         url = "/api/v1/auth/login/access-token"
#         data = {
#             "username": username,
#             "password": password
#         }
#         # OAuth2 password flow uses form-urlencoded
#         response = await self.client.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
#         if response.status_code == 200:
#             token_data = response.json()
#             self.token = token_data.get("access_token")
#             self.headers["Authorization"] = f"Bearer {self.token}"
#             return True
#         return False

#     async def get(self, endpoint, params=None):
#         return await self.client.get(endpoint, headers=self.headers, params=params)

#     async def post(self, endpoint, data=None, json=None):
#         return await self.client.post(endpoint, headers=self.headers, data=data, json=json)
    
#     async def put(self, endpoint, json=None):
#         return await self.client.put(endpoint, headers=self.headers, json=json)

#     async def delete(self, endpoint):
#         return await self.client.delete(endpoint, headers=self.headers)
    
#     async def close(self):
#         await self.client.aclose()
