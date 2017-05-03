name = raw_input("What do other people call you? ")
location = raw_input("Where do you live? ")
fears = raw_input("What are you so afraid of? ")

print "\n\nSo, your name is %r, you live in %r, and you're scared of %r." % (
    name, location, fears)
ans = raw_input("\nIs that correct? y/n ")
if ans == "y":
    print "\nYou're hiking in the woods when you come across a tower.  Do you enter?"
    print "\n1. Of course.  I enter."
    print "2. Definitely not.  I don't enter."
    tower = raw_input("\n1/2? ")

    if tower == "1":
        print "\nYou come across a mirror.  It is a reflection of %r.  What do you say to mirror %r?" % (
        name, name)
        print "\n1. Hey there, good looking!"
        print "2. You'll never do anything right or find peace financially."
        mirror = raw_input ("\n1/2? ")

        if mirror == "1":
            print "\nThe mirror opens up to reveal a staircase."
            print "\nYou climb the staircase to find an easel.  What do you draw?"
            print "\n1. An abstract representation of %r" % (
            fears)
            print "2. Nothing.  This is a waste of my time."
            easel = raw_input ("\n1/2? ")

            if easel == "1":
                print "\nA bird flies in through the window."
                print "It tells you that your art perfectly captures its own insecurities."
                print "\nYou feel slightly less alone.  A rope falls from the ceiling.  What do you do?"
                print "\n1. Ignore the rope and try to find a better way up."
                print "2. Climb the rope."
                rope = raw_input ("\n1/2? ")

                if rope == "1":
                    print "\nYou use your incredible intellect to find a secret door."
                    print "\nDo you open it?"
                    print "\n1. Of course.  I open the door."
                    print "2. Definitely not."
                    secret = raw_input ("\n1/2? ")

                    if secret == "1":
                        print "\nYou open the door to find someone using the toilet."
                        print "\nYou feel all embarrassed and run out.  You thought you were too good for the rope.  Oh well."
                    elif secret == "2":
                        print "\nYou do nothing, then."
                        print "\nI guess you're the kind of person who needs someone else to make decisions for you.  Oh well."

                elif rope == "2":
                    print "\nYou climb the rope and come out on the third floor.  It looks just like %r" % (
                    location)
                    print "\nHow do you feel?"
                    print "\n1. Angry.  I climbed all this way to get back where I started?"
                    print "2. Warm.  Seeing home reminds me of my friends and family."
                    print "3. Excited.  Think of the real estate possibilities."
                    home = raw_input ("\nHmm... 1/2/3? ")

                    if home == "1":
                        print "\nYou are angry to find home?"
                        print "\nThat's a little bit sad to hear."
                        print "Perhaps you should be looking for employment elsewhere instead of exploring a tower.  Oh well."
                    elif home == "2":
                        print "\nThinking of your friends and family, they all appear before you."
                        print "\nSlowly, they notice you, and run to embrace you."
                        print "Your mother says:"
                        print "\n\nStraighten your back or you'll grow like a gorilla."
                        print "\n\nHow do you respond?"
                        print "\n1. Remind her that you're an adult and done growing."
                        print "2. Ignore her and continue to embrace your friends."
                        speak = raw_input ("1/2? ")

                        if speak == "1":
                            print "\nSuddenly, the earth begins to shake."
                            print "\nAll of your friends and family slip down into the cracks and fall to the floor below."
                            print "Your mother, seeing your easel, screams from below:"
                            print "\n\nYou will never make a living from your art!"
                            print "\n\nSuddenly, the room is no longer false %r.  A beautiful enchantress descends from the top of the tower.  She speaks:" % (
                            location)
                            print "\n\nI can bestow upon you a great power.  But first, a test to show your true values."
                            print "\nWhich of these is the true scholar?"
                            print "\n\n1. The man who seeks inner peace."
                            print "2. The man who seeks inner truth."
                            print "3. The man who seeks his inner universe."
                            test = raw_input ("1/2/3? ")

                            if test == "1":
                                print "\nThe enchantress smiles down upon you."
                                print "She speaks:"
                                print "\n\nIt is true, the only way to truly understand anything at all is to accept that you understand nothing."
                                print "\nTo live with a tranquil mind and to find the freedom to laugh -- that is true wisdom!"
                                print "\nPlease accept this as a token of your accomplishments here today."
                                print "\n\n\nIt's a Denny's gift card."
                                print "\nWhat will you do with it?"
                                print "\n1. Use it for good - buy a few breakfast sandwiches for the homeless."
                                print "2. Use it for evil - break into a couple houses until the card snaps."
                                print "3. Use it for nothing - leave it in your back pocket until you notice it in the washing machine one day, expired."
                                end = raw_input ("1/2/3? ")

                                if end == "1":
                                    print "\nYou leave the tower and bring a bunch of breakfast sandwiches to the homeless shelter."
                                    print "You feel good about yourself for the rest of your life!"
                                    print "\nHowever, everyone else in your life seems like a disappointment compared to you."
                                    print "You sail the world hoping to find real connections, but nothing will ever feel quite as pure as the experiences from your childhood."
                                    print "\nYou live a long life but still die eventually.  Oh well."
                                elif end == "2":
                                    print "\nYou leave the tower and break into a bunch of strangers' houses, robbing them blind."
                                    print "You live surrounded with material comforts for the rest of your life!"
                                    print "\nHowever, you live your life completely in fear, wanting nothing more than to experience that same rush of adreneline."
                                    print "Your fear paralyzes you because even though you live your life on the edge, you still know you're too weak for prison."
                                    print "\nYou live a short life filled with gastrointestinal problems.  Oh well."
                                else:
                                    print "\nYou leave the tower, placing the gift card in your back pocket until you've already forgotten about it."
                                    print "You experience true contentedness for the rest of your life!"
                                    print "\nHowever, you'll always wonder if there isn't something that you're forgetting about, some entire life you've lived and blocked from your memory."
                                    print "Your distrust of yourself keeps you from experiencing true confidence, and you almost push yourself to forget to make the days feel easier."
                                    print "\nYou live forever, trapped in the cycles of forgetting, until eventually you forget even what you've forgotten."
                                    print "\nLucky you!"

                            elif test == "2":
                                print "\nThe enchantress laughs."
                                print "She speaks:"
                                print "\n\nThe truth?  Who can really actually see themselves for what they are.  Even the smartest people lie to themselves."
                                print "\nActually, especially the smartest people."
                                print "\nI really do wish you hadn't selected that answer.  I could have given you something really great.  Oh well."
                            else:
                                print "\nThe enchantress rolls her eyes."
                                print "She speaks:"
                                print "\n\nMy, you're a bit full of yourself, aren't you?  Or maybe someone just told you that it's more interesting to be complicated."
                                print "\nEither way, if you try too hard to construct ideas, you'll just miss out on the sincerity of life."
                                print "\nI really do wish you hadn't selected that answer.  I could have given you something really great.  Oh well."

                        if speak == "2":
                            print "\nYou embrace your friends and feel their warmth."
                            print "\nSlowly, you forget where you are and how far you have come."
                            print "\nYou forget your real friends, sitting back in real %r, drinking coffee and going to their jobs." % (location
                            )
                            print "You stay here forever, sustaining your delusions, never really questioning it because it's easier not to."
                            print "\nOh well."

                    else:
                        print "\nSo you're a bit of a capitalist then?"
                        print "\nThat's okay, though.  There is a housing crisis after all."
                        print "What do you build first?"
                        print "\n1. One giant home where all my friends can live together."
                        print "2. A shopping mall."
                        build = raw_input ("\n1/2? ")

                        if build == "1":
                            print "\nOne giant home for all of your friends?"
                            print "\nAre you crazy?  Your friends don't want to share a bathroom with you."
                            print "I guess you're not a very independent person.  Oh well."
                        elif build == "2":
                            print "\nA shopping mall?"
                            print "\nAre you crazy?  There's a whole huge world out there outside of Hollister and Hot Topic"
                            print "I guess you're kind of shallow.  Oh well."

            elif easel == "2":
                print "\nYou'll never fully comprehend your own passion or find love.  Oh well."

        elif mirror == "2":
            print "\nMirror %r opens its giant maw and devours you whole!  Oh well." % (
            name)

    if tower =="2":
        print "\nYou tell people you hike to find adventure, but that's not really true is it?"
        print "\nBut I guess you aren't a person very concerned with truths.  Oh well."

if ans == "n":
    print "\nYou don't seem to have a very tight grip on reality."
