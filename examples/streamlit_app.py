from coengineer import CoEngineerStack, Config
import streamlit as st

# Low energy/High efficiency setup
cfg = Config()
creds = cfg.get_credentials(st.secrets["gcp_service_account"])

# The engine now handles all VertexAI boilerplate internally
engine = CoEngineerStack(
    project_id=cfg.project_id,
    location=cfg.location,
    corpus_id=cfg.full_corpus_path,
    credentials=creds,
    system_prompt="..." 
)
