wn = 0

un = int(input("Enter  a number:"))



game_over = False    
while not game_over:
    if un > wn:
        print("^( 'O' )^")
        un = int(input("Enter another number:"))
    elif un < wn:
        print(":(")
        un = int(input("Enter  anoter number:"))
    else:
        print("<3") 
        game_over =True
