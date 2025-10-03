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
- **Ph.D. Candidate in Physics**, Tsinghua University (2023 – present)  
  GPA: 3.99/4.0, Rank 1/73  
- **B.Sc. in Physics**, Tsinghua University (2019 – 2023)  
  GPA: 3.94/4.0, Rank 1/54  

## Honors & Fellowships
- **National Scholarship for Ph.D. Students (博士生国奖)**, 2025  
- **NSFC Young Student Basic Research Project (博士生国自然基金)**, 2025  
- **Tsinghua University Special Scholarship (the highest honor for only 10 students in each year, 清华特奖)**, 2022  
-	Outstanding Graduate of Tsinghua University and Beijing (清华/北京优毕), 2023
-	Outstanding Bachelor Thesis of Tsinghua University and Beijing (清华/北京优毕设), 2023

## Research Interests
- Tensor-network approaches for **quantum computation** and **open quantum systems**  
- **Topological quantum matter** and symmetry-protected phases  
- **Noise, dissipation, and entanglement** in realistic quantum devices  

## Selected Publications
{% assign selected_pubs = site.publications | where: "selected", true | sort: "priority" %}
<ul>
{% for post in selected_pubs %}
  <li><b><a href="{{ post.paperurl }}">{{ post.title }}</a></b><br/>
  {{ post.citation | replace: "Yuchen Guo", "<b>Yuchen Guo</b>" }}<br/></li>
{% endfor %}
</ul>

👉 [Full publication list](/publications)

## Academic Service
- Referee for **PRX, PRL, PRX Quantum, PRR, PRA, PRB**
