import logging
logging.basicConfig(level=logging.DEBUG)

def check_users(current_users, new_users):
    pass

if __name__=="__main__":
    current_us = ['chris','haritha','sally','darnell','superman']
    new_us = ['george','ringo','Superman','hannibal','kai']
    check_users(current_us, new_us)

current_users = [user.lower() for user in current_us]

for avail_users in new_us:
    if avail_users.lower() in current_users:
        print(avail_users + " is not available. Please enter new username.")
    else:
        print(avail_users + " is available.")
