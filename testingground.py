def script():
    #program code here..
    import os
    os.system('cls')

    print('Welcome to Alone!')
    print('     After spending a lifetime honing your survival skills you are selected to be a contestant on the next season of the TV series “Alone”. In this game you will test yourself against nature by trying to survive alone in the arctic beginning on September 8. If you can stay in the wild longer than the other contestants you will be given the grand prize of 3.141592 million dollars! You must leave the game if the judges determine that staying will be hazardous to your health.\n     Your site will be located near a lake in a forest. There are several species of large and small game animals in the area as well as various predators.  All contestants will be given some basic survival gear plus the option to bring one of two additional items. Will you bring a HATCHET or a BOW AND ARROW? ')
    level_a = input('Indicate your choice by typing in HATCHET or BOW AND ARROW: ')
    if level_a.lower() == 'hatchet':
        level_b_1 = input('     You say goodbye to your family, take your gear, including your HATCHET, and report to studio headquarters. After orientation you are flown by bush plane to your campsite. What is the first thing you’ll do when you get there? Use your hatchet to make a FIRE or SHELTER? ')
        if level_b_1.lower() == 'fire':
            level_c_1 = input('     You have chosen to start a fire. Good choice. It will provide you with warmth and the ability to cook your food and sterilize your water. You weren’t given a lighter or any matches, so you’ll have to start it some other way. You’ve heard of people using flint and steel to makes sparks to start the fire. Using a bow and a drill to start it with friction could be another option. Which method will you choose? SPARKS or FRICTION? ')
            if level_c_1.lower() == 'sparks':
                print('     You scout around the area looking for flint. However, you don’t know what flint looks like or if it can be found in this area. You choose a few rocks that look like possible candidates. You use the back of your hatchet to strike them. You’re in luck, one of them creates a spark!\n     You gather some dry tinder and try to get a few sparks to land in it. After some practice you get a few into the tinder. None of them have ignited the tinder yet, but you can’t expect success the first try right?\n     You keep trying. Hours pass. Your optimism begins to turn into despair. It’s getting dark and cold, but still no fire. Why isn’t this working? You try different tinder. Still no success.\n     You take a break to assess the situation. Only then do you realize that you need a special material to catch the spark long enough to ignite your tinder. You need charcloth. You don’t have any or know how to make it. It is too cold to survive without a fire or at least a shelter. You are forced to leave the game.')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
            elif level_c_1.lower() == 'friction':
                print('     You find some pieces of wood that look like good materials for a constructing a bow and a drill. You use your hatchet to shape them properly and use your shoelace as a bow string. Fortunately during the coronavirus shutdown you had nothing else to do and are kind of strange, so you practiced doing this at home.\n     It takes a few tries and modifications, but soon you have your fire going and you live to compete another day.')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
            else:
                print('     Sorry, that is not not a choice.')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
        elif level_b_1.lower() == 'shelter':
            level_c_2 = input('     You have chosen to construct a shelter. Good choice. Adequate shelter is a necessity of survival. Now what will you build it out of? You can cut down green trees to make it really nice, but it’ll take a lot of work. On the other hand, you can scavenge for dead branches, break them to length, and hopefully save a bunch of energy. What will it be GREEN or DEAD trees? ')
            if level_c_2.lower() == 'green':
                print('     You spend a lot of time and energy finding the perfect green trees and cutting them to length. Your shelter looks awesome and is very warm! And since they trees are green you can build a fire inside your shelter with less risk of it burning down. This will keep you warmer at night and allow you to stay in the wilderness longer. Good job!')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
            elif level_c_2.lower() == 'dead':
                print('     You construct your shelter at record pace and with minimal energy expenditure. Looks like a good choice! However, the first night in your shelter is cold and drafty. You need to move your fire inside your shelter to keep warm enough to survive, especially as winter starts to set in. Unfortunately, on one fateful night your shelter catches fire and you are forced to leave the game.')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
            else:
                print('     Sorry, that is not not a choice.')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
        else:
            print('     Sorry, that is not not a choice.')
            restart = input('     Would you like to play again? ')
            if restart.lower() == 'yes':
                script()
            elif restart.lower() == 'no':
                print('     Game over. Goodbye.')
    elif level_a.lower() == 'bow and arrow':
        level_b_2 = input('     You say goodbye to your family, take your gear, including your bow and arrow, and report to studio headquarters. After orientation you are flown by bush plane to your campsite. What is the first thing you’ll do when you get there? Will you test your archery skills and go hunting or worry about that later and find a water source now? HUNT or WATER? ')
        if level_b_2.lower() == 'hunt':
            level_c_3 = input('     You have decided to go hunting. Its what all the cool kids do, especially when playing the old computer game, “The Oregon Trail”. Now the question is what game will you target? BIG GAME or SMALL GAME? ')
            if level_c_3.lower() == 'big game':
                print('     You’ve decided to go for the glory and hunt big game. A big moose rack would look nice hung over your shelter door. You spend the day hiking up and down mountains looking for that trophy bull or buck. You see some sign that looks promising, but don’t actually see any animals. You return to your shelter at the end of the day tired, sore, and empty handed. Obtaining food is going to be more difficult than you thought and now you’ve used a lot of time and energy with nothing to show for it. You can make it a few more days without food, but this is not a good way to start out. You will have a tough time winning this game.')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
            elif level_c_3.lower() == 'small game':
                print('     As you’ve looked around your camp you’ve seen a few squirrels and birds. They aren’t very big, but they’re better than nothing. You miss the first few shots you take, but soon you’re in the groove and manage to bag two squirrels and a bird. It’s not Thanksgiving dinner, but you managed to get some food without expending too much energy. You’re starting off well. Keep at it and you’ll have a good chance of winning.')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
            else:
                print('     Sorry, that is not not a choice.')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
        elif level_b_2.lower() == 'water':
            level_c_4 = input('     You’ve decided to take care of one of your essential needs first. Good thinking. After all studies have shown that humans can only live a short time without water. Where do you plan to get your water? You could find a spring or a clear stream and drink straight from them. You could also just find the closest water source no matter its quality and filter it with your shirt then boil it. What’s it going to be? SPRING, STREAM, OR purify the CLOSEST water source? ') 
            if level_c_4.lower() == 'spring':
                print('     You hike far and wide to find what looks like a clear spring. You take a big swig and it tastes good! You fill some improvised water vessels and prepare to head back to camp. Before going you decide to see what’s up the slope from your spring. You get near the top and see that there is some running water there too. Then you smell it – rotting flesh! You can now see that your spring water has just washed over a decaying animal carcass, seeped under the surface for a short distance, and reemerged to give the appearance of a spring. Looks like this trip is over for you!')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
            elif level_c_4.lower() == 'stream':
                print('     You spot a small canyon a short distance from your camp. You figure there’s a good chance a river or stream is flowing in the bottom of it. You hike over and find that there is indeed a small stream. It looks clear and feels cold. You figure this is a pristine landscape free from pollution and disease. You take a nice gulp of mountain water and fill your water vessels to take back to camp. Later that night your stomach starts hurting and you don’t feel so good. You ignore it at first, but soon it become too painful to ignore. Maybe it’ll pass by morning. You endure a sleepless night with the pain and sickness only intensifying. Looks like it’s time to tap out. Better luck next time!')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
            elif level_c_4.lower() == 'closest':
                print('     You find a small pond near your camp. It looks kind of gross, but it’s a short trip and you’re going to have to make it often so this might as well by your water source. You devise a filtration system from your shirt some other items you have on hand. That gets most of the silt and bugs out. You use your sharp arrow heads to carve a bow and drill fire starting set. Once your fire is going you boil your water, cool it and drink it. You do this for several days with no ill effects. Looks like you have a good method for purifying your water and it doesn’t take too much energy to get it. Now you can focus on your other needs and win this thing!')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
            else:
                print('    Sorry, that is not not a choice.')
                restart = input('     Would you like to play again? ')
                if restart.lower() == 'yes':
                    script()
                elif restart.lower() == 'no':
                     print('     Game over. Goodbye.')
        else:
            print('     Sorry, that is not not a choice.')
            restart = input('     Would you like to play again? ')
            if restart.lower() == 'yes':
                script()
            elif restart.lower() == 'no':
                 print('     Game over. Goodbye.')
    else:
        print('     Sorry, that is not not a choice.')
        restart = input('     Would you like to play again? ')
        if restart.lower() == 'yes':
            script()
        elif restart.lower() == 'no':
            print('     Game over. Goodbye.')
#code to replay game
#restart = input('     Would you like to play again? ')
#if restart.lower() == 'yes':
 #   script()
#elif restart.lower() == 'no':
 #   print('     Game over. Goodbye.')
script()
