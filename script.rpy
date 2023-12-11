define Chauser = Character("Chauser")
define Tanveer = Character("Tanveer")
define Bast = Character("Bast")
define MrO = Character("Mr.Oluwande")
define Maeve = Character("Maeve")
define GJudge = Character("Dr. Judge")
define BJudge = Character("(Not) Dr. Judge")
define Cathasar = Character("Cathasar")
define OJudge = Character("Doctor Judge")
define Wave = Character("Wave on the Shore")
define Nora = Character("Noraprashna")
define Lady = Character("Meredith")  
init python:
    import random
label start:
    play music "audio/bgm_horror_spooky.mp3"
    "You can't see. You can't make a noise. You hear your own breathing, but you can't move."
    "You try to scream, but nothing happens."
    "Or maybe it does and you just couldn't hear it, swallowed instantly but the oppressive darkness around you."
    "You're so cold."
    "So, so cold."
    "It's deep in your bones and makes you forget what warmth ever felt like."
    play sound "audio/sfx_heartbeat.wav"
    "Your heartbeat.. that's *your* heartbeat isn't it?"
    "You can hear *that*, it gets faster... "
    stop music fadeout 1.0
    scene bg dormday with fade
    play music "audio/bgm_casual1.mp3" fadein 1.0
    "Ah man, that dream again."
    "You rub your hands together to bring back the warmth to them, but to no avail."
    "Looking at the clock, it reads 4:00 PM."
    "That's right, you took a nap. (Don't really feel all that well rested though)"
    "You reach for the paper on your bedside table, reading it once again"
    "Newspaper" "People have been disappearing at night in the University of Silverymoon!"
    "Newspaper" "Some vanish entirely, leaving behind whispered  rumors of fiends or other evil creatures, having spirited them away, never  to be seen again."
    "Newspaper" "Others return strangely altered, with their memories of their kidnapping wiped clean and their minds strangely dulled, with their eyes glazed over."
    "Newspaper" "Local authorities say that they are on the case, but can we really trust them?"
    show charlie smile at left with easeinleft
    "You smile at that last line. You and your friends, much to the chagrin of the local enforcement, have taken an interest in the kidnappings."
    "That reminds you, you have that meeting with your friends in the library..."
    show charlie neutral
    "You should get ready for that."
define m = Character("[name]")
python:
    name = renpy.input("Your name:")
    name = name.strip() or "Charlie"
label postname:
    scene bg library with dissolve
    "At your weekly meeting (in the library) with your friends..."
    "Before you even enter the private room you can hear voices, you're the last one to arrive. As you get closer you can hear your friends arguing..."
    Chauser "\"I'm just saying!\""
    show chauser angry at left with easeinright
    Tanveer "\"You have no evidence!\""
    show tanveer angry at center with easeinright
    Chauser "\"I know! But I just have a feeling-\""
    Tanveer "\"You want to condemn a respected member of society on a *feeling*??\""
    "The girls are arguing about...something. But Bast notices that you've walked in."
    show bast neutral at right with easeinright
    Bast "\"Hey [name]. We were going to wait for you, but uh. Well the ladies had ideas.\""
    m "\"What's going on?\""
    show tanveer neutral
    Tanveer "\"Well Chauser is convinced that Doctor Judge has something to do with, well, y'know.\""
    "She gestures to the newspaper on the table. A copy of the same one you had on your bedside table."
    show bast smile
    Bast "\"He does have a weird name.\""
    show tanveer frown
    Tanveer "\"Please can we be serious about this, we can't go condemning the Town Doctor with nothing to back us up, no one will ever take us seriously ever again.\""
    Bast "\"Ever again? As if they did in the first place?\""
    show chauser neutral
    Chauser "\"I'm not saying we condemn him without evidence. I'm saying we find the evidence because he's definitely got something weird going on.\""
    show tanveer neutral
    Tanveer "\"You are walking yourself right into a confirmation bias. C'mon, [name] back me up!\""
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral 
menu: 
    "\"I mean, Tanveer's right, we can't go into this already thinking someone is guilty.\"":
        jump choice1_a
    "\"Well okay Chauser, say we humor you for a minute. What's got you thinking like this?\"":
        jump choice1_b
label choice1_a:
    hide charlie
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    show tanveer smile
    Tanveer "\"Thank you!\""
    Chauser "\"I know, I know. But, just hear me out okay? Nobody else has any idea and we've been trying to work at this for weeks. I'm not saying we do anything drastic, but maybe just, asking around? Would it hurt?\""
    Bast "\"Listen, Chauser's got a point, we've got nothing else to go off of. Unless- Tanveer? Any ideas?\""
    show tanveer frown
    Tanveer "\"...\""
    Bast "\"Right. So Chauser what were you thinking?\""
    jump postchoice1
label choice1_b:
    hide charlie
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    show tanveer frown
    Tanveer "\"...\""
    jump postchoice1
label postchoice1:
    Chauser "\"I had an appointment for my teeth because my fangs and everything right? So I went to the Doctor for just a normal check up.\""
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    m "\"And?\""
    hide charlie
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    show chauser frown
    Chauser "\"And.. and. He just seemed...I don't know.. off somehow.\""
    Chauser "\"I can't place my finger on it but being there gave me the creeps.\""
    Chauser "\"I got the Hell out of there, but even if it's not connected to the disappearances... that Doctor...something isn't right with him.\""
    hide tanveer
    hide chauser
    hide bast
    show charlie frown at left
    m "\"Hmmm. This is a lot to place on the man that the entire University trusts.\""
    hide charlie
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    Tanveer "\"Exactly!\""
    show bast smile
    Bast "\"Well I've got nothing better to do and this seems interesting enough, if only to put Chauser's paranoia to rest.\""
    show tanveer frown
    Tanveer "\"You have nothing better to do? Did you forget about our project?\""
    show bast scared
    show bast smile
    "Ah, The Final Project. The four of you are putting together a presentation about the inefficiency of the Police Department."    
    Bast "\"No, ha-ha. I most definitely, assuredly did not forget-\""
    show tanveer smile
    Tanveer "\"Good, that means your side of the research is done then?\""
    Bast "\"Yup! Completely unrelated I just remembered.. I uh- I need to go walk my fish. I'll see you guys in class tomorrow, bye!\""
    hide bast with easeoutright
    "Tanveer sighs."
    show tanveer neutral
    Tanveer "\"He's going to need some help, and I also need to work on my part. Are you two good with starting this...investigation?\""
    show chauser smile
    Chauser "\"So you're good with this? It's okay?\""
    show tanveer smile
    Tanveer "\"Yeah, yeah. Just don't get into too much trouble okay?\""
    show chauser grin
    Chauser "\"Yes! okay, we won't let you down.\""
    hide tanveer with easeoutright
    show charlie neutral at center
    m "\"Okay it's already almost evening, there's not much we can do today, do you have anywhere specific you want to start?\""
    show chauser neutral
    "Chauser takes out a piece of paper."
    Chauser "\"I made a list of the things we could start with, I'm fine with whatever really, where do you think we should start?\""
    stop music fadeout 1.0
default choice2_menu = set()
define c = Character("[char]")
python:
    daycount = 0
    if daycount == 0:
        char = Chauser
    elif daycount == 1:
        char = Tanveer
    else:
        char = Bast
default townsfolkChosen = False
default maeveChosen = False
default officeChosen = False
label investigate:
    menu:
        set choice2_menu
        "Talk to the townsfolk.":
            jump townsfolk
        "Talk to Dr. Judge's daughter.":
            jump maeveconvo
        "Go to Dr. Judge's office to talk and investigate":
            jump office
    
label townsfolk:
    play music "audio/bgm_city.mp3" fadein 1.0 #not playing for some reason
    scene bg cityday with fade
    show charlie neutral at left with easeinright
    if daycount == 0:
        show chauser neutral at center with easeinright
    elif daycount == 1:
        show tanveer neutral at center with easeinright
    else:
        show bast neutral at center with easeinright
    "You and [char] go out into town, talking to various townsfolk."
    "From what you two can glean, Doctor Judge is known to be an effective Doctor and an even better father."
    "But, he is also known to bad with his money."
    scene bg mros with dissolve
    show charlie neutral at left with easeinright
    if daycount == 0:
        show chauser neutral at center with easeinright
    elif daycount == 1:
        show tanveer neutral at center with easeinright
    else:
        show bast neutral at center with easeinright
    "For one final stop, you go to talk to his neighbor, Mr. Oluwande, a tailor."
    show mro neutral at right with easeinright 
    c "\"Hello, Mr. Oluwande! Could we speak with you for a moment?\""
    MrO "\"Hm? Sure, what seems to be the matter?\""
    c "\"Well. How well do you know your neighbor, Dr. Judge?\""
    show mro smile
    MrO "\"Hm? Haha, quite well I'd imagine, I've been living across from him for years.\""
    show mro neutral
    MrO "\"Why do you ask?\""
    c "\"Have you perchance noticed any, uh, strange behavior? Or strange happenings around his place?\""
    menu:
        "Roll": 
            $ roll = random.randint(1,20)
            "Your roll is [roll]."
    if roll <= 10:
        jump .susp
    else:
        jump .cont
label .susp:
    MrO "Hm. Why do you ask?"
    menu:
        "\"It's for a project for our psychology class.\"":
            show mro grin
            MrO "\"Haha! Studying the effects of old age then?\""
            jump .cont
        "\"We saw him and were concerned about him.\"":
            jump .cont
        "\"We think he might be up to something.\"":
            jump .cont
label .cont:
    show mro smile
    MrO "\"Hmm, now that you mention it..\""
    show mro neutral
    MrO "\"There was a strange while where there some mysterious little fellows hanging around his office. I thought they were planning on robbing Judge, and I tried telling him, but he didn't seem too concerned.\""
    show mro grin
    MrO "\"Anyway, I haven't seen them in months so it probably wasn't anything.\""
    "This is strange, but you're not quite sure yet how it fits into it all. It could be nothing, it could be everything." 
    m "\"Thank you, do you know if there's a way to contact these people? The one's that were hanging around?\""
    show mro neutral
    MrO "\"Hmm, I'm sure there is, there's the Shady Tavern. You post a bulletin there with a description of who you want to see, I'm sure you'll be able to get an audience.\""
    MrO "But I'd be careful if I were you kids, I wouldn't want to get messed up in that sort of business.\""
    m "\"Of course, of course; we're just curious is all. Is there anything else?\""
    show mro grin
    MrO "\"Let me think... hahaha it's probably just him being a bit of an eccentric and all..\""
    show mro smile
    MrO "\"For some reason, he had one of his teeth replaced. With iron of all things. But that's all I can think of.\""
    "Also strange, but what does it mean." 
    m "\"Huh, well. Thank you Mr. O, we'll see you around then.\""
    MrO "\"Haha, goodbye kids. And remember what they say about curiosity.\"" 
    show mro neutral
    MrO "\"She murdered a kitten in cold blood.\""
    show charlie smile
    "You're fairly certain that's not how the saying goes, but you wave to him as you leave either way."
    hide mro with easeoutright
    scene bg dormnight with fade
    stop music fadeout 1.0
    $ daycount += 1
    $ choice2_menu.add("Talk to the townsfolk.")
    $ townsfolkChosen = True
    if daycount == 1:
        jump postday0
    elif daycount == 2:
        jump postday1
label maeveconvo:
    play music "audio/bgm_piano_garden.mp3" fadein 1.0
    scene bg garden with dissolve
    show charlie neutral at left with easeinright
    if daycount == 0:
        show chauser neutral at center with easeinright
    elif daycount == 1:
        show tanveer neutral at center with easeinright
    else:
        show bast neutral at center with easeinright
    "You two ask around, and you know that Dr. Judge's daughter likes to hang around the garden area of park." 
    show maeve frown at right
    "You find her sitting down among the flowers, you're not sure but she looks a bit sad. Maybe if you're nice to her..."
    show charlie smile
    m "\"Hey there, what's wrong?\""
    Maeve "Maeve sighs."
    m "\"Your name is Maeve right? Dr. Judge's daughter?\""
    Maeve "\"Yeah?\""
    m "\"Is everything okay with your father?\""
    Maeve "\"...No.\""
    show charlie neutral
    m "\"Oh no what's wrong?\""
    Maeve "\"That's the problem, I don't know!\""
    m "\"It's okay we're trying to figure it out too. Maybe if we can compare notes?\""
    show maeve smile
    Maeve "\"You believe me? You're going to help?\""
    show charlie smile
    c "\"Yes, we're going to try our best.\""
    show maeve neutral
    Maeve "\"Something's off about dad. One of his teeth is weird now. But sometimes it isn't? He won't tell me anything.\""
    show charlie neutral
    c "\"Sometimes it isn't? Does he act any different?\""
    Maeve "\"When his tooth is weird, it's like...y'know when you're sleepy and you wake up and nothing makes sense. He's like that but the entire time.\""
    c "\"And when the tooth isn't there?\""
    show maeve frown
    Maeve "\"When it's gone, he.. He gets mean.\""
    show maeve neutral
    Maeve "\"But that's only at night, so when I go to sleep I just stay in my room. But sometimes I can't sleep.\""
    show charlie frown
    m "\"Nightmares?\""
    "Maeve shakes her head."
    show maeve frown
    Maeve "\"I hear people talking at night. From below. But we don't have anything below.\""
    show charlie neutral
    "You don't know what to say..."
    c "\"Okay we'll look into it, we promise. You stay safe okay?\""
    "Maeve nods, she looks up at the two of you earnestly."
    show maeve neutral
    Maeve "\"Please don't hurt my dad. He is a good person.\""
    hide maeve with easeoutright
    "You and [char] leave the park together in silence, in solemnity."
    "There was something happening here certainly. Whether it has anything to do with the disappearances or not, you're still unsure."
    stop music
    scene black
    $ daycount += 1
    $ choice2_menu.add("Talk to Dr. Judge's daughter.")
    $ maeveChosen = True
    if daycount == 1:
        jump postday0
    elif daycount == 2:
        jump postday1
label office:
    play music "audio/bgm_city.mp3"
    scene bg normaloffice with fade
    show charlie neutral at left with easeinright
    if daycount == 0:
        show chauser neutral at center with easeinright
    elif daycount == 1:
        show tanveer neutral at center with easeinright
    else:
        show bast neutral at center with easeinright
    "You and [char] go to the Dr. Judge's office to have a chat."
    "At the entrance there is a string of teeth that hands in the front window, advertising Dr. Judge's dentistry skills."
    "Upon entering, Dr. Judge looks over at you and smiles lazily, you see the glint of a strange tooth."
    show gjudge neutral at right
    GJudge "\"Welcome to Doctor Judge's Barbery and Surgery and Dentistry. What can I do for you?\""
    m "\"Hello Doc.\""
default talkjudge_menu = set()
label .talkjudge:
    if len(talkjudge_menu) < 3:
        menu:
            set talkjudge_menu
            "Current Affairs":
                jump .currentaffairs
            "Investigate the Office":
                jump .docoffice
            "His Health":
                jump .judgehealth
    else:
        hide judge with fade
        jump .postjudge 
label .currentaffairs:
    m "\"We're from the University and just wanted to get your opinion on what's been going on around town.\"" 
    "Dr. Judge shakes his head a bit."
    show gjudge frown
    GJudge "\"Hm? What's going on? There's nothing going on that I know about.\"" 
    show charlie frown
    c "\"The disappearances?\"" 
    GJudge "\"What disappearances?\""
    "[char] shares a glance with you. You look at Dr. Judge and his eyes seem to be strangely glazed over."
    show charlie smile
    m "\"Ah if it hasn't reached you yet, don't worry about it then.\""
    c "\"Well if you don't mind me asking, what happened to your tooth?\""
    show gjudge neutral
    GJudge "\"Hm, I don't remember.\""
    show gjudge smile
    GJudge "\"I suppose I must've been testing some new skills out on myself, haha.\""
    $ talkjudge_menu.add("Current Affairs")
    jump .talkjudge
label .docoffice:
    m "\"We're artists and we were wondering if we would be allowed to look around to draw, we won't disturb anyone we promise.\""
    "Dr. Judge shrugs and looks around distractedly."
    GJudge "\"Always happy to support the arts.\"" 
    "You take a look around."
    menu:
        "Roll":
            $ roll = random.randint(1,20)
            "Your roll is [roll]."
    if roll <= 10:
        "You look around and you see that there's a sink, some mirrors, a fireplace. All just normal barbery and surgery equipment."
        "Nothing out of ordinary here. A very normal place."
    else:
        "You look around and you see that there's a sink, some mirrors, a fireplace. All just normal barbery and surgery equipment."
        play sound "audio/sfx_clue_found.wav"
        "Underneath a barber chair there seems to be...is that? A trapdoor?"
        "You nudge [char] and their eyes follow yours and widen a bit. [char] nods at you."
    $ talkjudge_menu.add("Investigate the Office")
    jump .talkjudge
label .judgehealth:
    m "\"How have you been?\""
    show gjudge smile
    GJudge "\"Hm? Oh well I have been just fine, ha.\""
    "You look at Dr. Judge more closely."
    menu:
        "Roll":
            $ roll = random.randint(1,20)
            "Your roll is [roll]."
    if roll <= 10:
        "Dr. Judge seems...fine."
    elif roll <= 15:
        "Dr. Judge seems a bit absent-minded."
    else:
        "Dr. Judge seems a bit absent-minded."
        "With your University training you sense some magic around."
        play sound "audio/sfx_clue_found.wav"
        "Honing in on that...there seems to be a spell around Dr. Judge. An aura of transmutation magic."
        show charlie frown
        "You push against it with your mind but you can't break it. You file the information away."
    $ talkjudge_menu.add("His Health")
    jump .talkjudge
label .postjudge:
    scene bg cityeve with dissolve
    show charlie neutral at left
    "On your walk back home you fill in [char] with what you saw."
    stop music
    c "\"This is all strange isn't it. There's something here.\""
    play music "audio/bgm_chase.wav"
    show charlie scared
    if daycount == 0:
        show chauser scared at center
    elif daycount == 1:
        show tanveer scared at center
    else:
        show bast scared at center
    play sound "audio/sfx_monster_growl.wav"
    "Both of you stop in your tracks when you hear a deep croak and growl from behind you."
    "You look at each other and take off, not bothering to look behind you."
    "[char] takes the lead trying to lose the creature."
    scene black
    if daycount == 0:
        hide chauser
    elif daycount == 1:
        hide tanveer
    else:
        hide bast
    hide charlie
    jump .firstchase
default haveFought = True
default haveEvade = False
default evasion_check = 0
label .firstchase:
    "You run and ready a dagger to throw behind you."
    menu:
        "RUN":
            $ roll = random.randint(1,20)
            if roll <= 10:
                "Your roll is [roll] :(."
                play sound "audio/sfx_monster_growl.wav"
                "You run and run, all the while hearing heavy footsteps following, followed by growls, slowly getting louder."
                $ evasion_check -= 1
                jump .firstchase
            else:
                "You roll is [roll] :)."
                "Down the streets, twisting and turning, you and [char] are synchronized, stumbling and pulling each other this way and that. The growls get a bit quieter."
                $ evasion_check += 1
                if evasion_check == 2:
                    $ haveEvade = True
                if haveEvade:
                    jump .postfirstchase
            $ haveFought = True
            jump .firstchase
        "FIGHT" if [haveFought]:
            $ haveFought = False
            "You take one of your daggers and throw it."
            $ evasion_check += 1
            if evasion_check == 2:
                $ haveEvade = True
            if haveEvade:
                jump .postfirstchase
            jump .firstchase
label .postfirstchase:
    stop music
    play music "audio/bgm_horror_spooky.mp3"
    scene bg citynight with fade
    show charlie scared at left
    if daycount == 0:
        show chauser scared at center
    elif daycount == 1:
        show tanveer scared at center
    else:
        show bast scared at center
    play sound "audio/sfx_breathing.wav"
    "You and [char] stop finally in an unfamiliar place, panting."
    "You shake from adrenaline, cold, and fear. Rubbing your arms, you look around. You think you can get back home from here.. you can't see the creature anymore."
    "Maybe- hopefully, you lost it."
    show charlie neutral
    show charlie scared
    if daycount == 0:
        show chauser neutral
    elif daycount == 1:
        show tanveer neutral
    else:
        show bast neutral
    "Looking to [char], neither of you speak. Either out of shock or maybe fear that perhaps the creature could still hear you, you can't say."
    "Quietly the two of you start walking back to your dorms.."
    stop music fadeout 1.0
    if daycount == 0:
        hide chauser with easeoutright
    elif daycount == 1:
        hide tanveer with easeoutright
    else:
        hide bast with easeoutright
    scene black
    $ daycount += 1
    $ choice2_menu.add("Go to Dr. Judge's office to talk and investigate")
    $ officeChosen = True
    if daycount == 1:
        jump postday0
    elif daycount == 2:
        jump postday1
label postday0:
    play music "audio/bgm_city.mp3"
    show charlie neutral at left
    "The information from the days events swirl around in your head."
    "Perhaps Chauser is onto something, perhaps it has nothing to do with the disappearances."
    "You know that you need more information and that tomorrow is a new day." 
    stop music fadeout 1.0
    scene black
    "When you go to sleep, your dream is warm."
    "Filled with the sounds of laughter and the smell of coffee."
    "It fills in around you swelling and then slowly, slowly, leaking away."
    play music "audio/bgm_horror_spooky.mp3" fadein 1.0
    "The more it decreases the more you try to reach for it and the faster it seems to slip away.." 
    "You can't see, can't make a noise. You hear your own breathing, but you can't move."
    "You try to scream, but nothing happens."
    "Or maybe it does and you just couldn't hear it, swallowed instantly but the oppressive darkness around you."
    "You're so cold. So, so cold. It's deep in your bones and makes you forget what warmth ever felt like."
    "It smells different. Smells like wet earth. Your fingers brush against some mud, but still you can't see." 
    play sound "audio/sfx_heartbeat.wav"
    "Your heartbeat.. that's *your* heartbeat isn't it?"
    play sound "audio/sfx_cackle.wav"
    "You can hear it, it gets faster, cruel laughter echoes in your mind and in your bones..."
    stop music fadeout 1.0
    play music "audio/bgm_casual1.mp3" fadein 1.0
    scene bg dormday with fade
    show charlie neutral at left with fade
    "When you wake up, you see the morning light filtering through the window into the room."
    "That dream again. What could it mean?"
    show charlie frown
    show charlie scared
    show charlie neutral
    "Looking over at the clock tells you that you need to get to class in about... 10 minutes ago."
    scene bg cityday with dissolve
    "The day is uneventful, your mind is still preoccupied from what happened previously. After classes, you head straight to the library this time instead of the dorm."
    scene bg library with dissolve
    show charlie neutral at left
    "Arriving at the library, Tanveer is already at your guys' spot, studying."
    show tanveer smile at center with easeinright
    Tanveer "\"Afternoon!\""
    "Noticing your expression, she closes her textbook."
    show tanveer frown
    Tanveer "\"What's wrong?\""
    m "\"Me and Chauser, we checked some stuff out last night...\""
    show tanveer neutral
    Tanveer "\"'Chauser and I', you mean.\""
    m "\"...\""
    show tanveer smile
    Tanveer "\"Sorry, go on.\""
    "You share the information you learned from last night."
    m "\"Listen, I know it's nothing specifically incriminating...but it's still weird.\""
    show tanveer neutral
    Tanveer "\"Hm. Yeah I'm not yet convinced it has something to do with the kidnappings, but this is worth looking into.\""
    Tanveer "\"And you didn't see any cops around while you guys were doing all this, right?\""
    m "\"No cops, I don't think they have any idea.\""
    show tanveer grin
    Tanveer "\"Well, at the very least, if we solve this we'll have ample evidence that our law enforcement here is incompetent.\""
    show charlie smile
    m "\"So, you're on board now.\""
    show tanveer neutral
    Tanveer "\"Sure, it won't hurt.\""
    show bast neutral at right with easeinright
    Bast "\"What won't hurt?\""
    show charlie neutral
    m "\"Bast you will not believe what we learned.\""
    show bast smile
    "Bast quirks an eyebrow and leans forward conspiratorially."
    Bast "\"Tell me everything.\""
    hide charlie with fade
    "You rehash the information for Bast, by the end Chauser walks in."
    show chauser neutral at left
    show bast frown
    Bast "\"Man, you guys got all the fun.\""
    show chauser smile
    Chauser "\"I'm not sure, I'm a bit freaked out by it all. But still, we're keeping on this, I think we're onto something here.\""
    show bast smile
    Bast "\"For sure. I have no clue what, but something is definitely happening.\""
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    m "\"We need to keep looking, there's more to this, I'm sure. Chauser, what else did you have on that list?\""
    "Chauser takes out her list, showing everyone the remaining tasks on it."
    hide charlie
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    Tanveer "\"All right, we should split up to cover more ground. Me and [name] can do one thing, Bast and Chauser do the other. What do you think we should do [name]?\""
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    stop music fadeout 1.0
    jump investigate
label postday1:
    show charlie neutral at left with easeinright
    "Your mind is still swirling from all that you've learned."
    "One thing is certain, there's *definitely* something going on here. You're not quite sure how it's exactly related to the kidnappings, if it is at all."
    scene bg dormnight
    "When you reach your dorm, you fall asleep fitfully, dreading what you expect to be another nightmare."
    play music "audio/bgm_casual1.mp3" fadein 1.0
    scene bg dormday with fade
    "When you awake, you are freezing but you sigh in relief. No nightmare tonight, not that you can remember."
    "You rub your arms to try to bring warmth back into them and head out for the day."
    scene bg library with dissolve
    "After classes, you head to the library, as usual. This time, everyone else is already there."
    show chauser neutral at left with easeinright
    show tanveer neutral at center with easeinright
    show bast neutral at right with easeinright
    "Tanveer and Chauser are talking rapidly between themselves, comparing notes."
    hide chauser
    hide tanveer
    show charlie neutral at left with easeinright
    show bast grin
    "Bast leaps up  when he sees you and pulls you over to his side of the table." 
    Bast "\"Hello, hi yes. How are you, etc etc. Pleasantries exchanged? Great.\""
    Bast "\"Here's what we found out.\""
    if townsfolkChosen != True:
        jump .townsfolkdebrief
    elif maeveChosen != True:
        jump .maevedebrief
    elif officeChosen != True:
        jump .officedebrief
label .townsfolkdebrief:
    show bast neutral
    Bast "\"So apparently, Dr. Judge? Great doctor, great father, terrible with his money.\""
    Bast "\"We talked to his neighbor, Mr. Oluwande, y'know the tailor?\""
    Bast "\"And he said that for a while there were these weird guys hanging around the good Doctor's establishment. But they haven't been seen in months.\"" 
    Bast "\"And! Get this, he has a new tooth, but it's made of iron of all things.\""
    Bast "\"We also learned that about those weird guys? Apparently, if we want we can talk to them.\""
    show bast smile
    hide charlie
    jump .postdebrief1
label .maevedebrief:
    show bast neutral
    Bast "\"So we went and talked to Maeve yeah? She was super in the dumps.\""
    Bast "\"She was saying that sometimes her dad has this weird tooth and sometimes he doesn't.\"" 
    Bast "\"And she noticed that when he's got the tooth he's way out of it, but when he doesn't he's kinda an asshole-\""
    Bast "\"Well she didn't say that exactly, but you get the gist.\""
    Bast "\"And that's not all! She says its difficult for her to sleep because she can hear people in the basement.\"" 
    Bast "\"Weirdest part? She says they don't have a basement.\""
    show bast frown
    Bast "\"She's really concerned about her dad...\""
    hide charlie
    jump .postdebrief1
label .officedebrief:
    Bast "\"You will not believe what happened to us big man. So we chatted up Dr. Judge, who, by the by, is also a dentist.\""
    show bast neutral
    Bast "\"We tried asking him about what he thought about the kidnappings, discreetly of course, and this man had no idea about it.\""
    Bast "\"Now that might not be anything, like maybe he just doesn't read the newspaper, but man, *everyone's* been talking about the kidnappings.\""
    Bast "\"The other thing is, when we asked him about his weird tooth, he says he doesn't remember where he got it from! Man had a whole surgery and he doesn't even remember when it happened!\""
    show bast frown
    Bast "\"Anyways, there's more. On our way back, something started chasing us.\""
    show bast grin
    Bast "\"We ran like hell and we didn't look back. I threw a knife or two and eventually we lost it, but, man, something or someone doesn't like that we're snooping around.\""
    hide charlie
    jump .postdebrief1
label .postdebrief1:
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    Chauser "\"I thought of two other things we can do now that we have all this information. Take a look...\""
    "Chauser takes out her list, now with two new things on it."
default choice3_menu = set()
default cathaChosen = False
default stakeoutChosen = False
label inv2:
    menu:
        set choice3_menu
        "Meet with mysterious figures":
            jump cathaconvo
        "Stake out Dr. Judge's office":
            jump stakeout
label cathaconvo:
    Tanveer "\"Okay, me and Chauser will do what's left. We'll meet up tomorrow?\""
    Bast "\"Yes.\""
    Tanveer "\"Okay, let's-\""
    Chauser "\"Wait. Everyone stay safe, okay? Don't do anything rash.\""
    show chauser frown
    Chauser "\"If you feel like you need to get out of there, then get out of there.\""
    stop music fadeout 1.0
    play music "audio/bgm_tavern.wav" fadein 1.0
    scene bg tavern with dissolve
    show bast neutral at center with easeinright
    play sound "audio/bgm_chatter.mp3"
    "You and Bast go to Shady Inn, drunks and gamblers make a ruckus and various hooded figures brood in different corners."
    "You approach the bulletin that's put up, you see various wanted posters and mercenary requests. After putting up your note, you go back to Bast who has ordered a drink for himself."
    Bast "\"How long do you think it'll take?\""
    show charlie smile at left with easeinright
    m "\"I don't know Bast, I don't usually do this sort of thing.\""
    m "\"D'ya think it's such a good idea to have a drink right now?\""
    show bast smile
    Bast "\"Hm? Oh I'm not drinking it, this is just to keep up appearances.\""
    hide bast
    hide charlie
    "Looking around you notice that even with Bast ordering a drink, the two of you stick out like a sore thumb with your school uniforms." 
    "You sigh, at least it'll be easy for them to find you."
    show charlie neutral at left
    show bast neutral at center
    "After a bit of time passes you and Bast realize that perhaps meeting like these don't happen this easily... you really are getting a bit out of your depth"
    Bast "\"Do you think we should just come back tomorrow? Maybe wait a day or two.\""
    m "\"Man this is such a shot in the dark, I don't know. Mr. Oluwande said that they haven't been seen around in months. They might be out of here.\""
    show bast frown
    "Bast sighs swirling the shady looking alcohol around in his glass."
    show bast neutral
    "Unknown" "\"Oy, if you're not going to have that drink, then give it here.\""
    "Looking to where the gravelly voice came from, you see three cloaked figures, the tallest of which was the one who spoke to you." 
    "Bast slides the drink over to the figure, as he sits down. The two others stay standing behind him silently."
    show cathasar
    show bast scared
    show charlie scared
    "The man tips the drink back smoothly. He then fixes the two of you with his stare."
    "Unknown" "\"So what do two little schoolboys want with me, eh?\""
    "Bast is still stunned, he's also never done this before."
    show charlie neutral
    "You clear your throat."
    show bast frown
    m "\"Uh. Well, mhm.\""
    m "\"You had business with Dr. Judge a few months ago?\""
    "Unknown" "\"If I did, what is it to you?\""
    show charlie smile
    m "\"We just want to know who you are, and maybe why?\""
    "The man laughs. It's a mean laugh."
    Cathasar "\"I'm Cathasar. I'll ask a different question.\""
    "Cathasar leans closer in to the table, threateningly."
    show charlie frown
    Cathasar "\"Why should I tell you?\"" 
    "You think for a second."
    show charlie neutral
    m "\"What do you want?\""
    "Cathasar leans back and laughs again."
    Cathasar "\"Now you're speaking my language.\""
    Cathasar "\"You see, I don't have much I could want from a couple of brats.\""
    Cathasar "\"How about an I.O.U, eh? I do you this favor, and then, one day, you lot do a favor for me?\""
    "You look to Bast, he shakes his head."
    "You know this can't be a good idea, but you also can't see another way. Fighting most definitely isn't an option. This man was already on a payroll, he clearly didn't care for money."
    Cathasar "\"Oh, don't worry I won't make it too difficult.\""
    Cathasar "\"I'll make it fair, that's on my honor and my word.\""
    "Somehow, that doesn't make you feel any better. But honor among thieves and all that. If you didn't want to work with the cops, then this was inevitable.\""
    m "\"Fine.\""
    "Bast winces, shaking his head."
    "Cathasar leans forward a bit, extending a gray hand out towards you."
    Cathasar "\"Shake on it.\""
    "Tentatively, you take his hand." 
    show charlie frown
    "Immediately, magic pulses from where yours and his hands meet. You realize now, that this man is fae."
    show charlie scared
    "And you just made a deal with him."
    show charlie neutral
    "You swallow, pushing down your panic. That's something to worry about later, there's a task at hand."
    m "\"Information.\""
    "Your voice comes out weaker than you wanted it to, but you hold your stare." 
    "Cathasar chuckles."
    Cathasar "\"Ohoho. Okay, big man. Listen up because I'll only say this once.\"" 
    Cathasar "\"Your nice Dr. Judge needed money. He came to us. Our business is money.\"" 
    Cathasar "\"But now maybe, just maybe, no one ever told nice Dr. Judge that when you take money out, you have to repay it too.\"" 
    Cathasar "\"We tried to be magnanimous about it, really. We gave him so much time. But we have a business to run, so when he so rudely refused to pay up his due amount...\"" 
    Cathasar "\"Well.\""
    Bast "\"What did you do?\""
    Cathasar "\"We sold his debt. Easy.\""
    m "\"To who?\""
    Cathasar "\"You mean, 'to whom'? Well, that's it. Some human woman, quite wealthy, dark hair. She was smart, she refused to tell us her name. I suppose you could say she was pretty, but her teeth were strange.\""
    "You and Bast share a look."
    m "\"Her teeth?\""
    Cathasar "\"All made of iron.\""
    "A new player. A woman with all iron teeth."
    Bast "\"Do you know what she did to him?\""
    Cathasar "\"Nah not my business. I moved on.\""
    m "\"And you don't have any other information about her?\""
    Cathasar "\"Nope, like I said, I moved on.\""
    Bast "\"We should go then, we have people waiting for us.\""
    "You and Bast stand up."
    Cathasar "\"Remember, we've got a deal kid. And good luck! You'll need it.\""
    stop music fadeout 1.0
    stop music
    play music "audio/bgm_city.mp3"
    scene bg cityeve with dissolve
    "It's difficult to turn your back to the fae, but you keep your cool as you and Bast walk out." 
    show charlie neutral at left
    show bast frown at center
    Bast "\"I don't know if that was a good idea.\""
    m "\"Well it's done now, let's just make sure it wasn't for nothing.\""
    stop music fadeout 1.0
    scene black
    $ choice3_menu.add("Meet with mysterious figures")
    $ cathaChosen = True
    jump postday2

label stakeout:
    Tanveer "\"Okay, me and Chauser will do what's left. We'll meet up tomorrow?\""
    Bast "\"Yes.\""
    Tanveer "\"Okay, let's-\""
    show chauser frown
    Chauser "\"Wait. Everyone stay safe, okay? Don't do anything rash.\""
    Chauser "\"If you feel like you need to get out of there, then get out of there.\""
    stop music fadeout 1.0
    play music "audio/bgm_city.mp3" fadein 1.0
    scene bg cityeve with fade
    "The two of you go to Dr. Judge's office. You and Bast wait until dusk before you find somewhere to watch from." 
    "You crouch in the bushes near the Doctor's office, keeping an eye on Dr. Judge through the window. Neither of you dare to say a word out of fear that someone may overhear you."
    "You two watch Dr. Judge and Maeve close up his shop, cleaning up and turning the sign."
    "You watch as he makes a meager dinner for himself and Maeve and they eat quietly. Maeve attempts to make some conversation but it falls flat every time." 
    "Once she finishes up, she gives Dr. Judge a quick hug before running upstairs to go to her room. Dr. Judge appears to go to the back and down into the cellar."
    "After about an hour of waiting in the dark with no sound, Bast nudges you."
    show bast neutral at center with easeinright
    Bast "\"How long are we going to wait?\""
    show charlie neutral at left with easeinright
    m "\"Longer than this, we need to be patient.\""
    "Bast sighs and nods. He adjusts as subtly as he can." 
    hide bast
    hide charlie
    "Two hours later, finally you hear noise coming from the cellar around back." 
    show bjudge neutral at right with fade
    "You see the shadow of Dr. Judge...as he turns on the light you realize he looks different. This  is not the same man."
    "He opens the shop back up, turning on all the lights and setting everything up. For who? You can't tell."
    "He pushes a button and the barber chair slowly descends into a trapdoor. When the chair is gone, (Not) Dr. Judge looks around before jumping in after it, closing the hatch behind him."
    hide bjduge with easeoutright
    show bast frown at center
    Bast "\"Should we follow him?\""
    show charlie frown at left
    m "\"No, we were told not do anything rash, remember? We should recuperate with the girls first.\""
    "You and Bast sneak back to your dorms with this newfound information."
    stop music fadeout 1.0
    scene black
    $ choice3_menu.add("Stake out Dr. Judge's office")
    $ stakeoutChosen = True
    jump postday2
label postday2:
    play music "audio/bgm_casual1.mp3" fadein 1.0
    scene bg dormnight with fade
    show charlie neutral at center
    "When you get back to your dorm, you lay awake in bed for a while, tossing and turning."
    "You decide to use your restlessness to get some work done." 
    "As you're typing (using a typewriter, of course, nothing anachronistic here) an essay about the consequences of sharing the knowledge and practice of magic you start to nod off.." 
    "You put your head down on your arms..." 
    "Just for a second..."
    stop music fadeout 1.0
    scene black
    play music "audio/bgm_horror_spooky.mp3" fadein 1.0
    "You can't see, can't make a noise."
    "You hear your own breathing, but you can't move." 
    "You try to scream, but nothing happens. Or maybe it does and you just couldn't hear it, swallowed instantly but the oppressive darkness around you."
    "You're cold. So, so cold." 
    "It's deep in your bones and makes you forget what warmth ever felt like." 
    "It smells different. Smells like wet earth." 
    scene bg tunnel with fade
    show charlie scared at center
    "Your fingers brush against some mud, and you look around. A tunnel slowly comes into view, you're underground somehow." 
    "You spin around as you see more and more entrances to different tunnels, all in a circle around you." 
    play sound "audio/sfx_cackle.wav"
    "You stop, facing one. The tunnel is dark and the darkness seems to pull you in. From it, echoes a high-pitched, cruel cackling." 
    play sound "audio/sfx_heartbeat.wav"
    "Your heartbeat.. that's *your* heartbeat isn't it? You can hear it, it gets faster, the cruel laughter echoes in your mind and in your bones..."
    stop music fadeout 1.0
    play music "audio/bgm_casual1.mp3" fadein 1.0
    scene bg dormday with fade
    show charlie neutral
    "You wake up groggily at your desk. Picking up your head and looking at the clock tells you that it's early but you should be getting up soon to get to class." 
    "Your back is sore from falling asleep at your desk and your face is all red."
    scene bg cityday
    "You freshen up and head to class, whatever is happening with your dreams you decide to figure it out *after* all this business." 
    scene bg library
    "After classes, you head to the library. You're drained but you know there's still work to do, you buy an energy potion to chug on your way there. It tastes awful but it should do the trick." 
    show chauser neutral at left with easeinright
    show tanveer neutral at center with easeinright
    show bast smile at right with easeinright
    "When you get there, Bast is recounting your adventures excitedly to the girls. They look up when you enter."
    Tanveer "\"Hello [name], Bast was just filling us in. Say, are you doing alright?\""
    Chauser "\"Yeah man you look like crap.\""
    "Looking at Chauser, she also looks more tired than usual. But, perhaps the nightmares were hitting you harder than you thought." 
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    m "\"I'm fine, really.\""
    hide charlie
    show chauser neutral at left 
    show tanveer neutral at center 
    show bast neutral at right
    "Tanveer looks concerned."
    Tanveer "\"Are you sure? Are you sleeping fine?\""
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    "You consider telling them, but perhaps afterwards."
    "There were more pressing things." 
    m "\"Yeah, I'll be better once we figure this all out. What did you guys find?\""
    hide charlie
    show chauser neutral at left 
    show tanveer neutral at center 
    show bast neutral at right
    Chauser "\"Well. If you say so. Please take care of yourself, though.\""
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    m "\"Of course.\""
    hide charlie
    show chauser neutral at left 
    show tanveer neutral at center 
    show bast neutral at right
    if cathaChosen != True:
        jump .shadyinndebrief
    elif stakeoutChosen != True:
        jump .stakeoutdebrief
label .shadyinndebrief:
    Tanveer "\"We went to The Shady Inn, and first off let me tell you, that place gave me the creeps.\"" 
    Tanveer "\"We waited around until some fae showed up, he said his name was Cathasar. He's a moneylender. He told us that Dr. Judge took out a loan from him, but wasn't able to pay up.\""
    Tanveer "\"He sold the loan to this other woman, he said she concealed her identity pretty well. But he mentioned that she had all iron teeth, it could be a coincidence but it's a strange enough thing that it might be connected.\""
    show bast frown
    Bast "\"He just gave you all the information, just like that?\""
    "Chauser coughs pointedly at Tanveer."
    Tanveer "\"Oh yeah, well, I made a deal with him.\""
    Bast "\"Go on.\""
    Tanveer "\"He said he'd give us the information for a favor.\""
    Bast "\"What's the favor?\""
    Tanveer "\"Well, that's just it. I don't know yet, but.. he said he'd make it 'not so difficult'?\""
    "Even she didn't sound like she believed herself."
    show bast neutral
    "You and Bast stare at her."
    Bast "\"So you made a deal. With some random fae bloke. And you don't even know the terms of it?\""
    "Tanveer shrugs sheepishly."
    show  tanveer smile
    Tanveer "\"Look there's not much we can do now, and what's done is done. We'll worry about that later, okay?\"" 
    Tanveer "\"For now, we need to  focus on the fact that there's potentially a new player in the game. I don't what role she plays but she could be involved big time.\""
    jump .postdebrief2
label .stakeoutdebrief:
    Tanveer "\"We staked out Dr. Judge's office, and boy, did we see things.\""
    Tanveer "\"Everything seemed pretty normal for a while, we saw Maeve there, she had dinner and she went to sleep. Dr. Judge then went into the cellar.\"" 
    Tanveer "\"Then there was nothing for three hours. When he came back out of the cellar he looked different, we couldn't see him that closely, but he definitely looked different.\""
    Tanveer "\"And then, he went to the barbery chair, y'know the one that he has in the corner. He messed with it and then there was this trapdoor that opened underneath it and the chair descended slowly into, with some kind of mechanism.\"" 
    Tanveer "\"He jumped in after it and closed it behind himself.\""
    show bast smile
    Bast "\"Okay, so. We totally have to get in there, right?\""
    jump .postdebrief2
label .postdebrief2:
    Chauser "\"Right, here's what I'm thinking we should do.\""
    show chauser smile
    Chauser "\"That trapdoor under the barbery chair, that has to be leading to somewhere else. Maeve mentioned she heard voices from below, remember? I'm saying we go in a short while after the (Not) Dr. Judge goes into it.\""
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    m "\"And how are we supposed to get the trapdoor open?\""
    hide charlie
    show chauser neutral at left 
    show tanveer neutral at center 
    show bast neutral at right
    Chauser "\"...We can figure that out when we get there.\""
    Tanveer "\"If we get there. We're going to have to be careful. Oh and, no more splitting up. We're doing the rest of this together.\""
    Bast "\"Agreed, I'm feeling like we may be getting into some more dangerous waters here.\""
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    "A shiver runs across your shoulders and down your back. This was no longer a little anti-establishment, mystery-loving club." 
    "This was doing things. Nothing before last night was technically illegal (the staking out could be maybe taken as loitering or trespassing, but eh, who's counting)." 
    m "\"I guess I'll be the one to point out that from here on out, this is officially meddling in an ongoing police investigation.\"" 
    m "\"If we go through with this, that'll count as breaking and entering, and if we get caught...\""
    hide charlie
    show chauser neutral at left 
    show tanveer neutral at center 
    show bast smile at right
    "You shrug. Tanveer, Chauser, and Bast share a brief look before nodding."
    Bast "\"Technically, if we do this right, there *should* be no breaking.\""
    Bast "\"Entering? Absolutely.\""
    Bast "\"But if we're worth our salt - no breaking.\""
    Tanveer "\"Tonight, then?\""
    Chauser "\"I don't see any point in putting it off.\""
    stop music fadeout 1.0
    play music "audio/bgm_city.mp3" fadein 1.0
    scene bg cityeve with dissolve
    "That night, after dusk."
    "You and your friends meet up near Dr. Judge's office. The lights are on but peeking into the window you see that (Not) Dr. Judge has already gone underneath."
    show charlie neutral at left with easeinright
    m "\"Alright, what's our plan?\""
    hide charlie
    show chauser neutral at left with easeinright
    show tanveer neutral at center with easeinright
    show bast smile at right with easeinright
    Tanveer "\"I think I can get the windows to open, it shouldn't require anything to be broken.\""
    Chauser "\"Okay but before we go, everyone make sure you're armed. We won't be able to fight them properly, but maybe we can slow them down.\""
    Bast "\"Hold on, we're trying to fight them?\""
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    m "\"No, not trying. But Chauser's right, we should be prepared in case we have to do an expeditious retreat the hell out of there.\""
    "You, Bast, and Tanveer take on a few more daggers, a bottle of oil, and some thorns to throw on the ground."
    hide charlie
    show chauser neutral at left 
    show tanveer neutral at center 
    show bast neutral at right 
    "The four of you creep towards the windows. Chauser and Bast keeping her steady as she stands on their shoulders to work. You keep watch as Tanveer works."
    Tanveer "\"Okay, got it!\""
    scene bg officenight with dissolve
    "She pushes the window, and it swings open. Chauser and Bast prop her, and then you up and through the window."
    "You help Bast through with Tanveer, Chauser propelling him from below. Finally, Chauser jumps for the window, you and Bast catching her arms as she climbs through."
    show chauser neutral at left with easeinright
    show tanveer neutral at center with easeinright
    show bast neutral at right with easeinright
    "Tanveer is already moving towards the trap door. The door was metal and it would take some greater effort to figure out."
    hide tanveer
    hide chauser
    hide bast
    show charlie neutral at left
    m "Hold on, let me try this one. I have an idea. You three, stand watch."
    "You put your ear to the door and touch in with your magic."
    "That's what you're here to study after all, let's see if it's been any use."
    menu:
        "Roll":
            $ roll = random.randint(1,20)
            "Your roll is [roll]."
    if roll <= 10:
        show charlie frown
        "You can feel your control of your magic has gotten better, but you can't figure out this lock."
        show charlie neutral 
        "You sit up, frustrated. But you remember that (Not) Dr. Judge had pressed something around the counter."
        menu:
            "Roll":
                $ roll = random.randint(1,20)
                "Your roll is [roll]."
        if roll <= 10:
            show charlie frown
            "In your stress, you can't seem to figure out what he did." 
            "You shrug at your friends. Bast shrugs back and with his full strength kicks in the metal trapdoor."
            show bast grin at right
            "A resounding clang echoes throughout, for a tense minute, nobody moves a muscle." 
            hide charlie 
            hide bast
            show chauser frown at left
            show tanveer frown at center
            "Tanveer looks disappointed at you and Bast, and Chauser looks stressed."
        else:
            play sound "audio/sfx_clue_found.wav"
            "After some looking, you find the hidden button that (Not) Dr. Judge pressed, and with a breath, push it." 
            show charlie smile
            "The trapdoor opens up and you and your friends stand around it."
    else:
        show charlie smile
        play sound "audio/sfx_clue_found.wav"
        "You smile as you feel your magic weave through the inner mechanisms of the door, you instinctively know where to press to get the lock to shift and slowly, it unlocks, and swings open silently."
    stop music fadeout 1.0
    play music "audio/bgm_dungeon_creepy.mp3" fadein 1.0
    play sound "audio/sfx_water_in_cave.wav" #let's see if this works
    scene bg tunnel with dissolve
    "You jump down first, into the darkness." 
    show charlie neutral at left with easeinright
    "You land next to the barbery chair. As everyone, one by one, hops down, you look around." 
    "From the small amount of light coming from the office above, you turn around in a circle slowly. The four of you were in a sort of room, completely underground given the raw earth." 
    show charlie scared
    "Around you is five different tunnel entrances, each leading into complete darkness. With dread, you realize that you recognize this place." 
    "It's the same place from your dreams." 
    "Above you, the trapdoor automatically closes plunging the four of you into complete darkness." 
    show chauser frown at center with easeinright
    "You cry out in surprise before slapping a hand over your mouth. Next to you, Chauser ignites a small flame in her hand and you see everyone staring at you with concern." 
    "You shake your head, you'll explain later." 
    hide charlie
    show bast neutral at right with easeinright
    Bast "\"So.. where do we start?\""
    scene black
    "ATTENTION: From here on, the game can get a bit gory.. warning for descriptions and/or images of blood and severed heads."
default tunnel_menu = set()
$ tunnel_count = 0
label tunnels:
    scene bg tunnel with fade
    if tunnel_count > 1:
        show charlie neutral at left
        "You turn around to look at the other tunnels. In for a penny, in for a pound. You had to keep going."
        hide charlie
    menu:
        set tunnel_menu
        "Sinister Tunnel":
            jump eviljudge
        "Eerie Tunnel":
            jump heads
        "Uncanny Tunnel":
            jump realjudge
        "Mysterious Tunnel":
            jump tabaxi
label eviljudge:
    show chauser neutral at left with easeinright
    "You go into the tunnel with Chauser at the lead, holding out her flame to see.."
    show tanveer neutral at center with easeinright
    show bast neutral at right with easeinright
    scene bg eviloffice with dissolve
    "You walk and walk until a pale light is seen up ahead. Chauser puts out her flame, and by the light ahead, the four of you creep up." 
    "Looking out of the tunnel you see a replica of Dr. Judge's office. The only difference is that it's covered in blood." 
    show bast scared at right
    show tanveer scared at center
    show chauser scared at left
    "Tanveer and Chauser are frozen.. but they're not looking at the blood the way Bast is. Following their gaze, you see (Not) Dr. Judge." 
    hide tanveer
    hide chauser
    hide bast
    show bjudge neutral at left with easeinleft
    play sound "audio/sfx_humming.wav"
    "He is currently turned away from the entrance, humming to himself quietly."
    "You slowly creep backwards, pulling on Bast's arm gently. Tanveer and Chauser creep back as well."
    menu:
        "Roll":
            $ roll = random.randint(1,20)
            "Your roll is [roll]."
    if roll <= 10:
        "You step backwards onto wet mud, your foot slips from underneath you and your knee drives into the ground, hard." 
        show bjudge frown
        stop sound
        stop music
        "The sound reverberates through the tunnel and (Not) Dr. Judge turns around sharply."
        show bjudge smile
        "He cocks his head and grins."
        BJudge "\"Oh my my! New patients! Come on in!\""
        "No one moves for a tense second." 
        "You turn and run, bolting as fast as you can." 
        "You hear your friends following from behind you."
        BJudge "\"Aw, are you scared. Don't worry, this won't hurt... *a bit*\""
        hide bjudge
        "You hear his laugh, and he scrabbles into the tunnel after your and your friends."
        scene black
        play music "audio/bgm_chase.wav"
        jump .gotcaught
    elif roll <= 15:
        "The four of you slowly creep backwards, not daring to turn your backs to the unsuspecting and humming (Not) Dr. Judge." 
        scene black
        show charlie scared at left 
        "About a third of the way into the tunnel, the light coming from the (not) doctor's office has grown smaller, you step backwards onto wet mud." 
        "Your foot slips out from behind you, and your knee hits the ground hard. The sound reverberates through the tunnel."
        stop sound
        "From up ahead you hear (Not) Dr. Judge go silent." 
        "He steps towards the tunnel entrance." 
        "Nobody moves a muscle, hoping against hope that the darkness covers you enough."
        hide charlie
        play music "audio/bgm_horror_spooky.mp3" fadein 1.0
        "You press your eyes close and duck your head." 
        "Darkness all around you, cold seeping into your bones." 
        play sound "audio/sfx_heartbeat.wav"
        "The smell and feel of wet mud fill your senses. And your heartbeat. You will it slow down, but it picks up and up." 
        "For the first time you find yourself wishing this was one of your nightmares." 
        "You'll just wake up in a second, in your room or on your desk. You'll be cold but you'll warm up after you drink some coffee and go out into the sun for a bit."
        "But that doesn't happen." 
        "Your heartbeat gets louder and louder, and cold seeps deeper and deeper and you don't wake up." 
        "This is real." 
        play sound "audio/sfx_breathing.wav"
        "This is happening to you now and you can't run away from it." 
        "A hand on your shoulder almost makes you scream, before you realize that it's warm." 
        "You open your eyes and they take a second to adjust to the darkness."
        stop music fadeout 1.0
        show chauser smile at left with easeinright
        show tanveer smile at center with easeinright
        show bast smile at right with easeinright
        play music "audio/sfx_water_in_cave.wav"
        "Bast is crouched next to you, with Tanveer and Chauser standing in front of you looking concerned." 
        "With Bast's help, you right yourself. Your heartbeat slows and (Not) Dr. Judge's humming can be heard eerily lilting back to you." 
        "You look to your friends, they each have a hand on you, either on your shoulder or on your back." 
        "You didn't realize you were shaking, but you turn around, and with their warmth and strength, walk back the rest of the way."
        play music "audio/bgm_dungeon_creepy.mp3" fadein 1.0
        scene black
    else:
        "The four of you creep backwards." 
        "With one mind and even movement, methodically, silently, all of you creep away from the humming and away from the (not) doctor's office." 
        scene black
        "Halfway through, you finally have the courage to turn your backs and move a bit faster. Chauser lights her flame again, and takes to the front." 
        show charlie neutral at left
        show chauser neutral at center
        "You follow and focus in on that little bit of flame, pushing back the darkness and the cold all by it's self..."
        scene black
label .posteviljudge:
    scene bg tunnel with dissolve
    show charlie scared at left
    "You emerge into the main area shaken, everyone looks to you concerned but you ignore them."
    hide charlie
    show chauser scared at left 
    show tanveer scared at center 
    show bast scared at right 
    "Everyone stays silent...too afraid to say anything quite yet."
    $ tunnel_menu.add("Sinister Tunnel")
    $ tunnel_count += 1
    if tunnel_count == 4:
        jump bossmonologue
    else:
        jump tunnels

default haveFought2 = True
default haveEvade2 = False
default evasion_check2 = 0
label .gotcaught:
    "You got caught by (Not) Dr. Judge! You all run for it, readying your weapons and traps!"
    menu: 
        "RUN":
            $ haveFought2 = True
            $ run = random.randint(1,20)
            if run <= 10:
                "Your roll is [run] :(."
                "The four of you run into the darkness, without proper light and wet mud, your friends stumble and slip."
                show bjudge smile at left with easeinright
                BJudge "\"Oh calm down, it's just a check up!\""
                hide bjudge
                $ evasion_check2 -= 1
                jump .gotcaught
            else:
                "You roll is [run] :)."
                "You and your friends run as a group, feet beating against the mud as your legs take you farther."
                $ evasion_check2 += 1
                if evasion_check2 == 2:
                    $ haveEvade2 = True
                if haveEvade2 == True:
                    stop music fadeout 1.0
                    jump .posteviljudge
                jump .gotcaught
        "FIGHT" if [haveFought2]:
            $ haveFought2 = False
            "A dagger is thrown at (Not) Dr. Judge!"
            show bjudge frown at left with easeinright
            "You don't stop to see what happens, but you hear him hiss in pain."
            hide bjudge
            $ evasion_check2 += 1
            if evasion_check2 == 2:
                $ haveEvade2 = True
            if haveEvade2 == True:
                stop music fadeout 1.0
                jump .posteviljudge
            jump .gotcaught
        "DISRUPT" if [haveFought2]:
            $ haveFought2 = False
            $ disrupt = random.randint(1,2)
            if disrupt == 1:
                "A bottle of oil is thrown behind you guys, you hear it break." 
                show bjudge frown at left with easeinright
                "You don't look behind you but you hear (Not) Dr. Judge yell in frustration."
                hide bjudge
            else:
                show bjudge frown at left with easeinright
                "Thorns are thrown behind you. You hear (Not) Dr. Judge hiss in pain and frustration."
                hide bjudge
            $ evasion_check2 += 1
            if evasion_check2 == 2:
                $ haveEvade2 = True
            if haveEvade2 == True:
                stop music fadeout 1.0
                jump .posteviljudge
            jump .gotcaught
label heads:
    show chauser neutral at left with easeinright
    "You go into the tunnel with Chauser at the lead, holding out her flame to see..."
    stop music fadeout 1.0
    scene bg skulls with fade
    "As you approach, you enter a small room."
    play music "audio/bgm_horror_spooky.mp3" fadein 1.0
    show chauser scared at left with easeinright
    show tanveer scared at center with easeinright
    show bast scared at right with easeinright
    "Heads. Severed heads. Of students, adults, *kids*." 
    "Some you recognize from the newspapers. The missing people." 
    "Shelves and shelves of them. Floating, preserved in jars." 
    "So many." 
    "Too many."
    scene bg skulls
    show charlie scared at left
    "You tear your eyes away from them and look to the center of the room." 
    show charlie neutral
    "Sitting on a table are empty jars, waiting to be filled." 
    show charlie frown
    "So they weren't done yet. Whoever was doing this, they had no plans on slowing down."
    hide charlie
    show chauser frown at left
    show tanveer angry at center
    show bast frown at right
    Bast "\"There's no way of doing this without telling the police.\""
    Tanveer "\"How in the actual hell have they not found any of this yet? This is way more than just a few!\""
    Chauser "\"Maybe.. maybe they do know...maybe they were playing it down on purpose\""
    hide chauser
    hide tanveer
    hide bast
    show charlie frown at left
    m "\"C'mon let's get out of here, there's nothing we can do for them now except to keep going.\""
    scene bg skulls
    stop music fadeout 1.0
    play music "audio/bgm_dungeon_creepy.mp3" fadein 1.0
    play sound "audio/sfx_water_in_cave.wav"
    "You return to the main area, walking in stunned silence."
    scene bg tunnel with fade
    show bast frown at right 
    "Bast looks like he may throw up, but he'll be okay." 
    show charlie frown at left
    "You're still thinking about the police. He was right, there was no way to continue after you all got out of here without letting the police know."
    hide bast
    hide charlie with fade
    $ tunnel_menu.add("Eerie Tunnel")
    $ tunnel_count += 1
    if tunnel_count == 4:
        jump bossmonologue
    else:
        jump tunnels
label realjudge:
    show chauser neutral at left with easeinright
    "You go into the tunnel with Chauser at the lead, holding out her flame to see..."
    scene bg prison with fade
    "You enter an open area, with grates on the ground. Torches line the wall with some ropes laying around." 
    "As you approach them closer you realize what they are...oubliettes." 
    "This must be an area where... whoever...keeps their victims before killing them. Theress many. Looking into the one nearest to you, you see that itss dark and empty." 
    "A voice calls from further down." 
    show chauser neutral at left with easeinright
    show tanveer scared at center with easeinright
    show bast frown at right with easeinright
    "Unknown" "\"Hello?\""
    "Silence. The voice sounded rough."
    "Unknown" "\"What do you want from me?! Please, just let me know! I can work off the debt, I swear!\""
    show tanveer neutral
    "Tanveer puts a finger to her lips signaling everyone to stay quiet. She walks forward towards where the voice was coming from, everyone follows close behind."
    "As she approaches you all look down and you see..."
    hide chauser
    hide tanveer
    hide bast
    show ojudge scared at left with fade
    show bast smile at center with easeinright
    Bast "\"Dr. Judge!\""
    show tanveer frown at right with easeinright
    Tanveer "\"Shhh!\""
    Bast "*quieter* \"Dr. Judge?\""
    show ojudge neutral
    OJudge "\"Huh? You're not...her.\"" 
    show ojudge smile
    OJudge "\"Quick! Kids! Help me out of here, there's some rope you can grab, throw it down and I can climb it!\""
    hide ojudge
    hide tanveer
    hide bast
    show charlie neutral at left
    "You move to comply, remembering the rope you saw earlier before Chasuer grabs your arm."
    show chauser frown at center
    Chauser "\"Wait, how do we know we can trust you?\""
    hide chauser
    hide charlie
    show ojudge frown at left
    OJudge "\"Well, how do *I* know I can trust *you*? You're not working with her are you?\""
    hide ojudge
    show charlie frown at left
    m "\"Working with her? We don't even know who 'her' is! How do we know that you're not on her side?\""
    hide charlie
    show ojudge neutral at left
    OJudge "\"I wouldn't be down here, would I?\""
    OJudge "\"Listen, I'll explain everything, but we need to get out of here!\""
    hide ojudge
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    Bast "\"I don't know how useful this conversation is, honestly, we ought to just try. Whatever happens, happens.\""
    hide chauser
    hide tanveer
    hide bast
    show charlie neutral at left
    "Chauser and Tanveer don't look so sure, but you don't have much time." 
    "You make the decision, grab the rope, and throw it down to Doctor Judge." 
    hide charlie
    show ojudge neutral at left
    "Once you've pulled him up, he dusts himself off and gives you a smile. No metal tooth. But also no strange complexion." 
    hide ojudge
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    Tanveer "\"How many Doctor Judges' are there??\""
    hide chauser
    hide tanveer
    hide bast
    show ojudge frown at center
    OJudge "\"What a concerning thing to say to a man, I'm going to ignore that for the time being just for my own sanity.\""
    "You all share a look. He doesn't know then." 
    show charlie neutral at left
    m "\"How long have you been down here?\""
    OJudge "\"Can't tell. It's been a while because I know I reek. But, obviously, no sun. And the meals are inconsistent, so I can't tell how many days have passed.\""
    show charlie frown
    "*You* know though, it's been at least a few months." 
    "Mr. Oluwande and Maeve both reported that metal tooth as having been there for a while, as if it was old news." 
    hide charlie
    hide judge
    show bast neutral at right
    Bast "\"We'll get your home to your daughter, sir, we promise.\""
    hide bast
    show charlie smile at left
    "You're not sure how smart it is to promise something like that but you try to give a reassuring smile."
    show ojudge smile at center
    OJudge "\"You know my daughter! Is she okay?\""
    show charlie neutral
    m "\"She's doing alright, she's safe if a bit sad.\""
    show ojudge neutral
    OJudge "\"Who's taking care of her?\""
    hide ojudge
    hide charlie
    show chauser frown at left
    Chauser "\"Uh..\""
    show tanveer frown at center
    Tanveer "\"Hm..\""
    show bast frown at right
    Bast "\"...\""
    hide chauser
    hide tanveer
    hide bast
    show charlie neutral at left
    m "\"Well, uh... you are.\""
    hide charlie
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    "Everyone turns sharply to look at you, they wanted tact but you know there's no time for tact right now."
    hide chauser
    hide tanveer
    hide bast
    show charlie neutral at left
    m "\"As I said, she's safe but sad. She knows it's not the real you. Which is why we really need to figure out what's going on here.\"" 
    show ojudge frown at center
    m "\"Will you help us?\""
    show ojudge neutral
    OJudge "\"Yeah. Yes. I can. I can help.\"" 
    show ojudge frown
    OJudge "\"What did you mean that I'm taking care of her?\""
    m "\"Honestly? I'm not entirely sure.\""
    OJudge "\"That's not very comforting.\"" 
    show ojudge neutral
    OJudge "\"Okay. Okay, let's do this.\""
    hide ojudge
    "You gather some of the other rope and hand it around, it could prove to be useful."
    scene bg tunnel with dissolve
    "When you return to the main area, Doctor Judge looks around." 
    show ojudge neutral at left with easeinright
    OJudge "\"I'll stay here, I think.\""
    show tanveer smile at right with easeinright
    Tanveer "\"Good idea, you've been through a lot. We'll try our best to be quick.\""
    show ojudge smile
    scene black
    $ tunnel_menu.add("Uncanny Tunnel")
    $ tunnel_count += 1
    if tunnel_count == 4:
        jump bossmonologue
    else:
        jump tunnels
label tabaxi:
    show chauser neutral at left with easeinright
    "You go into the tunnel with Chauser at the lead, holding out her flame to see..."
    scene bg prison with fade
    "You enter an open area, with grates on the ground. Torches line the wall with some ropes laying around." 
    "As you approach them closer you realize what they are... oubliettes." 
    "This must be an area where...whoever...keeps their victims before killing them. There's many." 
    "Looking into the one nearest to you, you see that it's dark and empty." 
    "A voice calls from further down." 
    "Unknown" "\"What, finally decided to kill me?\""
    show chauser neutral at left with easeinright
    show tanveer scared at center with easeinright
    show bast frown at right with easeinright
    "Silence. The voice sounded somewhat scratchy."
    "Unknown" "\"Hahha, I don't have any more information to give you. If you don't kill me, I swear I'll kill you, Nora!\""
    show tanveer neutral
    "Tanveer puts a finger to her lips signaling everyone to stay quiet. She walks forward towards where the voice was coming from, everyone follows close behind."
    hide chauser
    hide tanveer
    hide bast
    show wave neutral at left with easeinright
    "As she approaches you all look down and you see an orange tabaxi woman. Her clothing would indicate that she was a mage-sailor, but they were dirty." 
    show wave smile
    "Her piercing green eyes started back up at you all.. squinting in confusion."
    hide wave
    show chauser frown at left
    show tanveer neutral at center
    show bast smile at right
    Chauser "\"Are you friend or foe?\""
    hide chauser 
    hide tanveer
    hide bast
    show wave neutral at left
    "Unknown" "\"You first. Are you with Nora?\""
    hide wave
    show chauser neutral at left
    show tanveer frown at center
    show bast smile at right
    Tanveer "\"Let's start off with: who's Nora?\""
    hide chauser 
    hide tanveer
    hide bast
    show wave neutral at left
    "Unknown" "\"How did you get down here without knowing who she is, or even without having met her?\""
    hide wave
    show charlie neutral at left
    "So this 'her' that keeps being mentioned.. perhaps that is Nora."
    m "\"If we save you, you promise not to kill us?\""
    hide charlie
    show wave neutral at left
    "Unknown" "\"As long as you promise not to kill me!\""
    hide wave
    show chauser neutral at left
    show tanveer neutral at center
    show bast smile at right
    Bast "\"Easy enough, let's get her up here.\""
    hide chauser 
    hide tanveer
    hide bast
    show wave neutral at left with fade
    "Using the ropes you saw earlier you throw it down to the tabaxi, she climbs easily, pulling herself up. She bows."
    Wave "\"My name is Wave on the Shore. You may call me Wave.\""
    hide wave
    show chauser neutral at left
    show tanveer neutral at center
    show bast smile at right
    "Everyone else introduces themselves."
    Tanveer "\"What do you have to do with all of this, I haven't seen your face on the missing papers yet.\""
    hide chauser 
    hide tanveer
    hide bast
    show wave neutral at left
    Wave "\"Ah, well Nora's had me for a while now. It's good to be free.\""
    hide wave
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    Chauser "\"Not to insult you or anything, but how have you not gotten free yet, if it was this easy?.\""
    hide chauser 
    hide tanveer
    hide bast
    show wave neutral at left
    "At this, Wave holds up her hands and you all see glowing cuffs on her."
    Wave "\"These weigh me down and take away my ability to spell cast. Which means the only way I could get out of here was to find someone that was alive and willing to help me.\"" 
    Wave "\"Nora rarely lets kids live long after she takes them, let alone lets anyone walk free.\""
    show wave smile
    Wave "\"You must be masterminds that have been planning this for months at least to be able to know when she was out hunting..\""
    show wave neutral
    Wave "\"How you did that without even knowing who she was must've been difficult...\""
    show wave smile
    Wave "\"Masterminds indeed.\""
    hide wave
    show chauser scared at left
    show tanveer scared at center
    show bast scared at right
    "You are all silent for a moment, giving yourself a second to allow the reality of just how reckless it was going down here without really telling anyone." 
    hide chauser
    hide tanveer
    hide bast
    show charlie neutral at left
    "Wordlessly you move forward and using a simple dispel magic works on the cuffs, they fall to the ground, useless." 
    hide charlie
    show wave neutral at left
    "Wave picks them up and pockets them."
    Wave "\"What's wrong?\""
    hide wave
    show chauser neutral at left
    show tanveer neutral at center
    show bast neutral at right
    Tanveer "\"Let's go, we need to stop her and get out of here.\""
    hide chauser 
    hide tanveer
    hide bast
    show wave neutral at left
    Wave "\"I like your confidence! And your optimism!\"" 
    show wave smile
    Wave "\"You all truly must be much stronger and intelligent than you look!\""
    hide wave
    show chauser neutral at left
    show tanveer neutral at center
    show bast frown at right
    "Bast winces but doesn't correct her, it was an insult, but not one he could say anything about."
    hide chauser
    hide tanveer
    hide bast
    show charlie neutral at left
    "You gather some of the other rope and hand it around, it could prove to be useful."
    scene bg tunnel with dissolve
    "When you return to the main area, Wave looks around."
    show wave neutral at left with easeinright 
    Wave "\"I'll stay here, I think.\""
    show tanveer smile at center with easeinright
    Tanveer "\"Good idea, you've been through a lot. We'll try our best to be quick.\""
    Wave "\"I'll be keeping a lookout.\""
    scene black
    $ tunnel_menu.add("Mysterious Tunnel")
    $ tunnel_count += 1
    if tunnel_count == 4:
        jump bossmonologue
    else:
        jump tunnels
label bossmonologue:
    scene bg tunnel with fade
    show charlie neutral at left with easeinright
    stop music fadeout 1.0
    play sound "audio/sfx_cackle.wav"
    "Laughter echoes from the tunnels. Wicked and creeping laughter." 
    show charlie scared
    play music "audio/bgm_horror_spooky.mp3" fadein 1.0
    "Laughter you recognize from your dream."
    show wave scared at center with easeinright
    Wave "\"Ah, she's back.\""
    "She unsheathes her claws."
    show ojudge scared at right with easeinright
    "Doctor Judge doesn't say anything, the terror in his eyes is enough."
    hide charlie
    hide wave
    hide ojudge
    "From one of the tunnels, a woman, Nora, emerges. She looked human enough, dark hair as the informant had said. Her smile showed a full set of iron teeth." 
    "Nora" "\"So you're the runts that have been meddling. Honestly, it's been quite a bit of fun all of this.\""
    "Her smile drops suddenly."
    "Nora" "\"But it's starting to become quite meddlesome. I think that's enough of that.\""
    "She raises her hand, and her glamour drops."
    show nora grin at center with easeinbottom
    "Where there once stood a human woman, now stood a 10 foot tall fae. Gone were her iron teeth, now replaced with a predatorial grin."
    Nora "\"My name is Noraprashna. I am a collector. I am a curator. I am The Corruptor.\"" 
    Nora "\"I want Silverymoon to *fall*. And you children, while you were fun to mess with,\""
    "At this, she stares directly at you. That cold creeps back in."
    show charlie scared at left with easeinleft 
    "You want nothing more than to die in this moment."
    hide charlie with easeoutleft
    Nora "\"you will not stop me. I will feast on the bodies of the children. I will bathe in the blood of the citizens. I will do what is required to prove that *I* am superior.\"" 
    Nora "\"You see what I did to the beloved Doctor! And no one knew! Nobody even suspected!\""
    hide nora
    show charlie scared at left
    scene black
    stop music fadeout 1.0
    "That's not true." 
    "Maeve suspected. You all suspected." 
    show charlie frown
    "The fear has started to give away now to something else. Something you haven't ever felt truly. Anger." 
    show charlie angry
    "How *dare* she hurt the innocent." 
    "How *dare* she assume that she's superior." 
    "How *dare* she torment you." 
    "How *dare* she underestimate you." 
    "And you know." 
    "You know that she knows nothing of true power, she knows nothing of love, and she knows nothing of warmth." 
    "All she wants is to take it away. You'd sooner freeze in hell than let that happen." 
    hide charlie
label prefight:
    show nora grin at center
    Nora "\"I will replace everyone with my minions and this shall be my base! I will-\""
    hide nora
    show charlie smile at left
    m "\"Nah.\""
    hide charlie
    show nora neutral at center
    Nora "\"'Nah?' What do you-\""
    show nora frown
    "You throw a dagger at her and it catches her in the shoulder." 
    "Everyone stares at it for a second, and watches it ease back out as she heals herself." 
    hide nora
    show charlie neutral at left
    "You weren't going to kill her. But maybe.. maybe you could trap her." 
    hide charlie
    play music "audio/bgm_finalbattle.mp3" fadein 1.0
    show nora grin
    Nora "\"Fine. Have it your way. I'll enjoy killing you all!\""
$ success_check = 0
$ failure_check = 0
$ hits = {"Bast":0, "Tanveer":0, "Chauser":0, "Wave":0, "Judge":0}
$ char_list = ['Bast', 'Tanveer', 'Chauser', 'Wave', 'Judge']
label bossfight:
    "There's nowhere to run. It's time to fight!"
    menu:
        "FIGHT":
            $ fight = random.randint(1,20)
            if fight <= 10:
                $ failure_check += 1
                if success_check > failure_check:
                    play sound "audio/sfx_cackle.wav"
                    "Noraprashna shakes off some rope!"
                $ success_check -= 1
                $ someone = random.choice((char_list))
                $ hits[someone] += 1 
                "Fail! Noraprashna lashes out!"
                "[someone] takes a hit!"
                if hits[someone] == 3:
                    jump prefight
                jump bossfight
            elif fight <= 15:
                "Success!"
                $ success_check += 1
                jump successdialogue
            else:
                if success_check == 4:
                    $ success_check += 1
                else:
                    $ success_check += 2
                "Double Success!"
                jump successdialogue
                
label successdialogue:
    if success_check == 1:
        show charlie angry at left with easeinleft
        "Using your rope you grapple Nora's hand!"
        show nora grin
        hide charlie with easeoutleft
    elif success_check == 2:
        show bast smile at left with easeinleft
        "Bast, catching onto what you're doing, grapples her other hand!"
        show nora smile
        hide bast with easeoutleft
    elif success_check == 3:
        show chauser smile at left with easeinleft
        "Chauser throws her rope around Noraprashna's mouth, silencing the fae hag's casting!"
        show nora neutral
        hide chauser with easeoutleft
    elif success_check == 4:
        show tanveer smile at left with easeinleft
        show ojudge scared at right with easeinright
        "Tanveer and Doctor Judge get the cue and grapple Nora around her legs! Everyone is concerningly proficient with lassos in this city!"
        show nora frown
        hide tanveer with easeoutleft
        hide ojudge with easeoutright
    else:
        show wave neutral at left with easeinleft
        "Wave rushes forward and slaps the manacles on Noraprashna's wrists, with everyone holding on, she casts the spells on the manacles to stem the wicked fae's magic!"
        show nora defeat
        show wave smile
        hide wave with fade
        jump postfight
    jump bossfight
label postfight:
    stop music fadeout 1.0
    play music "audio/bgm_city.mp3" fadein 1.0
    scene bg tunnel with fade
    show nora defeat
    "The cavern is filled with Noraprashna's muffled screams. She writhes against the ropes but you all hold steady. Now that she was without her magic it was clear that she wasn't all that physically strong."
    hide nora with easeoutbottom
    show wave smile at left with easeinright
    Wave "\"Hah! Retribution! Good job, I had complete faith in you kids! I knew you had a plan!\""
    hide wave
    show chauser smile at left with easeinright
    show tanveer smile at center with easeinright
    show bast grin at right with easeinright
    "Your friends look towards you in silent gratitude of thinking on your feet." 
    hide chauser
    hide tanveer
    hide bast
    show charlie scared at left with easeinright
    "You shake knowing that there was a strong possibility there that you would have all died and that rope thing would most definitely not have worked."
    show charlie neutral
    show ojudge neutral at center with easeinright
    OJudge "\"Let's get out of here. Please.\""
    hide charlie
    hide ojudge
    show nora defeat at center with easeinbottom
    "You nod, and with all of you working together you secure Noraprashna." 
    show wave neutral at right
    "At some point Wave just knocks her out with a swift punch to the face." 
    hide nora with easeoutbottom
    Wave "\"Hey listen kids, let me and the good Doc here deal with the cops. You folks get home and get some sleep. You look like you need it.\""
    show ojudge neutral at center
    "Doctor Judge nods."
    OJudge "\"Yeah, I'm sure there's a way we can spin this so that you lot don't get in trouble.\""
    hide wave
    hide ojudge
    show chauser grin at center
    Chauser "\"Thank you, so much.\""
    hide chauser
    show ojudge smile at center
    "Doctor Judge looks like he might cry tears of joy."
    OJudge "\"No, no, thank *you*. You kids saved my life. This is the least I can do. I will forever be in your debt.\"" 
    OJudge "\"Because of you, I will finally be able to see Maeve again.\""
    show wave smile at right
    Wave "\"Yes, thanks to your incredible work I am free once again to sail the seas. I will never forget this kindness as long as I live. If you ever need my help, simply use this I will come to your aid as soon as I can.\""
    "Wave hands you all a small disk the size of a large coin." 
    hide wave
    hide ojudge
    show bast grin at right
    Bast "\"Of course, we couldn't let this just go to rest. People were in danger, we can't let that pass.\""
    hide bast
    show ojudge smile at center
    OJudge "\"Stay safe, kids. Okay run along home now.\""
    hide ojudge
    show charlie neutral at left
    m "\"Wait.\"" 
    m "\"I hate to be the one to do this...but what happened to the (Not) Dr. Judge that we found?\""
    hide charlie
    show ojudge scared at center
    OJudge "\"What? You had found one? In here?\""
    hide ojudge
    show tanveer frown
    "Tanveer curses."
    show tanveer neutral
    Tanveer "\"We need to get out of here, we can let the police deal with him.\""
    hide tanveer
    show wave smile at right
    Wave "\"Yes, don't worry. I let you kids do most of the work just now because I knew you could handle it, but I'm pretty strong myself. Some random copy of the good Doctor won't defeat us.\""
    hide wave with fade
    "With that confidence given, you all leave the tunnels"
    stop music fadeout 1.0
    show charlie smile at left
    scene bg cityday with dissolve
    play music "audio/bgm_casual1.mp3" fadein 1.0
    "When you exit you see the sun starting to rise...you didn't realize how much time had passed while you were underneath there." 
    "You shiver, you never want to go back there again."
    show charlie neutral
    scene bg dormday with fade
    show charlie neutral
    "You all stumble on back to the dorms, take a much needed shower, and just as you're about to hit the bed you're thinking about skipping classes today. It's not like there's anything important..."
    show charlie scared
    "Crap. Hell. Shoot. Dammit. A cool panic comes over you." 
    "Your Final Project Presentation is today." 
    scene bg library with fade
    "You run to the library..."
    scene black
    stop music fadeout 1.0

    "EPILOGUE"
    "One week later..."
    
    play music "audio/bgm_hypepostfight.wav" fadein 1.0
    show charlie neutral at left with fade
    "You received your grade from the presentation, you got a solid B+. Not bad for it being thrown together at the crack of dawn after fighting some evil fae hag all night."
    "The newspapers hold some bittersweet news. The families of the dead were in mourning and there were services being held for them." 
    hide charlie with fade
    show nora defeat at center with fade
    show bjudge smile at right
    "Noraprashna was captured, but there was no mention of (Not) Dr. Judge." 
    "Talking to Wave, you learned that they did search for him, there was no trace left except for the bloody office." 
    "Once the police knew what to search for, they found a few of Noraprashna's creatures (like the one that gave chase) and took them in as well."
    "It seems as though Doctor Judge and Wave were able to keep your names out of the story anyways. Wave definitely exaggerated some things, but the narrative was believable enough." 
    hide nora
    hide bjudge with fade
    "Despite all this, though, people were definitely looking at you and your friends with some newfound respect." 
    show wave smile at left with fade
    "While Wave had kept your names out of the official papers, she was a sailor after all. And sailors loved their tales." 
    "She spread the news of four scrappy students who valiantly saved the town and solved the mystery using their wit and bravery."
    hide wave with fade
    show ojudge smile at left with fade
    show maeve smile at center with easeinright
    "Doctor Judge was finally reunited with his daughter. Maeve was a bit confused at first, but after everything was explained she was ecstatic." 
    show gjudge smile at right with easeinright
    "(The Other) Dr. Judge (the one with the tooth and was kinda out of it, remember?) was also confused. The tooth was no longer there, having fallen out once Noraprashna's magic was cut off." 
    "Him and Dr. Judge (the real one) decided that he could stay to help out and be a sort of uncle to Maeve." 
    "He was surprisingly calm about being told he was a copy, and did not at all get existential about it, which made everything easier for everyone."
    hide gjudge with easeoutright
    hide maeve with easeoutright
    hide ojudge with fade
    show chauser grin at left with fade
    show tanveer smile at center with easeinright
    "Chauser never let Tanveer doubt her ever again." 
    show chauser neutral
    show tanveer neutral
    show bast neutral at right with easeinright
    "There was an intervention from everyone to make you explain all that was happening to you. You give in and talk about your ongoing nightmares and the panic you felt earlier."
    hide chauser
    hide tanveer
    hide bast
    show charlie smile at left 
    "Though, you make sure to note, strangely enough, you haven't had any nightmares since the night in the tunnels."
    hide charlie with fade
    stop music fadeout 1.0

    "A month later..."

    play music "audio/bgm_chatter.mp3"
    scene bg cafe with fade
    "At a cafe..."
    show bast grin at right with fade
    Bast "\"I'm just saying! I think that if they were on the same horse, Sir Lewis would definitely beat Sir Maximillion!\""
    hide bast
    show charlie smile at left with easeinright
    m "\"No way! Just admit it, Sir Lewis is getting old, he had his time to shine, but he needs to move on! The younger jockeys are just more skilled!\""
    hide charlie
    show chauser smile at left with easeinright
    show tanveer smile at center with easeinright
    show bast smile at right with easeinright
    Chauser "\"It would definitely be interesting to see, but I'm not sure I can say this way or that.\""
    Tanveer "\"I can't believe that your newest interest are rich men on horses going around in circles.\""
    hide chauser
    hide tanveer
    hide bast
    show lady neutral at right with easeinleft
    "Unkown" "\"Um, excuse me, sorry to bother you?\""
    hide lady
    show chauser smile at left
    show tanveer neutral at center
    show bast smile at right
    Tanveer "\"Oh hello, yes? How can I help you?\""
    hide chauser
    hide tanveer
    hide bast
    show lady neutral at right
    Lady "\"Oh well...my name's Meredith and.. oh..\""
    show lady frown 
    Lady "\"My husband's gone missing.\""
    hide lady
    show chauser neutral at left
    show tanveer frown at center
    show bast neutral at right
    "Tanveer looks at everyone for a second." 
    Chauser "\"I'm so sorry ma'am...but what do you want us to do about it?\""
    hide chauser
    hide tanveer
    hide bast
    show lady frown at right
    Lady "\"Please! Please help, in any way you can.\"" 
    Lady "\"I went to the police but they won't do anything! I asked around and I was told to seek you out!\"" 
    Lady "\"Please..\""
    hide lady
    show chauser neutral at left
    show tanveer neutral at center
    show bast smile at right
    Bast "\"Ma'am please sit, it's okay. Alright...tell us everything.\""
    hide chauser
    hide tanveer
    hide bast
    show lady frown at right
    stop music fadeout 1.0
    "And as you all lean in you feel your hairs stand on end." 
    hide lady
    show charlie scared at left
    play sound "audio/sfx_heartbeat.wav"
    "So that nightmare last night...those nightmares...they do mean something..."
    scene black
    stop sound
    "THE END"
    
    play music "audio/bgm_endcredits.mp3" fadein 1.0
    "Credits!"
    "Story: Based on the free D&D module, \"The Barber of Silverymoon\", but heavily edited. Like 'is it even the same story at this point' edited."
    show charlie neutral at left with easeinright
    show chauser neutral at center with easeinright
    show bast at right with easeinright
    hide charlie with easeoutleft
    hide chauser with easeoutleft
    hide bast with easeoutleft
    show tanveer neutral at right with easeinleft
    show maeve neutral at center with easeinleft
    show mro neutral at left with easeinleft
    hide tanveer with easeoutright
    hide maeve with easeoutright
    hide mro with easeoutright
    show bjudge neutral at left with easeinbottom
    show gjudge neutral at center with easeinbottom
    show ojudge neutral at right with easeinbottom
    hide bjudge with easeouttop
    hide gjudge with easeoutop
    hide ojudge with easeoutop
    show wave neutral at left with easeintop
    show nora neutral at center with easeintop
    show cathasar neutral at right with easeintop
    hide cathasar with easeoutbottom
    show lady neutral at right with easeintop
    hide wave with easeoutbottom
    hide nora with easeoutbottom
    hide lady with easeoutbottom
    "Character Art: Me (Fatima Zaidi) please appreciate em thanks :)"
    scene bg skulls with fade
    "Specifically the heads in jars room: Me (Fatima Zaidi)"
    scene black with fade
    "Author: Me (Fatima Zaidi) please ignore the parts that don't make sense thanks :)"
    "Made using: Ren'py"
    "For legal reasons: The actions and decisions made by the characters are completely fictitious. I do not condone any of the illegal activities taken by these characters, nor do I condone skipping class. Stay in school kids and stay safe."
    "Images taken from Unsplash and Pinterest. Jez Timms for the tunnel main, Dylan Freedom for the city evening, Francesco Ungaro for the city night, M.R. for city day, Shalev Cohen for the garden, Elijah Lychik for the dorm, Hilderose C for Mr.Oluwande's shopfront, Museums of History New South Wales for dr's office"
    "Qui Nguyen for the tavern, RR Abrot for the cafe, Annie Spratt for the library, and Shelly the Countness for the oubilette room."
    "Background Editing (just a little): Me (Fatima Zaidi)(If that was still unclear)"
    "Audio from freesound.org. Horror spooky sound from UNIVERSFIELD, city music from Setuniman, heartbeat from newlocknew, breathing from drewsimko, water dripping in a cave by Sclolex, tavern from ralexpdx, clue found from paulnorthyorks, chase music from CollectionOfMemories, humming from 1Kaylin_Dickson, end credits music from M-Murray"
    "final battle from szegvari, post fight song from humanoide9000, garden music from szegvari."
    "Thank you for playing!"
    stop music fadeout 1.0


return
