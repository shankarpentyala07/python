class User:
    def __init__(self, name, email, password, current_job_title) -> None:
        self.user_name = name
        self.user_email = email
        self.user_password = password
        self.user_job = current_job_title


    def get_user_data(self):
        print(f"{self.user_name} works as {self.user_job} and can be contacted at {self.user_email}")

    
    def change_password(self,new_password):
        self.user_password = new_password

    
    def change_job_title(self,job_title):
        self.user_job = job_title