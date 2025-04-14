from ApolloToolkit.apollo_tool import ApolloTool
from superagi.tools.base_toolkit import BaseToolkit

class ApolloToolkit(BaseToolkit):
    name = "Apollo Toolkit"
    description = "Toolkit for searching companies using Apollo.io"

    def get_tools(self) -> list:
        return [ApolloTool()]

    def get_env_keys(self) -> list[str]:
        return ["api_key"]
