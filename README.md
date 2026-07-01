# AI Chatbot Project

A Flask-based AI chatbot application powered by Google's Generative AI (Gemini).

## Features

- Real-time chat interface with AI responses
- Built with Flask web framework
- Uses Google Generative AI for intelligent responses
- Clean and responsive UI
- Chat history tracking (coming soon)

## Tech Stack

- **Backend**: Flask 3.0.3
- **AI**: Google Generative AI 0.8.5
- **Environment Management**: python-dotenv 1.1.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Bishwaprotapi/ai_chatbot_project.git
cd ai_chatbot_project
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
- Create a `.env` file in the project root
- Add your Google Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Activate the virtual environment
2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
ai_chatbot_project/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── chatbot/           # Chatbot logic module
├── static/            # Static files (CSS, JS)
├── templates/         # HTML templates
└── .env              # Environment variables (not committed)
```

## API Key

To use this application, you need a Google Gemini API key. Get one from:
https://makersuite.google.com/app/apikey

## License

This project is open source and available under the MIT License.
