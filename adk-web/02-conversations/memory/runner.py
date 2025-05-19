import asyncio
from google.genai import types
from google.adk.sessions import BaseSessionService
from google.adk.runners import Runner, RunConfig, StreamingMode
from google.adk.memory import BaseMemoryService

from memory import agent

async def run_agent( session_service: BaseSessionService,
                     memory_service: BaseMemoryService,
                     app_name: str,
                     user_id: str,
                     session_id: str,
                     ):
    """
    Run Agent. 

   
    """
    
    runner = Runner(agent=agent.search_agent,
                    app_name=app_name,
                    session_service=session_service,
                    memory_service=memory_service)


    search_session = session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id,
    )

    search_input = input("You: ")
    if search_input.lower() == "exit":
        return
    
    print("Question 1: ", search_input)

    content_search = types.Content(role='user', parts=[types.Part(text=search_input)])

    async for event in runner.run_async(user_id=search_session.user_id, 
                            session_id=search_session.id, 
                            new_message=content_search):
        
        if event.is_final_response():
            final_response_text = event.content.parts[0].text
            print(f"Agent 1 Final Response: {final_response_text}")

    completed_session_1 = session_service.get_session(app_name=search_session.app_name, 
                                                      user_id=search_session.user_id, 
                                                      session_id=search_session.id)

    print("\n--- Adding Session 1 to Memory ---")
    await memory_service.add_session_to_memory(completed_session_1)
    print("Session added to memory.")

    #-----------------------------------------------------------------

    recall_session_id = "recall_session_id"
    recall_session = session_service.create_session(app_name=app_name, 
                                                    user_id=user_id, 
                                                    session_id=recall_session_id)

    runner.agent = agent.recall_agent
    
    recall_instruction = input("You: ")
    if recall_instruction.lower() == "exit":
        return
    
    print("Question 2: ", recall_instruction)

    content_recall = types.Content(role='user', parts=[types.Part(text=recall_instruction)])

    async for event in runner.run_async(user_id=recall_session.user_id, 
                                  session_id=recall_session.id, 
                                  new_message=content_recall):

        print(f"  Event: {event.author} - Type: {'Text' if event.content and event.content.parts and event.content.parts[0].text else ''}"
            f"{'FuncCall' if event.get_function_calls() else ''}"
            f"{'FuncResp' if event.get_function_responses() else ''}")
        
        if event.is_final_response():
            final_response_text_2 = event.content.parts[0].text
            print(f"Agent 2 Final Response: {final_response_text_2}")
            break 


