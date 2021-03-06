 # Copyright 2014 Google Inc. All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #   http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License

import os
import jinja2
import webapp2
import random
import re

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

    def choose_template_from_url(self, url):

        path = re.compile('/devsummit/([^/]*)');

        deeplink_path = path.match(url).group(1)
        deeplink_paths = [
            'schedule',
            'sessions',
            'attendee-information',
            'get-involved',
            'about-chrome-dev-summit']

        deeplink_class = ''

        if (deeplink_path in deeplink_paths):
            deeplink_class = 'deeplink-' + deeplink_path

        return {
            'path': 'dist/index.html',
            'data': {
                'deeplink_class': deeplink_class,
                'livestreamimage': random.randrange(1,5,1),
                'section': 'Home'
            }
        }

    def get(self, url):

        template_data = self.choose_template_from_url(url)
        template = JINJA_ENVIRONMENT.get_template(template_data['path'])
        self.response.write(template.render(template_data['data']))

app = webapp2.WSGIApplication([
    ('(.*)', MainPage),
], debug=False)
