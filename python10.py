menu = input('메뉴: ')

food={'오뎅','순대','만두'}
price ={'300','400','500'}

menus=dict(zip(food , price))

#print(menus.values())

true=menu in menus

if true == True:
    menus[menu]
    print('가격: {0}'.format(menus[menu]))

elif true==False:

    print('가격: 0 ')
