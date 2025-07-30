# Foundations: OpenAI Agent Building Guide
*Core Concepts, Architecture, and Design Principles*

---
*Part of: [OpenAI Agent Building Guide](README.md)*  
*Previous: [README](README.md) | Next: [DEMONSTRATIONS](DEMONSTRATIONS.md)*

---

## 🧠 What Is an Agent?

### Definition and Core Characteristics

**Agents are systems that independently accomplish tasks on your behalf.** Unlike conventional software that enables users to streamline and automate workflows, agents are able to perform the same workflows on the users' behalf with a high degree of independence.

### The Independence Principle

A workflow is a sequence of steps that must be executed to meet the user's goal, whether that's:
- Resolving a customer service issue
- Booking a restaurant reservation  
- Committing a code change
- Generating a report

**Key Distinction**: Applications that integrate LLMs but don't use them to control workflow execution—think simple chatbots, single-turn LLMs, or sentiment classifiers—are NOT agents.

### Core Agent Characteristics

An agent possesses two fundamental characteristics that allow it to act reliably and consistently on behalf of a user:

#### 1. **Workflow Management & Decision Making**
- Leverages an LLM to manage workflow execution and make decisions
- Recognizes when a workflow is complete
- Can proactively correct its actions if needed
- In case of failure, can halt execution and transfer control back to the user

#### 2. **Dynamic Tool Selection**
- Has access to various tools to interact with external systems
- Gathers context AND takes actions
- Dynamically selects appropriate tools depending on workflow's current state
- Always operates within clearly defined guardrails

## 🎯 When Should You Build an Agent?

### The Decision Framework

Building agents requires rethinking how your systems make decisions and handle complexity. Unlike conventional automation, agents are uniquely suited to workflows where traditional deterministic and rule-based approaches fall short.

### Real-World Example: Payment Fraud Analysis

**Traditional Rules Engine**: Works like a checklist, flagging transactions based on preset criteria.

**LLM Agent**: Functions like a seasoned investigator, evaluating context, considering subtle patterns, and identifying suspicious activity even when clear-cut rules aren't violated.

This nuanced reasoning capability is exactly what enables agents to manage complex, ambiguous situations effectively.

### Three Key Criteria for Agent Suitability

#### 1. **Complex Decision-Making** 🧩
- **Definition**: Workflows involving nuanced judgment, exceptions, or context-sensitive decisions
- **Example**: Refund approval in customer service workflows
- **Why Agents**: Can evaluate context and make judgment calls that rigid rules cannot handle

#### 2. **Difficult-to-Maintain Rules** 🔧
- **Definition**: Systems that have become unwieldy due to extensive and intricate rulesets
- **Challenge**: Updates are costly or error-prone
- **Example**: Performing vendor security reviews
- **Why Agents**: Replace complex rule maintenance with learned reasoning patterns

#### 3. **Heavy Reliance on Unstructured Data** 📄
- **Definition**: Scenarios involving natural language interpretation, document extraction, or conversational interaction
- **Example**: Processing home insurance claims
- **Why Agents**: Natural language understanding enables flexible data interpretation

### Validation Checklist

Before committing to building an agent, validate that your use case can meet these criteria clearly. Otherwise, a deterministic solution may suffice.

## 🏗️ Agent Design Foundations

### The Three Core Components

In its most fundamental form, an agent consists of three core components:

#### 1. **Model** 🤖
- **Role**: The LLM powering the agent's reasoning and decision-making
- **Considerations**: Task complexity, latency, cost tradeoffs
- **Strategy**: Different models for different tasks in the workflow

#### 2. **Tools** 🛠️
- **Role**: External functions or APIs the agent can use to take action
- **Integration**: Extends agent capabilities through system interactions
- **Categories**: Data retrieval, action execution, orchestration

#### 3. **Instructions** 📋
- **Role**: Explicit guidelines and guardrails defining how the agent behaves
- **Importance**: Critical for reliable workflow execution
- **Source**: Existing operating procedures, policy documents, support scripts

### Basic Agent Code Structure (OpenAI Agents SDK)

```python
weather_agent = Agent(
    name="Weather agent",
    instructions="You are a helpful agent who can talk to users about the weather.",
    tools=[get_weather],
)
```

## 🎛️ Model Selection Strategy

### Performance vs. Efficiency Tradeoffs

Not every task requires the smartest model:
- **Simple tasks**: Retrieval or intent classification → smaller, faster models
- **Complex tasks**: Refund approval decisions → more capable models

### Three-Phase Approach

#### Phase 1: Establish Baseline
- Build agent prototype with most capable model for every task
- Establish performance baseline with evaluations
- Don't prematurely limit agent abilities

#### Phase 2: Optimize Selectively  
- Swap in smaller models for specific tasks
- Test if acceptable results are maintained
- Diagnose where smaller models succeed or fail

#### Phase 3: Cost & Latency Optimization
- Focus on meeting accuracy targets first
- Optimize for cost and latency by replacing larger models where possible
- Maintain performance monitoring

### Model Selection Principles

1. **Set up evaluations** to establish a performance baseline
2. **Focus on accuracy** with the best models available
3. **Optimize efficiency** by replacing larger models with smaller ones where possible

## 🔧 Tool Categories and Design

### Three Types of Tools

#### 1. **Data Tools** 📊
- **Purpose**: Enable agents to retrieve context and information necessary for executing the workflow
- **Examples**: 
  - Query transaction databases or CRMs
  - Read PDF documents
  - Search the web

#### 2. **Action Tools** ⚡
- **Purpose**: Enable agents to interact with systems to take actions
- **Examples**:
  - Send emails and texts
  - Update CRM records
  - Hand-off customer service tickets to humans
  - Add information to databases

#### 3. **Orchestration Tools** 🔄
- **Purpose**: Agents themselves can serve as tools for other agents
- **Examples**: Refund agent, Research agent, Writing agent
- **Pattern**: See Manager Pattern in orchestration section

### Tool Design Principles

#### Standardization
- Each tool should have a standardized definition
- Enable flexible, many-to-many relationships between tools and agents
- Well-documented, thoroughly tested, and reusable

#### Benefits of Good Tool Design
- Improve discoverability
- Simplify version management  
- Prevent redundant definitions

### Tool Implementation Example

```python
from agents import Agent, WebSearchTool, function_tool

@function_tool
def save_results(output):
    db.insert({"output": output, "timestamp": datetime.time()})
    return "File saved"

search_agent = Agent(
    name="Search agent",
    instructions="Help the user search the internet and save results if asked.",
    tools=[WebSearchTool(), save_results],
)
```

## 📝 Instruction Configuration Best Practices

### Why Instructions Matter

High-quality instructions are essential for any LLM-powered app, but especially critical for agents. Clear instructions:
- Reduce ambiguity
- Improve agent decision-making
- Result in smoother workflow execution
- Lead to fewer errors

### Five Best Practices

#### 1. **Use Existing Documents** 📚
- Leverage existing operating procedures, support scripts, or policy documents
- Create LLM-friendly routines from established processes
- Example: Customer service routines map to knowledge base articles

#### 2. **Prompt Agents to Break Down Tasks** 🔨
- Provide smaller, clearer steps from dense resources
- Help minimize ambiguity
- Help models better follow instructions

#### 3. **Define Clear Actions** 🎯
- Every step should correspond to a specific action or output
- Be explicit about actions and even user-facing message wording
- Leave less room for errors in interpretation
- Example: "Ask the user for their order number" or "Call API to retrieve account details"

#### 4. **Capture Edge Cases** 🚨
- Real-world interactions create decision points
- Anticipate common variations
- Include instructions for handling incomplete information or unexpected questions
- Use conditional steps or branches for alternative paths

#### 5. **Leverage Advanced Models for Generation** 🤖
- Use models like o1 or o3-mini to automatically generate instructions
- Convert existing documents into clear instruction sets

### Instruction Generation Prompt Template

```
"You are an expert in writing instructions for an LLM agent. Convert the 
following help center document into a clear set of instructions, written in 
a numbered list. The document will be a policy followed by an LLM. Ensure 
that there is no ambiguity, and that the instructions are written as 
directions for an agent. The help center document to convert is the 
following {{help_center_doc}}"
```

## 🔗 Orchestration Fundamentals

### The Two Categories

Orchestration patterns fall into two categories:

#### 1. **Single-Agent Systems**
- Single model equipped with appropriate tools and instructions
- Executes workflows in a loop
- Simpler to implement and maintain

#### 2. **Multi-Agent Systems**  
- Workflow execution distributed across multiple coordinated agents
- More complex but enables specialization
- Better for complex, multi-domain workflows

### The "Run" Concept

Every orchestration approach needs the concept of a 'run', typically implemented as a loop that lets agents operate until an exit condition is reached.

#### Common Exit Conditions
- Tool calls
- Certain structured output
- Errors
- Reaching maximum number of turns

#### Example: OpenAI Agents SDK
```python
# Agents run until either:
# 1. A final-output tool is invoked
# 2. Model returns response without tool calls

Agents.run(agent, [UserMessage("What's the capital of the USA?")])
```

### Single-Agent Strategy: Prompt Templates

Instead of maintaining numerous individual prompts for distinct use cases, use a single flexible base prompt that accepts policy variables.

**Benefits**:
- Adapts easily to various contexts
- Significantly simplifies maintenance and evaluation
- Update variables rather than rewrite entire workflows

**Example Template**:
```
You are a call center agent. You are interacting with 
{{user_first_name}} who has been a member for {{user_tenure}}. The user's 
most common complaints are about {{user_complaint_categories}}. Greet the 
user, thank them for being a loyal customer, and answer any questions the 
user may have!
```

## 🎭 Multi-Agent Decision Framework

### When to Consider Multiple Agents

**General Recommendation**: Maximize a single agent's capabilities first. More agents can provide intuitive separation of concepts, but can introduce additional complexity and overhead.

### Practical Guidelines for Splitting Agents

#### 1. **Complex Logic** 🧠
- **Trigger**: Prompts contain many conditional statements (multiple if-then-else branches)
- **Problem**: Prompt templates become difficult to scale
- **Solution**: Divide each logical segment across separate agents

#### 2. **Tool Overload** 🛠️
- **Not Just Quantity**: The issue isn't solely the number of tools, but their similarity or overlap
- **Success Cases**: Some implementations manage 15+ well-defined, distinct tools
- **Failure Cases**: Others struggle with fewer than 10 overlapping tools
- **Solution**: Use multiple agents if improving tool clarity doesn't improve performance

### Multi-Agent System Patterns

#### 1. **Manager Pattern (Agents as Tools)**
- Central "manager" agent coordinates multiple specialized agents via tool calls
- Each handles specific task or domain
- Manager maintains workflow control

#### 2. **Decentralized Pattern (Agent Handoffs)**
- Multiple agents operate as peers
- Hand off tasks to one another based on specializations
- No central coordinator

### Graph-Based Modeling

Multi-agent systems can be modeled as graphs:
- **Nodes**: Represent agents
- **Edges in Manager Pattern**: Represent tool calls
- **Edges in Decentralized Pattern**: Represent handoffs that transfer execution

### Universal Principles

Regardless of orchestration pattern:
- Keep components flexible
- Maintain composability  
- Drive with clear, well-structured prompts

---

**Next**: Continue to [DEMONSTRATIONS.md](DEMONSTRATIONS.md) for working code examples and practical implementations of these foundational concepts.
