---
layout: default
title: Notes
---
<h3>My math notes:</h3>

<ul>
  {% for post in site.categories.math %}
    {% if post.url %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

---