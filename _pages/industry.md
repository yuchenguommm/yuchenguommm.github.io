---
layout: archive
title: "Industry"
permalink: /industry/
author_profile: true
---

{% include base_path %}

Alongside my doctoral work I have spent time building quantum software in a startup setting and
working on quantitative research in finance. This page collects that side of my work; the academic
record lives on the [Publications](/publications/) and [CV](/cv/) pages.

## FieldQuantum — Founding Partner, Head of Quantum Algorithms
*Feb 2026 – Aug 2026*

FieldQuantum is a venture-backed quantum computing startup of roughly 50 staff, which has raised
¥245M from investors including **Sequoia China** and **InnoAngel**. I joined as a founding partner and
built the quantum algorithm team from scratch, owning its technical roadmap, hiring, and delivery.

**What I worked on**

- **[fieldqkit](https://github.com/FieldQuantum/fieldqkit)** — shipped an open-source Python SDK that
  connects users to quantum hardware: a unified interface across multiple cloud platforms, with
  automatic transpilation, error mitigation, and variational algorithms built in.
- **Large-scale molecular simulation** — led a programme simulating systems of up to **12,000 atoms**,
  combining tensor-network and classical-quantum hybrid methods.
- **Real-time quantum error correction** — led the effort behind the company's whitepaper on the
  real-time QEC system stack ([arXiv:2605.30765](https://arxiv.org/abs/2605.30765)), which sets out
  the decoding-latency and control-stack requirements for closing the error-correction loop within a
  device's coherence budget.
- **Automated ansatz discovery** — designed an evolutionary search over variational ansätze built on
  **AlphaEvolve**, replacing hand-designed circuit families with an automated search procedure.

## Optiver — Quantitative Research Intern
*Offer accepted; internship summer 2027*

The offer followed **PhD QuantFocus**, a selective Optiver programme covering mental arithmetic,
options and contract pricing, market-making strategy design, and factor research.

In the programme's trading-strategy competition — a timed build ranked against the full cohort
across nine parameter regimes — I **placed first**, finishing roughly **30% ahead of second place** and
submitting the only entry that was profitable in every regime.

## Technical Toolkit

- **Languages** — Python (expert)
- **Numerical & optimisation** — large-scale linear algebra, tensor contraction, MILP (Gurobi),
  Monte Carlo, stochastic optimisation
- **Machine learning & data** — PyTorch, NumPy/SciPy, evolutionary search

<style>
.page__content p,
.page__content li {
  text-align: justify;
  text-justify: inter-word;
}
</style>
