#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Assignment 1 - Biography
-------------------------------

Your website must contain the following elements:

Index.html
A webpage that introduces your website. Explain to the user what they are going to see by coming here.
Biography.html
A webpage that tells the world a little about yourself. (2-3 paragraphs or so). This section can be completely made up – you don’t need to post personal details online if you do not want to.
Social.html
A webpage that tells the world how to contact you. Include elements like your facebook page, twitter account, email address, phone number. Use the anchor tag to provide links to all your content. This section can be completely made up – you do not need to post personal details online if you do not want to.
ImageGallery.html
A webpage that hosts at least 5 images of you/your family and friends, etc. NOTE: be sure that the photos you are using are not copyrighted or owned by another individual. Copyright and Trademark laws exist for a reason!
Resume.html
A webpage that replicates your resume. Use tables and/or divs to lay out the content on your page. Provide a link that will allow visitors to download a Word Document version of your resume.
One additional page
After you have created your pages create one additional page with any content you desire.

Your web pages elements must include:

Common banner
Common layout
Common menu and,
Common footer
"""

import sys

import dominate
from dominate.tags import *

sys.path.append("../../")
from PyPages import templates

from . import util

para_1 = """
Born in the year -5000000, Jack the Techno-Wizard came to a barren
void that would soon become our universe. Jack, alone in the void
became very well versed in these void magics
"""

para_2 = """
Using the tremendous might that Jack's magic gives him,
he single-handedly defeats the Devourer of Galaxies in
the year 500 B.C. Earth time.
"""

para_3 = """
In the year 1180, Jack accedently unleases a whirlwind, damaging Kyoto, Japan.
"""

_html = templates.html_head("CST8238 - Assignment 1")
with _html:
    with head():
        util.links()
    with body():
        with nav(cls="blue darken-2 white-text center"):
            h1("Biography")
        util.menu()

        with util.main():
            with div(cls="row center"):
                with div(cls="col"):
                    p(para_1)
                with div(cls="col"):
                    p(para_2)
                with div(cls="col"):
                    p(para_3)

    #FOOTER
    util.footer()
