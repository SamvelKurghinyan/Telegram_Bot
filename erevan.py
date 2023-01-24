import telebot
from telebot import types

bot = telebot.TeleBot('5772449654:AAEWqpn5d4MqoK6Sjmjxlhq745b1zfTrHtk')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    button1 = types.KeyboardButton("Restaurant 🍔🍕")
    button2 = types.KeyboardButton("Pubs / Bars 🍸")
    button3 = types.KeyboardButton("Clubs 💃🏼")
    button4 = types.KeyboardButton("Pools 🏝️")
    markup.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, 'Hello '+str(message.from_user.first_name)+'\n'+"Press a button to see the options:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Restaurant 🍔🍕")
def press_button1(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("Best Rate ★★★", callback_data='1')
    button2 = types.InlineKeyboardButton("Armenian 🍖", callback_data='2')
    button3 = types.InlineKeyboardButton("Asian 🍣", callback_data='3')
    button9 = types.InlineKeyboardButton("Eropian🍝", callback_data='9')
    buttonburger = types.InlineKeyboardButton("Fast Food🍔", callback_data='Burger')
    markup.add(button1, button2, button3,button9,buttonburger)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Pubs / Bars 🍸")
def press_button2(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button4 = types.InlineKeyboardButton("Best Rate Bars ★★★", callback_data='4')
    button5 = types.InlineKeyboardButton("Cocktails 🍸", callback_data='5')
    button6 = types.InlineKeyboardButton("Beer 🍻", callback_data='6')
    markup.add(button4, button5, button6)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Clubs 💃🏼")
def press_button3(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button7 = types.InlineKeyboardButton("Clubs", callback_data='7')
    button8 = types.InlineKeyboardButton("Night Clubs🍸", callback_data='8')
    
    markup.add(button7, button8, )
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Pools 🏝️")
def press_button4(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    button11 = types.InlineKeyboardButton("Outdoor Pool", callback_data='11')
    button12 = types.InlineKeyboardButton("Indoor Pool", callback_data='12')
    markup.add( button11, button12)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)    


# you can also add more message handlers for the other buttons as well.

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '1': 
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More High Rated Restaurants ★★★',url='https://www.tripadvisor.com/Restaurants-g293932-zfp58-Yerevan.html'))
        Katsin='KATSIN Restaurant & Dining Bar, 077 88 10 01\n'+''+'https://www.facebook.com/katsinyerevan/'
        sherep='Sherep Restaurant 043 60 08 80\n'+'https://ru-ru.facebook.com/sherep.resto/'
        asadoor='Asador Restaurant 044 00 22 00\n'+'https://ru-ru.facebook.com/asadoryerevan/'
        mao='Mao Yerevan 055 00 10 01\n'+'https://www.facebook.com/maoyerevan/'
        livingston='Livingston Restaurant 099 39 20 20\n'+'https://ru-ru.facebook.com/livingston.restaurant/'
        nag='NAG 041 33 73 38\n'+'https://m.facebook.com/nagepic/'
        hot_pub='Hot Pub 095 80 00 00\n'+'https://www.facebook.com/hotpub/'
        itog=(Katsin,sherep,asadoor,mao,hot_pub,livingston,nag)
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        for i in (itog):
            bot.send_message(call.message.chat.id,i) 
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Best Rated Restaurants in Yerevan⬆️',reply_markup=markup)          
       
        
    elif call.data == '2':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More Armenian Restaurants',url='https://www.tripadvisor.com/Restaurants-g293932-Yerevan.html'))
        mayrig='Mayrig Yerevan 041 76 07 60\n'+'https://www.facebook.com/mayrigyerevan/?locale=ru_RU'
        erevan_pandok='Pandok Yerevan 010 60 00 06\n'+'https://www.facebook.com/PandokYerevan/'
        dolmama="Dolmama - Armenia's Restaurant 010 56 13 54\n"+"https://www.facebook.com/Dolmama/"
        ktoor='Ktoor 011 24 24 00\n'+'https://www.facebook.com/KtoorYerevan/'
        lavash='Lavash Restaurant 091 60 88 00'+'https://ru-ru.facebook.com/Lavash.Restaurant.Yerevan/'
        itog=[mayrig,erevan_pandok,dolmama,ktoor,lavash]
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        for i in itog:
            bot.send_message(call.message.chat.id,i)
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Armenian Restaurants in Yerevan⬆️',reply_markup=markup)      
        # bot.send_message(call.message.chat.id,'⬆️Upper you can see Armenian Restaurants in Yerevan⬆️')  
        
    elif call.data == '3':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More Asian Restaurants',url='https://www.tripadvisor.com/Restaurants-g293932-c3-Yerevan.html'))
        dragon_garden='Dragon Garden 044 75 75 88\n'+'https://www.facebook.com/Dragongarden.am/?locale=ru_RU'
        wasabi='Wasabi Sushi & More 010 56 54 12\n'+'https://www.facebook.com/wasabi.am/'
        mao='Mao Yerevan 055 00 10 01\n'+'https://www.facebook.com/maoyerevan/'
        new_tao='New Tao 010 54 09 99\n'+'https://ru-ru.facebook.com/newtaoyerevan/'
        beijing='Pekin 010 54 53 42\n'+'https://www.facebook.com/pekin.sayatnova/'
        thai_wine='Thaiwine Republic 055 00 11 00'+'https://www.facebook.com/thaiwinerepublic/'
        itog=[dragon_garden,wasabi,mao,new_tao,beijing,thai_wine]
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        for i in itog:
            bot.send_message(call.message.chat.id,i)
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Asian Restaurants in Yerevan⬆️',reply_markup=markup)     
        # bot.send_message(call.message.chat.id,'⬆️Upper you can see Asian Restaurants in Yerevan⬆️')
           
    elif call.data == '4':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More High Rated\n   Bars',url='https://www.tripadvisor.com/Attractions-g293931-Activities-c20-t99-Armenia.html'))
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        kong='Kong Yerevan 044 34 73 47\n'+'https://www.facebook.com/kong.evn/'
        mamba='Mamba Yerevan 055 34 73 47\n'+'https://www.facebook.com/mamba.evn/'
        banderego='Banderego https://banderego.com/\n'+'https://www.facebook.com/banderego'
        pahest33='Pahest33 044 99 99 59\n'+'https://www.facebook.com/pahest33/'
        itog=[kong,mamba,banderego,pahest33]
        for i in itog:
            bot.send_message(call.message.chat.id,i)
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Best Rated Bars in Yerevan⬆️',reply_markup=markup)
        # bot.send_message(call.message.chat.id,'⬆️Upper you can see Best Rated Bars in Yerevan⬆️')

    elif call.data == '5':
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More Cocktail Bars',url='https://www.tripadvisor.com/Attractions-g293931-Activities-c20-t99-Armenia.html'))
        kong='Kong Yerevan 044 34 73 47\n'+'https://www.facebook.com/kong.evn/'
        mamba='Mamba Yerevan 055 34 73 47\n'+'https://www.facebook.com/mamba.evn/'
        banderego='Banderego https://banderego.com/\n'+'https://www.facebook.com/banderego'
        pahest33='Pahest33 044 99 99 59\n'+'https://www.facebook.com/pahest33/'
        simona='Simona 095 42 66 19\n'+'https://ru-ru.facebook.com/simonabarhome/'
        beatles='The Beatles Pub Yerevan 041 52 20 23\n'+'https://www.facebook.com/beatlesyerevan/'
        daboo='Daboo Cocktail Bar 099 51 15 21\n'+'https://ru-ru.facebook.com/DabooCocktailBar/'
        seed='Seeds Pub and Eatery 012 73 30 37\n'+'https://www.facebook.com/seedspubyerevan/'
        libert='Liberty Pub 055 25 25 55\n'+'https://www.facebook.com/libeertypub/?locale=ru_RU'
        itog=[kong,mamba,banderego,pahest33,simona,beatles,daboo,seed,libert]
        for i in itog:
            bot.send_message(call.message.chat.id,i)
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Top Cocktail Bars in Yerevan⬆️',reply_markup=markup)  
        # bot.send_message(call.message.chat.id,'⬆️Upper you can see Top Cocktail Bars in Yerevan⬆️')  
        
        
    elif call.data == '6':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More Beer',url='https://www.tripadvisor.com/Restaurants-g293932-zfg11776-Yerevan.html'))
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        beatles='The Beatles Pub Yerevan 041 52 20 23\n'+'https://www.facebook.com/beatlesyerevan/'
        hotpub='Hot Pub 095 80 00 00\n'+'https://www.facebook.com/hotpub/'
        darget='Darget BrewPub 096 87 08 70\n'+'https://ru-ru.facebook.com/DargettBrewpub/'
        vienna='Vienna Ribs 060 53 00 07\n'+'https://www.instagram.com/viennaribs/'
        beeracademy='Beer Academy Ethnograph 060 50 35 03\n'+'https://www.facebook.com/beeracademyethnograph/'
        beeracad='Beer Academy 060 50 45 04\n'+'https://www.facebook.com/BeerAcademy.Armenia/'
        doors='dors craft beer & kitchen 044 12 01 12\n'+'https://www.facebook.com/dors.craftbeerandkitchen/'
        itog=[beatles,hotpub,darget,vienna,beeracademy,beeracad,doors]
        for i in itog:
            bot.send_message(call.message.chat.id,i)
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Top Beer Pubs in Yerevan⬆️',reply_markup=markup)  
        # bot.send_message(call.message.chat.id,'⬆️Upper you can see Top Beer Pubs in Yerevan⬆️')      
    elif call.data == 'Burger':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More Fast Food 🍔',url='https://www.tripadvisor.com/Restaurants-g293932-c10646-Yerevan.html'))
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        artlunch='Art Lunch 012 88 28 82\n'+'https://ru-ru.facebook.com/artlunch2002/'
        tumanyan='Tumanyan Shaurma 011 81 88 88\n'+'https://ru-ru.facebook.com/TumanyanShaurma/'
        artash='Artashi Mot Restaurant  010 55 32 22\n'+'https://www.facebook.com/ArtashiMotRestaurant/?locale=ru_RU'
        foodetory='Foodetory Food Hall 012 31 21 00\n'+'https://www.facebook.com/FoodetoryFoodHall/'
        kfc='KFC 011 50 55 05\n'+'https://ru-ru.facebook.com/KFC.Armenia/'
        madeinchina='Made In China Armenia 011 60 60 66\n'+'https://www.facebook.com/people/Made-in-China-Armenia/100077592246541/'
        muchacho='Muchacho Mexican Kitchen 011 80 88 80\n'+'https://www.facebook.com/MuchachoArmenia/'
        bbq='Barbq Yerevan 033 33 32 22\n '+'https://www.facebook.com/barbq.evn/'
        ost='OST Bistro 010 53 95 80\n'+'https://ru-ru.facebook.com/OSTbistro/'
        sas='SAS FOOD COURT 011 53 88 88\n'+'https://www.facebook.com/SasFoodCourtOfficial/'
        
        itog=[artlunch,tumanyan,artash,foodetory,kfc,madeinchina,muchacho,bbq,ost,sas]
        for i in itog:
            bot.send_message(call.message.chat.id,i)
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Fast Food Restaurants in Yerevan⬆️',reply_markup=markup)    
        # bot.send_message(call.message.chat.id,'⬆️Upper you can see Asian Restaurants in Yerevan⬆️')
           
    elif call.data == '7':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More Clubes',url='https://www.tripadvisor.com/Attractions-g293932-Activities-c20-t109-Yerevan.html'))
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        kong='Kong Yerevan 044 34 73 47\n'+'https://www.facebook.com/kong.evn/'
        mamba='Mamba Yerevan 055 34 73 47\n'+'https://www.facebook.com/mamba.evn/'
        banderego='Banderego https://banderego.com/\n'+'https://www.facebook.com/banderego'
        pahest33='Pahest33 044 99 99 59\n'+'https://www.facebook.com/pahest33/'
        paparazzi='Paparazzi Club 055 44 41 44\n'+'https://www.facebook.com/PaparazziclubYerevan/about'
        simona='Simona 095 42 66 19\n'+'https://ru-ru.facebook.com/simonabarhome/'
        downtown='Downtown Club 044 43 34 99\n'+'https://www.facebook.com/downtownyerevan/'
        sky_by_verev='Sky By Verev077 88 98 89\n'+'https://www.facebook.com/SkybyVerev/'
        itog=[kong,mamba,banderego,pahest33,paparazzi,simona,downtown,sky_by_verev]
        for i in itog:
            bot.send_message(call.message.chat.id,i)
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Clubs in Yerevan⬆️',reply_markup=markup)    
    elif call.data == '8':
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        matryoshka='Matreshka SHow Club 055 33 88 48\n'+'https://www.facebook.com/Matreshkaclubyerevan/'
        diva='Diva Show Club 095 25 22 12\n'+'https://www.facebook.com/DivaShowClubYerevan/'
        charlote='Cabaret Charlotte 041 27 70 20\n'+'https://www.facebook.com/cabaretcharlotteyerevan/'
        itog=[matryoshka,diva,charlote,]
        for i in itog:
            bot.send_message(call.message.chat.id,i) 
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Night Clubs in Yerevan⬆️')                
    elif call.data == '11':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More Outdoor Pools 🏝️',url='https://araratour.com/top-7-outdoor-swimming-pools-in-yerevan'))
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        The_pool='The Pool 043 99 00 11\n'+'https://www.facebook.com/thepool.dvingroup/'
        lanj='Lanj 033 03 80 38\n'+'https://www.facebook.com/LanjYerevan/'
        latar='Latar Hotel Yerevan 010 33 07 11\n'+'https://www.booking.com/hotel/am/latar-erevan.ru.html'
        kovkas='Caucasus Hotel Complex 060 50 11 77\n'+'https://www.facebook.com/caucasushotel/'
        jelifish='Jellyfish Yerevan 044 49 05 00\n'+'https://www.facebook.com/jellyfishyerevan/'
        vahakni='Flamingo Vahakni Pool 043 17 72 20\n'+'https://www.facebook.com/FlamingoVahakni/'
        itog=[The_pool,lanj,latar,kovkas,jelifish,vahakni]
        for i in itog:
            bot.send_message(call.message.chat.id,i)
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Outdoor Pools in Yerevan⬆️',reply_markup=markup)    
    elif call.data == '12':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More Indoor Pools 🏊',url='https://araratour.com/top-7-outdoor-swimming-pools-in-yerevan'))
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅")
        reebok='Reebok Sports Club Armenia 010 36 36 36'+'https://www.facebook.com/reeboksportsclub/'
        goltsgym="Gold's Gym Armenia 010 32 20 10"
        multi='Multi Wellness Center 011 88 08 80'+'https://www.facebook.com/multi.wellness/'
        itog=[reebok,goltsgym,multi]
        for i in itog:
            bot.send_message(call.message.chat.id,i) 
            bot.send_message(call.message.chat.id,'⬆️Upper you can see Indoor Pools in Yerevan⬆️')
    elif call.data == '9':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('More Europian Restaurants',url='https://www.tripadvisor.ru/Restaurants-g293932-c18-Yerevan.html'))
        pesto='Pesto Cafe Osteria 044 07 55 55\n'+'https://www.facebook.com/pestocafeosteria/'
        patricks='Patrick’s Pastry 044 00 81 18\n'+'https://www.facebook.com/patrickspastry/'
        pomidoro='Pomodoro Italian Restaurant 012 77 70 00\n'+'https://www.facebook.com/pomodoroyerevan/'
        armat='Armat Restaurant 091 50 19 19\n'+'https://www.facebook.com/armatrestaurant/'
        wine='Wine Republic Yerevan 055 00 11 00\n'+'https://www.facebook.com/winerepublicyerevan/'
        seasons='Seasons Restaurant 043 70 90 70\n'+'https://ru-ru.facebook.com/SeasonsRestArmenia/'
        vienna='Vienna Ribs 060 53 00 07\n'+'https://www.instagram.com/viennaribs/'
        itog=[pesto,patricks,pomidoro,armat,wine,seasons,vienna]
        bot.answer_callback_query(call.id, text="✅GREAT CHOICE✅") 
        for i in itog:      
            bot.send_message(call.message.chat.id,i)
        bot.send_message(call.message.chat.id,'⬆️Upper you can see Europian in Yerevan⬆️',reply_markup=markup)    
bot.polling(non_stop=True)





