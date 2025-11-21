from gtts import gTTS 
import os
text = "hahahahahaha"
# generate our speech
output = gTTS(text=text,lang='en',slow=False)
# save it as an mp3 file
output.save('output.mp3')
# your operating system has a tool which can actually play this mp3 file
os.system("start output.mp3")




