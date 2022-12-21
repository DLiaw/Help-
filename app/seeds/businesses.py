from app.models import db, Business, environment, SCHEMA

# Business seeder
def seed_business():

    name = Business(
        owner_id = 1,
        name = "Seattle Best Tea",
        address = "506 S King St",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98104",
        lat = 47.59873,
        lng = -122.32733,
        phone_number = "(206) 749-9855",
        business_type = "Bubble Tea",
        business_hour = """ Mon
11:00 AM - 9:00 PM

Tue

11:00 AM - 9:00 PM

Wed

11:00 AM - 9:00 PM

Thu

11:00 AM - 9:00 PM

Fri

11:00 AM - 10:00 PM

Sat

11:00 AM - 10:00 PM

Sun

11:00 AM - 10:00 PM

 """,
        site = "http://seattlebesttea.com",
        price = "$$"
    )
        name1 = Business(
        owner_id = 1,
        name = "Atulea",
        address = "1715 12th Ave Suite.100",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98122",
        lat = 47.61709,
        lng = -122.31719,
        phone_number = "(206) 413-5903",
        business_type = "Bubble Tea",
        business_hour = """ Mon

4:00 PM - 9:00 PM

Tue

4:00 PM - 9:00 PM

Wed

4:00 PM - 9:00 PM

Thu

4:00 PM - 9:00 PM

Fri

4:00 PM - 10:00 PM

Sat

4:00 PM - 10:00 PM

Sun

4:00 PM - 9:00 PM """,
        site = "http://atulea.com",
        price = "$$"
    )
        name2 = Business(
        owner_id = 1,
        name = "Boba Up",
        address = "4141 University Way NE Ste 103",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98105",
        lat = 47.65825,
        lng = -122.31365,
        phone_number = "(206) 395-2953",
        business_type = "Bubble Tea",
        business_hour = """ Mon

11:00 AM - 9:00 PM

Tue

11:00 AM - 9:00 PM

Wed

11:00 AM - 9:00 PM

Thu

11:00 AM - 9:00 PM

Fri

11:00 AM - 10:00 PM

Sat

11:00 AM - 10:00 PM

Sun

11:00 AM - 9:00 PM

 """,
        site = "https://bobaupseattle.com",
        price = "$$"
    )
        name3 = Business(
        owner_id = 2,
        name = "Sunright Tea Studio",
        address = "4545 Roosevelt Way NE Ste 103",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98105",
        lat = 47.66261,
        lng = -122.31767,
        phone_number = "(207) 992-4444",
        business_type = "Bubble Tea",
        business_hour = """ Mon

12:00 PM - 9:00 PM

Tue

12:00 PM - 9:00 PM

Wed

12:00 PM - 9:00 PM

Thu

12:00 PM - 9:00 PM

Fri

12:00 PM - 9:00 PM

Sat

12:00 PM - 9:00 PM

Sun

12:00 PM - 9:00 PM

 """,
        site = "https://www.snrtea.com",
        price = "$"
    )
        name4 = Business(
        owner_id = 2,
        name = "Xing Fu Tang",
        address = "1905 4th Ave",
        city = "Seattle",
        state = "WZ",
        country = "USA",
        zip = "98101",
        lat = 47.61243,
        lng = -122.33914,
        phone_number = "(206) 765-8069",
        business_type = "Bubble Tea",
        business_hour = """ Mon

12:00 PM - 10:00 PM

Tue

12:00 PM - 10:00 PM

Wed

12:00 PM - 10:00 PM

Thu

12:00 PM - 10:00 PM

Fri

12:00 PM - 11:00 PM

Sat

12:00 PM - 11:00 PM

Sun

12:00 PM - 10:00 PM

 """,
        site = "https://xingfutangwa.com",
        price = "$"
    )
        name5 = Business(
        owner_id = 2,
        name = "DRIP TEA",
        address = "1416 10th Ave",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98122",
        lat = 47.61350,
        lng = -122.31908,
        phone_number = "(206) 457-4374",
        business_type = "Bubble Tea",
        business_hour = """ Mon

12:00 PM - 9:00 PM

Tue

12:00 PM - 9:00 PM

Wed

12:00 PM - 9:00 PM

Thu

12:00 PM - 9:00 PM

Fri

12:00 PM - 10:00 PM

Sat

12:00 PM - 10:00 PM

Sun

12:00 PM - 9:00 PM """,
        site = "http://dripteaseattle.com",
        price = "$"
    )
        name6 = Business(
        owner_id = 3,
        name = "Mochinut",
        address = "400 Fairview Ave N",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98109",
        lat = 47.62290,
        lng = -122.33389,
        phone_number = "(469) 289-0273",
        business_type = "Donuts",
        business_hour = """ Mon

10:30 AM - 8:30 PM

Tue

10:30 AM - 8:30 PM

Wed

10:30 AM - 8:30 PM

Thu

10:30 AM - 8:30 PM

Fri

10:30 AM - 8:30 PM

Sat

10:30 AM - 8:30 PM

Sun

10:30 AM - 8:30 PM """,
        site = "https://www.mochinut.com",
        price = "$$"
    )
        name7 = Business(
        owner_id = 3,
        name = "TP TEA",
        address = "679 S King St",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98104",
        lat = 47.59845,
        lng = -122.32396,
        phone_number = "(206) 485-7481",
        business_type = "Bubble Tea",
        business_hour = """ Mon

12:00 PM - 8:00 PM

Tue

12:00 PM - 8:00 PM

Wed

12:00 PM - 8:00 PM

Thu

12:00 PM - 8:00 PM

Fri

12:00 PM - 8:00 PM

Sat

12:00 PM - 8:00 PM

Sun

12:00 PM - 8:00 PM

 """,
        site = "https://en.tp-tea.com",
        price = "$$"
    )
        name8 = Business(
        owner_id = 3,
        name = "Tiger Sugar",
        address = "1422 2nd Ave",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98101",
        lat = 47.60906,
        lng = -122.33813,
        phone_number = "(206) 485-8888",
        business_type = "Bubble Tea",
        business_hour = """ Mon

11:30 AM - 7:30 PM

Tue

11:30 AM - 7:30 PM

Wed

11:30 AM - 7:30 PM

Thu

11:30 AM - 7:30 PM

Fri

11:30 AM - 7:30 PM

Sat

11:30 AM - 8:30 PM

Sun

11:30 AM - 8:30 PM

 """,
        site = "https://www.tigersugar-wa.com",
        price = "$"
    )
        name9 = Business(
        owner_id = 4,
        name = "Happy Lemon",
        address = "1171 NW Sammamish Rd Unit 109",
        city = "Issaquah",
        state = "WA",
        country = "USA",
        zip = "98027",
        lat = 47.55186,
        lng = -122.05811,
        phone_number = "(425) 395-7293",
        business_type = "Bubble Tea",
        business_hour = """ Mon

11:00 AM - 8:00 PM

Tue

11:00 AM - 8:00 PM

Wed

11:00 AM - 8:00 PM

Thu

11:00 AM - 8:00 PM

Fri

11:00 AM - 9:00 PM

Sat

10:30 AM - 9:00 PM

Sun

10:30 AM - 8:00 PM """,
        site = "https://happylemonseattle.com/",
        price = "$"
    )
        name10 = Business(
        owner_id = 4,
        name = "SUSU Dessert Bar",
        address = "665 S King St",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98104",
        lat = 47.59834,
        lng = -122.32437,
        phone_number = "(425) 395-4434",
        business_type = "Desserts",
        business_hour = """ Mon

11:00 AM - 8:00 PM

Tue

11:00 AM - 8:00 PM

Wed

11:00 AM - 8:00 PM

Thu

11:00 AM - 8:00 PM

Fri

11:00 AM - 9:00 PM

Sat

10:30 AM - 9:00 PM

Sun

10:30 AM - 8:00 PM """,
        site = "https://sususeattle.com",
        price = "$"
    )
        name11 = Business(
        owner_id = 4,
        name = "Dochi",
        address = "515 Weller St",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98104",
        lat = 47.59755,
        lng = -122.32717,
        phone_number = "(425) 888-4434",
        business_type = "Desserts",
        business_hour = """ Mon

11:00 AM - 5:00 PM

Tue

11:00 AM - 5:00 PM

Wed

11:00 AM - 5:00 PM

Thu

11:00 AM - 5:00 PM

Fri

11:00 AM - 5:00 PM

Sat

11:00 AM - 6:00 PM

Sun

11:00 AM - 6:00 PM """,
        site = "https://www.dochicompany.com",
        price = "$"
    )
        name12 = Business(
        owner_id = 5,
        name = "Kakigori Dessert Cafe",
        address = "2207 E Madison St",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98112",
        lat = 47.61824,
        lng = -122.30372,
        phone_number = "(206) 323-0659",
        business_type = "Ice Cream",
        business_hour = """ Mon

3:00 PM - 8:00 PM

Tue

3:00 PM - 8:00 PM

Wed

3:00 PM - 8:00 PM

Thu

3:00 PM - 8:00 PM

Fri

3:00 PM - 8:00 PM

Sat

12:00 PM - 9:00 PM

Sun

12:00 PM - 9:00 PM

 """,
        site = "https://www.instagram.com/kakigori_dessert_cafe/?hl=en",
        price = "$$"
    )
        name13 = Business(
        owner_id = 5,
        name = "Nana’s Green Tea",
        address = "1007 Stewart St Ste 103",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98101",
        lat = 47.61649,
        lng = -122.33328,
        phone_number = "(206) 785-6477",
        business_type = "Dessert",
        business_hour = """ Mon

11:00 AM - 9:00 PM

Tue

11:00 AM - 9:00 PM

Wed

11:00 AM - 9:00 PM

Thu

11:00 AM - 9:00 PM

Fri

11:00 AM - 9:00 PM

Sat

11:00 AM - 9:00 PM

Sun

11:00 AM - 9:00 PM

 """,
        site = "https://www.nanasgreenteaseattle.com/",
        price = "$$"
    )
        name14 = Business(
        owner_id = 5,
        name = "Hiroki",
        address = "2224 N 56th St",
        city = "Seattle",
        state = "WA",
        country = "USA",
        zip = "98103",
        lat = 47.66921,
        lng = -122.33212,
        phone_number = "(206) 547-4128",
        business_type = "Bakery",
        business_hour = """ Mon

12:00 PM - 6:00 PM

Tue

12:00 PM - 6:00 PM

Wed

12:00 PM - 6:00 PM

Thu

12:00 PM - 6:00 PM

Fri

12:00 PM - 6:00 PM

Sat

12:00 PM - 5:00 PM

Sun

12:00 PM - 5:00 PM

 """,
        site = "https://hirokiseattle.bestcafes.online/",
        price = "$"
    )

    db.session.add(name)
    db.session.add(name1)
    db.session.add(name2)
    db.session.add(name3)
    db.session.add(name4)
    db.session.add(name5)
    db.session.add(name6)
    db.session.add(name7)
    db.session.add(name8)
    db.session.add(name9)
    db.session.add(name10)
    db.session.add(name11)
    db.session.add(name12)
    db.session.add(name13)
    db.session.add(name14)
    db.session.commit()

##Mon-11:00AM-9:00PM,Tue-11:00AM-9:00PM,Wed-11:00AM-9:00PM,Thu-11:00AM-9:00PM,Fri11:00AM-10:00PM,Sat-11:00AM-10:00PM,Sun-11:00AM-10:00PM
