from app.models import db, BusinessImage, environment, SCHEMA

# Business image seeder
def seed_business_image():
    name1 = BusinessImage(
        business_id = 1,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/e7-_gIAg2Xe3QyeAQXoGAA/o.jpg"
    )
    name2 = BusinessImage(
        business_id = 1,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/0tT4HhAGordykx1-GYDF1w/o.jpg"
    )
    name3 = BusinessImage(
        business_id = 1,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/k2z0XH1FcnpCwBOWaGhVhQ/o.jpg"
    )
    name4 = BusinessImage(
        business_id = 1,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/PxyS3ZEJJF0HT0JKfinJzw/o.jpg"
    )
    name5 = BusinessImage(
        business_id = 1,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/yC26v0hWhpiNqDAYHpRUNQ/o.jpg"
    )
    name6 = BusinessImage(
        business_id = 1,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/NaXoq2zZFTY6pVlLO7_27w/o.jpg"
    )
    name7 = BusinessImage(
        business_id = 1,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/zAOPPC5_2Bv-H6rdOnEYmw/o.jpg"
    )
    name8 = BusinessImage(
        business_id = 2,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/s1b214-_eCapaEek4rQJqw/o.jpg"
    )
    name9 = BusinessImage(
        business_id = 2,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/-GipjpBVrIUKK9PQtdwe8g/o.jpg"
    )
    name10 = BusinessImage(
        business_id = 2,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/05i-5DOmQq8rgfoSsY3NUg/o.jpg"
    )
    name11 = BusinessImage(
        business_id = 2,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/pRovzc_FE9fdiw8BN42SYA/o.jpg"
    )
    name12 = BusinessImage(
        business_id = 2,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/yM79B3gVQfFt4h8DOZcppg/o.jpg"
    )
    name13 = BusinessImage(
        business_id = 2,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/YWCSF6slaI2A8KyCdcfoGQ/o.jpg"
    )
    name14 = BusinessImage(
        business_id = 2,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/gXBotyL321bW9L8DDY-GgA/o.jpg"
    )
    name15 = BusinessImage(
        business_id = 4,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/m6WV0LH8idydgvEpR158Lw/o.jpg"
    )
    name16 = BusinessImage(
        business_id = 4,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/9sslZRY7XcMRzXua9tScGA/o.jpg"
    )
    name17 = BusinessImage(
        business_id = 4,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/kggGX4Qb9ik7MQhA4Y1-Yw/o.jpg"
    )
    name18 = BusinessImage(
        business_id = 4,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/IQvOWgSynXUy8r9rr1Osag/o.jpg"
    )
    name19 = BusinessImage(
        business_id = 4,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/YROIvNwRgUaLvgq-tz4Ewg/o.jpg"
    )
    name20 = BusinessImage(
        business_id = 4,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/v6w_u-bW6vnKRFgfZi4xnQ/o.jpg"
    )
    name21 = BusinessImage(
        business_id = 4,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/me22WP362hpvDiLkMsk-Ww/o.jpg"
    )
    name22 = BusinessImage(
        business_id = 5,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/8pGLz1O_ZwaZV2_2ppU1vw/o.jpg"
    )
    name23 = BusinessImage(
        business_id = 5,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/E3J17mDFbDAYWcaoIjRxQw/o.jpg"
    )
    name24 = BusinessImage(
        business_id = 5,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/FF7JSOvwcAn_RxOMTp7MGA/o.jpg"
    )
    name25 = BusinessImage(
        business_id = 5,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/_9xjZ3dTl7pQ0e8T9QWr-A/o.jpg"
    )
    name26 = BusinessImage(
        business_id = 5,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/BmpJmlqXF513SyHs3OjJuw/o.jpg"
    )
    name27 = BusinessImage(
        business_id = 5,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/wVzs5nGSdcxZDFG8PSU0AQ/o.jpg"
    )
    name28 = BusinessImage(
        business_id = 5,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/wAW3XYc-vqYipRzMP67lQw/o.jpg"
    )
    name29 = BusinessImage(
        business_id = 6,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/9YrXO9YKZQPVgYEpuU5Crg/o.jpg"
    )
    name30 = BusinessImage(
        business_id = 6,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/j_YauB2WKeiQvHC1pgwUaQ/o.jpg"
    )
    name31 = BusinessImage(
        business_id = 6,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/BOBmrGrVSk6N3qB0ae2SKg/o.jpg"
    )
    name32 = BusinessImage(
        business_id = 6,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/4Ck4-j-2LlqJqP7Res-jJQ/o.jpg"
    )
    name33 = BusinessImage(
        business_id = 6,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/d7WWGTdcLy_lVBRIrX26Fw/o.jpg"
    )
    name34 = BusinessImage(
        business_id = 6,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/Wii__aeN3JwrGyyXdPgtYg/o.jpg"
    )
    name35 = BusinessImage(
        business_id = 6,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/i0kXa5H1tO8RO93lBmGm7w/o.jpg"
    )
    name36 = BusinessImage(
        business_id = 7,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/gc3eojH1nXvWC_YJS3mllg/o.jpg"
    )
    name37 = BusinessImage(
        business_id = 7,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/SKlsgq_XZEsQzyGdFL3k3Q/o.jpg"
    )
    name38 = BusinessImage(
        business_id = 7,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/O5xklkRNPgOCAuuqgEBgCQ/o.jpg"
    )
    name39 = BusinessImage(
        business_id = 7,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/b52qYt0yF2-dQuCbWxT3Fw/o.jpg"
    )
    name40 = BusinessImage(
        business_id = 7,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/lGTQ1crGVdjD9obWqRDmOQ/o.jpg"
    )
    name41 = BusinessImage(
        business_id = 7,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/0rdxUF0SYJlm1Ic6nhTmWg/o.jpg"
    )
    name42 = BusinessImage(
        business_id = 7,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/W93drKfwipkar2khGBHBqQ/o.jpg"
    )
    name43 = BusinessImage(
        business_id = 8,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/b_5pNZm46cMBpJTlFLAIAg/o.jpg"
    )
    name44 = BusinessImage(
        business_id = 8,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/3qGg2h_rUlVBijWTDUEIjQ/o.jpg"
    )
    name45 = BusinessImage(
        business_id = 8,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/uY9qoqCobOEUuxeDEQFp3w/o.jpg"
    )
    name46 = BusinessImage(
        business_id = 8,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/dUnQlzn8eSRu4H-eNHEvhA/o.jpg"
    )
    name47 = BusinessImage(
        business_id = 8,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/ub4bEM7_wH0Rlc9TDfbpbw/o.jpg"
    )
    name48 = BusinessImage(
        business_id = 8,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/BawSC8n5bfpHLujSkUuafA/o.jpg"
    )
    name49 = BusinessImage(
        business_id = 8,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/8UCZ-jx6JNnbZRC0ilQpLQ/o.jpg"
    )
    name50 = BusinessImage(
        business_id = 9,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/4r_S0wW-g4yeTFHRz4wwjQ/o.jpg"
    )
    name51 = BusinessImage(
        business_id = 9,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/14MNLFYkc5MKLvQA0VARDg/o.jpg"
    )
    name52 = BusinessImage(
        business_id = 9,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/BAghCieuitks2qiL5xBH2w/o.jpg"
    )
    name53 = BusinessImage(
        business_id = 9,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/PTFmb22fBrZskW0BERkt_g/o.jpg"
    )
    name54 = BusinessImage(
        business_id = 9,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/E3Lo8ggKnnwElb_aBu93lw/o.jpg"
    )
    name55 = BusinessImage(
        business_id = 9,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/-__uW-k3d6wz0P_3ecraKw/o.jpg"
    )
    name56 = BusinessImage(
        business_id = 9,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/v6DUbaM5fHH2AFbCX0QVYQ/o.jpg"
    )
    name57 = BusinessImage(
        business_id = 10,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/p8YiDn9am8r_0KWbCVP1ug/o.jpg"
    )
    name58 = BusinessImage(
        business_id = 10,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/bRV4YSF0T_f-ukJrlmbTTQ/o.jpg"
    )
    name59 = BusinessImage(
        business_id = 10,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/5oSo8cPWd9Gh6zlH5XESkg/o.jpg"
    )
    name60 = BusinessImage(
        business_id = 10,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/w85iJurZUm4gCdZ-MZDWiA/o.jpg"
    )
    name61 = BusinessImage(
        business_id = 10,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/xQF_zmbpfmLRFyDSKyhu1g/o.jpg"
    )
    name62 = BusinessImage(
        business_id = 10,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/lnLMkeesTmtdSYJta1YSgg/o.jpg"
    )
    name63 = BusinessImage(
        business_id = 10,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/LdVaU-69clg_UKgxv10qPw/o.jpg"
    )
    name64 = BusinessImage(
        business_id = 11,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/-Uwe10a0Rl4qsFW5yGq3sg/o.jpg"
    )
    name65 = BusinessImage(
        business_id = 11,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/WNKqe_dl7D8gh15gWtXwzQ/o.jpg"
    )
    name66 = BusinessImage(
        business_id = 11,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/OO0uGWKxfBTxKtwkKwqd2Q/o.jpg"
    )
    name67 = BusinessImage(
        business_id = 11,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/R2V3ZzrylUxdGW5xRetKCg/o.jpg"
    )
    name68 = BusinessImage(
        business_id = 11,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/FqQRltNxvYoWQu_RhuY8mg/o.jpg"
    )
    name69 = BusinessImage(
        business_id = 11,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/1BLK4AAwPQ_VWXOj-Q7dSA/o.jpg"
    )
    name70 = BusinessImage(
        business_id = 11,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/pVX049chlvqMjkss1rUY-Q/o.jpg"
    )
    name71 = BusinessImage(
        business_id = 12,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/OWr4t7xxv5PC5HFrhE0qag/o.jpg"
    )
    name72 = BusinessImage(
        business_id = 12,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/myHEL9YixbuYSaSKqwtBPA/o.jpg"
    )
    name73 = BusinessImage(
        business_id = 12,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/MD0LYrHykmFoGMLrUCuQvA/o.jpg"
    )
    name74 = BusinessImage(
        business_id = 12,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/MXCbAb1Mv5BrKayytdH3_Q/o.jpg"
    )
    name75 = BusinessImage(
        business_id = 12,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/CutjFtmxt6NCIIL4Lt8I9w/o.jpg"
    )
    name76 = BusinessImage(
        business_id = 12,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/IFKDtTZHDUoVTr1f4UZiUw/o.jpg"
    )
    name77 = BusinessImage(
        business_id = 12,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/81UGfvY0AoQ2biblKS-0nw/o.jpg"
    )
    name78 = BusinessImage(
        business_id = 13,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/DPdkvmpTeD6ejFg6etY7Dg/o.jpg"
    )
    name79 = BusinessImage(
        business_id = 13,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/5mh-lqmn8oD1RcKltmTGbg/o.jpg"
    )
    name80 = BusinessImage(
        business_id = 13,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/L5zJaFgVUheULTZuvDd8sQ/o.jpg"
    )
    name81 = BusinessImage(
        business_id = 13,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/jmuudfy7setzGcl-T4Lgfw/o.jpg"
    )
    name82 = BusinessImage(
        business_id = 13,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/vHpGIqv4UyNpDKJgtuHp2g/o.jpg"
    )
    name83 = BusinessImage(
        business_id = 13,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/vCWvtiRLzS7T4Dd_d4a0IQ/o.jpg"
    )
    name84 = BusinessImage(
        business_id = 13,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/TlmkWAADBiV2OpieXuvwtQ/o.jpg"
    )
    name85 = BusinessImage(
        business_id = 14,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/NeLDxcp9mIdGozl53JuEow/o.jpg"
    )
    name86 = BusinessImage(
        business_id = 14,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/ubCKhAYRfX_WUTH9STXZTQ/o.jpg"
    )
    name87 = BusinessImage(
        business_id = 14,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/9A4gGx-9q4ykU0wMmu35Cg/o.jpg"
    )
    name88 = BusinessImage(
        business_id = 14,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/t43s2D3D4o0My93914KLww/o.jpg"
    )
    name89 = BusinessImage(
        business_id = 14,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/TxoPNekJVu0NzI6tsJ5N0Q/o.jpg"
    )
    name90 = BusinessImage(
        business_id = 14,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/t4v6Q76XT5Q0x3A6ETpMPQ/o.jpg"
    )
    name91 = BusinessImage(
        business_id = 14,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/HXhlQ95kJm93KVbxVJlgmA/o.jpg"
    )
    name92 = BusinessImage(
        business_id = 15,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/vwHnKpSCNUDynOmBE3gksw/o.jpg"
    )
    name93 = BusinessImage(
        business_id = 15,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/0nz-JbuyEEPpfvwh4FhWwg/o.jpg"
    )
    name94 = BusinessImage(
        business_id = 15,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/z-B08wcXuXMX7-BkrgEO4g/o.jpg"
    )
    name95 = BusinessImage(
        business_id = 15,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/D-HPfo7GuTXIOHjQoEpWag/o.jpg"
    )
    name96 = BusinessImage(
        business_id = 15,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/i10a3cWQR7YJz9dWReU2OA/o.jpg"
    )
    name97 = BusinessImage(
        business_id = 15,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/u9fZFoiXOUB9Rz_2y-HSVA/o.jpg"
    )
    name98 = BusinessImage(
        business_id = 15,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/rJ8X_OgVwD54ywqU2YGazA/o.jpg"
    )
    name99 = BusinessImage(
        business_id = 3,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/WSmnubTmPhtDUzHxZN06gA/o.jpg"
    )
    name100 = BusinessImage(
        business_id = 3,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/Uzlo9kw_F1iCmVioZM9DUg/o.jpg"
    )
    name101 = BusinessImage(
        business_id = 3,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/bhv0rFBh4vc7SZbRdpGGbg/o.jpg"
    )
    name102 = BusinessImage(
        business_id = 3,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/EDIX52PNZbpa8PIBxjzZ2g/o.jpg"
    )
    name103 = BusinessImage(
        business_id = 3,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/gJ7dd7F1kRWvpXs3MjBSUg/o.jpg"
    )
    name104 = BusinessImage(
        business_id = 3,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/ttYnBrzM3ADc6Uqxz0bs8w/o.jpg"
    )
    name105 = BusinessImage(
        business_id = 3,
        business_image= "https://s3-media0.fl.yelpcdn.com/bphoto/tVsdG2lpjslyqZAO5_bSAg/o.jpg"
    )

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
    db.session.add(name15)
    db.session.add(name16)
    db.session.add(name17)
    db.session.add(name18)
    db.session.add(name19)
    db.session.add(name20)
    db.session.add(name21)
    db.session.add(name22)
    db.session.add(name23)
    db.session.add(name24)
    db.session.add(name25)
    db.session.add(name26)
    db.session.add(name27)
    db.session.add(name28)
    db.session.add(name29)
    db.session.add(name30)
    db.session.add(name31)
    db.session.add(name32)
    db.session.add(name33)
    db.session.add(name34)
    db.session.add(name35)
    db.session.add(name36)
    db.session.add(name37)
    db.session.add(name38)
    db.session.add(name39)
    db.session.add(name40)
    db.session.add(name41)
    db.session.add(name42)
    db.session.add(name43)
    db.session.add(name44)
    db.session.add(name45)
    db.session.add(name46)
    db.session.add(name47)
    db.session.add(name48)
    db.session.add(name49)
    db.session.add(name50)
    db.session.add(name51)
    db.session.add(name52)
    db.session.add(name53)
    db.session.add(name54)
    db.session.add(name55)
    db.session.add(name56)
    db.session.add(name57)
    db.session.add(name58)
    db.session.add(name59)
    db.session.add(name60)
    db.session.add(name61)
    db.session.add(name62)
    db.session.add(name63)
    db.session.add(name64)
    db.session.add(name65)
    db.session.add(name66)
    db.session.add(name67)
    db.session.add(name68)
    db.session.add(name69)
    db.session.add(name70)
    db.session.add(name71)
    db.session.add(name72)
    db.session.add(name73)
    db.session.add(name74)
    db.session.add(name75)
    db.session.add(name76)
    db.session.add(name77)
    db.session.add(name78)
    db.session.add(name79)
    db.session.add(name80)
    db.session.add(name81)
    db.session.add(name82)
    db.session.add(name83)
    db.session.add(name84)
    db.session.add(name85)
    db.session.add(name86)
    db.session.add(name87)
    db.session.add(name88)
    db.session.add(name89)
    db.session.add(name90)
    db.session.add(name91)
    db.session.add(name92)
    db.session.add(name93)
    db.session.add(name94)
    db.session.add(name95)
    db.session.add(name96)
    db.session.add(name97)
    db.session.add(name98)
    db.session.add(name99)
    db.session.add(name100)
    db.session.add(name101)
    db.session.add(name102)
    db.session.add(name103)
    db.session.add(name104)
    db.session.add(name105)
    db.session.commit()

def undo_seed_business_image():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.business_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM business_images")

    db.session.commit()
