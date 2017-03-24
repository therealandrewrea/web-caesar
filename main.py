#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Web Caesar</title>
    </head>
        <body>
        """

page_footer = """
</body>
</html>
"""

textarea = """
<form method="post">
    <textarea name="text" style="height: 100px; width: 400px;"></textarea>
        <br>
    <input type="submit" value="Encrypt!"/>
    """

class MainHandler(webapp2.RequestHandler):

    def get(self):
        message = "Test me Ssage!"
        encrypted_message = caesar.encrypt(message,13)
        encrypt_window = "<textarea>" + encrypted_message + "</textarea>"
        submit = """<input type="submit" value="Encrypt!"/>"""
        encrypt_form = """<form method="post">""" + encrypt_window + """</form>"""
        self.response.write(encrypt_form + submit)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
