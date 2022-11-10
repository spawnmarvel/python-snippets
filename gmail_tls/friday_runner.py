import smtplib, ssl
import json
import logging

logging.basicConfig(filename="app.log", filemode="a", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level="INFO")
logging.warning('This will get logged to a file')
class FridayMail():

    def __init__(self):
        self.mail_from = None
        self.mail_to = None
        self.mail_to_added = None
        self.user_cred_key = None
        self.file_exists = None
        self.mail_list = []

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
            with open("C:\giti2022\python-snippets\gmail_tls\config.json") as json_file:
                data = json.load(json_file)
                # print(str(type(data)))
                # print(data["configuration"])
                self.mail_from = data["configuration"]["mailfrom"]
                self.mail_to = data["configuration"]["mailto"]
                self.mail_to_added = data["configuration"]["mailto_added"]
                self.mail_list.append(self.mail_to)
                self.mail_list.append(self.mail_to_added)
                self.user_cred_key = data["configuration"]["usercred"]
                self.file_exist = True
        except FileNotFoundError as file_error:
            print(file_error)

    def send_gmail(self):
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:  
                email_address = self.mail_from
                email_password = self.user_cred_key
                connection.login(email_address, email_password )
                for mail_people in self.mail_list:

                    connection.sendmail(from_addr=email_address, to_addrs=mail_people, 
                    msg= "subject:It's Friday!! Stay hard and have fun: \n\n Please view all URLS \n\n https://www.hulen.no/ \n https://kvarteret.no/ \n https://www.kunsthall.no/no/arrangement/ \n https://www.visitbergen.com/hva-skjer/konserter   ")
                    rv = mail_people.split("@")
                    logging.info("sent to: " + str(rv[1]))
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    friday = FridayMail()
    friday.get_key()
    print(friday.mail_from)
    friday.send_gmail()