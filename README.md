# AI LangChain Base

A Docker-based Python application demonstrating LangChain integration with Google's Gemini AI model for generating article titles from content.

## Features

- **LangChain Integration**: Uses LangChain framework for AI application development
- **Google Gemini AI**: Leverages Google's Gemini 2.0 Flash model for content generation
- **Structured Output**: Implements structured output parsing for consistent JSON responses
- **Docker Support**: Containerized application for easy deployment and distribution
- **API Key Management**: Secure handling of Google Gemini API keys

## Prerequisites

- Docker installed on your system
- Google Gemini API key (get one at [Google AI Studio](https://aistudio.google.com))

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AI-langchain-base
```

### 2. Set Up API Key

Export your Google Gemini API key:

```bash
export GEMINI_API_KEY='your_api_key_here'
```

Or test your API key using the provided script:

```bash
chmod +x scripts/test_gemini_apikey.sh
./scripts/test_gemini_apikey.sh
```

### 3. Build and Run with Docker

```bash
# Build the Docker image
docker build -t langchain-base .

# Run the container
docker run -e GEMINI_API_KEY=$GEMINI_API_KEY langchain-base
```

## Local Development

### 1. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python main.py
```

## How It Works

The application demonstrates a LangChain workflow that:

1. **Takes an article** about AI-powered customer feedback analysis
2. **Uses Google Gemini AI** to generate creative article titles
3. **Applies structured output parsing** to ensure consistent JSON format
4. **Returns 10 suggested titles** based on the article content

### Example Output

```json
{
    "article_titles": [
        "AI-Powered Customer Feedback Analysis: Transforming Raw Data into Actionable Insights",
        "Real-Time Customer Sentiment: How AI Revolutionizes Product Development",
        "From Feedback to Success: AI-Driven Customer Experience Optimization",
        "The Future of Customer Satisfaction: AI Analytics in Action",
        "Smart Feedback Systems: AI's Role in Business Growth",
        "Customer Voice Amplified: AI Tools for Product Innovation",
        "Beyond Surveys: AI-Powered Customer Intelligence Platforms",
        "Data-Driven Decisions: AI Analytics for Customer-Centric Businesses",
        "The AI Advantage: Transforming Customer Feedback into Competitive Edge",
        "Intelligent Insights: How AI Reads Between the Lines of Customer Feedback"
    ]
}
```

## Project Structure

```
AI-langchain-base/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── README.md              # This file
└── scripts/
    └── test_gemini_apikey.sh  # API key validation script
```

## Dependencies

- **langchain**: Core LangChain framework
- **langchain_google_genai**: Google Gemini integration for LangChain
- **termcolor**: Colored terminal output
- **langchain_openai**: OpenAI integration (commented out, available for future use)

## Configuration

The application uses two AI models with different temperature settings:

- **Analytical Model**: `temperature=0.0` for consistent, factual responses
- **Creative Model**: `temperature=0.9` for more creative and varied outputs

## API Key Security

- API keys are handled securely through environment variables
- Interactive prompts for API key input when not set in environment
- Test script validates API key before running the main application

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker and local Python environment
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions:
- Check the [Google AI Studio documentation](https://aistudio.google.com)
- Review [LangChain documentation](https://python.langchain.com)
- Open an issue in this repository

