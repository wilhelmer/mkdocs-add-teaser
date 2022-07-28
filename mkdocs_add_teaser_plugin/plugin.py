from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
import re

class AddTeaserPlugin(BasePlugin):

    config_scheme = (
        ('teaser_class', config_options.Type(str, default='teaser')),
        ('add_to_meta', config_options.Type(bool, default=False)),
    )

    def on_page_content(self, html, page, config, files):
        # Find first paragraph on page
        first_paragraph = ""
        first_paragraph_text = ""
        result = re.search(r"<p>(.*?)<\/p>", html)
        if result is not None:
            first_paragraph = result.group()
            if result.group(1) is not None:
                first_paragraph_text = result.group(1)

        # Add teaser class
        if (first_paragraph != ""):
            html = html.replace(first_paragraph, first_paragraph.replace("<p>", "<p class='" + self.config["teaser_class"] + "'>"))

        # Create meta description based on the first paragraph of the page
        if (first_paragraph_text != "") and self.config["add_to_meta"] and not page.meta.get("description", None):
            # Strip HTML tags
            first_paragraph_text = re.sub('<[^<]+?>', '', first_paragraph_text)
            # Convert double quotes
            first_paragraph_text = first_paragraph_text.replace('"', '\'')
            page.meta["description"] = first_paragraph_text
           
        return html
