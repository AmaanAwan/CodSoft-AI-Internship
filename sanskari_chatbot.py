import random
user_input= " "
print("Hello! Main ek chatbot hoon. Aap ki kaise madad kar sakta hai? Conversation khatam karne ke liye 'End' likna.")
while True:

  while user_input.lower() != 'end':
    user_input = input("You: ")
    user_input = user_input.lower()

    if "aoa" in user_input or "assalam o alaikum" in user_input or "assalam-o-alaikum" in user_input or "asalam-o-alaikum" in user_input or "salam" in user_input:
      print("Sanskari Chatbot: Walaikumasalam! Mai ap ki kis trah madad kar sakta ho?")

    elif "hello" in user_input or "hi" in user_input:
      print("Sanskari Chatbot: Hello there! How can I help you?")

    elif "whats your name" in user_input or "what is your name" in user_input or "tumhara kiya nam ha" in user_input or "apna nam batao" in user_input or "ap kon" in user_input or "tum kon" in user_input or "introduce yourself" in user_input or "give introduction" in user_input or "give your introduction"in user_input:
      print("Sanskari Chatbot: Mera nam Sanskari Chatbot ha. Developed by 'Amaan' for 'Codsoft' as a part of Artificial Intelligence Internship")


    elif "kaise hain aap" in user_input or "kia hal ha" in user_input or "kese hain aap" in user_input or "kya hal ha" in user_input or "kia haal ha" in user_input or "kya haal ha" in user_input:
      print("Sanskari Chatbot: Main theek hoon, aap ka shukriya ke aap ne poucha.")

    elif "mujhe aik mazaq sunao" in user_input or "mujhe aik joke sunao" in user_input or "menu jukat mar" in user_input or "aik joke tou sunao" in user_input or "aik joke sunao" in user_input or "joke sunao" in user_input:
      jokes = ["batakh k paon nhi hoty Hein ..r agar hoty Hein tou wo murghi ban jaaty ha" ,
                 "aik bacha apny abu ky sath ja rha hota ha tou usky baba dariya mai gir jatay hein. bacha pareshani mai ghar bhag jata. Ghar jaky ammi ko bolta ami nalka kholo baba aatay he hongay",
                 "Banta: Yaar teri wife di maut da bara afsos hoya, vaise hoya ki si?" + "Sant: Goli lagi si mathe vich"+"Banta: Shukar kar ke akh bach gayi.",
                 ]
      print("Chatbot: " + random.choice(jokes))
      user_input = input("You: ")
      user_input = user_input.lower()
      if "chuss" in user_input or "thand ho rhi ha" in user_input or "thandi thi" in user_input or "cringe ho rha ha" in user_input or "cringe" in user_input or "cring" in user_input:
          print("   Boy- Pani Pani Pani Pani Pani... Uncle ji pani pila dijye, mera gala sookh rha ha       #ye ha aam zindagi")
          print("   Uncle- Tujay pani pena ha.... ye le pani")
          print("   Boy- Shukriya Uncle ap ko oper wala boht de       #ye ha mentos zindagi")
          print("\nSanskari Chatbot- kaisa diya. Nai diya acha xD.............Iss ko cringe/thandi kehte hein")

      elif "hehe" in user_input or "haha" in user_input or "buhahaha" in user_input or "xd" in user_input:
          print("Glad ap ko acha lga")


    elif "bye" in user_input or "goodbye" in user_input or "allah hafiz" in user_input or "bieee" in user_input:
        print("Chatbot: Khuda hafiz! Have a good day!")
        break

    else:
        print("Chatbot: Maafi chahiye, mujhe samajh nahi aaya. Kya aap apna sawaal dobara saaf alfazon mein keh sakte hain?")

