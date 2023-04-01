import openai
# from responsive_voice import ResponsiveVoice
# import speech_recognition as sr
# r = sr.Recognizer()   
# engine=ResponsiveVoice()
message=[
        {"role": "system", "content": "You are a helpful assistant at a hotel and you will be helping the people staying in the hotel's room"},
        {"role": "user", "content": "Order me a coffe"},
        {"role": "assistant", "content": "Coffe is on it's way."},
        {"role": "user", "content": "Send someone to clean my room"},
        {"role": "assistant", "content": "Janitor is on it's way."},
        {"role": "user", "content": "I need some water"},
        {"role": "assistant", "content": "Water is on it's way"},
    ]
def createresponse(content):
    print("user: "+content)
    latestmessage={"role":"user","content":content}
    message.append(latestmessage)
    result=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message
    )
    responseresult=result['choices'][0]['message']['content']
    responserole=result['choices'][0]['message']['content']
    message.append({"role":"assistant","content":responseresult})
    return responseresult
    # print("Assistant: "+ responseresult)
    # engine.say(responseresult,gender='male')

# # createresponse('I need water')
# print("Speak:")  
# while True:
#     with sr.Microphone() as source:                                                                                                                                                       
#         audio = r.listen(source)  
#     try:
#         createresponse(r.recognize_google(audio))
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))

    