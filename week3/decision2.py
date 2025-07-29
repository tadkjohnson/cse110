# few more lines, little longer story, few more choices. 
#my kids had fun with it,  only now they think i can make another one that is about pokemon characters.. 

print("You are the only child of a poor farmer, named after a legendary hero.  The town supplies have disappeared with a trail going into the forest.  The village need a volunteer to find out what happened to the supplies, so nobody dies this winter. ")
answer1 = input("do you VOLUNTEER? PUSH your neighbor forward? or be QUIET? ").lower()

# volunteer works 
if answer1 == "volunteer":
    print("You cautiously raise your hand to volunteer, the leaders quickly grab you and take you to the path by the forest")
    answer2 = input("do you HIKE up the path or RETREAT back to your house? ").lower()

    if answer2 == "hike":
        print("You hike up thru the forest a short distance to find a bridge over a deep chasm and on the other side a bandit army encamped.")
        answer3 = input("do you SNEAK into the camp, or DESTROY the bridge?").lower()

        if answer3 =="destroy":
            print("you destroy the bridge, at which time the bandits realize they can't continue that direction, they disappear in to the forest.")
        elif answer3 == "sneak":
            print("you sneak into the bandits camp, taking note of how many there are, their supplies, and notice all the cells, shackles, and traps they have stockpiled. ")
            answer4 = input("After geting all the information you can do you RETURN to town to warn them, start the stockpiles on FIRE, or quietly KILL the bandits? ").lower()
            if answer4 == "return":
                print("you return to town and warn them of what you saw.  They call in the army and destory the bandit army.")
            elif answer4 == "kill":
                print("You start to attack the bandits, which wakes others, they quickly knock you out, and then follow your path back to the town and enslave the town")
            elif answer4 == "fire":
                print("You start the stocks on fire which is all dry and stacked up nicely, it grows quickly and takes over the encampment, destroying everything and killing most the bandits, You return home a hero.")
            else: 
                    print("You hesitated, mistyped, or paniced, and now you found out the bandits have raided your town, and your standing by the wayside trying to pick the right outfit to wear.")
            
    elif answer2 =="retreat":
        print("You head back to your house, are spotted, arrested and thrown in jail for being a coward.")
        answer8 = input("do you sit and WAIT or do you ESCAPE? ").lower()
        if answer8 == "wait":
            print("while you wait you start to smell smoke and hear a battle. Eventually the building your in catches fire and burns with you in it, which ends your story.")
        elif answer8 == "escape":
            print("while you work on digging a tunnel out of your cell, the town is burnt to the ground. You escape to find your the only person left.")
        else: 
            print("You hesitated, mistyped, or paniced, either way your loss, the plot has broken and your out in of here.")


#push answer 1 no tab
elif answer1 == "push":
    print("your neighbor turns around and punches you in the nose. The towns leaders grab you and thank you for volunteering, while dragging you to the forest path.")
    answer5 = input("do you FOLLOW the path or CIRCLE around to your house to hide? ").lower()
    if answer5 == "circle":
        print("you get hopelessly lost in the woods ")
        answer22 = input("you find a path, do you go RIGHT or LEFT? ").lower()
        if answer22== "right":
            print("sun goes down you stumble along the path in darkness, in the darkness you dont notice you walk off the edge of a cliff and die.")
        elif answer22=="left":
            print("You head up the path, which leads to a cave, as you think that can't be good a cave bear comes out and eats you.  You were tasty.") 
    elif answer5 == "follow":
       print("You head down the path as fast as you dare, you round a curve and find your neighbor on the ground with a bandit over him, his back to you. ")
       answer6 = input("seeing the bandit do you ATTACK, or LEAVE? ").lower()
       if answer6 == "attack":
           print("You gain the upper hand on the bandit, take him captive and return him to the town for information.  They learn of the bandit army and request help from the local towns and militias")
       elif answer6 == "leave":
           print("you find there is no way around the clearing, eventually find your hoplessly lost, wander around for days, then find the path, follow it back to town, to find the town has been attacked, burned to the ground and nobody is left")
       else: 
            print("You hesitated, mistyped, or paniced, either way you lost, your neighbor found you, ripped your limbs off and beat you with them. ")

#quiet
elif answer1 == "quiet":
    print("You stay quiet while another volunteers, you return to your home and start to cook dinner")
    answer7 = input("while making dinner, you begin to hear alot of fighting outside, do you INVESTIGATE or BARRICADE the door? ").lower()
    if answer7 == "investigate":
         print("looks like the town is on fire and people are fleeing in all directions, you try to follow them, but are quickly lost in the forest.")
         answer12 = input("do you head HOMEWARD or to the closest CITY? ").lower()
         if answer12 == "homeward":
             print("you get lost in the forest and are eaten by a bear.")
         elif answer12 == "city":
             print("you head to the biggest city in the area, arrive to find it as the bandits have taken over, the enslave you and sell your body parts to science.")
    elif answer7 == "barricade":
         print("you get the door barricaded, just in time, someone is bashing in the front door, it is holding but you are smelling smoke and its burning your eyes.  You shut them, but the next time you open them You are at the pearly gates.")
         last_answer=input("you are asked by St Peter, do you want to go to HEAVEN or HELL? ").lower()
         if last_answer == "heaven":
             print("you should have volunteered to go investigate your going the other direction.")
         elif last_answer == "hell":
             print("you are right at home where the heat is always on.")

else:
    print("You hesitated, picked something that wasn't available, or lost your focus, the bandits razed the town, enslaved your friends, and sold your body to science.")
    


   

      