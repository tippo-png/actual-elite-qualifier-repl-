#                Simple chat program
import random


#                 the chatbot responses - start

#starting response after first print
def st_response(st_index):
  chatbot_st = [
#index # dictates which root is taken
#index [0] or in_0 - normal
    "hello, How are you.",
#index [1] or in_1 - sad
    "hi, my dog died.",
  ]
  st_index = random.randint(0,len(chatbot_st)-1)
  return st_index, chatbot_st[st_index]


chatbot_a = ["well thats great, im going to the store right now so maybe we could talk later. Test",
"cool kool, well i need to go so ill just leave you with this medal."]


chatbot_b = ["oh, um yea sure. can we talk later. Test", "its...its fine... i guess. i uhhh, i gotta go. see ya later"]


#                end of the chatbot responses 


def init_chat():
  index_st = 0
  user_input = ""
  temp_tup = ()
#quit funciton
  quit_character = 'q'
  if user_input == quit_character:
    print('Well, ok then. Thanks for talking to me.')
  
 #                  the game - the meat - the SAUCE

  while user_input != quit_character:
#first words printed

    user_input = input("This is a chatbot, to proceed with the chatting you need only say  hello... and only hello. Or hi, thats good to. \n")

    if user_input == "hi" or user_input == "hello":
      print("Good job. Lets start. \n")
      #root is randomly selected
      temp_tup = (st_response(index_st))
      index_st = temp_tup[0]
      print(temp_tup[1])
    else:
      print("I see your going to be a difficult one huh, well... well see about that at the end. Lets start \n")
      temp_tup = (st_response(index_st))
      index_st = temp_tup[0]
      print(temp_tup[1])

#Route 0 code
    if index_st == 0:
      #user responses list for chatbot_a
      user_res = {"good, how about you", "good how about you", "bad", }
      user_input = input()

      for phrase in user_res:
        if user_input.lower() == phrase:
          print(chatbot_a[0])
          print(' ')
          break
        else:
          print(chatbot_a[1])
          print(' ')
          break

#route 1 code
    if index_st == 1:
      #user responses list for chatbot_b
      user_res2 = {"well that sucks", "okay", "ok", "oh, ok", "oh ok","oh, no", "oh no", "thats not good"}

      user_input = input()


      for phrase in user_res2:
        if user_input.lower() == phrase:
          print(chatbot_b[0])
          print(' ')
          break
        else:
          print(chatbot_b[1])
          print(' ')
          break

    user_input = input("if you wish to play agian then press enter, if not then press 'q', then the 'enter' key"+ "\n")


  
    

if __name__ == "__main__":
  init_chat()
  
  

#websites used:
#https://www.w3schools.com/
