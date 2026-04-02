# Tech Stack Notes: AI Tools Landscape

This repository contains working notes for an orientation level brown bag talk on the AI coding tools.

## Cursor, and codex, and claude code ... oh my!

Are you finding it hard to keep up with all the developments in AI coding? It seems like every month there is a new tool. Well, this Thursday (4/2) is your chance to eat some lunch and catch up on the latest developments. (Yes it will obsolete before you graduate, but practicing keeping up is going to be a key skill going forward 🙂).

<p align="center">
  <img src="images/ltb.webp" alt="ltb" />
</p>


## Picking up from where we left off
**Two years ago...**
* Ask chatGPT a question and copy and paste the answer into your code

**A year ago...**
1. Code to Code
2. Comment to Code
3. Chat to Code

and

"Claude code ... agentic coding tool" ~anthtopic

**Today...**

we are going to talk about the progress to the current paradigm of ***Agentic coding*** and how to evolve your workflow.

### Outline
1. Survey of Landscape
2. Today: What's my use case
3. Homework




# Survey of Landscape

### Tools
| Tool | Company | Category | Release Quarter |
|------|---------|----------|-----------------|
| OpenClaw | Open source | Agent tooling ecosystem | — |
| Windsurf (Cascade) | Codeium / Exafunction | Agentic IDE | 2024 Q4 |
| Claude Code | Anthropic | Agentic coding (CLI/IDE) | 2025 Q1 |
| OpenAI Codex | OpenAI | Agentic coding (cloud/CLI) | 2021 Q3 |
| Cursor | Anysphere | AI-native IDE | 2023 |
| Devin | Cognition AI | Autonomous agent | 2024 Q1 |
| Aider | Open source | CLI (git-centric) | 2023 Q2 |
| Replit Ghostwriter | Replit | Cloud IDE assistant | 2022 Q4 |
| Gemini Code Assist  | Google | IDE + CLI assistant | 2024 Q2 |
| GitHub Copilot | GitHub / Microsoft | IDE assistant  | 2021 Q2 |
| Code Llama | Meta | Open model (self-hosted) | 2023 Q3 |

Sources for release quarters.[^survey-tools]

### Jargon 
| Term | Definition |
|------|------------|
| Agentic coding | Task-oriented workflows where the system plans and executes multi-step changes across your repo. |
| AI-native IDE | Editor built around AI from the start (repo-wide chat/edits), not only a plugin on a classic IDE. |
| Autonomous agent | System that can carry a ticket or task end-to-end with little step-by-step prompting. |
| Multi-agent workflow | Several specialized agents or tools coordinated to split work (planner, coder, reviewer). |
| SKILL.md | a small instruction set to define behavior for an agent |
| "Rules" | higher level than skills (e.g. in cursor `.cursor/rules/*.mdc`) |

Sources and older vocabulary.[^survey-jargon]

> [!TIP]
> How to keep your head straight? Practice with **definition comparisons**.

### E.G. Claude Cowork vs. Claude Code
Cowork has had a faster adoption and so far is reaching a broader audience because it is designed to be more general purpose than Claude Code. Claude code is a CLI interface built for programming tasks where as Claude Cowork is app based and handles a broad range of tasks like making presentations (I'll believe that when I see it).

### Try these on for practice later
* Copilot vs. Cursor
* Claude Code vs. Cursor
* Claude Code vs. OpenClaw




## Steps from Chat Copy Pasta to Integrated AI Environment to Agentic

**Two years ago...**
Autocomplete tools (e.g. Copilot)


**One year ago...**
AI-native IDEs (e.g. Cursor)


**Today...**
Agentic systems (e.g. Claude Code)

### Trends
* from suggesting code to doing tasks
* from file level context to repo-level context (and even integration - think OpenClaw)
* from micro to macro (think delegation - especially with Plan mode, more to come)

### What the AI "says"
“Copilot helps you type faster, Cursor helps you think across files, Claude Code helps you delegate entire tasks.” ~ChatGPT



# Today: What's my use case?

### AI is strong on middle to middle, not end to end.
* Goals and problem definition live with the human.
* Evaluations live with the human.
* Project milestones live with the AI.
* Project executions live with the AI.

***Spend your time as a designer and architech; let the AI build.***


### Ask yourself
* What do you wish you didn't have to do?
* What drains my energy and I put it off to garbage time?

**My answer: Email!**

* What do I do that is repetitive?
* What requires my expertise to set up, but not to do?
* What should I be delegating?

### How to get it done?

#### Plan mode

#### Skills and MD profiles/configuration/rules
[The-Complete-Guide-to-Building-Skill-for-Claude.pdf](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

#### Human in the loop - trust but verify - tests

#### The 3 core permissions

"We give you two out of three rights. Agentic systems can access sensitive information, it can execute code, and it can communicate externally."

"We could keep things safe if we gave you two out of those three capabilities at any time, but not all three."[^nvidia-lex]

# Homework ... where do we go from here
<p align="center">
  <img src="images/ybr.webp" alt="ybr" />
</p>


Homework
1. Pick a workflow (repetitive, draining, delegatable)
2. Write out the steps
3. Determine the 80% that's routine
4. The 20% that requires judgement
5. Build the system



***E.G. from me - publication quality plots***

[^survey-tools]: [Tools (release quarter)](sources.md#tools-release-quarter) in `sources.md`.

[^survey-jargon]: [Jargon](sources.md#jargon) in `sources.md`. Older / general terms: [`zold/legacy-jargon.md`](zold/legacy-jargon.md).

[^nvidia-lex]: [Jensen Huang: NVIDIA — The $4 Trillion Company & the AI Revolution — Lex Fridman Podcast #494](https://www.youtube.com/watch?v=vif8NQcjVf0)
