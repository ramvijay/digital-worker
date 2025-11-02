# DIGITAL WORKER using Computer-Use Agent

The implementation uses -
    Gemini 2.5 Computer Use model as the brain for deciding on actions
    Playwright as the tool for executing the actions
    CLI as interface to interact with users to get their prompt/intent

Following pre-requisties are required before running the project -

### Installation 

**Set up Python Virtual Environment and Install Dependencies**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Install Playwright and Browser Dependencies**

```bash
# Install system dependencies required by Playwright for Chrome
playwright install-deps chrome

# Install the Chrome browser for Playwright
playwright install chrome

### Configuration

You need a Gemini API key to use the agent:

How to get Gemini API key - You can create and manage all your Gemini API Keys from the [Google AI Studio](https://aistudio.google.com/app/api-keys) API Keys page. More info on setup of API key in google doc - https://ai.google.dev/gemini-api/docs/api-key

```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

### Execution

`main.py` is the entry point for the application

**Command to use to invoke agent**

```bash
python main.py --query "Go to Google and type 'Hello World' into the search bar"
```