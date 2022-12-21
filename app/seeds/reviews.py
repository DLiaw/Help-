from app.models import db, Review, environment, SCHEMA

## Review seeder
def seed_review():
    review1 = Review(
        user_id = '3',
        business_id = '1',
        review = ''' My fav boba spot in Seattle! The ingredients are always fresh, customer service is very friendly, super cute inside too. Def worth checking out :)
        ''',
        stars = 5
    )
    review2 = Review(
        user_id = '6',
        business_id = '1',
        review = ''' We happened to walk by for their soft opening and decided to try it! They have some nice flavor combos and all the things we like about bubble tea.
        I tried a mashed purple yam milk tea, could not customize sugar level but it wasn't too sweet! Also got 0% ice and they still filled it all the way up. I live
        that it came in a cute panda cup and a no spill cap for the opening. Only a few small tables for seating so hard for groups to sit. They have kiosks to order
        which makes the process faster! Didn't talk with servers much as they were super busy but seems rather efficient. Would go back to try a few more flavors and options.''',
        stars = 4
    )
    review3 = Review(
        user_id = '4',
        business_id = '1',
        review = ''' A friend showed me this place and it did not disappoint! He got a roasted milk tea that had really deep flavors and I got a mango/pomelo slush with
        cheese foam which was super refreshing and was just the right amount of sweetness at 50%!

        There are a few tables to sit at but other than that, the place is pretty barren. They don't offer free wifi to customers, which is the only downside, so not a good study
        spot. Would highly recommend for good bubble tea though! ''',
        stars = 5
    )
    review4 = Review(
        user_id = '2',
        business_id = '2',
        review = '''Pretty good boba here, I definitely should've got one of their speciality drinks! The ordering system is nice and the drinks came out moderately fast.
         The drink itself was good, not too sweet and they give you a lot of boba which is nice! ''',
        stars = 4
    )
    review5 = Review(
        user_id = '6',
        business_id = '2',
        review = ''' Really good bubble tea spot at UW!! All fresh ingredients and great service :) highly recommend coming here to grab your drinks!! ''',
        stars = 5
    )
    review6 = Review(
        user_id = '2',
        business_id = '2',
        review = ''' I happened to see this place after stopping by HMart. Their menu options look very similar to Sunright but with more
        flavor options. I decided to try the cheese foam black tea grape slush. It has slightly less grape flavor than Sunright's version
        but still good. Cute decor with some seating, I'd definitely come back to try one of their other drinks especially in the late
        evening when I'm looking for more options with no caffeine!

        ''',
        stars = 4
    )
    review7 = Review(
        user_id = '3',
        business_id = '3',
        review = ''' A completely new experience for me as a bubble tea lover where I got to make my own bubble tea.!
        Best part is you have sampler cups so that u can taste and put stuff that you like. No extra charges for any number of toppings.!
        The brown sugar boba tea was great and i made it with boba, jelly, and all good things ''',
        stars = 5
    )
    review8 = Review(
        user_id = '4',
        business_id = '3',
        review = ''' I was excited to try this new boba spot but it wasn't as good as I was expecting. With so many boba
        options on the Ave, they did a good job drawing you into the location. The decor was simple and cute. It was a clean
        spot with different table options. The present is all done via touchscreen. I got the milk tea at 50% sweet and the
        drink itself was great. The boba balls itself were subpar. They were small disappointing balls and not full of much
        flavor. The milk tea was good but not the boba. It was a bit pricey for the size too. I got the regular size and it
        was $6.50. I would try out another spot before coming back here unfortunately. ''',
        stars = 5
    )
    review9 = Review(
        user_id = '5',
        business_id = '3',
        review = ''' there are quite a lot of drinks you can choose from as well as a couple of the toppings. the taste isn't
        great but honestly it's just "normal" boba. my only concern was although you are required to wear the plastic "gloves"
        when making your drink, the toppings are in an open container and everyone scoops out of it, so it seems pretty unsanitary
        but I would assume it's the only way it would work so yeah.. ''',
        stars = 4
    )
    review10 = Review(
        user_id = '2',
        business_id = '4',
        review = ''' The best tapioca pearls I have ever tasted!!

        Even though I hate driving to Westlake, when I found out Xing Fu Tang opened a location in Seattle
        I had to go. I tried this place when I was in Vancouver and was so amazed by the flavor and texture
        of the tapioca pearls, and the tea was good too. The boba was perfectly chewy and sweetened with
        brown sugar. You can see them making their tapioca from scratch and then letting it sit in brown sugar
        right in front. They are known for their boba for a reason. Drinks are kind of sweet though,
        if you're not a fan of that.

        Definitely worth a try if you like boba! ''',
        stars = 5
    )
    review11 = Review(
        user_id = '5',
        business_id = '4',
        review = ''' Literally just the definition of okay.

        I'm used to paying $7 for boba; if it's good, it's worth it. This was NOT good.

        We ordered the Signature Brown Sugar Boba Milk. We also got the Taiwan Boba Milk Tea hot.
        Unfortunately, drinks were pretty much just flavorless milk :( Couldn't taste the brown sugar
        or the tea and considering they're #1 and #2 on their menu, I expected more than that.

        Service was kind, so the three stars are solely for that. ''',
        stars = 4
    )
    review12 = Review(
        user_id = '4',
        business_id = '4',
        review = ''' The first time I had Xing Fu Tang was at Richmond, BC and had read that they were known
        for their brown sugar boba milk drink and their giant sized Chinese fortune sticks which I thought was pretty cool.

        I've been here enough times to say this is probably my favorite boba spot near Downtown Seattle.

        - Signature Brown Sugar Boba Milk - This is so good and probably the best version of this drink that I've had.
        - Taiwan Boba Milk Tea - My go to drink from Xing Fu Tang.
        - Mango Smoothie and Rabbit Panna Cotta - This drink is so adorable and yummy!
        - Strawberry Boba Milk - The strawberry boba is so delicious!
        - Thai Tea - Yummy!
        - World Peace - Yummy!
        - Matcha Boba Milk - It's ok, its not my favorite drink. The matcha flavor is a bit too powdery for me.
        - Curacao Soda and Handmade Jelly - The soda's color as really cool but I didn't care much for the drink.

        You can substitute your milk to a plant based milk or lactose free milk.

        I also absolutely love how there's no need to change sweetness level in their drinks! It's always perfect!

        Yeah definitely go here! ''',
        stars = 5
    )
    review13 = Review(
        user_id = '6',
        business_id = '5',
        review = ''' Foods Tried:
        - Signature Brown Sugar Boba with Soy Milk

        My Review:
        I came to Seattle today for the sole purpose of ordering a Signature Brown Sugar Boba, and instead of ordering just one, I came back later in
        the day for a second. Since trying the Signature Brown Sugar Boba in my last review, I have gone to other bubble tea shops and tried their bobas,
        but none are as good as the homemade brown sugar boba that Xing Fu Tang makes. My only remark about the Signature Brown Sugar Boba is that it
        comes with ice; they should seriously remove it; it makes the hot gooey stir-frying bobas at the bottom of the drink harder and less satisfying.

        P.S. When ordering your Signature Brown Sugar Boba drink, ask for "no ice," it makes the drink taste better, and you get more bang for your buck. ''',
        stars = 4
    )
    review14 = Review(
        user_id = '1',
        business_id = '5',
        review = ''' The best brown sugar milk tea with boba you can't get in Washington, much better in my opinion than daboba and tiger sugar.
        The boba is made fresh and warm, the drink itself is not too sweet either. I'll be back. ''',
        stars = 5
    )
    review15 = Review(
        user_id = '1',
        business_id = '5',
        review = ''' Delicious drink with sweet and chewy boba. The cream was a little salty so I didn't like it much. The price is about $7 so
        it is on a more expensive level for a small drink. But I will come back because the drink is fantastic. We doordashed because we hated
        to find parking around there ''',
        stars = 4
    )
    review16 = Review(
        user_id = '3',
        business_id = '6',
        review = ''' This is fairly new in town. A friend recommended me to try out this place and I am glad I did try it out.
        They have an extensive menu and their drinks are very cute too. Highly quality boba. I have been here a couple of times
        with my friends and tried different options every time and all of them were good.
        This will be on my favorite boba place list in this town. Highly recommend checking this place out.
        There is good amount of seating inside. There is no designated parking, so will have to fish around for street parking. ''',
        stars = 4
    )
    review17 = Review(
        user_id = '3',
        business_id = '6',
        review = ''' Came tonight at around 10:10 PM (closes at 11 PM) and they were out of boba :( they were out of both normal and
        strawberry boba :( Unfortunately, I really felt like getting boba
        after my concert at the Showbox so I just didn't order anything :(

        Parking is also on the difficult side since it's next to Pike Place Market and only street parking is available. Interior
        is nice and modern but there were not enough seating. ''',
        stars = 5
    )
    review18 = Review(
        user_id = '1',
        business_id = '6',
        review = ''' I would say that the drink itself was between ok to good. Nothing out of the ordinary and we definitely had better
        before. I would say though that their fresh handmade boba is good
        and fun to chew (has a mochi-like texture)! Give it a try if you're normally picky with your boba. ''',
        stars = 4
    )
    review19 = Review(
        user_id = '6',
        business_id = '7',
        review = ''' Only bummer: It was a really cold day out, ordered this hot, and got it cold with ice cubes. They acknowledged it was
        the wrong order, but no apology or offer to make a new one. Went from already cold to ever colder!
        Hopefully this is one off, they're usually lovely. ''',
        stars = 5
    )
    review20 = Review(
        user_id = '4',
        business_id = '7',
        review = ''' A crowded a popular milk tea shop in Chinatown Seattle. The drinks are decently priced, quite large, but also very sugary.
        They offer free toppings on any drinks and have a wide selection of mix and matching syrups with different types of teas. I really liked
        the heavy oolong I got here, though it was too sweet. Will definitely get a sugar adjustment next time. ''',
        stars = 4
    )
    review21 = Review(
        user_id = '2',
        business_id = '7',
        review = ''' This is the highest rated boba spot in chinatown at Seattle, but unfortunately I thought it was a solid 2.5 stars.
         I purchased 3 drinks here, and each tasted like they were powdered teas, instead of steeped tea.

        The three flavors, which are all on the top sellers were:
        1) Brown sugar milk tea
        2) Jasmine milk tea
        3) Black milk tea

        Milk substitutes are free. The staff was very friendly and conversational, and they also sell ice cream at the store as well ''',
        stars = 4
    )
    review22 = Review(
        user_id = '1',
        business_id = '8',
        review = ''' Honestly not sure why this place has such high ratings. Our jasmine milk tea tasted nothing like jasmine tea.
        All you can taste is sweetness. Their boba is pretty ok (chewy and sweet) but definitely not worth coming here.
         Giving it a 3 because the worker there was nice. ''',
        stars = 5
    )
    review23 = Review(
        user_id = '6',
        business_id = '8',
        review = ''' This is a little hole-in-the-wall local business. The tea quality is TRULY the best! I can see why this place is so hyped up.
         I got the Heavy Oolong Milk Tea. Very fragrant tea and not too much milk! All drinks come with unlimited toppings. I didn't try any, but
         my friends tried the boba and said it was not very good. Docking off a star for the boba. ''',
        stars = 4
    )
    review24 = Review(
        user_id = '5',
        business_id = '8',
        review = ''' Overall rating: 4.5/5

        Wait: 4/5
        Arrival time: Monday 12:30pm

        Food: 4.5/5
        Order: heavy oolong

        Service: 4/5

        Price: 4/5

        Definitely coming back ''',
        stars = 5
    )
    review25 = Review(
        user_id = '4',
        business_id = '9',
        review = ''' TLDR; fast service, cheapest Boba Tea in Seattle, super nice staff.

        I LOVE SBT! This place seriously rocks. Right next to the beautiful gates in the ID, SBT usually has a little
        line outside but gets through it so quickly. I mean seriously SO FAST.

        The Boba is SO CHEAP too!!! Heavy Oolong is incredible and for $5 and unlimited toppings, it can't be beat.

        There's a cute little tea shop in the back too and usually people drinking tea and enjoying themselves :)

        I love SBT when I'm in the ID. So tasty and the folks who run it are so kind! ''',
        stars = 4
    )
    review26 = Review(
        user_id = '2',
        business_id = '9',
        review = ''' Can confirm, this place lives up to its name!

        I don't like most things, but I'm obsessed with the Heavy Oolong milk tea from here.

        First of all - sick name, idk how they came up with it but it's truly the perfect name for this drink. Second of all,
        this drink is amazing. I adjusted the sweetness to 75%, got light ice, light boba, apologized to the cashier and had
        a great time walking through the ID with one of the best milk teas I've ever had.

        The service here is great - everyone is patient and friendly, and so fast with your order.

        Would highly recommend checking this spot out! ''',
        stars = 4
    )
    review27 = Review(
        user_id = '1',
        business_id = '9',
        review = ''' Super nice staff! It was pretty busy when I went so I thought it was nice they had microphone and speakers
         set up so people can hear their orders being called outside while waiting.

        Most affordable drinks in the area and you get a free topping too! Lots of options to choose from with milk tea, sweet tea,
        smoothies, etc. Taro milk tea was good and didn't taste like the artificial taro powder that most places use. But boba wasn't
        cooked all the way so that it was a soft texture boba normally is. ''',
        stars = 5
    )
    review28 = Review(
        user_id = '6',
        business_id = '10',
        review = ''' 3.5 stars rounding up - a mom and pop tea shop that also sells milk tea drinks and ice cream

        Heavy oolong milk tea - this wasn't bad but wasn't great

        Brown Sugar milk tea - better than the oolong milk tea in terms of taste so will probably get this next time

        24oz only for cold drinks and start at $5

        Love supporting local business so I'll be back in the future to and recommend checking out if you're in the area wanting a sweet treat ''',
        stars = 4
    )
    review29 = Review(
        user_id = '1',
        business_id = '10',
        review = ''' Favorite bubble tea place in seattle!
        You can actually taste the tea!!!

        This has quickly become my favorite bubble tea shop in seattle. The service is amazing and the workers seem genuinely
        happy to be there and interact with customers.

        I've gotten the brown sugar milk tea (recommend 25-50 percent as it can be very sweet if higher) and the green tea
        milk tea. My friend loves the jasmine tea and the mango black tea was definitely not bad at all. Usually not a fan
        of Ice cream myself, but their oolong and jasmine ice cream is so good too! Not too sweet and the tea
        flavor just really comes through.

        We have been fortunate to find parking every time as there are spots designated for random pickup.

        Will continue coming back for more for the random cravings! ''',
        stars = 5
    )
    review30 = Review(
        user_id = '2',
        business_id = '10',
        review = ''' I've made it my life's mission to try every bubble tea place in Seattle. This place is hands down the
        best tasting and one of the most affordable. THEY DON'T CHARGE FOR TOPPINGS AND MILK SUBSTITUTES. The employees are
        very kind and personable. ''',
        stars = 4
    )
    review31 = Review(
        user_id = '3',
        business_id = '11',
        review = ''' I came here on Tuesday afternoon around 2pm and ordered two black milk teas with boba. The two staff
        members were very nice and I was in and out super quickly which was great. In reality I'd have to say that my
        review is probably closer to 4/5 on account of the very little boba pearls in each drink (ran out of boba halfway
        through the drink), but the flavor of the tea was excellent. It just might be my favorite in Seattle ''',
        stars = 4
    )
    review32 = Review(
        user_id = '6',
        business_id = '11',
        review = ''' Solid 4 star boba shop in C-ID. Only half the shop is utilized for customers with a short wait line.
        The menu is pretty extensive, staff super friendly, and drinks are made insanely quickly. There's also a handful of
        ice cream flavors available.

        So far everything I've tried has been pretty solid - black milk tea, green milk tea, and yogurt milk tea. The drinks
        can be a little sweet for me - the 50 percent sweetness tasted like 75 percent so adjust that sweetness! Definitely
        one of my go to spots for milk tea. ''',
        stars = 5
    )
    review33 = Review(
        user_id = '5',
        business_id = '11',
        review = ''' Small unassuming tea shop in the I district area steps away from uwajimaya by the gate, this small tea
        shop also sells boba. If you like that tea taste, this is the shop for you. Their tea drinks are always good. You can
        adjust sweetness and ice level and the service is always above and beyond. Too sweet, they can help you with that.

        One topping is free and their boba is definitely the best I've had in the area. ''',
        stars = 4
    )
    review34 = Review(
        user_id = '2',
        business_id = '12',
        review = ''' Tried out this boba shop called Seattle's Best Tea in Seattle's International District! It has surprisingly
        high reviews on Yelp but the taste is just ok contrary to what the name suggests (Bay Area boba is much better than
        Seattle boba). The fruit teas were watered down and bland and the boba was a bit mushy :| However, for 2 people working,
        this place has the fastest service I've seen! Once I placed my order they make it within minutes. Also, prices were fairly
        low (everything was $4.50 with free toppings). ''',
        stars = 5
    )
    review35 = Review(
        user_id = '1',
        business_id = '12',
        review = ''' The best tea spot in Chinatown! Stop by for their hot or cold teas~ they're all amazing. Every time I come here,
        I end up loving what I got, and the wait time is always so short. No complaints! ''',
        stars = 4
    )
    review36 = Review(
        user_id = '3',
        business_id = '12',
        review = ''' One of the best drinks I've had and love the large cup size options! The unsweet tea smoothie is so yummy and I
        love sugar but it was better than any sweet tea. The ice-cream is flavorful but not grossly artificial! Loved it and the
        employees energy was so sweet, I left smiling. There is also lots of parking on the street so it's easy access! ''',
        stars = 4
    )
    review37 = Review(
        user_id = '3',
        business_id = '13',
        review = ''' Stopped by Seattle Best Tea and trued their Heavy Oolong Tea and Kiwi milk tea with boba. The kiwi milk boba tea
        was refreshing but the heavy oolong was too strong for my taste. It is a great choice for tea lovers as you can taste the notes
        in every sip. Service is pretty quick and the owners are welcoming explaining what their best sellers are and also help you make
        a choice if you are confused. Highly recommend giving them a try. ''',
        stars = 5
    )
    review38 = Review(
        user_id = '1',
        business_id = '13',
        review = ''' Interesting. I honestly wasn't too big of a fan. I don't think it's the best tea spot here in Seattle but it's decent.
        Workers are friendly ''',
        stars = 4
    )
    review39 = Review(
        user_id = '2',
        business_id = '13',
        review = ''' Pink Lady (Rose, lychee, and lemon) for $5.25: it's really a rose-based tea with lychee bits and lemon slices. Perfect
        refresher, not too sweet, and I added crystal boba for the perfect chew. Would recommend. ''',
        stars = 5
    )
    review40 = Review(
        user_id = '6',
        business_id = '14',
        review = ''' Thanks to the excellent reviews, we had to try this place as we were waiting for our Korean hot dogs. I enjoyed my
        Oolong tea. It was creamy and delicious. My toddlers loved their mango bubble tea. So good. Recommend. ''',
        stars = 4
    )
    review41 = Review(
        user_id = '3',
        business_id = '14',
        review = ''' So many choices of tea/milk tea to choose from! I had to just stand outside for a bit to look at what they had on
        the menu. I ended up getting their iced black milk tea and it was refreshing. You can taste the brewed tea flavor and it had the
        right amount for milk and sweetness. I didn't have to ask for any adjustments in sugar, milk, tea.

        It's a very hole in the wall lowkey place which seems to make it more special in this community. ''',
        stars = 4
    )
    review42 = Review(
        user_id = '2',
        business_id = '14',
        review = ''' Awesome service, really good tea, and multiple options for a good price. I love how it's a small business owned by a
        family. I also love authentic the store and the back of the store is LOL...if you're Chinese, you'll know what I mean. @ Owners,
        please never change.

        Highly recommend the heavy oolong tea with egg pudding!

        ''',
        stars = 5
    )
    review43 = Review(
        user_id = '3',
        business_id = '15',
        review = ''' One of a kind heavy oolong milk tea. There's nothing comparable. If you love a strong oolong tea flavor, this is your spot.
        Seems to be family owned as it's always the same chill dude making the drinks. They take your time but they're good at what they do.
        Definitely recommend. You know it's going to be good when their name just states what they do, Seattle's best tea.

        I personally get 25-50 percent sweetness as their standard is quite sweet for my taste. In addition, their boba itself can be hit or miss,
        which is unfortunately. But honestly the heavy oolong is what makes them standard out here. ''',
        stars = 4
    )
    review44 = Review(
        user_id = '2',
        business_id = '15',
        review = ''' I'm from Hawaii and have been to and tried MANY bubble tea places. This is one of the few places I will go to in Washington
        for my milk tea. I thought the name was silly at first, but then I tried it and it really just hits the spot! They also have fruit-flavored
        milk teas (which is my absolute favorite, but isn't commonly sold) and it does not taste powdery or weird like I've experienced at other shops.

        Seriously! Try the peach milk tea with boba ''',
        stars = 5
    )
    review45 = Review(
        user_id = '1',
        business_id = '15',
        review = ''' Truly one of the best boba milk teas I've tried. The inside is unassuming - kind of has grandma's house vibes so you can tell it's
        a family run spot, not a chain. They have SO many flavors and ice cream too. Definitely will be back, I went on a rainy day pretty early and there
        was no line, and the woman working was super nice. ''',
        stars = 4
    )

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.add(reivew7)
    db.session.add(reivew8)
    db.session.add(reivew9)
    db.session.add(reivew10)
    db.session.add(review11)
    db.session.add(review12)
    db.session.add(review13)
    db.session.add(review14)
    db.session.add(review15)
    db.session.add(review16)
    db.session.add(reivew17)
    db.session.add(reivew18)
    db.session.add(reivew19)
    db.session.add(reivew20)
    db.session.add(review21)
    db.session.add(review22)
    db.session.add(review23)
    db.session.add(review24)
    db.session.add(review25)
    db.session.add(review26)
    db.session.add(reivew27)
    db.session.add(reivew28)
    db.session.add(reivew29)
    db.session.add(reivew30)
    db.session.add(review31)
    db.session.add(review32)
    db.session.add(review33)
    db.session.add(review34)
    db.session.add(review35)
    db.session.add(review36)
    db.session.add(reivew37)
    db.session.add(reivew38)
    db.session.add(reivew39)
    db.session.add(reivew40)
    db.session.add(review41)
    db.session.add(review42)
    db.session.add(review43)
    db.session.add(review44)
    db.session.add(review45)
    db.session.commit()

def undo_review():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM reviews")

    db.session.commit()
