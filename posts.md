---
layout: default
title: Posts
---

# Posts

Here you can find a list of my posts by topic.

{% assign rawtags = "" %}
{% for post in site.posts %}
  {% assign ttags = post.tags | join:'|' | append:'|' %}
  {% assign rawtags = rawtags | append:ttags %}
{% endfor %}
{% assign rawtags = rawtags | split:'|' | sort %}

{% comment %}
=======================
The following part removes dulpicated tags and invalid tags like blank tag.
=======================
{% endcomment %}
{% assign tags = "" %}
{% for tag in rawtags %}
  {% if tag != "" %}
    {% if tags == "" %}
      {% assign tags = tag | split:'|' %}
    {% endif %}
    {% unless tags contains tag %}
      {% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
    {% endunless %}
  {% endif %}
{% endfor %}

{% for tag in tags %}
  <a href="#{{ tag | slugify }}"> {{ tag }} </a>
{% endfor %}

{% for tag in tags %}
  <h4 id="{{ tag | slugify }}">{{ tag }}</h4>
  <ul>
   {% for post in site.posts %}
     {% if post.tags contains tag %}
     <li> <a href="{{ post.url }}"> {{ post.title }} </a> </li>
     {% endif %}
   {% endfor %}
  </ul>
{% endfor %}

---