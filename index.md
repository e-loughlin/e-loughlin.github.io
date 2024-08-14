---
title: "Evan Loughlin"
layout: splash
sticky: false
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/Mountains.jpeg
excerpt: "Software Engineer / Machine Learning"  
---

<!-- <center> -->
<!--   <img src="/assets/images/EvanFace.jpg" style="max-width: 180px; border-radius: 50%;" alt="Evan Loughlin">  -->
<!--   <div class="half-line"><br></div> -->
<!-- </center> -->

<h3 class="archive__subtitle">Recent posts</h3>
{% if paginator %}
  {% assign posts = paginator.posts %}
{% else %}
  {% assign posts = site.posts %}
{% endif %}

{% assign entries_layout = page.entries_layout | default: 'grid' %}
<div class="entries-{{ entries_layout }}">
  {% for post in posts %}
    {% include archive-single.html type=entries_layout %}
  {% endfor %}
</div>

<div id="feed"></div>
