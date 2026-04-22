from agents import function_tool, AgentHooks, Agent, Tool, RunContextWrapper
import streamlit as st
from models import UserAccountContext

class AgentToolUsageLoggingHooks(AgentHooks):
    async def on_tool_start(self,
        context: RunContextWrapper[UserAccountContext],
        agent: Agent[UserAccountContext],
        tool: Tool,
        ):
            with st.sidebar:
                st.write(f"{agent.name} starting tool: {tool.name}")
    async def on_tool_end(self,
        context: RunContextWrapper[UserAccountContext],
        agent: Agent[UserAccountContext],
        tool: Tool,
        result: str,
        ):
            with st.sidebar:
                st.write(f"{agent.name} used tool: {tool.name}")
                st.code(result)
    async def on_handoff(
        self,
        context: RunContextWrapper[UserAccountContext],
        agent: Agent[UserAccountContext],
        source: Agent[UserAccountContext],
    ):
        with st.sidebar:
            st.write(f"🔄 Handoff: **{source.name}** → **{agent.name}**")

    async def on_start(
        self,
        context: RunContextWrapper[UserAccountContext],
        agent: Agent[UserAccountContext],
    ):
        with st.sidebar:
            st.write(f"🚀 **{agent.name}** activated")

    async def on_end(
        self,
        context: RunContextWrapper[UserAccountContext],
        agent: Agent[UserAccountContext],
        output,
    ):
        with st.sidebar:
            st.write(f"🏁 **{agent.name}** completed")