---
layout: post
title: "Postmaking Tools"
date: 2016-06-12 19:38:39
---
Upon starting the blog with Github Pages' integrated Jekyll, I was disappointed by the lack of tools to handle making posts. So, rather than being annoyed, I made my own.

<script src="https://gist.github.com/wanderso/8f25549cc3bd772e9a7801d03f65689e.js"></script>

This first shell script is small and simple, but it handles all the needed git commands to update, and still has an option to give unique commit messages. But if git scared us, we wouldn't be on github, so the scripting can't stop here. Instead, I added a 'postmaker' that takes a plaintext file and converts it to markdown for a post in the Jekyll format. 

<script src="https://gist.github.com/wanderso/a6d6f88191530a6d17a7a27dd4ff03c5.js"></script>

This takes posts in a 'queue' folder and adds them to _post. Don't forget to use the new python 'with' keyword for your file needs - it's so much more convenient than try/catch/finally blocks.
