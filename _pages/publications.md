---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

## 1. Quantum Computation & Information

<ul>
{% for post in site.publications %}
  {% if post.tags contains "quantum-computation" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

## 2. Locally Purified Density Operators

<ul>
{% for post in site.publications %}
  {% if post.tags contains "lpdo" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

## 3. Non-Hermitian Physics & Open Systems

<ul>
{% for post in site.publications %}
  {% if post.tags contains "open-system" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

## 4. Strongly-Correlated Electron Systems

<ul>
{% for post in site.publications %}
  {% if post.tags contains "correlated-electrons" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

## Preprints / Under Review

<ul>
{% for post in site.preprints reversed %}
  {% include archive-single.html %}
{% endfor %}
<ul>