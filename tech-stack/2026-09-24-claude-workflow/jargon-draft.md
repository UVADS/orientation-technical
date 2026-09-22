# Jargon Table

## Model & company landscape

| Generic term | Claude version | Meaning | Motivation / When to use |
|---|---|---|---|
| Model / LLM | Claude (Sonnet, Opus, Haiku) | The trained neural network doing the reasoning/generation | Know what's actually "thinking" vs. what's just the interface around it |
| Weights | Claude = closed weights | Learned parameters that make a model work; open = downloadable, closed = provider-only | Explains why you can't download/self-host Claude, and what open-weight models (Llama) let you do instead |
| Frontier vs. open-source model | Claude = frontier | Current state-of-the-art, largest, most capable models — usually closed | Frontier when you want the best result with no setup; open-source when you need to self-host, cut cost, or fine-tune |
| Hardware company | N/A — Anthropic doesn't make chips (examples: Nvidia, AMD, Google TPUs) | Companies building the physical chips/infrastructure AI runs on | Distinguishes the chip business from the model business |
| Software company | Anthropic (examples: Anthropic, OpenAI, Google, Microsoft) | Companies building the models and AI products/applications | Places Claude in the stack — a software/model company sitting on top of hardware it doesn't own |
| Hyperscaler | Amazon Bedrock, Google Cloud Vertex AI | Massive cloud providers (AWS, Google Cloud, Azure) that host and serve AI models at scale | If your org already runs on AWS/GCP, you can access Claude through that existing infrastructure/billing |

## Interacting with Claude

| Generic term | Claude version | Meaning | Motivation / When to use |
|---|---|---|---|
| Chat | claude.ai | Basic conversational interface — no tools, no persistent files | Fine for one-off questions; the whole talk is about knowing when this isn't enough |
| Harness | Claude Code | Software wrapped around a model giving it tools, memory, a way to act | Pick the harness for the job — chat for quick answers, Code/Cowork when Claude needs to touch files, run code, or use tools |
| OS | Claude (the model itself) | The base platform other software is built on top of | Industry framing: "the model is the new OS," with harnesses/Skills/MCP as apps/drivers on top |
| Shell | Claude Code | A command-line interface for issuing instructions directly to the system | Ties to the shell-script analogy — Claude Code is text commands, scriptable, no GUI |
| Agent | Claude running agentically (e.g. in Claude Code or Cowork) | A system that loops — plans, acts, checks, repeats | Use when a task needs multiple steps and self-checking, not a single answer |
| Agentic coding | Claude Code | Task-oriented workflows where the system plans and executes multi-step changes, not just answers | Use when the task is "do this multi-step thing," not "answer this one question" |
| Autonomous agent | Claude Code / an agentic session | A system that carries a task end-to-end with little step-by-step prompting | Use once you trust the task enough to let it run several steps unsupervised, then review |
| Multi-agent workflow / Subagent | Subagents (via the Agent/Task tool) | Several specialized agents coordinated to split work (planner, coder, reviewer) | Use when a task has genuinely separable pieces worth parallelizing or isolating |
| Plan Mode | Plan Mode | A mode where Claude drafts and shows its approach before executing | Good default for higher-stakes tasks — review the plan before Claude touches anything |
| AI-native IDE | N/A — Claude Code integrates *into* editors, it isn't one (example: Cursor) | An editor built around AI from the start, vs. AI bolted on as a plugin | Correctly places Claude Code when comparing tools — it's a CLI/agent layer, not a competing IDE |
| Tool use / function calling | Tools (built-in or via MCP) | The mechanism that lets a model call an external function and use the result | The thing agents, Skills, and MCP are all built on top of — worth naming once directly instead of only at the layers above it |
| Extended thinking | Extended thinking | A model spending extra inference-time compute reasoning before it answers | Students will see the toggle; explains why some answers are visibly slower but more reliable on hard problems |
| Vibe coding | N/A — informal industry slang, not a Claude product term | Building software by iterating on natural-language prompts rather than hand-writing code, often without closely reading the output | They'll hear this everywhere outside the room; worth one debunking sentence — fine for prototypes, risky without review for anything that ships |

## Configuring & extending Claude

| Generic term | Claude version | Meaning | Motivation / When to use |
|---|---|---|---|
| Skill | Skills (SKILL.md) | A packaged, reusable set of instructions the model loads when relevant | Build one once you're repeating the same detailed instructions more than once or twice |
| Config / instructions file | CLAUDE.md | Standing instructions Claude reads automatically — global or project-level | Stop re-explaining your preferences every chat — set it once, globally or per project |
| "Rules" (cross-tool cognate) | CLAUDE.md | What other tools call this same concept (e.g. Cursor's `.cursor/rules/*.mdc`) | Shows students the concept is universal across AI coding tools, not a Claude-only quirk |
| MCP (Model Context Protocol) | Connectors (claude.ai/Desktop) / MCP servers (Claude Code) | Open protocol (Anthropic-authored, now industry-adopted) for letting a model reach outside tools and data | Use when Claude needs live/current info it wasn't trained on — your inbox, a job board, your codebase |
| RAG (Retrieval-Augmented Generation) | Project knowledge / connector-backed retrieval | Pulling relevant external text into the context window at query time to ground an answer | Contrast with MCP: RAG fetches passages of text; MCP lets the model take live actions and reach live data, not just read a document |

## Persistence & output

| Generic term | Claude version | Meaning | Motivation / When to use |
|---|---|---|---|
| Persisted/shareable output | Artifact | A saved output that outlives the chat | Use when the output is something you'll reopen or share, not just read once |
| Workspace | Project | A persistent container of files/instructions/context across chats | Use for ongoing work in one context (a course, a client) where files and instructions should persist |

## Fundamentals

| Generic term | Claude version | Meaning | Motivation / When to use |
|---|---|---|---|
| Prompt | Prompt | The input/instructions you give the model | Still the single biggest lever on output quality, even with Skills/MCP in play |
| Context engineering | Context engineering | Managing everything assembled into the context window — retrieved docs, tool outputs, memory, files — not just the wording of the prompt | Becomes the real skill once MCP/tools/Skills are stacked and the model's input is no longer just what you typed |
| Context window | Context window (size varies by model) | How much text/history the model can hold at once | Explains why very long chats/documents get truncated or "forgotten" |
| Token | Token | The unit of text models read/generate | Drives cost and limits — longer input/output = more tokens |
| Training vs. inference | Anthropic trains Claude; you run inference when chatting | Building the model vs. using it | Claude isn't learning from your chat permanently — every session starts from the same trained model |
| Fine-tuning | Limited — only via Amazon Bedrock for select older models (e.g. Claude 3 Haiku); not something you do to Claude directly | Adjusting a model's own weights on your data, rather than steering it with prompts/context | A much heavier lever than prompting, Skills, or RAG — explains why "train your own AI" isn't the default move with Claude |
| Hallucination | Hallucination | Confident, plausible-sounding output that is factually wrong | Sets expectations for verifying facts — especially important once an agent is working several steps unsupervised |
| Multimodal | Claude reads text, images, PDFs, etc. | A model handling more than one input type | Skip manual transcription — hand Claude the image/PDF/screenshot directly |
| GenAI | Claude is a GenAI product | The umbrella category for the whole talk | Framing term — locates Claude in the broader AI landscape |

## In the news

Anthropic (Dario Amodei, CEO), OpenAI (Sam Altman, CEO), Google DeepMind (Demis Hassabis, CEO), xAI (Elon Musk), Meta AI/Superintelligence Labs (Mark Zuckerberg, CEO — note: Yann LeCun left Meta in Nov 2025 to start his own "world models" company), Microsoft (Satya Nadella, CEO), Mistral AI (Arthur Mensch, CEO), Nvidia (Jensen Huang, CEO), Safe Superintelligence Inc. (Ilya Sutskever, ex-OpenAI cofounder).

## Bonus

"Three core permissions" framing (from the UVA agentic-coding notes): an agent can safely have any two of — access to sensitive info, ability to execute code, ability to communicate externally — giving it all three at once is the risk zone. Good line for a human-in-the-loop moment.
