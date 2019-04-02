# mkdocs-add-teaser

A MkDocs plugin to add a custom CSS class to the first paragraph after heading 1.

## Configuration

```yaml
# excerpt from mkdocs.yml:

plugins:
    - search
    - mkdocs-add-teaser:
        teaser_class: "teaser"
```

## Usage

### HTML before processing

This is the HTML that Markdown will produce:

```html
<h1 id="example-topic">Example Topic<a class="headerlink" href="#example-topic" title="Permanent link">#</a></h1>
<p>First paragraph</p>
```

### HTML after processing

This is the HTML after this plugin has run:

```html
<h1 id="example-topic">Example Topic<a class="headerlink" href="#example-topic" title="Permanent link">#</a></h1>
<p class="teaser">First paragraph</p>
```