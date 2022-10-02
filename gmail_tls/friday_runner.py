import smtplib 
import json

class FridayMail():

    def __init__(self):
        self.mail_from = None
        self.mail_to = None
        self.user_cred_key = None
        self.file_exists = None

    def get_key(self):
        """Example json 
        {
            "configuration": {
            "mailfrom": "xxx@mail.com",
            "mailto": "yyyyy@mail.com",
            "usercred": "xxxxyyyyzzzzz"
            }
        }
        """
        try:
            # could store this in keyvault or an env
            with open("config.json") as json_file:
                data = json.load(json_file)
                # print(str(type(data)))
                # print(data["configuration"])
                self.mail_from = data["configuration"]["mailfrom"]
                self.mail_to = data["configuration"]["mailto"]
                self.user_cred_key = data["configuration"]["usercred"]
                self.file_exist = True
        except FileNotFoundError as file_error:
            print(file_error)

    def send_gmail(self):
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:  
                email_address = self.mail_from
                email_password = self.user_cred_key
                connection.login(email_address, email_password )
                connection.sendmail(from_addr=email_address, to_addrs=self.mail_to, 
                msg="subject:It's Friday !!! \n\n Please view the check all URLS \n\n www.ba.no")
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    friday = FridayMail()
    friday.get_key()
    print(friday.mail_from)
    friday.send_gmail()