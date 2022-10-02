{option:title=Quickstart Guide}

This guide will teach you the basics of bSSG. If you have not yet installed it, read the installation guide [here](https://bevan0.github.io/bSSG/install). This page is still a WIP, as-is bSSG itself.

## Get started
Running the command `bssg-generate` will generate your site. Of course, you haven't written your site yet so it will do nearly nothing. But, this command will create some folders for you: `content`, `templates`, and `generated-site`. Place HTML templates in `templates` and Markdown content in `content`. When you next run `bssg-generate`, the site will be generated using what you've put in those folders.

## Your first template
Create a file called `template.html` in the `templates` folder; this will act as the default template for all pages on your site. This is standard HTML, with a few additions:

* Entering `{subst!title}` will replace (substitute, hence `subst`) itself with the pages title, inferred from either the Markdown file name or as it was specified in the Markdown file.
* Entering `{subst!content}` will substitute itself with the content of the Markdown file.
* Entering `{subst!anything else}` will substitute itself with the content of the specified Markdown file.
This template can be a simple heading and paragraph for now.

## Writing content
Now, you can write your content files. In the content folder, create a file called `index.md`. This file is raw Markdown, plus the above additions and these additional additions:

* Entering `{option!title=Title}` will change what `{subst!title}` substitutes itself as, though this will not change where the file is saved.
* Entering `{option!template=template}` will change the template the page is using from the default `template.html`.

## Generating the new site
Run `bssg-generate` in the root directory of your project to generate the site! The generated HTML will be stored in the `generated-site` folder. Inspect it all you want, you've created a site and learned the core features of bSSG!

## Other tips for advanced development
* When working further, running `bssg-watch` will regenerate the site whenever a change is detected.
* Appending content file names with an `_` will skip that file during generation. This is useful for content pages that have no content that are substituted in multiple pages.