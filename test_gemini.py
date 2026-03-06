import google.generativeai as genai

genai.configure(api_key='AIzaSyBKeip6QChlcpzYtYK6Nv0mq8MiygDMSAI')
model = genai.GenerativeModel('gemini-flash-latest')

try:
    response = model.generate_content('Say hello in 3 words')
    print('✓ Gemini API is working!')
    print(f'Response: {response.text}')
except Exception as e:
    print(f'✗ Gemini API failed: {str(e)[:150]}')
