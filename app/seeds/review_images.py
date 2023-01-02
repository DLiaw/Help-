from app.models import db, ReviewImage, environment, SCHEMA

# Review image seeder
def seed_review_image():
   reviews = [{
   'review_id': 4,
   'preview': True,
   'review_image': "https://toasttab.s3.amazonaws.com/restaurants/restaurant-58102000000000000/banner_1608707902.jpg"
},

{
   'review_id': 4,
   'preview': True,
   'review_image': "htts://s3-media0.fl.yelpcdn.com/bphoto/FcHKksQcR9kpwMBUmtzSrA/o.jpg"
},

{
   'review_id': 4,
   'preview': True,
   'review_image': "htts://s3-media0.fl.yelpcdn.com/bphoto/iKZp_Da158pANEXtpRGyiw/o.jpg"
},

{
   'review_id': 4,
   'preview': True,
   'review_image': "htts://s3-media0.fl.yelpcdn.com/bphoto/W_ep0hHniRvAbmXUgChJvA/o.jpg"
},

{
   'review_id': 4,
   'preview': True,
   'review_image': "htts://s3-media0.fl.yelpcdn.com/bphoto/eAasVrFpdbCsGPFIMh7L-Q/o.jpg"
},

{
   'review_id': 4,
   'preview': True,
   'review_image': "htts://s3-media0.fl.yelpcdn.com/bphoto/FYex_vFz-XgQWxgdlvQZKA/o.jpg"
},

{
   'review_id': 4,
   'preview': True,
   'review_image': "htts://s3-media0.fl.yelpcdn.com/bphoto/lyEBKRqi_OX_vAlcI9dsqg/o.jpg"
},

{
   'review_id': 2,
   'preview': True,
   'review_image': "https://secretbirmingham.com/wp-content/uploads/2022/11/shutterstock_1612664575-1.jpg"
},

{
   'review_id': 2,
   'preview': True,
   'review_image': "https://images.squarespace-cdn.com/content/v1/60e4b18a79406d29fe6738f7/425bd544-5089-4488-9a51-af94ed310def/Xing+Fu+Tang+Thai+Tea.jpg?format=1500w"
},

{
   'review_id': 2,
   'preview': True,
   'review_image': "https://soyacincau.com/wp-content/uploads/2019/10/191025-xing-fu-tang-malaysia-taiwan-dispute.jpg"
},

{
   'review_id': 2,
   'preview': True,
   'review_image': "https://talkboba.com/wp-content/uploads/2020/05/xingfutang-tb.jpg"
},

{
   'review_id': 2,
   'preview': True,
   'review_image': "https://media-cdn.tripadvisor.com/media/photo-s/1a/8f/1e/ac/preparing-the-bubble.jpg"
},

{
   'review_id': 2,
   'preview': True,
   'review_image': "https://secretbirmingham.com/wp-content/uploads/2022/11/shutterstock_1612664575-1.jpg"
},

{
   'review_id': 2,
   'preview': True,
   'review_image': "https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=1000,height=300,format=auto,quality=80/https://doordash-static.s3.amazonaws.com/media/store/header/fa79a5db-9197-4070-8c88-56e0d97bb6fb.jpg"
},

{
   'review_id': 3,
   'preview': True,
   'review_image': "https://www.udistrictseattle.com/wp-content/uploads/2020/10/AE82D3D8-3527-4AD7-920B-8F725AA5383F-2000x1333.jpeg"
},

{
   'review_id': 3,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/jrIAkk6RzXhlhRyTBoShQQ/o.jpg"
},

{
   'review_id': 3,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/E2Co11pJ1vBK9ePOytMzvg/o.jpg"
},

{
   'review_id': 3,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/9lDw00iBqpfCqud5vkzBMQ/o.jpg"
},

{
   'review_id': 3,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/OJjD2OsYGFODbL2ZdftLIA/o.jpg"
},

{
   'review_id': 3,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/0-GPT4eev_42m-evqN54kg/o.jpg"
},

{
   'review_id': 3,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Li74NW_RfxfRBSrlUUu-xQ/o.jpg"
},

{
   'review_id': 1,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/TV_CkQWdXmk56Ge6p7bM8A/o.jpg"
},

{
   'review_id': 1,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/H9gyrUQuaM98RaHg0Klq8w/o.jpg"
},

{
   'review_id': 1,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/1aiajJQV64rSPgO_6_feVw/o.jpg"
},

{
   'review_id': 1,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/JyTk3dG9-JiX1alfip8RUA/o.jpg"
},

{
   'review_id': 1,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/6qLOoTWdfT88c56DDHS5WQ/o.jpg"
},

{
   'review_id': 1,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/QCtIuEWx-3n0QiZXbzCSYw/o.jpg"
},

{
   'review_id': 1,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/jVsoSbUOOX0Dfv12qDff6A/o.jpg"
},

{
   'review_id': 5,
   'preview': True,
   'review_image': "https://media.king5.com/assets/KING/images/d3395381-0e51-4f69-9703-e320000dce48/d3395381-0e51-4f69-9703-e320000dce48_1920x1080.jpg"
},

{
   'review_id': 5,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/kNtyPnon-XTBCrblOwTCkg/o.jpg"
},

{
   'review_id': 5,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/36UrOPnaI54FpnLiXYUiBA/o.jpg"
},

{
   'review_id': 5,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Gn5VNw6GcVawJISTippjZw/o.jpg"
},

{
   'review_id': 5,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/_di30mtMO5a1T_xt3NSM6w/o.jpg"
},

{
   'review_id': 5,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/FMD5mMvVGY2pDXwm220sjg/o.jpg"
},

{
   'review_id': 5,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/WRr6aURGm6Li3zevTwBWog/o.jpg"
},

{
   'review_id': 6,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/j_YauB2WKeiQvHC1pgwUaQ/o.jpg"
},

{
   'review_id': 6,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/kdKjKc74h_ct3lfehSDrDA/o.jpg"
},

{
   'review_id': 6,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/KwUnfkSPynb30Nr1L4P2sA/o.jpg"
},

{
   'review_id': 6,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Jwp_uWsB1DekSgtoLEhuOA/o.jpg"
},

{
   'review_id': 6,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/VJ4q3fjXdOPtHCxJYdjuzw/o.jpg"
},

{
   'review_id': 6,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/aDUcTC98yuyHhQBSs_fy1w/o.jpg"
},

{
   'review_id': 6,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Mq5sAeWB2WgXeb4sQ5Q6yA/o.jpg"
},

{
   'review_id': 7,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/q0krfrDqF-oBxST3AtJ2wA/o.jpg"
},

{
   'review_id': 7,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/eHBdi-45qmO5S55tAu7bAQ/o.jpg"
},

{
   'review_id': 7,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/hbYU9qq9Gx5KE91OWgGdog/o.jpg"
},

{
   'review_id': 7,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/OzSOpHq3B8B4zGvae_FblQ/o.jpg"
},

{
   'review_id': 7,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/q0krfrDqF-oBxST3AtJ2wA/o.jpg"
},

{
   'review_id': 7,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/eHBdi-45qmO5S55tAu7bAQ/o.jpg"
},

{
   'review_id': 7,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/hbYU9qq9Gx5KE91OWgGdog/o.jpg"
},

{
   'review_id': 8,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/9WJp1U9Npks_Uk_BfHnk0A/o.jpg"
},

{
   'review_id': 8,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/QBjx__rXwdfLLAAbW01wEg/o.jpg"
},

{
   'review_id': 8,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/FeZi3gzxCltzM156n9zvFw/o.jpg"
},

{
   'review_id': 8,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/ciou0CmIi0Yb3J1nv_8LGw/o.jpg"
},

{
   'review_id': 8,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/NlLPm0bX_N-ryfgI3UZfXA/o.jpg"
},

{
   'review_id': 8,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/IFoeYlCXicJMODScFtnJeQ/o.jpg"
},

{
   'review_id': 8,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Q_HX_aZ6W561dFy22xZUiA/o.jpg"
},

{
   'review_id': 9,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/U7H17PPuAIeycye4MS9PZQ/o.jpg"
},

{
   'review_id': 9,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/p_asy_zGnuTDlJ4kYhymCw/o.jpg"
},

{
   'review_id': 9,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/j3AFBJNNMdTKnBb7jSWHXQ/o.jpg"
},

{
   'review_id': 9,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/hwVYvJn2tktuPW2fhM9bdg/o.jpg"
},

{
   'review_id': 9,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/tmZsk73rYyQ_n9ivIZeYqw/o.jpg"
},

{
   'review_id': 9,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/GU35WZdjXmiS6u7PY5_aFQ/o.jpg"
},

{
   'review_id': 9,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/ey7R9te2z2yh4P8PhEwyjQ/o.jpg"
},

{
   'review_id': 10,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Qi8hMKq8jrnhrmSlCV8qFg/o.jpg"
},

{
   'review_id': 10,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/QrfCIL3o9_N2EZ3oDET8MQ/o.jpg"
},

{
   'review_id': 10,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/B7dnnDf8sMIi70N5eF8vTw/o.jpg"
},

{
   'review_id': 10,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/TP916Qi89c5rLDtS8hMQUQ/o.jpg"
},

{
   'review_id': 10,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/i-sG4ZzD7b-7EbeTlico6Q/o.jpg"
},

{
   'review_id': 10,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/C98I5UH_jG7JyMDG_eysyQ/o.jpg"
},

{
   'review_id': 10,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/KmOXwgdD-y69dNsnS2BwcQ/o.jpg"
},

{
   'review_id': 11,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/ilrbT2VKJ6iCJVt5L6xo7g/o.jpg"
},

{
   'review_id': 11,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/ehvbg9iv0ZujD2NV6-DO9g/o.jpg"
},

{
   'review_id': 11,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/fCwXvMrdgWILJVEVDgTyMA/o.jpg"
},

{
   'review_id': 11,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/zuyFELWoIIGWwLEuVHme8A/o.jpg"
},

{
   'review_id': 11,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/XDIfUDGe0FZRQ0PeTlVEhQ/o.jpg"
},

{
   'review_id': 11,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/WRBvSsbYFy8Nb64qGB5eyw/o.jpg"
},

{
   'review_id': 11,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/w6KXuWpCf9yXIMx40BFSpA/o.jpg"
},

{
   'review_id': 12,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/nhVrubajrcglX1yPSjTOag/o.jpg"
},

{
   'review_id': 12,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/wz6bb-vL1lBwyVsTc7EMcQ/o.jpg"
},

{
   'review_id': 12,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/sXryAqzaAttSKIvdwpP-HQ/o.jpg"
},

{
   'review_id': 12,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/NToQINjg6dxR_m4_fohc7w/o.jpg"
},

{
   'review_id': 12,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/3ugal6k0c0s0Yb9-K3WBTw/o.jpg"
},

{
   'review_id': 12,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/rXQlAS9E0VETc_9rKmL8EA/o.jpg"
},

{
   'review_id': 12,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/UXPKrLJkOY8ZioAKlO8KyA/o.jpg"
},

{
   'review_id': 13,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/JvB-pkWJR_MY2MpWSrMz3Q/o.jpg"
},

{
   'review_id': 13,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/WGEBbqMsNwd5bgjTqBOTMg/o.jpg"
},

{
   'review_id': 13,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/OIfVdk6Zu3iW_9thwc1hdQ/o.jpg"
},

{
   'review_id': 13,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Z6eHKPSp-4FDlVLwJW_0Mw/o.jpg"
},

{
   'review_id': 13,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/8ML0RianxA7A4kx7w0l61w/o.jpg"
},

{
   'review_id': 13,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/BwL5gfGHYOS7LezbG6Haww/o.jpg"
},

{
   'review_id': 13,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/TcHe28rW-JJg1Ft3QTSrmg/o.jpg"
},

{
   'review_id': 14,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/W6dZ-KKhQb2JwKqwVaUreg/o.jpg"
},

{
   'review_id': 14,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/uU9KSqrghcszMNynm62ABQ/o.jpg"
},

{
   'review_id': 14,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/pk-P0jsTKfCySupLydRtnA/o.jpg"
},

{
   'review_id': 14,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/SkqLucwkqs0p_yInT2V_iQ/o.jpg"
},

{
   'review_id': 14,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/FVAilXTysrFTF05sRSVZ8Q/o.jpg"
},

{
   'review_id': 14,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/RHLX1lPUvWFxcXIH8AkcMA/o.jpg"
},

{
   'review_id': 14,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Z0NgAbjLXUIwNBikhmRg5w/o.jpg"
},

{
   'review_id': 15,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Z5QmGm81VCAJWFoW8jD-Ig/o.jpg"
},


{
   'review_id': 15,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/7WkWnVDSVdgeV7dN8SdLSg/o.jpg"
},


{
   'review_id': 15,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/tIMjnigejIIQtE458K0t8A/o.jpg"
},


{
   'review_id': 15,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/_tcofbzq1Ta0G8ZsjdZJzw/o.jpg"
},


{
   'review_id': 15,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/h9Ng8InjXvKckDCZiQBW9g/o.jpg"
},


{
   'review_id': 15,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/M2q2HVk0zG_ZWlPS02WxTQ/o.jpg"
},


{
   'review_id': 15,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/jR2YM2spyatuVP4SicH09Q/o.jpg"
},


{
   'review_id': 16,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/9SR2c7fIGfJCGhOcMHq0ig/o.jpg"
},


{
   'review_id': 17,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/mBvhexapUuf-eds-NkI9Qg/o.jpg"
},


{
   'review_id': 18,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/XQF_w9Ow1okQ55Qa6t2d9g/o.jpg"
},


{
   'review_id': 19,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/ofaXi1SRGB3Ah6TVl1nPYg/o.jpg"
},


{
   'review_id': 20,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/ZN-DHJtokD3YS_uLuZutFw/o.jpg"
},


{
   'review_id': 21,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/SVHnnqRf51UHQJhHrST2kw/o.jpg"
},


{
   'review_id': 22,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/Di9J5iTOmlNQDJu_iQbSvQ/o.jpg"
},


{
   'review_id': 23,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/-ohw-QEQw6fNJmSzJM0W6A/o.jpg"
},


{
   'review_id': 24,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/DZ7Vp4NouIjICSaKHPl4PQ/o.jpg"
},


{
   'review_id': 25,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/V-iUi2ATWvF4U6I7mB4cwA/o.jpg"
},


{
   'review_id': 26,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/spl26snrSb0jyQF65LcvZg/o.jpg"
},


{
   'review_id': 27,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/V2JkOFlKziEX_6MqyQ-mvg/o.jpg"
},


{
   'review_id': 28,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/BHnkIsQCVJrAtZdyF-X3kg/o.jpg"
},


{
   'review_id': 29,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/CyEudZ_U_rytkgMprVSWzg/o.jpg"
},


{
   'review_id': 30,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/VjzSnwBt3wyK0yshvOfGcQ/o.jpg"
},


{
   'review_id': 31,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/-xME7lRsZL1fhVJEZjmUTw/o.jpg"
},


{
   'review_id': 32,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/1HGcfloKI0ZUBsugWlNjdA/o.jpg"
},


{
   'review_id': 33,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/FhFfopM8lPWnrk29Mb_eQQ/o.jpg"
},


{
   'review_id': 34,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/9D2D5GL5rxuND0wUx9BeSQ/o.jpg"
},


{
   'review_id': 35,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/3DFLEhv-6U5v9RwegDZ9kQ/o.jpg"
},


{
   'review_id': 36,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/0MtqNMbOPd31LyWi3p-rIA/o.jpg"
},


{
   'review_id': 37,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/FdiEx1NCa1hot-7pecHgYQ/o.jpg"
},


{
   'review_id': 38,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/NAgPcA1uIT3tmzgIV2gdcg/o.jpg"
},


{
   'review_id': 39,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/ccPAwjtZxaazLtoufFsNEg/o.jpg"
},


{
   'review_id': 40,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/eJxCNG2P3iPbPWXQ69j2OA/o.jpg"
},


{
   'review_id': 41,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/vFdcquZonMHAaQM5GV8UTw/o.jpg"
},


{
   'review_id': 42,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/cBr2NK8eI2pWfMqPYF-fPA/o.jpg"
},


{
   'review_id': 43,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/jtVCifiCWc2uCu64kTzO4g/o.jpg"
},


{
   'review_id': 44,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/nWlVWqBb2Ef8KWSCKnQ2pw/o.jpg"
},


{
   'review_id': 45,
   'preview': True,
   'review_image': "https://s3-media0.fl.yelpcdn.com/bphoto/CV1Tm4ErDXeZrqPAPcmTeQ/o.jpg"
}]

   for review in reviews:
      new_review = ReviewImage(
         review_id = review['review_id'],
         preview = review['preview'],
         review_image = review['review_image']
      )
      db.session.add(new_review)
   db.session.commit()


def undo_seed_review_images():
   if environment == "production":
      db.session.execute(f"TRUNCATE table {SCHEMA}.review_images RESTART IDENTITY CASCADE;")
   else:
      db.session.execute("DELETE FROM review_images")
   db.session.commit()
