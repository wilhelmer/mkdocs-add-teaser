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
        ('teaser_class', config_options.Type(str, default='teaser')),
        ('add_to_meta', config_options.Type(bool, default=False)),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_post_page(self, output_content, page, config):
        if self.config["add_to_meta"]:
            # Add teaser text to meta description
            teaser_text = re.search(r"<h1.*?<\/h1>\n<p>(.*?)<\/p>", output_content)
            if teaser_text and teaser_text.group(1): 
                teaser_text = teaser_text.group(1)
                # Strip HTML tags
                teaser_text = re.sub('<[^<]+?>', '', teaser_text)
                # Convert double quotes
                teaser_text = re.sub('"', '\'', teaser_text)
                if teaser_text:
                    # Look for existing meta description
                    meta_description = re.search(r"<meta name=\"description\" content=\"(.*?)\">", output_content)
                    if meta_description and meta_description.group(1):
                        # Replace existing
                        output_content = re.sub(meta_description.group(1), teaser_text, output_content, 1)
                    else:
                        # Create new, append to head
                        output_content = re.sub("<head>", "<head>\n<meta name=\"description\" content=\"" + teaser_text + "\">", output_content, 1)
        
        # Add teaser class
        output_content = re.sub(r"(<h1.*?<\/h1>\n)<p>", r"\1<p class='" + self.config["teaser_class"] + "'>", output_content, 1)
                   
        return output_content
