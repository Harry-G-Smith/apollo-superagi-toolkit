import requests
from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field

class ApolloInput(BaseModel):
    search_query: str = Field(..., description="Search keyword, e.g., 'FinTech SaaS'")

class ApolloTool(BaseTool):
    name = "Apollo Lead Finder"
    description = "Finds leads from Apollo based on a keyword search"
    args_schema = ApolloInput

    def _execute(self, search_query: str):
        headers = {
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.get_tool_config('api_key')}"
        }

        params = {
            "q_organization_domains": search_query,
            "page": 1,
            "per_page": 5
        }

        response = requests.get(
            "https://api.apollo.io/v1/organizations/search",
            headers=headers,
            params=params
        )

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"
