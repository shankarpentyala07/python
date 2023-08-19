class Post:
    def __init__(self,message,user) -> None:
        self.user_post = message
        self.user = user


    def get_post(self):
        print(f'{self.user} posted {self.user_post}')