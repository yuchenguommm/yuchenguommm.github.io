---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

📄 A PDF version is available here: [Download full CV](../assets/CV.pdf)

## Education
- **Ph.D. in Physics**, Tsinghua University (2023 – present)  
  GPA: 3.99/4.0, Rank 1/73  
- **B.Sc. in Physics**, Tsinghua University (2019 – 2023)  
  GPA: 3.94/4.0, Rank 1/54  

## Honors & Fellowships
- **National Scholarship for Ph.D. Students (博士生国奖)**, 2025  
- **NSFC Young Student Basic Research Project (国自然（博士研究生）)**, 2025  
- **Tsinghua University Special Scholarship (清华特奖)**, 2022  
- Outstanding Graduate & Outstanding Thesis of Tsinghua University and Beijing, 2023  

## Research Interests
- Tensor-network approaches for **quantum computation** and **open quantum systems**  
- **Topological quantum matter** and symmetry-protected phases  
- **Noise, dissipation, and entanglement** in realistic quantum devices  

## Selected Publications
<ul>
{% for post in site.publications reversed %}
  {% if post.selected == true %}
    {% if post.citation contains "Phys. Rev. X 15, 021060 (2025)" %}
      <li><b><a href="{{ post.paperurl }}">{{ post.title }}</a></b><br/>
      <i>{{ post.citation }}</i><br/><li>
    {% endif %}
    {% if post.citation contains "PRX Quantum 3, 040313 (2022)" %}
      <li><b><a href="{{ post.paperurl }}">{{ post.title }}</a></b><br/>
      <i>{{ post.citation }}</i><br/><li>
    {% endif %}
    {% if post.citation contains "Phys. Rev. Lett. 135, 116504 (2025)" %}
      <li><b><a href="{{ post.paperurl }}">{{ post.title }}</a></b><br/>
      <i>{{ post.citation }}</i><br/><li>
    {% endif %}
    {% if post.citation contains "Commun. Phys. 7, 322 (2024)" %}
      <li><b><a href="{{ post.paperurl }}">{{ post.title }}</a></b><br/>
      <i>{{ post.citation }}</i><br/><li>
    {% endif %}
    {% if post.citation contains "Phys. Rev. B 111, L201108 (2025)" %}
      <li><b><a href="{{ post.paperurl }}">{{ post.title }}</a></b><br/>
      <i>{{ post.citation }}</i><br/><li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

👉 [Full publication list](/publications)

## Academic Service
- Referee for **PRX, PRL, PRX Quantum, PRR, PRA, PRB**
