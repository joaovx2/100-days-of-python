##making a treasure hunter with everything done so far
print('''
************************************************************************************************************************************************    
                         __
                     _.-'.-'-.__
                  .-'.       '-.'-._ __.--._
           -..'\,-,/..-  _         .'   \   '----._
            ). /_ _\' ( ' '.         '-  '/'-----._'-.__
            '..'     '-r   _      .-.       '-._ \
            '.\. Y .).'       ( .'  .      .\          '\'.
            .-')'|'/'-.        \)    )      '',_      _.c_.\
              .<, ,>.          |   _/\        . ',   :   : \\
             .' \_/ '.        /  .'   |          '.     .'  \)
                             / .-'    '-.        : \   _;   ||
                            / /    _     \_      '.'\ ' /   ||
                           /.'   .'        \_      .|   \   \|
                          / /   /      __.---'      '._  ;  ||
                         /.'  _:-.____< ,_           '.\ \  ||
                        // .-'     '-.__  '-'-\_      '.\/_ \|
                       ( };====.===-==='        '.    .  \\: \
                        \\ '._        /          :   ,'   )\_ \
                         \\   '------/            \ .    /   )/
                          \|        _|             )Y    |   /
                           \\      \             .','   /  ,/
                            \\    _/            /     _/
                             \\   \           .'    .'
                              '| '1          /    .'
                                '. \        |:    /
                                  \ |       /', .'
                                   \(      ( ;z'
                                    \:      \ '(_
                                     \_,     '._ '-.___
                           snd                   '-' -.\

************************************************************************************************************************************************         
''')
print("Welcome to the Dragon game")
print("it is up to you to fight the monster")
first_choice = input('The dragon is coming at you in a straight line which side do you dodge? Type "Left" or "Right".\n').lower()
if first_choice == "left":
  second_choice = input('Now you have dodged, the dragon has his back turned to you, will you attack it or wait for a next chance? Tye "Attack" or "Wait" \n').lower()
  if second_choice == "attack":
    third_choice = input('You started attacking its back, the dragon is crying out in pain, where will you attack next? Type "head", "tail" "back"\n')
    if third_choice == "head":
        print("You managed to beat the beast, it died at your mercy and you leveled up.")
    elif third_choice == "back":
      print("You hit the beast on its back, but it recovered after some time and you couldn't delivery the final blow, it roasted you with its fire breath after turning around")
    elif third_choice == "tail":
      print("Retarded hitting a dragon tails? deserved death")
    else:
     print("dont pick something that doesnt exist dumbass")
  elif second_choice == "wait":
    print("You waited instead of acting, the dragon piercied your body with its tail and you died.")
  else:
    print("You didnt pick a valid choice, deserved death")
else:
    print("Too bad you dodge to the wrong side, the dragon cut you into to pieces with it's sharp claws")

