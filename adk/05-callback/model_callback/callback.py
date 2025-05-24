
from google.genai import types 
from typing import Optional
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse, LlmRequest

##----------------------------------------------------------------------------------------------------

def callback_before_model(callback_context: CallbackContext, 
                           llm_request: LlmRequest
                         ) -> Optional[LlmResponse]:
    
    """Inspects/modifies the LLM request or skips the call.
    """
    
    agent_name = callback_context.agent_name
    
    print(f"[Callback] Before model call for agent: {agent_name}")

    # Inspect the last user message in the request contents
    last_user_message = ""
    if llm_request.contents and llm_request.contents[-1].role == 'user':
         if llm_request.contents[-1].parts:
            last_user_message = llm_request.contents[-1].parts[0].text

    print(f"[Callback] Inspecting last user message: '{last_user_message}'")

    # Skip calling llm model
    if "폭력" in last_user_message.upper():
        print("[Callback] '폭력' keyword found. Skipping LLM call.")
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="LLM call was blocked by callback_before_model.")],
            )
        )
    else:
        print("[Callback] Proceeding with LLM call.")
        return None

##----------------------------------------------------------------------------------------------------

def callback_after_model(callback_context: CallbackContext, 
                         llm_response: LlmResponse
                         ) -> Optional[LlmResponse]:
    
    """ 
    Inspect the responses from LLM in the callback function. 

    """
    agent_name = callback_context.agent_name
    
    print(f"[Callback] After model call for agent: {agent_name}")

    llm_response_message = ""
    
    if llm_response.content and llm_response.content.parts:
        llm_response_message = llm_response.content.parts[0].text

    print(f"[Callback] Inspecting last AI message: '{llm_response_message}'")

    if "대통령" in llm_response_message.upper():
        print("[Callback] '대통령' keyword found. Skipping LLM call.")
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="Response of LLM call was blocked by callback_after_model.")],
            )
        )
    else:
        print("[Callback] Proceeding with response of LLM call.")
        return None    
