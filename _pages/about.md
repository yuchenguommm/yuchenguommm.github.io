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

I'm a **fourth-year Ph.D. student** in the [Department of Physics](https://www.phys.tsinghua.edu.cn/), [Tsinghua University](https://www.tsinghua.edu.cn/), working on tensor-network approaches to **quantum computation**, **open quantum systems**, and **topological phases**. My long-term goal is to develop theoretical and experimental strategies to characterize and control quantum phases in realistic noisy quantum systems. I am very fortunate to be advised by **Prof. Shuo Yang** ([homepage](https://sites.google.com/view/shuoyang1984)).

I am based in Beijing, and am in Hong Kong from September 2026 to January 2027 as a Junior Research Assistant at the Chinese University of Hong Kong.
### Research Focus
- Developing new quantum computation techniques  
- Discovering novel topological quantum matter  
- Exploring the interplay between noise/dissipation and entanglement
- Rigorous analysis of quantum algorithms, including cryptographic applications

## News / Updates
- **Sep 2026** — Our theory–experiment collaboration on non-Hermitian parent Hamiltonians is published in **Phys. Rev. Lett. 137, 110401** — the first experimental realization of NH parent Hamiltonians, with **Prof. Peng Xue**'s group.  
- **Sep 2026 – Jan 2027** — Visiting the **Chinese University of Hong Kong** as a Junior Research Assistant.  
- **2025** — **National Scholarship for Ph.D. Students**; **NSFC Young Student Basic Research Project**.  
- **New preprints** — Quantum criticality in open systems from the purification perspective ([arXiv:2602.21979](https://arxiv.org/abs/2602.21979)); tensor-network readout error mitigation ([arXiv:2606.25974](https://arxiv.org/abs/2606.25974)); rigorous lemmas for Simon's dihedral-coset algorithm ([arXiv:2608.16598](https://arxiv.org/abs/2608.16598)).

## Selected Publications

{% assign selected_pubs = site.publications | where: "selected", true | sort: "priority" %}
<ul>
{% for post in selected_pubs %}
  <li><b><a href="{{ post.paperurl }}">{{ post.title }}</a></b><br/>
  {{ post.citation | replace: "Yuchen Guo", "<b>Yuchen Guo</b>" }}<br/>
  {{ post.excerpt }}</li>
{% endfor %}
</ul>

👉 Full list: see **[Publications](/publications/)**.

## CV · Service · Contact

- 📄 **[Full CV (PDF)](/assets/CV.pdf)** — last updated Sep 2026  
- 📝 **Academic Service**: Referee for *PRX, PRL, PRX Quantum, PRR, PRA, PRB*  
- 🌍 **Profiles**:  
  [Email](mailto:guo-yc23@mails.tsinghua.edu.cn) · 
  [Google Scholar](https://scholar.google.com/citations?user=ZbaW22gAAAAJ&hl) (<small>automatically updated</small>) · 
  [ORCID](https://orcid.org/0000-0002-4901-2737) · 
  [ResearchGate](https://www.researchgate.net/profile/Yuchen-Guo-31) · 
  [Github](https://github.com/yuchenguommm)

<br/>
<img src="/images/scholar.png" alt="Google Scholar daily snapshot" />

<style>
.page__content p, 
.page__content li {
  text-align: justify;
  text-justify: inter-word;
}
</style>
