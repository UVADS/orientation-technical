# Using Claude Code

## Preamble
![](luke-training.png)
![](luke-battle.jpg)

## Motivation
![](brown-tests.png)
![](deskill-lancet.png)

## Specific Goals
**1. Show you the gym equipment**
* AI Workflow / Agentic Loop
    * Using the loop as designed
    * Avoiding Deskilling/Never-skilling
    * Understanding what you are telling the loop to do
    * Claude: "which is exactly how feynmf's auto-layout works internally"
* Review AI Coding Terminology 
* Extensions 
    * Contex (CLAUDE.md)
    * Skills (SKILL.md)

**2. Give you a workout plan**
* Definition Practice
* Coding Practice


# The Agent Loop

### Jan 2025 - before Claude Code
![](agent-workflow.png)

### Sep 2026 - after Claude code
![](agentic-loop.png)

**The main point is that the context is gathered two ways, from the user and the environment**


## Jargon

![](agent-equation.png)

| Generic term | Claude version | Meaning | Note |
|---|---|---|---|
| Model | Claude |LLM|Token Prediction|
| Agent | Claude Code |(see equation)||
| Harness | Claude Agent SDK (was Claude Code SDK Jan-Sep 2025)| Manages the Loop| |
| Coding Agent | Claude Code | agentic coding solution | originally built to support developer productivity at Anthropic |

### Context

How Claude remembers your project
* Automatic learning (aka Auto memory)
* CLAUDE.md files (aka AGENTS.md)


![https://code.claude.com/docs/en/memory](context-scope.png)

| Generic term | Claude version | Meaning | Motivation / When to use |
|---|---|---|---|
| Context | n/a |||
| Workspace | Project |Context Boundary||
| Persistent/Agent/Long-term/Cross-session Memory | Auto Memory|Persistent instructions|loaded as context at start of conversation|
| Agents.md | CLAUDE.md |instructions you write to give Claude persistent context||


### Extensions
![https://code.claude.com/docs/en/features-overview](when-context.png)


| Generic term | Claude version | Meaning | Motivation / When to use |
|---|---|---|---|
| Skill | Skill |reusable knowledge and invocable workflows|repeated tasks|
| Command | `/` |shortcut to trigger an action|e.g. `/model` to switch model|
| Agents.md | CLAUDE.md |instructions you write to give Claude persistent context||
| Model Context Protocol (MCP) | "connectors" |standardized integrations to external services|e.g. search slack messages|


## Skills

### When and Why
You could just put it all into CLAUDE.md but ... that costs 

> [!NOTE] 
> Skills only load on use

#### Look for
* repeated instructions (instead of pasting the same multi-step prompt into chat every time)
* something you keep re-explaining to Claude
* a section of CLAUDE.md that's grown into a "how to do X" procedure (as opposed to a Dragnet)

![](bryan-wright-code-hierarchy.png)


> [!NOTE]
> "A skill is a markdown file"


> ![NOTE]
> "Skills extend Claude’s knowledge with information specific to your project, team, or domain. Claude applies them automatically when relevant, or you can invoke them directly"

### Anatomy
* File path
    * User: `.claude/skills/<skill-name>/SKILL.md`
    * Project: `<project>/.claude/skills/<skill-name>/SKILL.md` 
* YAML (always loaded into context)
    * name
    * description
* Markdown (loaded into context on use)

#### Example 1
> [!Note]
>
> .claude/skills/api-conventions/SKILL.md
> ```---
> name: api-conventions
> description: REST API design conventions for our services
> ---
> # API Conventions
> - Use kebab-case for URL paths
> - Use camelCase for JSON properties
> - Always include pagination for list endpoints
> - Version APIs in the URL path (/v1/, /v2/)
> ```

#### Example 2
https://github.com/UVADS/ai-tools-skills-agents/blob/main/skills/python-vscode-setup/SKILL.md


## Workout Plan

### Definition practice
Given two related terms, explain what's different in a sentence or two. Example pairs:

- **Model vs. Harness** — the "brain" vs. the "body." Claude is the model; Claude Code is one harness that puts tools around it.
- **Skill vs. MCP/Connector** — Skill packages *how* to do something (instructions); MCP/Connector reaches *outside data* Claude wouldn't otherwise have.
- **CLAUDE.md vs. System prompt** — both are standing instructions, but CLAUDE.md is yours to write and edit; the system prompt is set by Anthropic/the app, invisible to you.
- **Chat vs. Agent** — same underlying model, different interaction mode: one-shot Q&A vs. a loop that plans, acts, and checks its own work.
- **Project vs. Artifact** — Project is the persistent container (files, context, spans many chats); Artifact is one saved output that comes out of it.
- **Agentic coding vs. Autonomous agent** — agentic coding is the style of workflow (multi-step, repo-wide); autonomous agent is the system carrying it out with minimal prompting.


### Coding Practice
* Work the docs: Complete [Step 3-8: Your first session](https://code.claude.com/docs/en/quickstart#step-3-start-your-first-session) (we did 1 and 2 in orientation)
* Work the docs: Complete [Create your first skill](https://code.claude.com/docs/en/skills#create-your-first-skill)
* Make a useful skill:
    * Write your own skill that sets up the scoffolding for a new python project:
        * e.g. initialize a git repo, create the virtual environment, etc.
        * e.g. https://github.com/UVADS/ai-tools-skills-agents/blob/main/skills/python-vscode-setup/SKILL.md
    * Write your own skill that profiles datasets:
        * Takes a unnormalized flat file
        * Uses DuckDB or pandas to report row counts, inferred types, null rates, cardinality, date ranges, and suspicious values
        * Proposed schema and a list of cleaning decisions



# References
* Google search for memes and ECON 1170 chart
* Berzin & Topol, Preserving clinical skills in the age of AI assistance, The Lancet, 18 Oct 2025 (406:1719, PMID 41109709)
* https://martinfowler.com/articles/harness-engineering.html
* https://discovery.phys.virginia.edu/~bkw1a/
* https://www.anthropic.com/engineering/building-effective-agents
* https://claude.com/blog/building-agents-with-the-claude-agent-sdk
* https://code.claude.com/docs/en/how-claude-code-works
* https://code.claude.com/docs/en/features-overview
* https://code.claude.com/docs/en/memory
