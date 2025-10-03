---
permalink: /
title: "Yuchen Guo (he/him/his)"
excerpt: "Yuchen Guo"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

*"To establish a unifying framework that connects theoretical tensor-network tools with experimental quantum computing platforms, enabling robust characterization and control of open-system quantum phases."*

I'm a **third-year Ph.D. student** in the [Department of Physics](https://www.phys.tsinghua.edu.cn/), [Tsinghua University](https://www.tsinghua.edu.cn/), working on tensor-network approaches to **quantum computation**, **open quantum systems**, and **topological phases**. My long-term goal is to develop theoretical and experimental strategies to characterize and control quantum phases in realistic noisy quantum systems. I am very fortunate to be advised by **Prof. Shuo Yang** ([homepage](https://sites.google.com/view/shuoyang1984)).
### Research Focus
- Developing new quantum computation techniques  
- Discovering novel topological quantum matter  
- Exploring the interplay between noise/dissipation and entanglement

## News / Updates
- **Oct 2025** — Oral presentation at **APPC16** (Asia Pacific Physics Conference).  
- **Spring–Summer 2026 (planned)** — Visiting PhD student at **Max Planck Institute of Quantum Optics (MPQ)** with **Prof. J. I. Cirac**.  
- **Recent honors** — National Scholarship for Ph.D. Students; **NSFC Young Student Basic Research Project (PhD)**.  
- **Manuscript status** — *A New Framework for Quantum Phases in Open Systems* (ROPP), revised and resubmitted.

## Selected Publications

<ul>
{% for post in site.publications reversed %}
  {% if post.selected == true %}
    {% if post.citation contains "Phys. Rev. X 15, 021060 (2025)" %}
      <li><b><a href="{{ post.paperurl }}">{{ post.title }}</a></b><br/>
      <i>{{ post.venue }}</i><br/>
      <small>{{ post.excerpt }}</small></li>
    {% endif %}
    {% if post.citation contains "PRX Quantum 3, 040313 (2022)" %}
      <li> ... </li>
    {% endif %}
    {% if post.citation contains "Phys. Rev. Lett. 135, 116504 (2025)" %}
      <li> ... </li>
    {% endif %}
    {% if post.citation contains "Commun. Phys. 7, 322 (2024)" %}
      <li> ... </li>
    {% endif %}
    {% if post.citation contains "Phys. Rev. B 111, L201108 (2025)" %}
      <li> ... </li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

👉 Full list: see **[Publications](/publications/)**.

## CV · Service · Contact

- 📄 **[Full CV (PDF)](/assets/CV.pdf)** — last updated Oct 2025  
- 📝 **Academic Service**: Referee for *PRX, PRL, PRX Quantum, PRR, PRA, PRB*  
- 🌍 **Profiles**:  
  [Email](mailto:guo-yc23@mails.tsinghua.edu.cn) · 
  [Google Scholar](https://scholar.google.com/citations?user=ZbaW22gAAAAJ&hl) (<small>自动更新：每日一次</small>) · 
  [ORCID](https://orcid.org/0000-0002-4901-2737) · 
  [ResearchGate](https://www.researchgate.net/profile/Yuchen-Guo-31)  

<br/>
<img src="/images/scholar.png" alt="Google Scholar daily snapshot" />
