<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=190&section=header&text=Fadi%20%C2%B7%200xmortuex&fontSize=48&fontColor=ffffff&animation=fadeIn&desc=compilers%20%C2%B7%20kernels%20%C2%B7%20browsers%20%C2%B7%20security%20tools&descSize=18&descAlignY=62" alt="banner" />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1200&center=true&vCenter=true&width=620&lines=I+built+a+programming+language...;...then+wrote+an+OS+kernel+in+it.;I+ship+a+desktop+browser+with+an+AI+agent.;Cybersecurity+%C2%B7+OSINT+%C2%B7+AI+tools;9th+grader+%E2%80%94+Istanbul+%F0%9F%87%B9%F0%9F%87%B7" alt="typing intro" />

<br/>

[![Portfolio](https://img.shields.io/badge/🖥️_mortuexOS-boot_my_portfolio-2c5364?style=for-the-badge)](https://0xmortuex.github.io)
[![Vex](https://img.shields.io/badge/⬇_Vex_Browser-download-47848F?style=for-the-badge&logo=electron&logoColor=white)](https://0xmortuex.github.io/vex-website/)
![Profile views](https://komarev.com/ghpvc/?username=0xmortuex&color=2c5364&style=for-the-badge)

</div>

---

# 🏆 The Big Three

*My strongest work, in order. Start here.*

## 1 · [Mort](https://github.com/0xmortuex/Mort) — I built a language, then wrote an OS in it

[![CI](https://github.com/0xmortuex/Mort/actions/workflows/ci.yml/badge.svg)](https://github.com/0xmortuex/Mort/actions/workflows/ci.yml)
![tests](https://img.shields.io/badge/tests-101%20passing-brightgreen)
![license](https://img.shields.io/badge/license-MIT-blue)

**Mort** is a statically-typed programming language that compiles to C. The whole compiler — lexer, parser, type checker, C code generator — is written from scratch in Python with **zero libraries**. And it exists for one reason: the same compiler builds **MORT OS**, a multiboot kernel *written in Mort* that boots in QEMU, sets up an IDT, remaps the PICs, and takes interrupt-driven keyboard input into an interactive shell.

<div align="center">
<img src="https://raw.githubusercontent.com/0xmortuex/Mort/main/docs/mortos.png" alt="MORT OS booted in QEMU" width="640" />
<br/><sub>MORT OS in QEMU — the shell, keyboard driver, and command parser are all written in Mort.</sub>
</div>

```rust
fn fib(n: int) -> int {
    if n < 2 { return n; }
    return fib(n - 1) + fib(n - 2);
}
```

> Why compile to C instead of an interpreter? Because an interpreter can't boot. Mort emits freestanding-friendly C so the kernel and your `hello.mx` go through the exact same pipeline.

## 2 · [Vex](https://github.com/0xmortuex/Vex) — a desktop browser built just for you

A fast, private, minimal **Electron browser** I actually ship — versioned releases, changelog, self-hosting docs, the whole thing. Arc-style vertical tabs and tab groups, a `Ctrl+K` command bar that does everything, ad & tracker blocking on by default, workspaces, tab sleep, split screen — and a **built-in AI agent** that can summarize pages, answer questions about what you're reading, and click/type to complete tasks, running on a local Ollama model or your own cloud worker.

**[⬇ Download for Windows](https://0xmortuex.github.io/vex-website/)** · [Latest release](https://github.com/0xmortuex/Vex/releases/latest) · [Self-hosting guide](https://github.com/0xmortuex/Vex/blob/main/SELF_HOSTING.md)

## 3 · [mortuexOS](https://0xmortuex.github.io) — my portfolio is a desktop OS

Instead of a portfolio page, I built a **fully interactive desktop operating system in the browser** — windows, a taskbar, apps. Every project below runs as a demo you can open from it. [Boot it.](https://0xmortuex.github.io)

---

## 🥇 Standouts

The next tier — each one solves a real problem end to end:

| | Project | Why it matters |
|---|---------|----------------|
| 🔍 | [**ReconX**](https://github.com/0xmortuex/ReconX) · [demo](https://0xmortuex.github.io/ReconX/) | Full-spectrum domain recon in one dashboard — DNS, WHOIS, SSL, headers, tech stack, subdomains |
| 🔑 | [**PassCrack**](https://github.com/0xmortuex/PassCrack) · [demo](https://0xmortuex.github.io/PassCrack/) | Password analyzer that simulates real attack techniques — crack times, pattern detection, l33t decoding, entropy. 100% in-browser, zero data transmitted |
| 🛡️ | [**Roblox Anticheat: The Hard Way**](https://github.com/0xmortuex/roblox-anticheat-the-hard-way) | A written-from-scratch, production-grade server-side anticheat — every line explained, built as a teaching resource |
| 🧩 | [**RoSuite**](https://github.com/0xmortuex/RoSuite) | Free RoPro alternative as a Chrome extension — server browser, player info, trade calculator, game stats |
| 🖥️ | [**MiniOS**](https://github.com/0xmortuex/MiniOS) · [demo](https://0xmortuex.github.io/MiniOS/) | The browser-OS experiment that grew into mortuexOS |

## 🔒 Cybersecurity & OSINT

| Project | Description | Live Demo |
|---------|-------------|-----------|
| [**NetMap**](https://github.com/0xmortuex/NetMap) | Visual traceroute on a world map — animated packets hop across the globe | [Demo](https://0xmortuex.github.io/NetMap/) |
| [**CipherLab**](https://github.com/0xmortuex/CipherLab) | Encryption playground — 13 ciphers with visual step-by-step breakdowns | [Demo](https://0xmortuex.github.io/CipherLab/) |
| [**CodeLens**](https://github.com/0xmortuex/CodeLens) | AI-powered code security auditor with quality scoring | [Demo](https://0xmortuex.github.io/CodeLens/) |

## 🤖 AI-Powered Tools

| Project | Description | Live Demo |
|---------|-------------|-----------|
| [**FlashMind**](https://github.com/0xmortuex/FlashMind) | AI study tool — paste notes or upload a PDF, get flashcards, quizzes, and summary notes | [Demo](https://0xmortuex.github.io/FlashMind/) |
| [**LoopholeMap**](https://github.com/0xmortuex/LoopholeMap) | Find vulnerabilities in any regulation — interactive node graph + AI analysis | [Demo](https://0xmortuex.github.io/LoopholeMap/) |
| [**AIJudge**](https://github.com/0xmortuex/AIJudge) | Describe an argument, AI delivers a verdict with shareable court ruling cards | [Demo](https://0xmortuex.github.io/AIJudge/) |
| [**TermsTrap**](https://github.com/0xmortuex/TermsTrap) | ToS analyzer that finds hidden clauses with risk scoring | [Demo](https://0xmortuex.github.io/TermsTrap/) |
| [**DebateBot**](https://github.com/0xmortuex/DebateBot) | Dual-side AI debate analysis with evidence and rebuttals | [Demo](https://0xmortuex.github.io/DebateBot/) |
| [**LexScope**](https://github.com/0xmortuex/LexScope) | Interactive legislation explorer with AI suggestions | [Demo](https://0xmortuex.github.io/LexScope/) |

## 🛠️ Tools, Apps & Plugins

| Project | Description | Live Demo |
|---------|-------------|-----------|
| [**ChatRoom**](https://github.com/0xmortuex/ChatRoom) | Real-time anonymous chat with rooms — Cloudflare KV backend | [Demo](https://0xmortuex.github.io/ChatRoom/) |
| [**BillForge**](https://github.com/0xmortuex/BillForge) | CUSA legislative bill builder with templates and AI assist | [Demo](https://0xmortuex.github.io/BillForge/) |
| [**GitPulse**](https://github.com/0xmortuex/GitPulse) | GitHub profile visualizer with charts | [Demo](https://0xmortuex.github.io/GitPulse/) |
| [**TypeRush**](https://github.com/0xmortuex/TypeRush) | Typing speed game with code mode and achievements | [Demo](https://0xmortuex.github.io/TypeRush/) |
| [**steamogames**](https://github.com/0xmortuex/steamogames) | Live Steam player statistics — concurrent players, peaks, and trends | — |
| **Vencord plugins** | [InactivityTracker](https://github.com/0xmortuex/vencord-inactivitytracker) · [QuickNotes](https://github.com/0xmortuex/vencord-quicknotes) · [RoleMembers](https://github.com/0xmortuex/vencord-rolemembers) · ServerClock · DMOrganizer | — |

---

## ⚙️ Tech I use

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![Electron](https://img.shields.io/badge/Electron-47848F?style=for-the-badge&logo=electron&logoColor=white)
![Cloudflare Workers](https://img.shields.io/badge/Cloudflare_Workers-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![D3.js](https://img.shields.io/badge/D3.js-F9A03C?style=for-the-badge&logo=d3dotjs&logoColor=white)
![Chrome Extensions](https://img.shields.io/badge/Chrome_Extensions-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
![QEMU](https://img.shields.io/badge/QEMU-FF6600?style=for-the-badge&logo=qemu&logoColor=white)

</div>

## 📊 Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=0xmortuex&show_icons=true&theme=transparent&hide_border=true&rank_icon=github" height="165" alt="GitHub stats" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=0xmortuex&layout=compact&theme=transparent&hide_border=true&langs_count=8" height="165" alt="Top languages" />

<img src="https://streak-stats.demolab.com?user=0xmortuex&theme=transparent&hide_border=true" height="165" alt="Streak" />

</div>

## 🐍 Contribution snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/0xmortuex/0xmortuex/output/github-contribution-grid-snake-dark.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/0xmortuex/0xmortuex/output/github-contribution-grid-snake.svg" />
</picture>

</div>

---

<div align="center">

*All web projects are open source and live on GitHub Pages. Not sure where to start? Boot [mortuexOS](https://0xmortuex.github.io).*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=100&section=footer" alt="footer" />

</div>
