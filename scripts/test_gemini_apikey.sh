if [ -z "$GEMINI_API_KEY" ]; then
  echo -e "\nERROR: GEMINI_API_KEY is not set.\n"
  echo "Generate your API key at 'aistudio.google.com'"
  echo -e "Then export your Google GEMINI_API_KEY using:\n"
  echo -e "  export GEMINI_API_KEY='your_api_key_here'\n"
  exit 1
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
