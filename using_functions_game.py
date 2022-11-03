game=[[0,0,0],
      [0,0,0],
      [0,0,0]]
# print("   0  1  2")
# count=0
# for row in game:
#     print(count,row)
#     count+=1
# or
def game_board(player=0, row=0, column=0, just_display=False):
    print("   a  b  c")
    if not just_display:
        game[row][column]=player
    for count,row in enumerate(game):
        print(count,row)
        
#game[0][1]=1
#game_board(current_player,row_choice,col_choice)
game_board(1,1,1)