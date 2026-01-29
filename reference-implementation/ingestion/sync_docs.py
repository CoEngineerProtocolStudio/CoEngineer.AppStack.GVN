import os
from google.oauth2 import service_account
from vertexai.preview import rag
import vertexai

# Senior Overviewer Pivot: 
# Using direct file uploads for the initial corpus seeding.
# Trade-off: Local file upload is faster for small protocol sets (<100MB) 
# compared to setting up a GCS trigger.

def sync_protocols(project_id, location, corpus_id, file_path):
    vertexai.init(project=project_id, location=location)
    
    # Logic: Point to specific corpus and upload protocol
    # Trade-off: Using 'preview.rag' for the latest vector search features.
    response = rag.upload_file(
        corpus_name=f"projects/{project_id}/locations/{location}/ragCorpora/{corpus_id}",
        display_name=os.path.basename(file_path),
        path=file_path,
    )
    return response

if __name__ == "__main__":
    # Developer: Replace these with your actual IDs from .streamlit/secrets.toml
    PID = "your-project-id"
    LOC = "us-central1"
    CID = "your-corpus-id"
    FILE = "protocols.md"
    
    print(f"Syncing {FILE} to Corpus {CID}...")
    res = sync_protocols(PID, LOC, CID, FILE)
    print(f"Success. File ID: {res.name}")
