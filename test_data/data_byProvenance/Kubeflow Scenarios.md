# Kubeflow Notebooks 2.0 \- Roadmap

**TIP**: To make comments on the document, please join **[kubeflow-discuss](https://groups.google.com/g/kubeflow-discuss)** on the Google account you are using.

**This document outlines the current state of the Notebooks 2.0-alpha community proposal.**

***Note:** We are actively seeking feedback. If you believe any functionality is missing from the proposed milestone, please document it in the [Gaps and Missing Requirements](https://docs.google.com/document/d/1-z6FCaJHm13v6OUZUvtdW7f6ftOWlnyVyQkNhFKwyw0/edit?tab=t.o1q6cbihbpf3#heading=h.qpihlu427ikp) section.*  

## Terminology and Personas

Some terminology to keep in mind while reading:

### 👩‍🔬Bella \- AI/ML practitioner

*"Bella is an AI/ML practitioner focused on building, fine-tuning, and deploying GenAI models. She needs to launch interactive environments that feel intuitive, powerful, and low-friction — so she can focus on experimenting with models, fine-tuning large datasets, and accelerating her workflows, without worrying about the underlying infrastructure."*

**Core Needs**:

* **Easy environment setup:** **Bella wants to launch an interactive environment to run AI/ML development tasks. First, she selects from the list of workspace templates (kinds) provided by her organization. Each kind has a meaningful name, description, icon, and technical tags like IDE type JupyterLab or VSCode. After choosing a kind, she can choose the size (GPUs, CPUs, RAM) of the environment, and the applications which are pre-installed (Pytorch, CUDA, vLLM, etc)**  
* **Workspace lifecycle control:** She wants to pause, unpause, restart, or delete her workspace. If an update is available (e.g., new image or config), she wants to be notified, shown what will change, and given the option to apply or defer it, similar to software updates on Mac OS.  
* **Customizability post-launch:** Bella expects to be able to edit an existing workspace — change its resources, switch to another compatible image, mount additional volumes, or inject secrets — without starting from scratch.  
* **Workbench status visibility:** She wants to understand what’s happening when a workspace is launching or failing, with feedback on pod status, liveness probes, logs, and readiness state directly in the UI.  
* **Toolchain flexibility:** Bella wants support for multiple web-based IDEs (Jupyter, RStudio, VSCode) and expects new ones to be added over time, without her needing to wait for custom integrations.

### 👨‍💻 Persona: Joel – Cluster Admin / Platform Engineer

*“Joel manages multi-tenant, GPU-enabled Kubernetes clusters for hundreds or thousands of users. His priorities are control, observability, scalability, and safety — all without needing to micromanage individual workloads.”*

**Core Needs**:

* **WorkspaceKind as the control plane:** Joel wants to define a WorkspaceKind once and use it as the single source of truth for all aspects of a workspace: display metadata, pod templates, IDE support, security policies, and selectable options (images, pod configs). These definitions are versionable, reviewable, and deployable via GitOps or UI.  
* **Safe update & deprecation flows:** When an image or config becomes outdated, Joel wants to deprecate it, redirect users to new options, and, optionally, force updates on paused or idle workspaces. Running workspaces should never break, but users should be guided to upgrade at the next restart, with complete visibility.  
* **Bulk and fine-grained administration:** From the UI, Joel wants to:  
  * List all workspaces using a given option.  
  * Filter by namespace, image, config, or GPU usage;  
  * Trigger **bulk actions** (e.g., pause all, force restart, apply updates);  
  * Edit workspace kinds and propagate changes with controlled rollout plans;  
* **Built-in support for secrets and volumes:** He wants users to mount pre-defined secrets, storage volumes, and custom configs safely and manage them declaratively in the WorkspaceKind, not through hand-edited manifests.  
* **Scalable governance:** Joel needs confidence that this model and its administration will scale — from a few workspace kinds to hundreds, and from a handful of users to thousands — without creating unmanageable sprawl.  
* **Resource and access control:** Joel needs the ability to scope GPU-heavy or sensitive configurations to authorized users/namespaces — enforced via selectors, labels, or RBAC — and track them across time.  
* **Forward extensibility:** He expects future support for VMs, job-like workloads, etc.

# Alpha Release \- Late 2025

##  Milestone Proposal

This section outlines the user stories and flows for the Notebooks 2.0-alpha milestone, aligned with Bella’s and Joel’s core needs. Each flow captures key functionalities from the user’s perspective, helping guide incremental development, validate the experience, and gather community feedback.

**👨‍💻Joel:  Initial setup of WorkspaceKind templates (epic: [\#270](https://github.com/kubeflow/notebooks/issues/270))**

Joel, the Cluster Admin, needs to quickly populate his Notebooks 2.0 installation by uploading or fetching WorkspaceKind YAML definitions and easily customizing basic metadata (display name, description, icon). This allows him to efficiently set up the initial templates without manually configuring each one. 

**👩‍🔬Bella: Setting up a workspace to fine-tune a Gen AI model  (epic: [\#274](https://github.com/kubeflow/notebooks/issues/274))**

As an AI/ML practitioner, Bella needs to quickly set up an interactive environment to fine-tune a Gen AI model. She browses the list of available WorkspaceKinds, filtering by IDE type and supported frameworks (e.g., JupyterLab, Pytorch).

After selecting a suitable kind, she chooses a pod configuration with enough GPU, CPU, and memory resources to support model fine-tuning.

She then selects a pre-built image with key libraries like CUDA, Hugging Face, and InstructLab tools.

During the setup, Bella creates a new secret to securely store her access tokens and mounts a persistent volume to hold training datasets and model outputs.

She launches her environment with just a few clicks, ready to fine-tune her first Gen AI model.

**👩‍🔬Bella: Connecting to a running workspace (epic: [\#291](https://github.com/kubeflow/notebooks/issues/291))**

After creating her workspace, Bella wants to connect to it seamlessly through her web browser. She expects to simply click on her workspace from the dashboard workspace list and be automatically redirected to the running environment (e.g., JupyterLab, VSCode) over HTTP, without manually configuring URLs, ports, or authentication.

**👩‍🔬Bella: Managing and updating running workspaces**  

Bella has multiple workspaces and needs to manage them efficiently. She pauses workspaces she’s not actively using to save resources.

For her active workspace, she scales it up — increasing the number of GPUs, to accelerate fine-tuning. Later, when less power is needed, she scales it back down, without needing to recreate or lose her environment.

**👨‍💻Joel: Monitoring GPU cluster usage and reclaiming idle resources  (epic: [\#307](https://github.com/kubeflow/notebooks/issues/307))**

Joel, the Cluster Admin, wants to monitor which users and teams consume the most expensive GPU resources. He lists all active workspaces, filters them by pod configuration to find those using high-end GPUs, and views usage metrics like last activity and GPU load.

Using custom probes, he identifies workspaces that have been idle for a defined period.

Joel then performs bulk actions, such as pausing or reclaiming idle workspaces, ensuring that GPU resources are used efficiently across the cluster without manually inspecting each workspace.

**👨‍💻Joel: Diagnosing a user’s workspace resource problem** 

When Bella reports that her workspace is crashing during model fine-tuning, Joel, the Cluster Admin, searches for her workspace, reviews logs and resource metrics, and identifies that the assigned instance size with 2 GPUs is insufficient for her workload (Deepseek-R1 fine-tuning).

**👨‍💻Joel: Updating WorkspaceKind options to meet new resource needs**  

After diagnosing the problem, Joel updates the system to support Bella’s needs. He sets up a new node type with 8 GPUs in the Kubernetes cluster, creates a new pod config referencing the larger instance type, and adds it to the appropriate WorkspaceKind. This enables Bella to restart her workspace with an appropriately sized option, ensuring stable model training.

**👨‍💻Joel: Adding a new image option to support updated libraries** 

Bella needs to use the latest version of vLLM, which requires a newer PyTorch version than what is available in her current workspace image. Joel, the Cluster Admin, builds an out-of-band new container image with the updated PyTorch and vLLM libraries installed.

He then creates a new image config pointing to this image and adds it to the appropriate WorkspaceKind, allowing Bella to select the updated environment without disrupting her existing workspaces.

**👨‍💻Joel: Rolling out a JupyterLab version update with minimal user disruption**  

Joel, the Cluster Admin, must roll out a new JupyterLab version across existing workspaces without breaking users’ environments. He first reviews which image options are in use, then builds new container images that only update JupyterLab (keeping user SDKs like PyTorch unchanged).

For each updated image, Joel creates a corresponding new image config and sets up a redirect from the old option to the new one. When users restart their workspaces, they are prompted to apply the update, along with a clear explanation of what has changed.

**👨‍💻Joel: Urgently patching vulnerable workspaces after a security incident**   

After the security team identifies a critical vulnerability in a shared package, Joel must quickly patch all affected workspaces. He builds a new container image that includes the security fix, creates a new image config, and redirects all relevant old image options to the new, secure version.

Using bulk actions, Joel applies pending updates across impacted workspaces, filtering by namespace and other criteria, ensuring the cluster is secure with minimal manual intervention.

**👨‍💻Bella: Upgrading workspace resources to complete fine-tuning**  

Bella notices a warning that her workspace has a pending update offering a new, larger GPU configuration, which Joel added. She reviews the update changelog, sees that it will upgrade her workspace to an 8-GPU node, and decides to apply the update immediately.

After applying, her environment restarts with the expanded resources, allowing her to finish fine-tuning her Deepseek-R1 model successfully.

**👨‍💻Bella: Upgrading workspace resources to complete fine-tuning** 

Bella has been notified that her workspace has a pending update to a newer JupyterLab version. She opens the changelog, reviews the changes (noting that user SDKs are unaffected), and decides to defer the update until she finishes her current experiment.

Later, at her convenience, she applies the update from the UI, triggering a controlled restart with the new JupyterLab environment.

**👨‍💻Bella: Understanding and recovering from workspace launch failures**  

When Bella tries to launch a new workspace, she encounters a failure caused by missing storage capacity in the cluster. Instead of a generic error, the UI clearly explains the root cause (e.g., "Insufficient storage available to create the requested volume").

Bella can view detailed logs and status information directly from the workspace page, helping her understand the problem. She can either retry with a smaller volume size, choose a storage, or contact the platform admin with the exact error details, reducing downtime and frustration.

###  Milestone Extras

**👨‍💻Connecting to a workspace via SSH from a local environment**

Bella wants to connect to her running workspace remotely using her local development environment (e.g., VSCode). She retrieves the SSH connection information from the workspace details page, including the hostname, username, and port.  
Using this information, Bella configures a remote SSH session in her VSCode setup, allowing her to edit files, run commands, and interact with the workspace directly from her laptop while leveraging the cluster’s compute resources.

##  Gap and Missing Requirements

If you notice any functionality, flows, or scenarios missing from this milestone proposal, please document them here. Your input is critical to ensure the Notebooks 2.0-alpha milestone addresses real user and admin needs as fully as possible.

- GAP \<TBD\>

# Initial Release \- ???

# Next Release \- ???

