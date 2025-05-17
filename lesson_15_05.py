class User:
    def __init__(self,name: str, mail: str, password: str ):
        self.__name = name
        self.__mail = mail
        self.__password = password

    def get_name(self):
        return self.__name
    def get_mail(self):
        return self.__mail
    def get_password(self):
        return '*' * self.__password 
    
    def set_name(self, new_name):
        self.__name = new_name
    def set_mail(self, new_mail):
        if '@' in new_mail:
            self.__mail = new_mail
    def set_password(self, old_pass: str, new_password):
        if old_pass == self.__password and len(new_password) == 8:
            self.__password = new_password

