"""
Centralized configuration management with environment validation.
Architectural Choice: Singleton pattern ensures consistent configuration 
across all components and prevents multiple env file reads.
"""
import os
import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Load environment variables
load_dotenv()

@dataclass
class NewsAPIConfig:
    """News API configuration with validation"""
    api_key: str
    sources: str
    page_size: int