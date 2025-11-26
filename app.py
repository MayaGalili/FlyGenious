import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System prompt for backyard chicken expert
SYSTEM_PROMPT = """You are an expert on backyard chicken care, specializing in:
- Chicken feeding: nutrition requirements, feed types, feeding schedules, treats, and supplements
- Chicken health: common diseases, symptoms, treatments, preventive care, and when to consult a veterinarian
- Chicken lifecycle: breeding, hatching, growth stages, egg production, molting, and aging

Provide clear, practical, and accurate advice to help backyard chicken keepers care for their flock. Be friendly, informative, and focus on best practices for small-scale backyard operations."""


def chat_function(message, history):
    """
    Chat function that processes user messages and returns AI responses.
    
    Args:
        message: Current user message
        history: List of previous messages in format [(user_msg, bot_msg), ...]
    
    Returns:
        AI response string
    """
    try:
        # Convert Gradio history format to OpenAI format
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        # Add conversation history
        for user_msg, bot_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": bot_msg})
        
        # Add current user message
        messages.append({"role": "user", "content": message})
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        # Extract and return the assistant's response
        return response.choices[0].message.content
    
    except Exception as e:
        # Handle errors gracefully
        return f"I apologize, but I encountered an error: {str(e)}. Please check your API key and try again."


# Create Gradio interface
def create_interface():
    """Create and launch the Gradio chat interface."""
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
    
    # Create chat interface
    demo = gr.ChatInterface(
        fn=chat_function,
        title="🐔 Backyard Chicken Expert Bot",
        description="Ask me anything about backyard chicken feeding, health, and lifecycle!",
        examples=[
            "What should I feed my chickens?",
            "How often should I check my chickens' health?",
            "When do chickens start laying eggs?",
            "What are common chicken diseases?",
            "How do I care for baby chicks?"
        ]
    )
    
    return demo


if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=False, server_name="0.0.0.0", server_port=7860)

