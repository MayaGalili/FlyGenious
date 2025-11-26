# Backyard Chicken AI Bot

A web-based AI chatbot that answers technical questions about backyard chicken feeding, health, and lifecycle. Built with Python, Gradio, and OpenAI.

## Features

- 🤖 AI-powered expert advice on backyard chicken care
- 💬 Simple, intuitive chat interface
- 🐔 Covers feeding, health, and lifecycle topics
- 🚀 Easy to set up and run

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation

1. Clone or navigate to this repository:
   ```bash
   cd FlyGenious
   ```

2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install --index-url https://pypi.org/simple/ -r requirements.txt
   ```

4. Set up your API keys:
   - Create a `.env` file in the project root
   - Add your OpenAI API key (required):
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

1. Make sure your virtual environment is activated (if using one)

2. Run the application:
   ```bash
   python3 app.py
   ```

3. Open your browser and navigate to the URL shown in the terminal (typically `http://127.0.0.1:7860`)

4. Start asking questions about backyard chickens!

## Example Questions

- "What should I feed my chickens?"
- "How often should I check my chickens' health?"
- "When do chickens start laying eggs?"
- "What are common chicken diseases?"
- "How do I care for baby chicks?"
- "What's the best feed for laying hens?"
- "How do I prevent mites in my chicken coop?"

## Project Structure

```
FlyGenious/
├── app.py                 # Main Gradio application with OpenAI integration
├── requirements.txt       # Python dependencies
├── .gitignore           # Git ignore file
├── LICENSE              # MIT License
└── README.md            # This file
```

## Configuration

The bot uses OpenAI's `gpt-3.5-turbo` model by default. You can modify the model in `app.py` if needed:

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Change this to "gpt-4" for better responses
    ...
)
```

## Troubleshooting

- **API Key Error**: Make sure your `.env` file exists and contains a valid `OPENAI_API_KEY`
- **Import Errors**: Ensure all dependencies are installed: `pip install --index-url https://pypi.org/simple/ -r requirements.txt`
- **Port Already in Use**: Change the port in `app.py` (line with `server_port=7860`)
- **Module Not Found**: Make sure your virtual environment is activated: `source venv/bin/activate`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

