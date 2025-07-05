# Declarative UX

### 🦆 Haters Gonna Quack
Declarative UX is built to leap over the objections.

When UXers say 'but our process requires X,Y,Z and it will take A,B,C weeks to ....', or crossfunctional partners say UX is too slow, not credible, or it is hard to test—we don’t argue. We execute.
From research to validated prototype in under three weeks.
Let the DUX quack. We ship at the speed of modern software.

**Declarative UX** is an open-source framework for generating, testing, and delivering user experiences using declarative specifications, AI collaboration, and behavior-driven development (BDD).

> _From protocol to prototype, Declarative UX transforms UX design into an executable, testable, and scalable system._

## 🚀 What Is It?
Declarative UX replaces traditional, imperative UX workflows with a declarative model:
- You define **what** the user must accomplish
- The system (LLM + BDD + automation) determines **how** to generate and test it

Declarative UX is:
- **AI-assisted**: Use LLMs to generate Feature files and Step Definitions from UX research protocols
- **BDD-driven**: Create testable experiences using Gherkin syntax and Behave
- **Prototype-first**: Generate usable prototypes automatically from behavioral specs
- **Infrastructure-ready**: Integrates into engineering workflows (CI/CD, version control, test automation)

## 🧠 Core Philosophy
Declarative UX is a declaration of independence from product engineering’s backlog. It empowers UX to define what needs to be tested, validated, and proven—without relying on engineering to interpret, groom, or implement exploratory concepts. UX work becomes executable, testable, and outcome-aligned, enabling faster cycles and clearer decision-making.

UX should be:
- **Declarative** – Defined by outcomes, not pixel-pushed deliverables
- **Executable** – Testable through code, not just in concept decks
- **System-integrated** – A first-class input into engineering, sales, and support decision-making

## 🧩 Strategic Outcome (Josh Seiden Framework)

🧠 Outcome-Driven Objective

Declarative UX supports high-impact behaviors across UX and Product Management by defining measurable outcomes that guide execution and investment decisions.

#### Key Results

| **Who** | **Has to do what** | **By how much** |
|--------|---------------------|-----------------|
| A UX Designer | Turn research into working, usability-tested code | Within a 3-week sprint from research to validation—so senior PMs can confidently drop or advance product directions |
| A Product Manager | Ship the highest-value feature set | In under 2 months, using demand signals, business value, and differentiation data to identify, test, and deliver the top-performing experience |
| A Product Manager | Avoid shipping low-value features | In under 2 months, by identifying and divesting in underperforming feature candidates—freeing up design, engineering, and AI capacity to focus on what matters most |

## 🦆 The DUX Stack

Declarative UX is powered by a modular, open-source stack that enables rapid, testable experience development across research, design, and engineering.

![duxstack_withcontent](https://github.com/user-attachments/assets/f83d591b-8075-4d2b-8c12-9056c8843443)

| **Component** | **Purpose** |
|---------------|-------------|
| **Chunkee** | Semantic chunking and domain model detection from unstructured data (e.g., transcripts, PDFs) |
| **Evergreen** | Graph-based qualitative feature store for versioning design models and structuring insight |
| **Duckie** | Declarative UX CLI that generates Gherkin specs, BDD Step Definitions, and GitHub issues |
| **Artee** | Automation + analytics trigger engine for test execution, preview deploys, and PRs |
| **NOPE** | Validation and decision logic engine that connects analytics platforms (Amplitude, Mixpanel) and unmoderated UX testing tools (UserZoom, Pendo) to promote or suppress variants |
| **Fidelity Runners** | Low → high-fidelity test environments: from Streamlit scripts to Carbon Design System prototypes |
| **Duckie Stack (BYOD/M)** | Optional layer for privacy-preserving federated data + model sharing between organizations |

Each module is independently usable, interoperable, and optimized for "bring your own data" (BYOD) and "bring your own model" (BYOM) workflows—making DUX extensible across teams, tools, and org boundaries.

## 🔍 Use Cases
- Reduce UX’s dependency on product engineering to test new ideas at scale—with speed and statistical rigor
- Prevent wasted engineering time spent grooming ill-defined UX tickets or triaging unclear RFEs
- Refocus engineering effort on well-validated features, not exploratory UX-driven R&D
- Empower PMs to drop or advance ideas in under 3 weeks based on real usability evidence

## 💡 Why It Matters to Engineering & Product
Declarative UX helps teams:
- Test R&D concepts quickly, without overloading engineering teams with design ambiguity
- Avoid wasted engineering cycles assessing feasibility or grooming early-stage UX concepts
- Provide PMs with rapid usability-tested outputs that reduce uncertainty and accelerate roadmap clarity

## 🧪 Example Project

Want to see Declarative UX in action?

Check out [CHunkee](https://github.com/nicholasjayantylearns/chunkee) — a sample project that applies Declarative UX principles to chunking structured qualitative data and generating graph-ready design models. It's a live demonstration of using LLMs + BDD to go from research protocols to testable, code-ready UX components.

## 🔧 Example Workflow
1. Write a UX research protocol or usability scenario
2. Use LLM (e.g., via CLI or API) to convert the scenario into Gherkin syntax
3. Behave executes the scenario using generated Step Definitions
4. Prototype and stubbed API interactions are generated
5. A/B test results drive automated PRs to engineering based on usability benchmarks

## 📦 Components (Planned Modules)
- `dux-cli`: Command-line tool for turning protocols into Gherkin specs
- `dux-agent`: LLM interface for transforming UX inputs
- `dux-prototype`: Auto-generates front-end prototypes from feature specs
- `dux-testkit`: Usability test automation with analytics integrations
- `dux-integrate`: GitOps-style deployment tools for integrating tested UX into engineering

## 🤝 Contributing
We’re in early development. Contributions welcome!
- Use Discussions to propose features
- File Issues to report bugs or share use cases
- Submit PRs to help us build the future of executable UX

## 📜 License
GNU General Public License (GPL)

## ✨ Shout-out
Inspired by the elegant split between imperative and declarative logic in engineering—and brought to life through AI + open source. Special thanks to Marty Jackson (@mjhacks), who once said so kindly: *"The software is the table."* Also inspired by Robert Fabricant’s article in Fast Company, [The Big Design Freak-Out](https://www.fastcompany.com/91027996/the-big-design-freak-out-a-generation-of-design-leaders-grapple-with-their-future).

I'm listening.

---
Let’s build a future where **UX isn’t just designed—it’s declared, executed, and scaled.** 
email:nicholasjayantylearnswithyouatgmail.com
GitHub: [nicholasjayantylearns](
