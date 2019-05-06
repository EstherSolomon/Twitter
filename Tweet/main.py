import webapp2
import jinja2
import os
from userAuth import UserAuth
from HomePage import HomePage,TweetUpload
from RegisterNewUser import RegisterNewUser
from UserDetailsProfile import UserDetailsProfile
from UserProfileEdit import UserProfileEdit
from EditUserTweets import EditUserTweets
from Search import Search
from SearchTweetContent import SearchTweetContent

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class DisplayPage(webapp2.RequestHandler):
    def get(self):
        template_values = UserAuth(self.request.uri).userTemplateVals()
        if template_values['user'] == '' or template_values['user'] is None:
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))
        else:
            if template_values['username'] == '' or template_values['username'] is None:
                self.redirect('/register')
            else:
                self.redirect('/home')


app = webapp2.WSGIApplication([
    ('/', DisplayPage),
    ('/home', HomePage),
    ('/register', RegisterNewUser),
    ('/profile', UserDetailsProfile),
    ('/profile-edit', UserProfileEdit),
    ('/tweet-edit', EditUserTweets),
    ('/search-user', Search),
    ('/search-content', SearchTweetContent),
    ('/upload', TweetUpload),
], debug=True)
