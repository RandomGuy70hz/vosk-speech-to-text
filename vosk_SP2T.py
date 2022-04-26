import time
import speech_recognition as sr
from vosk import Model

r = sr.Recognizer()
source = sr.Microphone()
model = Model("model/")
timestr = time.strftime("H(%H) - M(%M) - S(%S)")
moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())

f = open(moment+'.log', 'w')
init = True

while init:

    try: 

        with sr.Microphone() as source:


            print("recording...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            
            audio2 = r.listen(source)
            MyText = r.recognize_vosk(audio2)
            MyText = MyText.lower()

            if str is bytes:
                result = u"{}".format(MyText).encode("utf-8")

            else:
                result = "{}".format(MyText)

            print(MyText)
            f.write("\n")
            f.write(timestr)
            f.write("\n")
            f.write(MyText)
            f.write("\n")
            print(result)                



    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occured")
    
    except LookupError:  
        print("Could not understand audio")

    except KeyboardInterrupt:
        print('\n ...stopped')
        break
