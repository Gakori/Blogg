import unittest
from blog.models import User, Blog
from blog import db

class BlogModelTest(unittest.TestCase):
    
    def setUp(self):
        self.user_faith = User(username = "faith", password = "456789", email="faithgakori@gmail.com")
        self.new_Blog = Blog(title="code", body = "coding rocks", user_id =self.user_faith.id )
        
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'code')
        self.assertEquals(self.new_blog.body,"blogs")
        self.assertEquals(self.new_blog.user_id, self.user_faithgakori.id)
        
    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(lenblogs.query.all())>0)
        
    def test_get_blogs(self):
        self.new_blog.save_blog()
        blogs =blogs.get_blogs()
        self.assertTrue(len(blogs)==1)