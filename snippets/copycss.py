# -*- coding: utf-8 -*-

"""
**Module Docstring:**
Copy the default style sheet out of the docutils package

"""

import os.path
import shutil
import docutils.writers.html4css1 as h

shutil.copy(os.path.dirname(h.__file__)+"/html4css1.css","../doc/_static/defaultStyle.css")