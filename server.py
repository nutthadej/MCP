from mcp_sdk import McpServer

def get_weather(location: str) -> str:
    return f"สภาพอากาศที่ {location} คือ แดดออก"

server = McpServer(name="WeatherServer", version="1.0.0")
server.add_tool(get_weather)
server.run()
