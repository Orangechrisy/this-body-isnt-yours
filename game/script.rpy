# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    style.hyperlink_text = Style(style.say_dialogue)
    style.hyperlink_text.idle_color = "#725894"
    style.hyperlink_text.hover_color = "#a580d4"

    renpy.music.register_channel("extra_sound", loop=False)

define config.default_textshader = "typewriter"
define fadehold = Fade(0.5, 1.5, 1.0)
define fadered = Fade(0.1, 0.0, 0.5, color="#c70000")

default week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
default wi = 0
default time = "10:00 AM"
define t = Character("[week[wi]] - [time]", who_color="#e27a19")
define hm_color = "#a200ff70"
# todo make ^ this variable in opacity if talked with them enough?
define mc_color = "#208fda"
define name = "{shader=jitter:u__jitter=(1.0, 1.0)}{s}[[Wrong]{/s}{/shader}"
default cycles = 0
default talks_with_hm = 0
default gone_outside = 0
default takeout = ["Chinese", "Chinese", "Italian", "Mexican", "Indian", "Vietnamese"]
default game = ["Run 'n Gun 3: Maximum Pain", "Stowaway Sim", "Garden's Delight", "Prism", "Sweet Spells", "The Haunting of Igonia 2", "Untitled Bee Game"]
default book = ["The Withering Rose", "The Book of Time", "Infin8", "An Enticing Show (Volume 1)", "Hellspawn (Volume 3)", "Can A Deadbeat Father Who Lost His Family's Fortune Because Of Horse Race Betting Really Become The Greatest Swordsman After Being Brought To A New World While Building A Harem Of Beautiful Girls? Well I'm Going To Find Out! (Volume 34)"]
default opt = False

default woke_once = False
default woke_today = False
default ran_away = False
default ate_once = False
default found_phone = False
default named_once = False
default cried_over_food_today = False
default offer_to_go_out = False
default not_alone = False


# The game starts here.

label start:

    play sound birds volume 0.05 fadein 2.0

    scene bedroom
    with fadehold

    show frame onlayer frameOverlay

    $ renpy.pause(delay=2.0, hard=True)

    jump l10am

label restart_day:

    $ wi = (wi + 1) % 7
    $ cycles += 1
    $ woke_today = False
    $ cried_over_food_today = False
    $ offer_to_go_out = False

    stop music fadeout 2.0
    stop sound fadeout 2.0
    queue sound birds volume 0.05 fadein 3.0
    
    scene bedroom
    with fadehold

    jump l10am

# the normal start
label l10am:

    play music inside loop

    $ time = "10:00 AM"

    t "You wake up in a body that isn't yours."

    stop sound fadeout 2.0

# todo go over how this functions thank
    if cycles > 5:
        if woke_once:
            if ((not ran_away) and (renpy.random.randint(1, 100) <= 10 + cycles)) or (renpy.random.randint(1, 100) <= 5):
                t "You want to escape."
                
                t "{a=l1002am}You {b}need{/b} to escape.{/a}" (advance=False)
            elif renpy.random.randint(1, 100) <= min(75, 25 + cycles):
                t "{a=l1030am}You want to get out of bed.{/a}" (advance=False)
        else:
            t "{a=l1030am}You want to get out of bed.{/a}" (advance=False)

    t "{a=l1pm}You want to get out of bed.{/a}" (advance=False)

# when you escape
label l1002am:

    stop music

    scene alley
    with fade

    play music alleyway loop volume 0.2

    $ time = "10:02 AM"

    t "The concrete walls of the alley next to your apartment cool you, but the thumping of your lungs doesn't quiet down." 
    
    t "{a=l1010am}You can't run forever.{/a}" (advance=False)

# escape 2
label l1010am:

    $ time = "10:10 AM"

    play sound headache loop volume 0.3 fadein 1.5

    t "The pounding in your ears just keeps getting louder, you {b}need{/b} to escape.\n\n{a=l1015am}Anywhere but here.{/a}" (advance=False)

# escape 3
label l1015am:

    $ time = "10:15 AM"

    play extra_sound breathing volume 0.5 fadein 1.0 fadeout 1.0

    t "You run until your legs crumple beneath you. How long has it been since you were so far from your room?"

    t "A week? A month? Maybe even a year? Everything has become {alpha=-0.4}{shader=jitter:u__jitter=(2.0, 2.0)}hazy{/shader}{/alpha}."

    t "You grab your head in an effort to stop the noise."

    $ time = "10:16 AM"

    t "Everything feels like it's going to burst."

    $ renpy.music.set_volume(0.3, 0.0)

    stop sound fadeout 3.0

    scene black 
    with fade

    "...{w=2.5}"

    scene alley
    with fade

    $ renpy.music.set_volume(1.0, 0.0)

    $ ran_away = True

    jump l918pm

# actually get out of bed
label l1030am:

    scene bathroom
    with fade

    $ time = "10:30 AM"

    if not ran_away:
        $ woke_once = True
        t "The mirror shows what feels like a decrepit animal. Maybe to others you look okay, but this isn't you." 
        
        t "{a=l11am}Why can't it be you?{/a}" (advance=False)
    else:
        t "The mirror shows what feels like a decrepit animal. Everything fits wrong."

        t "You wish you could rip it all off. Expose the muscles and sinew that's surely rotting underneath. Maybe then you'd only look half as deformed as you do right now."

        play sound headache loop volume 0.3 fadein 1.5

        t "Or maybe you'd look even worse. Maybe the core is what's wrong. The flesh and bone."

        $ time = "10:31 AM"

        t "{a=l1048am}Does this headache ever go away?{/a}" (advance=False)

# get out of bed 2
label l1048am:
    
    $ time = "10:48 AM"

    t "No, no it doesn't.\n\n{a=l11am}Maybe that was too much to ask.{/a}\n{a=l1050am}Maybe food would help?{/a}" (advance=False)

# leave room for food
label l1050am:

    stop sound fadeout 3.0

    scene kitchen
    with fade

    $ time = "10:50 AM"

    if week[wi] != "Saturday" and week[wi] != "Sunday":
        t "Luckily your housemate is out. Probably at their job."

        t "You don't know if they have a job. They probably do, it's not like you've been capable of paying rent for a long time."

        t "Worthless."

        t "You eat a small bit.\n\n{a=l1130am}Your desire to eat left long ago.{/a}" (advance=False)
    else:
        t "You peak out of your room and see your housemate standing in the kitchen area. They give you a smile and a small wave."

        t "{a=l11am}You can't handle this right now.{/a}\n\n{a=l1051am}Wave back.{/a}" (advance=False)

# greeting housemate
label l1051am:

    $ time = "10:51 AM"

    t "You timidly wave back and try to match their smile.\n\nIt's more of a grimace."

    t "{color=[hm_color]}\"Hey [name], it's good to see you.\"{/color}"

    if not named_once:
        t "They don't know they don't know they don't know they don't know why would they know they had no way of knowing but it hurts all the same."

        $ named_once = True

        t "Nothing feels real.\n\n{a=l1pm}Maybe lying down will stop the pain.{/a}" (advance=False)

    t "\"It's not their fault\" you have to remind yourself."

    t "{color=[mc_color]}\"You too.\"{/color}"

    t "You croak it out. Why does your voice have to sound like that?"

    t "{color=[hm_color]}\"Would you like something to eat? There's leftovers.\"{/color}"

    play sound growl volume 0.3

    t "You hear your stomach growl and look down. It was a mistake to look down."

    t "{a=l1107am}You can't handle any more of this.{/a}\n\n{a=l1052am}Just take one step.{/a}" (advance=False)

# eat with housemate
label l1052am:
    
    $ time = "10:52 AM"

    if talks_with_hm >= 5:
        t "You move to the table, it's a small thing, you doubt it gets used any more than the countertop."

        t "{color=[hm_color]}\"Did you sleep well?\"{/color}"

        t "You open your mouth to respond, but close it when you realize you don't know the answer."

        t "You spend so much time sleeping it becomes a blur. Nightmares that you don't remember. Dreams that you wish to forget."

        $ time = "10:53 AM"

        t "{color=[hm_color]}\"Yeah... It's like that sometimes.\"{/color}"

        t "You don't think they feel what you feel."

        t "{color=[hm_color]}\"Here, what would you like to eat?\"{/color}"

        $ rng = renpy.random.randint(1, len(takeout) - 2)

        t "{color=[hm_color]}\"There's {a=l1052food}[takeout[rng]]{/a} or {a=l1052food2}[takeout[rng+1]]{/a}, take your pick.\"{/color}"

        $ opt = False

        label l1052food:
            $ opt = True
        
        label l1052food2:
            if opt:
                t "You grab the [takeout[rng]] container and start to take a few hesitent nibbles."
            else:
                t "You grab the [takeout[rng+1]] container and start to take a few hesitent nibbles."
        
        jump l1057am  

    else:
        t "You cautiously step forward. It's not often you come out here. Not to talk, not to eat, not for anything."

        t "Your room is the only safe place."

        t "..."

        t "Well, most of the time."

        t "There are times when even it doesn't feel like a place you can be safe in."

        $ time = "10:53 AM"

        t "You grab a small amount of food. You can't handle eating too much."

        t "{i}Any amount is too much.{/i}"

        $ time = "10:56 AM"

        t "Your housemate starts to talk, sometimes asking you things which only get grunts and grumbles as answers."

        t "It's not like what you say means anything."

        $ talks_with_hm += 1

        t "{a=l1230pm}When did existing become so difficult?{/a}" (advance=False)

# eating with housemate
label l1057am:

    $ time = "10:57 AM"

    t "The food doesn't taste good. You're not really sure if that's because it's leftovers or just you. Your housemate seems to like it well enough."
    
    t "{color=[hm_color]}\"So I wanted to ask you something, and you can say no.\"{/color}" 
    
    t "You already know that will be the response anyways.\n\nYou nod along anyways."
    
    play sound headache loop volume 0.3 fadein 1.5

    t "{color=[hm_color]}\"Would you be up for going out with me later? Not like, anywhere specific, just a walk outside for a bit.\"{/color}"
    
    t "The prospect fills you with dread."
    
    t "The pounding in your ears feels like it engulfs your mind."
    
    t "You grab your head in an attempt to quiet it but it's to little avail."
    
    t "{color=[hm_color]}\"How about I ask again a bit later?\"{/color}"

    $ offer_to_go_out = True
    
    t "You barely hear what they say but you nod along anyways.\n\n{a=l1115am}Run back to your room before it's too late.{/a}" (advance=False)

# go back to bed in the morning
label l11am:

    stop sound fadeout 2.0

    $ s_list = renpy.get_showing_tags(layer='master')
    if "bedroom" not in s_list:
        scene bedroom
        with fade

    $ time = "11:00 AM"

    t "Well, you did get out of bed, at least for a bit.\n\n{a=l1pm}Once in a while feels like too much to ask.{/a}" (advance=False)

# cant eat to housemate
label l1107am:

    scene bedroom
    with fade

    t "You turn back into your room with tears starting to appear in your eyes and close the door, perhaps a bit forcefully."

    $ time = "11:07 AM"

    $ cried_over_food_today = True

    t "By the time you stop crying, your face is all red and puffy and even worse than before."

    t "You wish you were better.\n\n{a=l1pm}We wish for a lot of things that can't come true.{/a}" (advance=False)

# post lunch escape
label l1115am:

    scene bedroom
    with fade

    stop sound fadeout 3.0

    $ time = "11:15 AM"

    t "You hate how pathetic you are. Struggling to hold a conversation and fleeing at the first sign of danger."

    t "What even was the danger? An offer? Who knows. Why's your housemate even asking for something as hard as \"going out\"?"

    t "You feel gross even just thinking about it."

    t "You {i}are{/i} gross."

    t "Why are they trying to go outside with such a detestable being?"

    t "The thoughts keep growing until you feel the need to force yourself into the {a=l1210pm}shower.{/a}" (advance=False)

# ate a morning meal
label l1130am:

    $ time = "11:30 AM"

    if not ate_once:
        t "When was the last time you ate an actual meal?"

        $ ate_once = True
    
    t "Sometime years ago it just stopped feeling good to eat. Every bite felt like a stab in the brain."

    t "{a=l12pm}It's hard not to dwell.{/a}" (advance=False)

# noontime dwelling
label l12pm:

    $ time = "12:00 PM"

    t "You don't really know what to do now. It's like the piece of you that functions is missing."

    t "Whatever you used to do in your freetime is far gone."

    t "An emotionless husk."

    t "A walking corpse."

    t "Why are you alive?"

    t "..."

    $ time = "12:01 PM"

    t "{a=l1pm}Maybe you should go lay down.{/a}\n{a=l1215pm}You have a phone, don't you?{/a}" (advance=False)

# showering
label l1210pm:

    stop music

    scene shower
    with fade

    play music showering loop volume 0.1

    $ time = "12:10 PM"

    t "The thoughts tormenting your mind eventually win out against the disgust you have."

    t "Showers are awful, same with all forms of cleaning, they force you to be acutely aware of your physical form."

    t "When the water starts to pelt your body you can feel every bump, every curve, and how {shader=jitter:u__jitter=(3.0, 3.0)}wrong{/shader} they are."

    t "You didn't ask to be built this way, and yet you're the one trapped in it, unable to escape."

    $ time = "12:15 PM"

    t "You want to scream."

    t "You don't.\n\n{a=l1245pm}But you really want to.{/a}" (advance=False)

# check out phone
label l1215pm:

    scene apartment
    with fade

    $ time = "12:15 PM"

    if found_phone:
        t "You spend 15 minutes finding your phone from wherever you placed it."

        t "There's really not that much to do on a phone. Why did you even get it?" 

        t "{a=l1220pm}Anything else would be better.{/a}\n\n{a=l230pm}And yet what else is there to do?{/a}" (advance=False)
    else:
        t "It's in the apartment somewhere..."

        $ time = "1:07 PM"

        t "Like, it's gotta be here, it's not like you've left the house much recently."

        $ time = "3:23pm"

        t "The apartment is starting to look ransacked."

        $ time = "5:11pm"

        t "Well, you found it, wedged in the back of your dresser behind some junk and clothes you haven't worn in ages."

        t "You haven't even changed clothes in a long while. You probably should."

        t "Tomorrow.\n\nMaybe."

        play sound headache loop volume 0.3 fadein 1.5

        t "The pounding in your head grows."

        t "You hope your housemate won't hate you for the mess."

        t "They probably already hate you for everything else."

        stop sound fadeout 3.0

        $ found_phone = True

        jump l9pm

# dont go on phone
label l1220pm:
    
    $ time = "12:20 PM"

    t "There really isn't that much to do. At some point you just forgot how to live."

    t "Your housemate has some video games, but they hardly seem appealing to you right now. Your mind is in too much of a haze to be able to understand anything anyways."

    t "But you don't really want to hide in your blankets again just yet."

    t "{a=l630pm}Just try a game for now.{/a}\n\n{a=l130pm}It's okay to be a bit listless.{/a}" (advance=False)

# ate lunch with hm but havent talked enough
label l1230pm:

    scene bedroom
    with fade

    $ time = "12:30 PM" 

    t "You left the kitchenette a while ago, but your mind still feels like its swirling and thundering."

    t "You think there used to be a time when it wasn't this bad. When it wasn't this hard to just talk to someone."

    t "But that's the past, and the present is flashing by like a kaleidoscope. A bright yet blurry mess of colors that assault your eyes until they bleed."

    t "And yet the present affects the past and it affects the future and it obscures what was and what will be."

    t "When the present hurts it makes everything hurt. And it feels like the present has been hurting you for a while."

    t "{a=l4pm}You could use a break.{/a}" (advance=False)

# shower 2
label l1245pm:

    $ time = "12:45 PM"

    t "The heat of the water makes you feel numb."

    t "Maybe that's the advantage of showers. You get hit and hit and hit until you can't feel anything anymore."

    t "{a=l210pm}Let the pain wash away.{/a}\n\n{a=l1250pm}You really can't stand your body being here longer.{/a}" (advance=False)

# get out of shower
label l1250pm:
    
    stop music fadeout 4.0

    $ time = "12:50 PM"

    t "You dry off as fast as possible so you can return to wearing your baggy oversized clothes."

    t "You feel terrible, you still feel just as disgusting as before. Why did you even do this?"

    t "The only thing you think you can manage is to rot for a while."

    t "{a=l4pm}The world can't see you under the blankets.{/a}" (advance=False)

# still in bed 
label l1pm:

    $ s_list = renpy.get_showing_tags(layer='master')
    if "bedroom" not in s_list:
        scene bedroom
        with fade

    $ time = "1:00 PM"
  
    t "You're still in bed. Some days, most days, you just can't help yourself."

    t "When only one place is safe, and only one place doesn't hate you, where else are you supposed to go?"

    t "The only thing that can hurt you here is your own thoughts."
    
    t "It's just gonna be one of those days.\n\n{a=l4pm}Isn't it always \"one of those days\"?{/a}" (advance=False)

# listless
label l130pm:
    
    $ time = "1:30 PM"

    t "You stumble around for an hour, not really sure of what to do. Lying on the couch, letting your head rest against the dining table. It's all the same really."

    $ time = "1:35 PM"
    
    t "You lost the ability to have fun at some point as well. Now you just sway in the wind. Hoping the next light breeze doesn't knock you over."

    t "{a=l2pm}Crying to yourself when it always does.{/a}" (advance=False)

# prepare to go outside
label l2pm:

    $ time = "2:00 PM"

    t "You feel like you've explored the entirety of the apartment three times already."

    t "You've seen all the dust and lint. All nooks and crannies. All the books and magazines your housemate owns. Nothing of interest."

    t "Right now, you're just wobbling around, hoping the days goes by soon enough."

    t "{a=l230pm}Is the phone really the only option at this point?{/a}\n\n{a=l205pm}Desperate times call for desperate measures.{/a}" (advance=False)

# desperate measures
label l205pm:

    $ time = "2:05 PM"

    t "{a=l215pm}You could curl up in the alleyway again.{/a}\n\n{a=l530pm}Maybe those reading materials can catch your fancy.{/a}" (advance=False)

# passed out in shower
label l210pm:

    # fade to black and back

    stop music fadeout 2.0

    scene black
    with fadehold

    "...{w=2.5}"

    scene bedroom
    with fadehold

    play music inside loop

    $ time = "2:10 PM"

    t "You awake to find yourself covered in a blanket in bed, your housemate is nearby with a concerned look on their face."

    t "Only one thought goes through your mind."

    t "{shader=jitter:u__jitter=(4.0, 2.0)}{b}{i}{size=+10}THEY SAW{/size}{/i}{/b}{/shader}"

    t "{shader=jitter:u__jitter=(4.0, 2.0)}{b}{i}{size=+10}THEY SAW THEY\n\ \ \ \ \ \ \ SAWTHEY SAW THEY SAW \ \ \ \ THEYSAW{/size}{/i}{/b}{/shader}"

    t "{a=l3pm}You need to escape.{/a}" (advance=False)

# alley by choice
label l215pm:

    stop music

    scene alley
    with fade

    play music alleyway loop volume 0.2

    $ time = "2:15 PM"

    t "You don't know why you've done it. But you managed to step outside. Out the door, down the stairwell, around the corner, and into the alley that sits a few floors below your window."

    t "It's dark.{w=0.5}\nAnd a little bit damp.{w=0.5}\nAnd altogether a fair bit gross."

    t "But that's just like you. Together you can be two gross never changing beings."

    t "One of flesh, one of concrete.\nOne of pain and one of indifference."

    $ time = "2:35 PM"

    t "Maybe you came out here because you deserve to be here."

    t "To curl up on the hard stone rather than your soft bed."

    t "Alone in the streets rather than in a home."

    t "Can you even call it a home when you don't contribute towards keeping it?"

    $ time = "3:31 PM"

    t "You don't even know why your housemate bothers. How did this agreement even come to be? Did they ask to be given a large burden for no discernable reason?"

    t "Or maybe they did something wrong in a past life and this is their punishment."

    $ time = "6:15 PM"

    t "You should probably go back inside so your housemate doesn't find you lifeless out here."

    $ gone_outside += 1

    t "{a=l620pm}Just to ease the burden a little. It's the most you can do.{/a}" (advance=False)

# doomscrolling
label l230pm:

    $ time = "2:30 PM"

    t "It's maddening, it's repulsive, and it's hard to stop."

    t "But you really are finding it hard to keep scrolling. Social media is evidently a plague."

    t "You don't find any joy in it, and it's no better than your normal day to day haze."

    play sound ["<silence 0.5", "thump.mp3"] volume 0.15

    t "You throw the phone just to get it out of your hands. Good thing it has a strong case. Or maybe that's a bad thing."

    t "{a=l4pm}You should go lie down, your thoughts are at least your own that way.{/a}" (advance=False)

# ran after shower
label l3pm:

    stop music

    scene alley
    with fadehold

    play music alleyway loop volume 0.2

    play sound breathing volume 0.5 fadein 1.0 fadeout 1.0

    $ time = "3:00 PM"

    t "You ran until your legs gave out and you curled up in an alley."

    t "Tears stain your cheeks, everything hurts."

    t "You don't want to go home."

    t "How could you, knowing your housemate saw that wretched form?"

    t "It makes you sick just thinking about it."

    t "You want to rip apart this body."

    t "{a=l840pm}You want to bleed.{/a}" (advance=False)

# still in bed 2
label l4pm:

    $ s_list = renpy.get_showing_tags(layer='master')
    if "bedroom" not in s_list:
        scene bedroom
        with fade

    $ time = "4:00 PM"

    if offer_to_go_out:
        play sound knocking volume 0.5

        t "You hear a knock at the door."

        t "The time passed by so fast. How can you be ready? How can you ever be ready?"

        t "{color=[mc_color]}\"Come in\"{/color} you meekly mumble out."

        t "Your housemate opens the door and steps in to ask the fated question."

        t "{color=[hm_color]}\"Would you like to go out on a walk with me?\"{/color}"

        t "They're looking at you with what could be kindness but could also just be contempt. How are you supposed to know? Why would they want to walk with you?"

        t "Why?"

        t "Haven't you done enough?"

        t "Aren't they doing too much?"
        
        if not_alone and (gone_outside > 5):
            t "{a=l401pm}It's all just too much for you.{/a}\n\n{a=l402pm}But maybe it will be okay.{/a}" (advance=False)
        else:
            t "{a=l401pm}It's all just too much for you.{/a}" (advance=False)
    else:
        t "You are in your manmade nest."

        t "You could leave, but that would mean facing a world not built for you."

        t "So you don't. You stay in bed."

        t "The covers remain heavy on top of you. Their weight is a comfort and a curse.\n\n{a=l9pm}Nothing feels real.{/a}" (advance=False)

# dont go out
label l401pm:
    
    $ time = "4:01 PM"

    t "You just can't right now."

    t "How could you when the world is so heavy and nothing feels real?"

    t "Braving the dreary alley is hard enough, much less the full force of the outside."

    t "You shake your head and return to hiding in your soft cocoon. The world doesn't have to be faced right now."

    jump l9pm

# go out
label l402pm:
    
    t "You give a nod and your housemate smiles in return."

    t "{color=[hm_color]}\"Here let me get your shoes.\"{/color}"

    $ time = "4:02 PM"

    t "You get your shoes on and they offer their hand."

    t "{color=[hm_color]}\"It's gonna be alright\"{/color} they soothingly say.\n\nYou don't know if it helps or makes you more scared of what's to come."

    t "..."

    t "{a=lend}Take their hand.{/a}" (advance=False)

# reading materials
label l530pm:

    t "You scrounge around your housemate's room for a bit, taking a look at some of the books and magazines."

    $ rng = renpy.random.randint(0, len(book) - 1)

    t "You end up grabbing \"[book[rng]]\"."

    $ time = "5:30 PM"

    play sound headache loop volume 0.3 fadein 1.5

    t "Well, reading gave you a headache so you didn't really understand any of it. Or maybe your housemate just has a bad taste in literature."

    t "It did provide you with a few hours of distraction though. But you're not sure if it was worth it."

    t "Your head hurting just makes you want to go hide in bed for the rest of the day."

    jump l9pm

# go inside
label l620pm:

    stop music

    scene bedroom
    with fade

    play music inside loop

    $ time = "6:20 PM"

    t "You manage to get back inside and into your room before your housemate returns from work."

    t "{a=l9pm}You're safe for now.{/a}" (advance=False)

# video games
label l630pm:

    $ rng = renpy.random.randint(0, len(game) - 1)

    t "You grab [game[rng]] and put it in the console. You know you used to play games, but you forget what."

    t "The game loads up and your brain quickly loses all sense of focus."

    $ time = "6:30 PM"

    t "You're startled from your stupor by the door opening. Your housemate returning from their workday."

    t "{color=[hm_color]}\"Oh! You're playing [game[rng]]! I love that game.\"{/color}"

    t "They smile at you. But you don't know what to say. You don't know what you were doing, where in the game you were, or even how long you were playing."
    
    t "You start to panic and run back to your room."

    t "{alpha=0.1}{color=[hm_color]}\"It was nice to see you out of your room!\"{/color}{/alpha}"

    t "You struggle to make out what they said but it doesn't matter."

    t "You're safe in your room again."

    t "{a=l9pm}It'll be okay.{/a}" (advance=False)

# self harm
label l840pm:

    scene black
    with fade

    $ renpy.music.set_volume(0.3, 0.0)

    scene alley
    with fadered

    $ renpy.music.set_volume(1.0, 0.0)

    $ time = "8:40 PM"

    t "Everything hurts."

    t "Blood crusts under your nails."

    t "You're alone. Just like always."

    t "You wish you weren't alone."

    t "You don't have to be."

    $ not_alone = True

    t "{a=l946pm}Go home.{/a}" (advance=False)

# given takeout
label l9pm:

    stop sound fadeout 2.0

    scene takeout
    with fade

    $ time = "9:00 PM"

    $ rng = renpy.random.randint(0, len(takeout) - 1)

    if not cried_over_food_today:
        play sound growl volume 0.3

        t "The growling of your stomach is becoming too much to bear."

        t "You hate that constant reminder of food."

        t "You already eat enough as is."
        

        t "You peek out of your room to find that your housemate left some takeout outside your door, the local [takeout[rng]] place." 
        
        t "{a=restart_day}The food goes mostly cold as you drift to sleep.{/a}" (advance=False)
    else:
        play sound knocking volume 0.5

        t "You hear a knock on your door. Your housemate doesn't knock often."

        $ opt = False

        t "{a=lopendoor}Open the door.{/a}\n\n{a=ldoor}Keep it closed.{/a}" (advance=False)

        label lopendoor:
            $ opt = True

        label ldoor:
            if opt:
                jump l901pm
            else:
                $ time = "9:18 PM"

                t "After a few minutes they leave, you wait a bit longer before grabbing the takeout they left for you."

                t "The container has a note on it."

                t "I hope you feel better."

                $ time = "9:20 PM"

                t "You stare at the note for a minute before tossing it away, a bit of water in your eyes for reasons you don't know."

                t "{a=restart_day}You take a few bites of food before drifting to sleep.{/a}" (advance=False)

# talk to housemate
label l901pm:

    $ time = "9:01 PM"

    t "{color=[hm_color]}\"Hey.\"{/color}"

    t "Their words feel like they are dripping with emotion.\n\nWhy?"

    t "{color=[mc_color]}\"Hey...\"{/color}"

    t "{color=[hm_color]}\"Can I come in?\"{/color}"

    t "You waver with fright in your eyes before giving a slight nod."

    $ time = "9:02 PM"

    t "They step in, takeout container in hand."

    t "{color=[hm_color]}\"Here, let's eat together. You don't have to talk about it.\"{/color}"

    t "You nod again, tears already forming in your eyes."

    $ time = "9:53 PM"

    t "You poked and proded at the food before giving up after only a few mouthfuls, the rest of the hour passing in a haze."

    t "Your housemate has been talking about, something, {i}somethings{/i} probably, you don't know what. You weren't paying attention. You never can."

    t "They probably hate how you can't focus on their words, your mind more attuned to the shakes of the hair on their shin."

    t "It's not like you can share anything yourself. It'd only be words of how hopeless and pathetic you are."

    $ time = "10:08 PM"

    t "Eventually they stand up, taking the mostly empty container."

    t "{color=[hm_color]}\"Let's eat together again soon, okay?\"{/color}"

    t "Nodding is the only way you can hold back the tears."

    $ talks_with_hm += 1

    jump restart_day

# escape 4
label l918pm:
    $ time = "9:18 PM"

    t "You wake when it starts to get dark. You're in some random alleyway, curled up against a dumpster."

    t "It's a fitting place."

    play sound growl volume 0.3

    t "Your stomach growls.\n\n{a=l946pm}You should find your way home.{/a}" (advance=False)

# escape 5
label l946pm:

    stop music

    scene apartment
    with fade

    play music inside loop

    $ time = "9:46 PM"

    if not ran_away:
        t "You step inside to find a worried expression on your housemate's face. When was the last time you actually saw them?"

        t "A week? A month? Maybe even a year? Everything has bec...{nw}"
    else:
        t "You step inside to find a worried expression on your housemate's face."

    play sound headache loop volume 0.3 fadein 1.5

    t "Your head starts pounding again."

    t "You tell them that you're fine and brush off any other questions."

    t "You enter your room and close the door. The food from last night is still there on the ground.\n\n{a=restart_day}You don't feel like eating it.{/a}" (advance=False)

label lend:

    t "Your housemate opens the door and pulls you forward."

    t "Not towards the alley, but towards the light."

    t "Your hand feels clammy and you feel at least a little bit sick. It's not a good day."

    t "But no day is a good day."

    t "And this one may be better than the one before it."

    t "So maybe it'll be okay."

    $ time = "4:15 PM"

    t "{w=1.0}It's certainly not as bad as you thought."

    t "Even though you can't feel the warmth of the sun."

    t "Even though you feel like throwing up."

    t "Even though you can't feel the hand holding yours."

    t "Even though this body still isn't your own."

    t "Even though the world still feels like its crushing you from above."

    t "Maybe it's okay."

    t "{w=1.5}{a=end}Maybe it's okay.{/a}" (advance=False)

label end:

    scene black
    with fade

    $ renpy.pause(delay=5, hard=True)

return
