
from google.genai import types 
from typing import Dict, Any

from typing import Optional
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.base_tool import BaseTool
from copy import copy

##----------------------------------------------------------------------------------------------------

def get_capital_city(country: str) -> str:
    """Retrieves the capital city of a given country."""
    print(f"--- Tool 'get_capital_city' executing with country: {country} ---")
    country_capitals = {
        "US": "Washington, D.C.",
        "canada": "Ottawa",
        "france": "Paris",
        "germany": "Berlin",
        "italy": "Rome",
        "japan": "Tokyo",
        "South Korea": "Seoul",
    }
    return country_capitals.get(country.lower(), f"Capital not found for {country}")

##----------------------------------------------------------------------------------------------------

def callback_before_tool(tool: BaseTool, 
                         args: Dict[str, Any], 
                         tool_context: ToolContext
                        ) -> Optional[Dict]:
    
    """Inspects/modifies the LLM request or skips the call.
    """
    
    agent_name = tool_context.agent_name
    tool_name = tool.name
    print(f"[Before Tool] Before tool call for tool '{tool_name}' in agent '{agent_name}'")
    print(f"[Before Tool] Original args: {args}")

    if tool_name == 'get_capital_city' and args.get('country', '').lower() == 'seoul':
        print("[Before Tool] Detected 'Canada'. Modifying args to 'France'.")
        args['country'] = 'South Korea'
        print(f"[Before Tool] Modified args: {args}")
        return None

    
    if tool_name == 'get_capital_city' :
        print("[Before Tool] Detected 'BLOCK'. Skipping tool execution.")
        return {"result": "Tool execution was blocked by before_tool_callback."}

    print("[Before Tool] Proceeding with original or previously modified args.")
    return None

##----------------------------------------------------------------------------------------------------

def callback_after_tool(tool: BaseTool, 
                        args: Dict[str, Any], 
                        tool_context: ToolContext, 
                        tool_response: Dict
                        ) -> Optional[Dict]:
    
    agent_name = tool_context.agent_name
    tool_name = tool.name
    print(f"[After Tool] After tool call for tool '{tool_name}' in agent '{agent_name}'")
    print(f"[After Tool] Args used: {args}")
    print(f"[After Tool] Original tool_response: {tool_response}")

    original_result_value = tool_response

    # --- Modification Example ---
    # If the tool was 'get_capital_city' and result is 'Washington, D.C.'
    if tool_name == 'get_capital_city' and original_result_value == "Washington, D.C.":
        print("[After Tool] Detected 'Washington, D.C.'. Modifying tool response.")

        # IMPORTANT: Create a new dictionary or modify a copy
        modified_response = copy.deepcopy(tool_response)
        modified_response["result"] = f"{original_result_value} (Note: This is the capital of the USA)."
        modified_response["note_added_by_callback"] = True # Add extra info if needed

        print(f"[After Tool] Modified tool_response: {modified_response}")
        return modified_response # Return the modified dictionary

    print("[After Tool] Passing original tool response through.")
    # Return None to use the original tool_response
    return None