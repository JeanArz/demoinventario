import web

db_host = 'gk90usy5ik2otcvi.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'yt0qg4y68pc921rv'
db_user = 'ohz7uswsh4s4hipu'
db_pw = 'b2s31qp04qmo5atr'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )