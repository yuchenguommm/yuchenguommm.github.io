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

---

## Education
- **Ph.D. in Physics**, Tsinghua University (2023 – present)  
  GPA: 3.99/4.0, Rank 1/73  
- **B.Sc. in Physics**, Tsinghua University (2019 – 2023)  
  GPA: 3.94/4.0, Rank 1/54  

---

## Honors & Fellowships
- **National Scholarship for Ph.D. Students (博士生国奖)**, 2025  
- **NSFC Young Student Basic Research Project (国自然（博士研究生）)**, 2025  
- **Tsinghua University Special Scholarship (清华特奖)**, 2022  
- Outstanding Graduate & Outstanding Thesis of Tsinghua University and Beijing, 2023  

---

## Research Interests
- Tensor-network approaches for **quantum computation** and **open quantum systems**  
- **Topological quantum matter** and symmetry-protected phases  
- **Noise, dissipation, and entanglement** in realistic quantum devices  

---

## Selected Publications
<ul>
{% for post in site.publications reversed %}
  {% if post.selected == true %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}
</ul>

[Full publication list](/publications)

## Selected Talks
<ul>
{% for post in site.talks reversed %}
  {% if post.selected == true %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}
</ul>

[Full talk list](/talks)

---

## Academic Service
- Referee for **PRX, PRL, PRX Quantum, PRR, PRA, PRB**

---
