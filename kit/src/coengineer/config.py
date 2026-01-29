import os
import json
from google.oauth2 import service_account
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.project_id = os.getenv("PROJECT_ID")
        self.location = os.getenv("LOCATION")
        self.corpus_id = os.getenv("CORPUS_ID")
        
        if not all([self.project_id, self.location, self.corpus_id]):
            raise EnvironmentError("Missing PROJECT_ID, LOCATION, or CORPUS_ID in .env")

    def get_credentials(self, raw_creds):
        """
        Pivot: Standardizes credentials from Streamlit secrets or local JSON.
        Handles the newline escape character issues found in TOML/Env files.
        """
        creds_info = dict(raw_creds) if not isinstance(raw_creds, str) else json.loads(raw_creds)
        
        if "private_key" in creds_info:
            creds_info["private_key"] = creds_info["private_key"].strip().replace("\\n", "\n")
            
        return service_account.Credentials.from_service_account_info(creds_info)

    @property
    def full_corpus_path(self):
        return f"projects/{self.project_id}/locations/{self.location}/ragCorpora/{self.corpus_id}"
