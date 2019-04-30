import unittest
from app.models import Post,User
from flask_login import current_user
from app import db

class TestBlog(unittest.TestCase):

    def setUp(self):
        self.user_Manka = User(username = 'Manka',
                                 password = 'jhkk',
                                 email = 'manka@ms.com')

        self.new_blog = Post(id=12345,title='Post itself')

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.id,12345)
        self.assertEquals(self.new_post.title,'Post itself')

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)


    def test_get_post_by_id(self):

        self.new_post.save_post()
        got_posts = Post.get_post(12345)
        self.assertTrue(len(got_posts) == 1)
