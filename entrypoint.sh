#!/bin/bash

echo "Starting Ollama server..."
# Launch the Ollama server
ollama serve &
# Wait for the server to start
sleep 5

echo "Pulling deepseek model..."
ollama pull deepseek-r1:1.5b

echo "Pulling zephyr model..."
ollama pull zephyr:7b

# Keep the container running
tail -f /dev/null
