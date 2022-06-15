# mkdocs-add-teaser

An MkDocs plugin to customize the first paragraph of your pages, and to use it as the page's meta description.

This is useful if the first paragraph of your pages 

* contains information that should stand out from the rest of the text, e.g., should be printed in bold ("teaser" text)
* should appear as the page description in search engines (for SEO).

The plugin detects and uses the first paragraph after the first heading 1 in all pages of your project.

## Installation

Install the package with pip:

```
pip install mkdocs-add-teaser
```

Enable the plugin in your mkdocs.yml:

```yaml
plugins:
    - search
    - mkdocs-add-teaser:
        teaser_class: "teaser"
        add_to_meta: false
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

Add the CSS class to your extra CSS file. See examples below.

### CSS Examples

#### Use bold text

```css
.teaser {
    font-weight: bold;
}
```

#### Use larger font

```css
.teaser {
    font-size: 120%;
}
```

#### Use different color

```css
.teaser {
    color: darkgray;
}
```

#### Use all of the above

```css
.teaser {
    font-weight: bold;
    font-size: 120%;
    color: darkgray;
}
```

## Usage

The following options are provided to configure the output:

* `add_to_meta`: If set to `true`, the teaser text will be added to the page's meta description. Existing meta descriptions will be replaced. Defaults to `false`.

## How it works

### HTML before processing

This is the HTML that Markdown will produce:

```html
<h1 id="...">...</h1>
<p>First paragraph</p>
```

### HTML after processing

This is the HTML after this plugin has run:

With `add_to_meta` set to `false` (default):

```html
<h1 id="...">...</h1>
<p class="teaser">First paragraph</p>
```

With `add_to_meta` set to `true`:

```html
<meta content="description" content="First paragraph">
...
<h1 id="...">...</h1>
<p class="teaser">First paragraph</p>
```
