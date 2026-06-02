import ollama

def test_ollama_connection():
    print("Testing Ollama connection...")
    
    try:
        models = ollama.list()
        print("Available models:")
        for model in models['models']:
            print(f"  - {model['name']}")
        
        print("\nTesting model response...")
        response = ollama.chat(
            model='deepseek-r1:7b',
            messages=[{'role': 'user', 'content': 'Hello!'}]
        )
        print(f"Response: {response['message']['content']}")
        print("\n鉁?Ollama API is working correctly!")
        return True
    except Exception as e:
        print(f"鉂?Error: {e}")
        print("\nNote: Please ensure Ollama is installed and running.")
        print("Install Ollama: https://ollama.com/download")
        print("Download model: ollama pull deepseek-r1:7b")
        return False

if __name__ == "__main__":
    test_ollama_connection()