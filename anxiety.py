from sys import exit
from random import randint

        
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
        str1 = "o 0           ~~~ANXIETY~~~        o 0"
        str2 = "^^^                                ^^^"
        str3 = "a game by Wendy Dherin"
        print "\n", str1.center(50, " ")
        print str2.center(50, " "), "\n"
        print str3.center(50, " ")
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
            print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        
class Bathroom(Scene):
    
    def enter(self):
        for i in range(100):
            print ""
        print """\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
        Your alarm goes off, and you wake up feeling so relaxed and well rested.
        You get out of bed, yawn and stretch, look out the window, and smile.
        It's a gorgeous morning, and you have a great sense of optimism.
        You head into the bathroom to brush your teeth.
        Wow! You're looking great this morning!
        One thing catches your eye though. 
        Your right eye tooth. It just ...
        flashed or something.
        You look closer ... and you see it's discolored. 
        Now you feel a slight stirring of uneasiness in the pit of your belly.
        Part of you wants to ignore it.
        But part of you wants to look closer.\n"""
        
        while True:
            
            print "Do you ignore it, or do you look?"
            
            answer = raw_input("> ")
            answer = answer.lower()
            
            if answer.__contains__("ignore"):
                return 'brush_teeth'
        
            elif answer.__contains__("look"):
                return 'tooth_dialogue'
                
            elif answer.__contains__("pinch"):
                return 'wake'
            
            else:
                continue
                
                
class ToothDialogue(Scene):
    
    def enter(self):
        print """What the?!?
        You see that the eye tooth has a brilliant, bright green eye.
        The eye blinks at you innocently,
        and then you hear a thin, whispery voice.
        TOOTH: I am your inner voice. Your true essential self; your deepest wisdom.
        YOU: Shouldn't that be the role of my wisdom teeth?
        TOOTH: You had them extracted, remember?
        We eye teeth are heirs to their throne.
        YOU: So why is it just you? What happened to my other eye tooth?
        TOOTH: Oh, him? He's kind of a deadbeat. I'm all you've got now.
        YOU: So why now? What do you want from me?
        TOOTH: The question is, what do you want from me?
        If you can answer all three of my questions correctly,
        I can make you very happy.
        Are you game?\n"""        
                
        while True:
            
            answer = raw_input("type 'yes' or 'no': ")
            answer = answer.lower()
            
            if answer == "yes":
                return 'riddle1'
        
            elif answer == "no":
                return 'brush_teeth'
            
            elif answer.__contains__("pinch"):
                return 'wake'    
    
            else: 
                continue
   
                    
class BrushTeeth(Scene):
    
    def enter(self):
        print """You start brushing your teeth, pretending nothing weird happened just now.
        But something's off.
        Your eye tooth is wiggling as you brush.
        You stop brushing and gingerly take hold of your eye tooth with your fingers.
        As soon as you touch it, it falls into the palm of your hand!
        You look in the mirror and see a ridiculous gap where your tooth once was.
        You close your eyes in anguish. Why you?!
        All of a sudden, like an avalanche, all of your teeth start falling into your mouth.
        You are horrified, and start screaming.
        What do you scream?"""
        answer = raw_input("> ")
        return "wake"
     
        
class Riddle(Scene):
    
    def enter(self):
        exit(1)
      
        
class RiddleOne(Riddle):
    
    def enter(self):
        print """Your eye tooth clears its throat.
        'The first riddle is the easiest,' it says.
        'What is the name of a surface with only one side
        and only one boundary component?'"""
        
        answer = raw_input("> ")
        answer = answer.lower()
        
        if answer.__contains__("mobius") or answer.__contains__("moebius"):
            return "riddle2"
        
        elif answer.__contains__("pinch"):
            return 'wake'
                
        else:
            for i in range(100):
                print ""
            print """'Wow. I don't think you even tried,' says the eye tooth.
            'I don't know why I even waste my time.' And with that, the eye closes, and
            your tooth goes back to normal.
            You decide the whole thing must have been a hallucination.
            (Hit 'Enter' to continue)"""
            answer = raw_input()
            return "brush_teeth"


class RiddleTwo(Riddle):
    
    def enter(self):
        print """'That's right!' the tooth says.
        'Hey, remember that '80s band Pop Will Eat Itself?' asks the tooth.
        'They were cool. Anyway, your second riddle is this:'
        What is the name of the serpent that eats its own tail?"""
        
        answer = raw_input("> ")
        answer = answer.lower()
        
        if answer.__contains__("uroboros"):  
            return "riddle3"
        elif answer.__contains__("pinch"):
            return 'wake'
        
        else:
            for i in range(100):
                print ""
            print """'Geez louise,' says the eye tooth.
            'That serpent may have its ass up its head,
            but you have it the other way around.'
            And with that, the eye closes, and your tooth goes back to normal.
            (Hit 'Enter' to continue)"""
            answer = raw_input()
            return "brush_teeth"


class RiddleThree(Riddle):
    
    def enter(self):
        print """'You got it!' says the tooth.
        'Okay, last one, and then I'll grant you a wish.'
        'You're really close!' the eye says, 'Don't screw it up:'
        What is the last name of the strange loop whose most popular work
        is often referred to by its acronym, G.E.B.?\n"""
        
        answer = raw_input("> ")
        answer = answer.lower()
        
        if answer.__contains__("hofstadter"):
            return "wishes"
        elif answer.__contains__("pinch"):
            return 'wake'
        
        else:
            for i in range(100):
                print ""
            print """You hear a groan.
           'Really?!? That's your answer?!?'
           The eye tooth closes its eye and disappears.\n
           (Hit 'Enter' to continue)"""
            answer = raw_input()            
            return "brush_teeth"


class Wishes(object):
    def enter(self):
        print """'Congratulations!' the eye tooth says, beaming with delight.
        'You've correctly answered all three riddles!!!'\n
        For that, you have your choice of three options, each of them a dream come true:
        1. You can choose to be young again.
        2. You can choose to experience true love.
        3. You can choose to have the ability to fly.\n
        What will it be?"""

        while True:
                    
            answer = raw_input("> ")
            answer = answer.lower()

            if answer.__contains__("young") or answer.__contains__("1"):
                    return "school"
            
            elif answer.__contains__("love") or answer.__contains__("2"): 
                return "sex"
        
            elif answer.__contains__("fly") or answer.__contains__("3"):
                return "fly"
            elif answer.__contains__("pinch"):
                return 'wake'
            
            else:
                print """\nThat wasn't one of your choices.
                Do you want:
                1. to be young again
                2. to have true love
                3. the ability to fly?\n"""
                continue


class School(object):

    def enter(self):
        print "This scene is not yet configured."
        exit(1)
        
        
class Sex(object):

    def enter(self):
        print """
        You hear someone calling your name.
        It's a familiar voice, a voice that pulls at your heart ....
        and at your loins.

        And then you remember: it's the love of your life.
        
        You hear your love calling your name again, seductively.

        You forget about your tooth and all that weirdness and return to the bedroom.

        You crawl under the sheets and embrace your love.

        It's the most comforting and exicting feeling, to be this close 
        to someone you adore so much.

        Soon, the cuddles turn into kisses, first sweet, and then more and more 
        passionate.

        Before you know it, you're having sex, again, and even though it's always been amazing
        this time, you think you might die and go to heaven.

        Your lover's hand touch your face ... but it's not a caress. It's a wet thumb,
        wiping schmutz off your face.

        "Honey, you've got toothpaste on your face."

        It takes you out of the moment, and you look up in confusion.

        And you see your mother.

        "You're doing very well," she assures you. "Don't give up! Keep going!"

        You open your mouth to scream.

        What do you scream?"""
        answer = raw_input("> ")
        return "wake"
        exit(1)


class Fly(object):

    def enter(self):
        print "This scene is not yet configured."
        exit(1)
         
                        
class School(Scene):
    
    def enter(self):
        print """You're suddenly in a large hallway filled with lockers.
        It looks like a high school. In fact ...
        it's YOUR high school!
        You look down and realize you're a teenager again ... \n
        and that you aren't wearing any pants.
        Or underwear, for that matter.
        Your heart starts racing.
        The hallway is empty but you look at your watch and realize
        that the bell is going to ring in 2 minutes.
        Then everyone will come pouring out of the classrooms
        to find you buck naked from the waist down.
        You suddenly remember that you have some gym shorts in your locker.
        You can either make a run for a hiding place,
        or you can run to your locker and get out those shorts.\n
        What's it going to be?"""

        while True:
        
            answer = raw_input("> ")
            answer = answer.lower()
                    
            if answer.__contains__("run") or answer.__contains__("hide"):
                return "chase"
            
            elif answer.__contains__("locker") or answer.__contains__("shorts"):
                return "locker"
            
            elif answer.__contains__("pinch"):
                return "wake"
            
            else: 
                continue
                
                
class Locker(Scene):
    
    def enter(self):
        print "You run to your locker ...\n"
        print "... and immediately draw a blank."
        print "For the life of you, you can't remember your combination."
        print "All you remember is that the first number is in the 30s,"
        print "the second number is in the 20s, and the third number is in the 40s."
        print "You can squeeze in 10 tries before the bell rings."
        print "Hurry!"
        combo1, combo2, combo3 = randint(30,39), randint(20,29), randint(40,49)
        print combo1, combo2, combo3
        guesses = 0
        
        while guesses < 11:
            
            guess1 = int(raw_input("First number, in the 30s: "))
            guess2 = int(raw_input("Second number, in the 20s: "))
            guess3 = int(raw_input("Third number, in the 40s: "))
            guesses += 1              
            
            if (guess1, guess2, guess3) == (combo1, combo2, combo3):
                return "wake"
            
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
        "(Sheesh. Freud would have a field day with that one.)\n", 
        "(Yikes. That was rough. Maybe you should stay away from dairy before bed.)\n",
        "(Dang. If that's your dreamworld, I'd hate to see your reality.)\n",
        "(Ahem. Excuse me, your Freudian slip is showing.)\n"
    ]
    
    def enter(self):
        print "You wake up screaming." 
        print "Your heart is racing.\n"
        print "Thank god! It was all just a bad dream.\n"
        print "Now you can go back to sleep and get some rest...\n"
        print "... if you DARE!!!!!\n\n\n".center(50, " ")
        print "~~GAME OVER~~~\n".center(50, " ")
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

if __name__ == "__main__":    
    the_map = Map('bathroom')
    the_game = Engine(the_map)
    the_game.play()