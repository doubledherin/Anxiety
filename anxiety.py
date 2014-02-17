from sys import exit
from random import randint

def clear_screen():
    i = 0
    while i < 20:
        print " "
        i += 1
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    
while True:
    
    if answer == "pinch myself":
        Wake()
    
    elif answer == "quit" or answer == "stop":
        exit()
    
class Scene(object):
    
    def enter(self):
        exit(1)
        
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map

        
    def play(self):
        current_scene = self.scene_map.opening_scene()
                                 
        print """
                                    o 0           ~~~ANXIETY~~~        o 0
                                    ^^^                                ^^^  
                                
                                          a game by Wendy Dherin"""
        while True:     
            print "\n" * 25
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)        
        
class Bathroom(Scene):
    
    def enter(self):
        clear_screen()
        print "\nYour alarm goes off, and you wake up feeling so relaxed and well rested."
        print "You really needed a good night's sleep like that, after all that's been going on!"
        print "You get out of bed, yawn and stretch, look out the window, and smile. It's a"
        print "gorgeous morning, and you have a profound sense that things are going to"
        print "start turning around. You head into the bathroom to brush your teeth. Wow! You're"
        print "looking great! One thing catches your eye though. Your right eye tooth ... it just ..."
        print " flashed or something. You look closer ... and you see it's discolored. Now you feel the"
        print " slight stirring of uneasiness in the pit of your belly. Part of you wants to ignore it."
        print " The day is going way too well. Why ruin a good thing? But part of you wants to look"
        print " closer. What do you do?"
        
        while True:
            
            answer = raw_input("type 'ignore' or 'look': ")
        
            if answer == "ignore":
                clear_screen()
                return 'brush_teeth'
        
            elif answer == "look":
                clear_screen()
                return 'tooth_dialogue'
                
                
class ToothDialogue(Scene):
    def enter(self):
        clear_screen()
        print "You lean in closer to the mirror to examine the suspect tooth. It's more discolored than"
        print "you thought. In fact ... there's a concave arc lined with tiny little hairs. It looks"
        print "just like--"
        print "all of a sudden, the little hairs flutter, and the concave arc moves, opening up into a brilliant"
        print "bright green eye. You want to scream, but all of the air has rushed out of your lungs."
        print "The eye blinks at you, innocently, and then you hear a voice in your head. A thin, whispery voice."
        print "'I am your inner voice,' it says. 'Your true essential self; your deepest wisdom.'"
        print "'Shouldn't that be the role of my wisdom teeth?' you think."
        print "You hear a sigh. 'You had them extracted in the 10th grade, remember? We eye teeth are heirs to their throne."
        print "You realize the eye tooth can read your mind."
        print "'Why is it just you? What happened to my other eye tooth?'"
        print "'He's kind of a deadbeat, to be honest. I'm all you've got now."
        print "'So why now? What do you want from me?"
        print "'The question is, what do you want from me? I'm only here because you need me."
        print "'If you can answer all three of my questions correctly, I'll grant you a wish. Are you game?"        
                
        while True:
            
            answer = raw_input("type 'yes' or 'no': ")
        
            if answer == "yes":
                return 'riddle1'
        
            elif answer == "no":
                return 'brush_teeth'
            
            elif answer == "pinch myself":
                return 'wake'    
    
            else: 
                continue
                    
class BrushTeeth(Scene):
    
    def enter(self):
        print "\nYou start brushing your teeth, pretending nothing weird happened just now."
        print "But something's off. Your eye tooth is wiggling as you brush. It's loose! You stop"
        print "brushing, put down the toothbrush, and gingerly take hold of your eye tooth with"
        print "your fingers. As soon as you touch it, it falls into the palm of your hand. You look"
        print "in the mirror and see a ridiculous gap where your tooth once was. You close your eyes"
        print " in anguish. Why you?! Now you're going to have to face everyone today looking like"
        print "this. All of a sudden, like an avalanche, all of your teeth start crumbling and falling"
        print "into your mouth, and you start gagging on them."
        return 'wake'
        
class Riddle(Scene):
    
    def enter(self):
        exit(1)
        
class RiddleOne(Riddle):
    
    def enter(self):
        print "Your eye tooth clears its throat. 'The first riddle is the easiest."
        print "What is the name of a surface with only one side and only one boundary component?"
        
        answer = raw_input("> ")
        answer = answer.lower()
        
        if answer.__contains__("mobius") or answer.__contains__("moebius"):
            return "riddle2"
        else:
            print "'Wow. I don't think you even tried,' says the eye tooth."
            print "'I don't know why I even waste my time.' And with that, the eye closes, and "
            print "your tooth goes back to normal. You decide it was a weird hallucination and "
            print "try to put it all behind you."
            return "brush_teeth"

class RiddleTwo(Riddle):
    
    def enter(self):
        print "'That's right! Congratulations. Hey, remember that '80s band Pop Will Eat Itself?' asks the eye tooth. I really liked "
        print "'them. Anyway, your second riddle is this: What is the name of the serpent that eats "
        print "its own tail?"
        
        answer = raw_input("> ")
        answer = answer.lower()
        
        if answer.__contains__("uroboros"):
            return "riddle3"
        
        else:
            print "Geez louise. That serpent may have its ass up its head, but you have it the other"
            print "way around. I don't know why I bothered. And with that, the eye closes, and "
            print "your tooth goes back to normal. You decide it was a weird hallucination and "
            print "try to put it all behind you."
            return "brush_teeth"

class RiddleThree(Riddle):
    
    def enter(self):
        print "'You got it! Okay, last one, and then I'll grant you a wish. You're really close!' the eye says,"
        print "'don't screw it up. Here you go: What is the last name of the strange loop who's most popular"
        print "work is often referred to by its acronym, G.E.B.?"
        
        answer = raw_input("> ")
        answer = answer.lower()
        
        if answer.__contains__("hofstadter"):
            return "wishes"
        
        else:
            print "You hear a groan. 'Really?? That's your answer?' The eye tooth closes its eye and "
            print " disappears. You were so close! Or was it just a weird hallucination? You decide to"
            print "try to put it all behind you."
            return "brush_teeth"

class Wishes(object):
    def enter(self):
        print "'Congratulations!' the eye tooth says, beaming with delight. 'You've correctly answered all"
        print " three riddles.' For that, you have your choice of three options, each of them a dream come true."
        print " You can choose to be young again. Or, you can choose to experience true love. Or, you can choose "
        print "to have the ability to fly. What will it be?"

        while True:
                    
            answer = raw_input("> ")
            answer = answer.lower()

            if answer.__contains__("young"):
                    return "school"
            
            elif answer.__contains__("love"):
                return "sex"
        
            elif answer.__contains__("fly"):
                return "fly"
            
            else:
                print "That wasn't one of your choices. Do you want to be young again, to have true love, or to fly?"
                continue

class School(object):

    def enter(self):
        print "This scene is not yet configured."
        exit(1)
        
class Sex(object):

    def enter(self):
        print "This scene is not yet configured."
        exit(1)

class Fly(object):

    def enter(self):
        print "This scene is not yet configured."
        exit(1)
                        
class School(Scene):
    
    def enter(self):
        print "You're suddenly in a large hallway filled with lockers. It looks like a high school. In fact ..."
        print "it's YOUR high school! You look down and realize you're a teenager again ... and that you aren't"
        print "wearing any pants. Or underwear, for that matter. Your heart starts racing. The hallway is empty"
        print "but you look at your watch and realize the bell is going to ring in 2 minutes. Then everyone will"
        print "come pouring out of the classrooms to find you buck naked from the waist down. You suddenly"
        print "when you remember that you have some gym shorts in your locker. You can either make a run for a hiding"
        print "place, or you can run to your locker and get out those shorts. What's it going to be?"

        while True:
        
            answer = raw_input("> ")
            answer = answer.lower()
                    
            if answer.__contains__("run") or answer.__contains__("hide"):
                return "chase"
            
            elif answer.__contains__("locker") or answer.__contains__("shorts"):
                return "locker"
            
            elif answer == "pinch myself":
                return "wake"
            
            else: 
                continue
                
class Locker(Scene):
    
    def enter(self):
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses < 9:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
            
        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
       
            
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."

                        
class Chase(Scene):
    def enter(self):
        print "This scene is not yet configured."
        exit(1)
        
class EscapePod(Scene):
    
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"
        
        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")
        
        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'wake'

        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!"
            
            return "finished"
            
class Wake(Scene):
    
    quips = [
        "Sheesh. Freud would have a field day with that one.\n", 
        "Yikes. That was rough. Maybe you should stay away from dairy before bed.\n",
        "Dang. If that's your dreamworld, I'd hate to see your reality.\n",
        "Ahem. Excuse me, your Freudian slip is showing.\n"
    ]
    
    def enter(self):
        print "You wake up in a cold sweat, your heart racing. Thank god! It was all just a bad dream. Now you can go back to sleep and get some rest..."
        print "    IF YOU DARE!!!!!\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        print Wake.quips[randint(0, len(self.quips)-1)]
        exit(1)
            
class Map(object):
    
    scenes = {
        "bathroom": Bathroom(),
        "brush_teeth": BrushTeeth(),
        "tooth_dialogue": ToothDialogue(),
        "riddle": Riddle(),
        "riddle1": RiddleOne(),
        "riddle2": RiddleTwo(),
        "riddle3": RiddleThree(),
        "wishes": Wishes(),
        "school": School(),
        "chase": Chase(),
        "locker": Locker(),
        "sex": Sex(),
        "fly": Fly(),
        "escape_pod": EscapePod(),
        "wake": Wake()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        # print "start_scene in __init__", self.start_scene
        
    def next_scene(self, scene_name):
        # print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        # print "next_scene returns", val
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
the_map = Map('bathroom')
the_game = Engine(the_map)
the_game.play()