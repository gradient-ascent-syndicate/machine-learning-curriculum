# 13 — Agentic AI

This track studies systems in which models choose actions, use tools, maintain state, plan, and interact with environments over multiple steps.

## Foundations
- what makes a system agentic
- agents versus workflows
- environment, observation, state, action, and objective
- model-based versus model-free intuition
- deterministic workflows versus autonomous decision loops

## Tool use
- function calling
- API/tool schemas
- tool selection
- argument generation
- tool-result interpretation
- tool errors and retries
- permissions and least privilege

## Reasoning and planning
- decomposition
- plan-and-execute patterns
- reactive patterns
- search over action sequences
- reflection and critique loops
- verification
- tree/graph-style reasoning patterns
- when planning hurts rather than helps

## Memory and state
- short-term working context
- persistent memory
- episodic and semantic memory concepts
- retrieval-based memory
- state machines
- context compaction
- memory quality and contamination

## Architectures
- single-agent loops
- router systems
- supervisor-worker patterns
- multi-agent systems
- event-driven agents
- human-in-the-loop agents
- computer-use agents
- coding agents
- research agents

## Reliability and control
- loop termination
- retry policies
- idempotency
- tool misuse
- cascading errors
- prompt injection through tools/data
- permission boundaries
- sandboxing
- observability and traces
- cost and latency budgets

## Agent evaluation
- task success
- step-level correctness
- trajectory quality
- tool-selection accuracy
- efficiency
- robustness
- recovery from failure
- benchmark leakage
- simulated versus real-world environments
- offline versus online evaluation

## Production agent engineering
- orchestration
- queues and asynchronous execution
- durable state
- checkpoints
- resumability
- human approval gates
- tracing
- monitoring
- regression evaluation
- deployment patterns

This track assumes competence with LLMs, retrieval, evaluation, APIs, and software-engineering fundamentals.
