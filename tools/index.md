---
title: Tools
nav:
  order: 2
  tooltip: Software and documentation
---

# {% include icon.html icon="fa-solid fa-wrench" %}Tools

Software developed in the lab, with documentation.

{% include section.html %}

{% include list.html component="card" data="projects" filter="group == 'featured'" %}

{% include list.html component="card" data="projects" filter="!group" style="small" %}
