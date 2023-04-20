import requests

from settings import BASE_URL, BE_PORT


class APIClient:
    def __init__(self):
        self.base_url = f"{BASE_URL}:{BE_PORT}/v1"

    def post(self, tx_hash: str, endpoint: str = "/transaction") -> requests.Response:
        """
        We will not handle any exceptions for unsuccessful response
        This will be done at fixture/test level for negative scenarios
        """
        url = self.base_url + endpoint
        headers = {"Content-Type": "application/json"}
        data = {"hash": tx_hash}
        response = requests.post(url, headers=headers, json=data)
        return response
