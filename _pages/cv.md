---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

📄 A PDF version is available here: [Download full CV](../assets/CV.pdf) — last updated Sep 2026

Based in Beijing; in Hong Kong from September 2026 to January 2027.

## Education
- **Ph.D. in Physics**, Tsinghua University (2023 – 2028 expected)  
  GPA: 4.0/4.0, Rank 1/73  
- **Junior Research Assistant**, The Chinese University of Hong Kong (Sep 2026 – Jan 2027)  
- **B.Sc. in Physics**, Tsinghua University (2019 – 2023)  
  GPA: 3.94/4.0, Rank 1/120  
- **Shanghai High School** (2016 – 2019) — olympiad track in mathematics and physics  

## Experience
- **FieldQuantum** — Founding Partner and Head of Quantum Algorithms (Feb 2026 – Aug 2026)  
  Built and led the quantum algorithm team at a venture-backed startup of ~50 staff (¥245M raised,
  backed by Sequoia China and InnoAngel); shipped the open-source [`fieldqkit`](https://github.com/FieldQuantum/fieldqkit) SDK and led a
  12,000-atom molecular simulation programme. → [details](/industry/)
- **Optiver** — Quantitative Research Intern (offer accepted; summer 2027)  
  Offer following the selective PhD QuantFocus programme; placed first in the trading-strategy
  competition. → [details](/industry/)
- **Tsinghua University** — Doctoral Researcher (2023 – present)  
  Tensor-network methods for quantum computation, open quantum systems, and topological matter,
  combining analytical derivation with large-scale numerical simulation.

## Competitions & Honors
- **Chinese Physics Olympiad — Gold Medal and National Team (国集)**, 2018. Top 50 nationally; admitted to Tsinghua ahead of the standard cycle.  
- **Tsinghua University Special Scholarship (清华特奖)**, 2022. Highest student honour at Tsinghua; ten recipients university-wide per year.  
- **National Scholarship for Ph.D. Students (博士生国奖)**, 2025  
- **NSFC Young Student Basic Research Project (国自然博士生专项, independent grant)**, 2025  
- **Outstanding Graduate** of Tsinghua University and Beijing (清华/北京优秀毕业生), 2023  
- **Outstanding Bachelor Thesis** of Tsinghua University and Beijing (清华/北京优秀毕设), 2023  

## Research Interests
- Tensor-network approaches for **quantum computation** and **open quantum systems**  
- **Topological quantum matter** and symmetry-protected phases  
- **Noise, dissipation, and entanglement** in realistic quantum devices  
- Rigorous analysis of **quantum algorithms**, including cryptographic applications  

## Technical Skills
- **Languages**: Python (expert)  
- **Numerical and optimisation**: large-scale linear algebra, tensor contraction, MILP (Gurobi), Monte Carlo, stochastic optimisation  
- **Machine learning and data**: PyTorch, NumPy/SciPy, evolutionary search  

## Research Output
**13 journal papers**, 12 of them as first or co-first author, in *Phys. Rev. X*, *Phys. Rev. Lett.* (×3), *PRX Quantum*, *Phys. Rev. B*, *Phys. Rev. Research* (×2), *Rep. Prog. Phys.*, *npj Quantum Information*, *Communications Physics*, *Chinese Physics Letters*, and *EPJ Quantum Technology*; plus **3 first-authored preprints** under review.

Invited and contributed talks include the **APS Global Physics Summit** (2025) and the **Asia-Pacific Physics Conference** (2025).

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

## Other
- First and corresponding author of a cryptography proofs paper on the Simon dihedral coset problem ([ePrint 2026/1714](https://eprint.iacr.org/2026/1714)).  
- Physics olympiad coach for several years.  
- Writes a long-running essay column on science and technology.  
- Classical pianist; performs each semester — see [Personal Life](/portfolio/).  

<style>
.page__content p, 
.page__content li {
  text-align: justify;
  text-justify: inter-word;
}
</style>
