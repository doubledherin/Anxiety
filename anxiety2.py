from sys import exit
from random import randint
from text_strings import *

scream = ""
    
class Scene(object):
    
    pass
        
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
 
    def play(self):
        
        # initial clearing of screen for game start
        for i in range(100):
            print ""
        
        # game header
        print game_header.center(50, " ")
        for i in range(12):
            print ""
        print "(Hit 'Enter' to begin)".center(50, " ")
        answer = raw_input()
        
        current_scene = self.scene_map.opening_scene()                                                              
        
        while True:     
            next_scene_name = current_scene.enter()
            
            # clear screen for next scene
            for i in range(100):
                print ""
        
            current_scene = self.scene_map.next_scene(next_scene_name)        
            print wavy_line
    
class Bathroom(Scene):
    
    def enter(self):
        for i in range(100):
            print ""
        print wavy_line
        print bathroom_opener
        
        while True:
            
            print "Do you ignore it, or do you look?"
            
            answer = raw_input("> ")
            answer = answer.lower()
            
            if answer.__contains__("ignore"):
                return 'brush_teeth'
        
            elif answer.__contains__("look"):
                return 'tooth_dialogue'
                
            elif answer == "pinch myself":
                return 'wake'
            
            else:
                continue     
                
class ToothDialogue(Scene):
    
    def enter(self):
        print tooth_dialogue       
                
        while True:
            
            answer = raw_input("Type 'yes' or 'no': ")
            answer = answer.lower()
            
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
        print tooth_brushing
        global scream
        scream = raw_input("> ")
        return "wake"
     
        
class Riddle(Scene):
    
    def enter(self):
        exit(1)
      
        
class RiddleOne(Riddle):
    
    def enter(self):
        
        print riddle1
        
        answer = raw_input("> ")
        answer = answer.lower()
        
        if answer.__contains__("mobius") or answer.__contains__("moebius"):
            return "riddle2"
        
        elif answer == "pinch myself":
            return 'wake'
                
        else:
            for i in range(100):
                print ""
            print riddle1_fail
            print "(Hit 'Enter' to continue)"
            answer = raw_input()
            return "brush_teeth"


class RiddleTwo(Riddle):
    
    def enter(self):
        
        print riddle2
        
        answer = raw_input("> ")
        answer = answer.lower()
        
        if answer.__contains__("uroboros"):  
            return "riddle3"
        
        else:
            for i in range(100):
                print ""
            print riddle2_fail
            print "(Hit 'Enter' to continue)"
            answer = raw_input()
            return "brush_teeth"


class RiddleThree(Riddle):
    
    def enter(self):
        
        print riddle3
        
        answer = raw_input("> ")
        answer = answer.lower()
        
        if answer.__contains__("hofstadter"):
            return "wishes"
        
        else:
            for i in range(100):
                print ""
            print riddle3_fail
            print "(Hit 'Enter' to continue)"
            answer = raw_input()            
            return "brush_teeth"

class Wishes(object):
    def enter(self):
        print wishes_opener

        while True:
                    
            answer = raw_input("> ")
            answer = answer.lower()

            if answer.__contains__("young") or answer.__contains__("1"):
                    return "school"
            
            elif answer.__contains__("love") or answer.__contains__("2"): 
                return "sex"
        
            elif answer.__contains__("fly") or answer.__contains__("3"):
                return "fly"
            
            else:
                print wishes_corrector
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
        
        print school_opener

        while True:
        
            answer = raw_input("> ")
            answer = answer.lower()
                    
            if answer.__contains__("run") or answer.__contains__("hide") or answer == "1":
                return "chase"
            
            elif answer.__contains__("locker") or answer.__contains__("shorts") or answer.__contains__("open") or answer == "2":
                return "locker"
            
            elif answer == "pinch myself":
                return "wake"
            
            else: 
                continue
                
                
class Locker(Scene):
    
    def enter(self):
        
        print locker_opener
        
        combo1, combo2, combo3 = randint(30,39), randint(20,29), randint(40,49)
        print combo1, combo2, combo3
        guesses = 0
        
        while guesses < 11:
            
            guess1 = int(raw_input("First number, in the 30s: "))
            guess2 = int(raw_input("Second number, in the 20s: "))
            guess3 = int(raw_input("Third number, in the 40s: "))
            guesses += 1              
            
            if (guess1, guess2, guess3) == (combo1, combo2, combo3):
                return "bomb"
            
            elif guess1 == combo1 and guess2 != combo2 and guess3 != combo3:
                print "You got the first number right! Try again! Hurry!"
                continue
            
            elif guess2 == combo2 and guess1 != combo1 and guess3 != combo3:
                print "You got the second number right! Try again! Hurry!"
                continue
                
            elif guess3 == combo3 and guess1 != combo1 and guess2 != combo2:
                print "You got the third number right! Try again! Hurry!"
                continue
                
            elif guess1 == combo1 and guess2 == combo2:
                print "You got the first and second number right! Try again! Hurry!"
                continue
            
            elif guess1 == combo1 and guess3 == combo3:
                print "You got the first and third number right! Try again! Hurry!"
                continue
                
            elif guess2 == combo2 and guess3 == combo3:
                print "You got the second and third number right! Try again! Hurry!"
                continue
            
            else:
                print "Wrong code! Try again! Hurry!"
                continue
            
class Bomb(Scene):
    
    def enter(self):
        
        print bomb_opener
        
        while True:
            
            answer = raw_input("> ")
            answer = answer.lower()
            
            if answer.__contains__("defuse") or answer.__contains__("hero") or answer.__contains__("school") or answer == "1":
                return "defuse"
            
            elif answer.__contains__("run") or answer.__contains__("leave") or answer.__contains__("out of") or answer.__contains__("gtfo") or answer.__contains__("save myself") or answer == "2":
                print "also not yet configured."
                break
                
            else:
                continue
                
class Defuse(Scene):
    
    def enter(self):
        
        print defuse_opener
        
        while True:
            
            print "Which will you pull, the pink or the blue? Hurry!!!\n"
        
            answer = raw_input("> ")
        
            if answer.__contains__("pink"):
                for i in range(25):
                    print ""
                print wavy_line
                print defuse_success
                return "wake"

            if answer.__contains__("blue"):
                for i in range(25):
                    print ""
                print wavy_line
                print defuse_fail
                
                global scream
                scream = raw_input("> ")
                return "wake"

            else:
                 continue
                 
class Chase(Scene):
    
    def enter(self):
        print "This scene is not yet configured."
        exit(1)       
            
class Wake(Scene):
    
    quips = [
        "(Sheesh. Freud would have a field day with that one.)\n", 
        "(Yikes. That was rough. Maybe you should stay away from dairy before bed.)\n",
        "(Dang. If that's your dreamworld, I'd hate to see your reality.)\n",
        "(Ahem. Excuse me, your Freudian slip is showing.)\n"
    ]
    
    def enter(self):
        print "You wake up screaming '" + scream.upper() +"!!!'"
        print outro.center(50, " ")
        print Wake.quips[randint(0, len(self.quips)-1)].center(50, " ")
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
        "bomb": Bomb(),
        "defuse": Defuse(),
        "locker": Locker(),
        "sex": Sex(),
        "fly": Fly(),
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