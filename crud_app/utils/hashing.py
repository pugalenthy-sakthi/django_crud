import bcrypt

def gethashpwd(pwd):
  
  return bcrypt.hashpw(bytes(pwd,'utf-8'),bcrypt.gensalt())


def checkpwd(pwd,hpwd):
  
  return bcrypt.checkpw(pwd,hpwd)
  