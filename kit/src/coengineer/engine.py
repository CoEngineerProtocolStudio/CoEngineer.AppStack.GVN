import vertexai
from vertexai.generative_models import GenerativeModel, Tool, Content, Part
from vertexai.preview import rag

class CoEngineerStack:
    def __init__(self, project_id, location, corpus_id, credentials, system_prompt):
        """
        Senior Overviewer: Logic encapsulated. 
        Trade-off: Passing credentials directly ensures the engine is platform-agnostic 
        (works in Streamlit, CLI, or Cloud Functions).
        """
        vertexai.init(project=project_id, location=location, credentials=credentials)
        
        self.tool = Tool.from_retrieval(
            retrieval=rag.Retrieval(
                source=rag.VertexRagStore(
                    rag_resources=[rag.RagResource(rag_corpus=corpus_id)],
                    similarity_top_k=3,
                ),
            )
        )
        
        self.model = GenerativeModel(
            model_name="gemini-2.0-flash",
            tools=[self.tool],
            system_instruction=system_prompt
        )

    def get_chat_response(self, prompt, history_messages=None):
        """
        Converts list of dicts to Vertex AI Content objects.
        """
        history = []
        if history_messages:
            history = [
                Content(
                    role="user" if m["role"] == "user" else "model", 
                    parts=[Part.from_text(m["content"])]
                ) for m in history_messages
            ]
            
        chat = self.model.start_chat(history=history)
        return chat.send_message(prompt)
