---
permalink: /adventures/
layout: home
---

{% assign entries_layout = page.entries_layout | default: 'grid' %}
<section id="adventures" class="taxonomy__section">
  <h2 class="archive__subtitle">Adventures</h2>
  <div class="entries-{{ entries_layout }}">
    {% assign adventures_posts = site.tags.Adventures %}
    {% for post in adventures_posts %}
      {% include archive-single.html type=entries_layout %}
    {% endfor %}
  </div>
  <a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: 'Back to Top' }} &uarr;</a>
</section>


