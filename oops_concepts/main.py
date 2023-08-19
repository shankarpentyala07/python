from user import User
from post import Post

user1 = User("shankar","shankarpentyala@gmail.com","password","platform_engineer")
user1.get_user_data()

print(f"user1 name is {user1.user_name}")

user1.change_job_title("software Engineer")
user1.get_user_data()

user1_post = Post("Hi Everybody",user1.user_name)
user1_post.get_post()

