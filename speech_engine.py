import pyttsx3 
  
class Speech_Engine:
    def __init__(self):
        self.engine = pyttsx3.init() 
    
    def set_rate(self, rate):
        print(f"Setting Rate to {rate}")
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume):
        print(f"Setting Volume to {volume}")
        self.engine.setProperty('volume', volume)

    def set_voice(self, voice_type):
        print(f"Setting Voice to {voice_type}")
        voices = self.engine.getProperty('voices') 
        if voice_type == "female":
            self.engine.setProperty('voice', voices[1].id)
        elif voice_type == "male":
            self.engine.setProperty('voice', voices[0].id)
        else:
            print(f"Error Setting the Voice Type to {voice_type}. Possible voice types are female/male")

    def get_engine_properties(self):
        rate = self.engine.getProperty('rate')
        volume = self.engine.getProperty('volume')
        volume_level = volume*100
        print(f"Speech Rate is {rate}")
        print(f"Speech Volume level is {volume_level}%")
        
    def speak(self, word):
        self.engine.say(word) 
        self.engine.runAndWait()
    
            
speech_engine = Speech_Engine()
speech_engine.get_engine_properties()
speech_engine.set_rate(140)
speech_engine.speak("It is working as expected")
  
    
