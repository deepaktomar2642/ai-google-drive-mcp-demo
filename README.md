# ai-google-drive-mcp-demo
Demo project: AI agent interacting with Google Drive via MCP

This is a complete end-to-end Python demo that:


- Connects to Google Drive (via MCP)
- Lists, uploads, downloads, deletes files
- Uses OpenAI GPT to summarize, generate, and rewrite files
- Runs as a simple CLI application


## Setup


1. Install dependencies:
```
pip install -r requirements.txt
```


2. Set your OpenAI API key:
```
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```


3. Download Google OAuth credentials and save as `credentials.json`.


4. Run the app:
```
python main.py
```
"""
