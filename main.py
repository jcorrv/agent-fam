import asyncio
import os

from mcp import ClientSession
from mcp.client.sse import sse_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

async def main():
    model = "openai:gpt-5"
    sse_url = os.environ['ACIDEV_ENDPOINT']
    async with sse_client(sse_url) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)

            agent = create_react_agent(model, tools)

            # TODO fill in invocation


if __name__ == "__main__":
    asyncio.run(main())
