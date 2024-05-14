# Класс Post описывает публикацию от пользователя в сети: – никнейм пользователя, – время публикации,
# – количество лайков, – текст сообщения, – список комментариев.
# Конструктор класса получает автора, устанавливает время, зануляет количество ругательств, а для комментариев создает
# списочный массив. Добавить метод, позволяющий поставить лайк сообщению.
import datetime


class Post:
    def __init__(self, username, text):
        self.username = username
        self.time_publication = datetime.datetime.now()
        self.likes = 0
        self.text = text
        self.comments = []


    def to_like_post(self):
        self.likes += 1


    def get_time(self):
        self.time_publication = datetime.datetime.now()
        return self.time_publication

    def add_comment(self, comment):
        self.comments.append(comment)


post = Post('John', 'Breaking news')
print(post.text)
print(f'Initial likes {post.likes}')
post.to_like_post()
print(f'Update likes {post.likes}')
print(post.time_publication)
post.add_comment('hi')
print(post.comments)
