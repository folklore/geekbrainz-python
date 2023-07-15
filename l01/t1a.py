while True:
    height = int(input('Введите высоту елки (или 0 для выхода): '))

    if height == 0:
        break
    print()

    for x in range(height):
        margin = ' ' * (height - x)
        side = x * '#'

        level = margin + side + '#' + side
        print(level)
    print()

# Введите высоту елки (или 0 для выхода): 9
#
#          #
#         ###
#        #####
#       #######
#      #########
#     ###########
#    #############
#   ###############
#  #################
