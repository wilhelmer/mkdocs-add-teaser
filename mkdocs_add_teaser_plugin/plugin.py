import os
import sys
import re
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

class AddTeaserPlugin(BasePlugin):

    config_scheme = (
        ('teaser_class', config_options.Type(mkdocs_utils.string_types, default='teaser')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_post_page(self, output_content, page, config):
        output_content = re.sub(r"(<h1.*?<\/h1>\n)<p>", r"\1<p class='" + self.config["teaser_class"] + "'>", output_content, 1)
        return output_content