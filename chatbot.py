import google.generativeai as genai
genai.configure(api_key="AIzaSyC28oa2gxbJYxVGQ2POdhSSQF794KhJMPE") 
model = genai.GenerativeModel("gemini-pro")
def chatbot_response(user_input):
 response = model.generate_content(user_input)
 return response.text
while True:
 user_input = input("You: ")
 if user_input.lower() == "exit":
   break
 print("AI:", chatbot_response(user_input)) 