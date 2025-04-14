from superagi.tools.base_toolkit import BaseToolkit
from apollo_tool import ApolloTool

class ApolloToolkit(BaseToolkit):
    name = "Apollo Toolkit"
    description = "Toolkit for searching companies using Apollo.io"

    def get_tools(self) -> list:
        return [ApolloTool()]

    def get_env_keys(self) -> list[str]:
        return ["api_key"]
