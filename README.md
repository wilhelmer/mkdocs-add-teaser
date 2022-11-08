# mkdocs-add-teaser

An MkDocs plugin to customize the first paragraph of your pages, and to use it as the page's meta description.

This is useful if the first paragraph of your pages 

* contains information that should stand out from the rest of the text, e.g., should be printed in bold ("teaser" text)
* should appear as the page description in search engines (for SEO).

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
        teaser_class: 'teaser'
        add_to_meta: true
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

Add the CSS class to your extra CSS file. See examples below.

### CSS Examples

#### Use Bold Text

```css
.teaser {
    font-weight: bold;
}
```

#### Use Larger Font

```css
.teaser {
    font-size: 120%;
}
```

#### Use Different Color

```css
.teaser {
    color: darkgray;
}
```

#### Use All of the Above

```css
.teaser {
    font-weight: bold;
    font-size: 120%;
    color: darkgray;
}
```

## Usage

The following options are provided to configure the output:

* `add_to_meta`: If set to `true` and your page doesn't contain a meta description, the teaser text will be used as the meta description. Defaults to `false`.
* `teaser_class`: The CSS class to be applied to the first paragraph of your pages. Defaults to `teaser`.

### Disabling the Plugin

The teaser plugin can be disabled on specific pages using the front matter `hide` property. The teaser text will still be shown, but no CSS class will be applied, and the meta description won't be changed.

Add the following lines at the top of a Markdown file:

```md
---
hide:
  - teaser
---

# Document Title
...
```

## How It Works

### HTML before Processing

This is the HTML that Markdown will produce:

```html
<h1 id="...">...</h1>
<p>First paragraph</p>
```

### HTML after Processing

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
