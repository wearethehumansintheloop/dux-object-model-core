Here are the extracted DUX objects from the provided sources, formatted as requested with Markdown summaries, JSON schema blocks, evidence arrays with Provenance, and inline citations.

---

### Fit Template: Consolidating POC to Subscription Conversion

This Fit Template represents the strategic objective of consolidating Proof of Concept (POC) to subscription conversions, particularly through achieving better product market fit. The goal is to improve the conversion rate from initial exploratory engagements to full-scale, revenue-generating subscriptions, addressing current challenges in customer adoption and platform utility.

```json
{
  "object_type": "FitTemplate",
  "id": "ft-001",
  "fit_statement": "The business aims to consolidate Proof of Concept (POC) engagements into full subscription sales by achieving better product market fit for Red Hat OpenShift AI (RHOAI).",
  "evidence": [
    {
      "object_type": "Provenance",
      "id": "prov-ft-001-1",
      "evidence_block": {
        "source_filename": "AI-Enabled IT Operating Model Service Blueprint.pdf",
        "timestamp_in": null,
        "timestamp_out": null,
        "quote": "Consider Consolidating with PoC to Sub Conversion",
        "citation": "",
        "evidence_type": "textual_data"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-ft-001-2",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:09:26",
        "timestamp_out": "00:09:45",
        "quote": "That's absolutely been our experience. No, again, I think, I think a lot of it's just has to do with like product market fit. Our product is immature, it's maturing. As we get better product market fit, it'll be an easier pathway for them to say, oh this is, this is the right solution to our problems and it'll be easier to roll out.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-ft-001-3",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:28:30",
        "timestamp_out": "00:29:55",
        "quote": "I, I am thinking on the number of profile concepts. So the part that makes these question harder is that in our current state of raw ai, most of our customers start with a proof of concept. Like there is no customer that I know of that didn't start with it. So like, like they go and oh yeah, yeah I know the product, I know where to use it. Let's go to ML ops opportunity already. No, we go to like all the bigger projects that that we have, they have started with a proof of concept, but not all the proof of concepts that we have have translated into lops. Now I am trying to think about one project that went all the way to lops from the proof of concept and probably the one that is closer to do that is MasterCard. So if we count, let me go to to our latest report on Roy. Yeah. I am thinking like 25%. That's why I'm thinking at the moment.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    }
  ]
}
```

### Problem 1: Cloud-based AI workloads incur high costs and privacy/vendor lock-in risks, hindering on-prem adoption.

Customers often face challenges with high costs, data privacy concerns, and potential vendor lock-in when building AI workloads with cloud providers like OpenAI. This drives their need for an on-premise solution that offers greater control, cost efficiency, and protection of intellectual property.

```json
{
  "object_type": "Problem",
  "id": "pr-001",
  "job_statement": "When organizations build AI workloads on public cloud providers, they want to avoid high ongoing costs and protect their data privacy, so they can maintain control over their intellectual property and achieve better economics.",
  "evidence": [
    {
      "object_type": "Provenance",
      "id": "prov-pr-001-1",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:07:23",
        "timestamp_out": "00:07:45",
        "quote": "No, for sure. We're starting to see more and more uptake of that concern over the course of this year. Let's say like we had, you know, customers that were doing early experiments, they've gotten something running with open ai, then they are looking for a cheaper, better, more privacy protecting way to run those same AI workloads and we enter the story at that point.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-pr-001-2",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:31:51",
        "timestamp_out": "00:32:51",
        "quote": "Yeah, like the, I'd say like the two pain points are data privacy concerns. So like they're looking at us as an alternative to build these AI workloads with an on-premise solution that they can control. So that's one pain point. ... And that, and that's, that's privacy concerns and also cost concerns. 'Cause they build this POC and open AI or another cloud provider, they get, they get the sticker shop and realize they can't roll up a big enough dump truck of money and then they start looking around for alternatives.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-pr-001-3",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint_Service Blueprinting Activity - 2024/11/15 10:30 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:12:02",
        "timestamp_out": "00:14:50",
        "quote": "Many of them use cloud-based services and you see some, these organization in those cloud-based services such as some of them are using Databricks and other ones are using, another group is using Azure ai. Another group is using Google ai, some something else. So there, there are spars cloud services and tools and versions and IDs that they will be using across the organization. And there is some, there is a need of the organization to try to standardize and to regulate costs and to regulate security around that. And when I'm talking about security, imagine that we start using chat GPT in order to create most of our emails for communicating with our customers. And there is some concern about, hey, are we giving these information about the emails of our customers to chat, to open AI to the chat GPT organization because all this information is going to the cloud. Or if we are going to empower, for example, the developers for, for code completion, if we use GitHub copilot, there could be also a leaking of our code into, into the code, into copilot. We don't know how safe it is to use these different kind of cloud tools. They are mature, they are using it, but they just start having concerns about security and about the standardization tool standardization. So... And so we present ourselves as this solution that can use the hybrid cloud to try to continue to empower these developers, data scientists with the standard sort of solutions with standard type of solutions. And one of, one of the things that is our flag that we rise out there is we can do all of these on-premise, on your private cloud on Rosa, so that your information will not leave your cloud or your environment. You, you will make, we will make sure of that. And yeah, that's, that's the main reason why these mature organizations are interested.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    }
  ]
}
```

### Problem 2: Customers face challenges fully adopting and utilizing subscribed AI platforms, leading to underutilized "empty clusters."

After a subscription sale, organizations often struggle with the internal onboarding process and full adoption of the AI platform, resulting in "empty clusters" that are not being used to their full potential. Specific issues include difficulty in enabling GPUs, which can become a major stumbling block for customers.

```json
{
  "object_type": "Problem",
  "id": "pr-002",
  "job_statement": "When organizations subscribe to an AI platform, they want to ensure widespread internal adoption and efficient utilization of all platform capabilities, so they can maximize their investment and avoid underutilized infrastructure.",
  "evidence": [
    {
      "object_type": "Provenance",
      "id": "prov-pr-002-1",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:08:30",
        "timestamp_out": "00:09:25",
        "quote": "Noted. So then I, I think something that jumped out to me that you said David, was it can sometimes take a year go from like the consulting engagement to an actual subscription sale. So I ideally would love to maybe focus on these two phases, right? And focus on the, the actual pilot phase. 'Cause I think there's a, oftentimes we in product make an assumption that we sold a subscription, now the entire organization's gonna use it. But we all know that's not necessarily true. You know, empty clusters is a big pain point sometimes.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-pr-002-2",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:27:07",
        "timestamp_out": "00:27:17",
        "quote": "because obviously that's important too. Otherwise you have the empty cluster problem, which has plagued us for many, many years. You get the platform all set up and ready to go and then nothing rises on it. So",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-pr-002-3",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:10:47",
        "timestamp_out": "00:11:15",
        "quote": "Well the installation of OpenShift AI is not, that is not that complicated. So that most of our clients are very comfortable of running the operator there. So they, they go ahead with that. The, the part of the installation process that is more complicated to them sometimes is how to enable GPUs so that the datas involved into that. Like, oh, oh I need to enable those GPUs so it has probably some hidden genes or something in the documentation that is not very straightforward for them to catch up with. So enabling GPUs for, for the platform, that's, that's the thing that gets some of our consultants to be there and and to extend to, to something else now.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    }
  ]
}
```

### Behavior 1: Customers engage in Proof of Concepts (POCs) and pilot programs to validate the AI platform's value.

Customers frequently engage in Proof of Concepts (POCs) or pilot phases to test and prove the value of an AI platform before full organizational adoption. These initial engagements serve as a critical requirements gathering exercise, revealing specific needs and use cases for day-to-day operations and validating that the platform can meet their needs.

```json
{
  "object_type": "Behavior",
  "id": "beh-001",
  "user_enablement": "The customer is able to validate an AI platform's suitability for their specific needs and use cases through initial engagements.",
  "behavior_type": "Validation",
  "signals": [
    "Customer participates in 'pilot' or 'proof of concept' engagements",
    "Customer uses the pilot phase to gather requirements and identify use cases",
    "Customer states that they are trying the product to see if it 'fits their needs'",
    "Customer engages Red Hat for 'short engagement to ostensibly answer their questions'"
  ],
  "acceptance_criteria": [
    "A clear understanding of the platform's capabilities in relation to specific customer needs is established.",
    "Potential blockers or requirements for productive use (day two operations) are identified and documented.",
    "The customer gains confidence in the platform's ability to address their problems.",
    "The pilot successfully showcases the platform's capabilities, leading to acceptance or further engagement."
  ],
  "evidence": [
    {
      "object_type": "Provenance",
      "id": "prov-beh-001-1",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:03:34",
        "timestamp_out": "00:04:19",
        "quote": "This would be, okay. So my understanding of our Go-to-market activities for a lot of these platforms is they're very much consulting driven, right? I know that PM is, is sometimes involved in some of those conversations, but we are looking at day zero from the day that the deal is made to before, you know, we're letting people into the system. Historically I've seen activities around like pilots and proof of values kind of get done first before they kind of scale the offering to the rest of the organization. And I'm not sure if that's considered more of like a day zero activity or a day one activity, but these are the things that I'd love to challenge.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-beh-001-2",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:09:45",
        "timestamp_out": "00:10:03",
        "quote": "Noted. So if we focused on maybe the last engagement that you, that you worked on, let's maybe use that as a straw person and you know, would you talk to us a little bit about, you know, who was involved and, and who the actors in the, in the conversation were?",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-beh-001-3",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:22:02",
        "timestamp_out": "00:22:52",
        "quote": "Basis, yes. We are defining day two as productive use. Yeah. Meaning, but for the scope of this document, we can look at like kinda the first team or like the second team. I'm assuming one of the assumptions that I have that we can kind of break down is that there's typically a proof of concept or pilot before they open it up to everyone as my hypothesis is through that day zero and day one kind of, or through that pilot, right? It reveals requirements for day two operations, right? So as we go through the process of setting this up, you know, requirements get generated, use cases get identified and then we're creating, you know, solutions to solve some of those problems as well. Let me say that a little more succinctly. Could we see the pilot as almost like a requirements gathering exercise as well?",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-beh-001-4",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:27:58",
        "timestamp_out": "00:28:20",
        "quote": "Noted. And one question I had was with regards to the proof of concepts that we do, is that kind of standard operating procedure or do we ever just go straight to subscription And the follow up would be like what percentage of our proof of concepts convert to a sub?",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    }
  ]
}
```

### Behavior 2: Red Hat consultants primarily engage with customers through 'over the shoulder' support due to access limitations.

Due to factors like short engagement durations (6-8 weeks) and lengthy client onboarding processes for system access (up to 4 weeks), Red Hat consultants often provide 'over the shoulder' guidance rather than direct hands-on keyboard access during AI platform engagements. This approach means Red Hat is dependent on the client's internal team to move things forward. Historically, the breakdown was 50/50, but post-pandemic, it shifted to approximately 75% 'over the shoulder'.

```json
{
  "object_type": "Behavior",
  "id": "beh-002",
  "user_enablement": "Red Hat consultants are able to support client AI platform implementations and problem-solving effectively without direct system access.",
  "behavior_type": "Support",
  "signals": [
    "Client engagements are frequently 'over the shoulder' (e.g., 75% post-pandemic)",
    "Red Hat personnel communicate instructions that a client's internal team then executes",
    "Access to client systems takes significant time (e.g., 4 weeks for a 6-8 week engagement)",
    "Client resources may be limited, leading them to prefer Red Hat 'do it for me' without shadowing"
  ],
  "acceptance_criteria": [
    "Consulting engagement objectives are met within the defined short timelines.",
    "Client's internal team gains sufficient knowledge transfer to proceed independently.",
    "Complex technical tasks (e.g., GPU enablement) are successfully navigated despite indirect access.",
    "Client ultimately perceives value in the engagement, leading to potential subscription or further work."
  ],
  "evidence": [
    {
      "object_type": "Provenance",
      "id": "prov-beh-002-1",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:12:56",
        "timestamp_out": "00:13:25",
        "quote": "I'm thinking that our senior consultant, Corbit is working with the infrastructure team to get the access to the platform and is working with the operations team of our architect Trevor is working with the business leads and operations in order to confirm the requirements. That's why I am thinking about of the latest one that we have, which is CIBC. Now it got me thinking about the difference between over the shoulder engagements or engagements where we actually have access to the platform because in the case of CABC is over the shoulder so that we are interacting a lot with the, with the infrastructure team later probably with the app dev teams or data scientists.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-beh-002-2",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:15:45",
        "timestamp_out": "00:16:01",
        "quote": "And did, you mentioned some of your engagements are like they're over the shoulder versus direct hands on keyboard. What percent roughly is the breakdown there? Do most, are we able to get direct hands and keyboard initially at most customers or is it usually over the shoulder? It's more usually over the shoulder at the moment.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-beh-002-3",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:16:42",
        "timestamp_out": "00:17:49",
        "quote": "Yeah, well, yeah, what, what I think is that the onboarding process has become cumbersome probably in many of our clients. So that imagine that we are running this pilot for six weeks and it's going to take four weeks to give you access. So it's a combination between the nature of engagements that we have in ai, which are short duration. So our cycles of the different projects that we have with them is let's say six to eight weeks. But having access to their system is going to take us like four weeks. So they're like, yeah, let's, let's don't do that. I mean four weeks just to get access and then what, two weeks of your access with us? So it's not worth it. Hmm. I would say that that's the main reason why. So if we have probably engagements that will be like 16, 20 weeks, things like that, then we will probably get access to their system.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-beh-002-4",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:37:22",
        "timestamp_out": "00:39:30",
        "quote": "And then the work itself, is that something where Red Hat just kind of goes and goes heads down and, and you know, hands stuff back or just, it's more of like an over the shoulder activity? Are we really kind of depending on the client to kind move things forward? Yeah, that depends on the nature of engagement. Again, most of them are over the shoulder, so we are dependent. But if we have those kind of projects in which they can give us access to the resources in two to three days, then because they have a very straightforward kind of give you access infrastructure, then we'll be provided access and we'll have two options in the engagement. We call it residency type engagements in which even though we have access to the system, we will show them in each one of our steps, we'll have someone shadowing us so that they learn how to do this and they can ask questions and that. So it is a bit more of a delay there. But at the end of the engagement of our resiliency style, they will have also the knowledge about how we did the things that we did. But there are also customers that they, they prefer to set the results first. So they don't, they don't want to assign resources and, and probably this is a limitation on resources in their side. Like I don't have the people at the moment to follow your instructions or to follow what you are doing. So I'm gonna give you access to my system, just create the solution for me and tell me how it is working. So probably we can be faster there because we, we just don't have anyone to, to teach anything or something like that. We just go ahead heads down and, and roll with the punches. But yeah, depends on what we put there in the SOW, if this is resiliency style and the customer is interested in gathering this knowledge so somebody inside of the organization actually knows what to do, most of the customers are interested in getting that knowledge. But most of the customers also, they don't have the resources to assign to us so that at the end they end up being interested only on Red Hat do it, do it for me and tell me the results.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    }
  ]
}
```

### Result 1: Increase the conversion rate of Proof of Concepts (POCs) to RHOAI subscriptions.

The current conversion rate for Red Hat OpenShift AI (RHOAI) Proof of Concepts (POCs) to full ML Ops subscriptions is low, estimated at 20-25%. A key business objective is to significantly increase this conversion rate, translating initial engagements into broader adoption and revenue. This improvement is critical for achieving overall revenue goals and demonstrating the effectiveness of UX support.

```json
{
  "object_type": "Result",
  "id": "res-001",
  "target_impact": "Higher revenue and market penetration for RHOAI.",
  "success_criteria": "The percentage of Proof of Concepts (POCs) that convert into Red Hat OpenShift AI (RHOAI) subscriptions increases from the current 20-25%.",
  "evidence": [
    {
      "object_type": "Provenance",
      "id": "prov-res-001-1",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:28:30",
        "timestamp_out": "00:29:55",
        "quote": "I, I am thinking on the number of profile concepts. So the part that makes these question harder is that in our current state of raw ai, most of our customers start with a proof of concept. Like there is no customer that I know of that didn't start with it. So like, like they go and oh yeah, yeah I know the product, I know where to use it. Let's go to ML ops opportunity already. No, we go to like all the bigger projects that that we have, they have started with a proof of concept, but not all the proof of concepts that we have have translated into lops. Now I am trying to think about one project that went all the way to lops from the proof of concept and probably the one that is closer to do that is MasterCard. So if we count, let me go to to our latest report on Roy. Yeah. I am thinking like 25%. That's why I'm thinking at the moment. Yeah. Of the number. And",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-res-001-2",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:30:26",
        "timestamp_out": "00:31:50",
        "quote": "Yeah. So we are going for one out of five to go from proof of concept into an lops. So yeah, so 20% let's say at the moment. And yeah, it may be case of being in a bubble of... Yeah, and the reason I ask that question, you know, some of the business results for roy, you know there are revenue goals and then there's like a thousand proof of concept thousand POCs kind of goal for CY 2025. Yeah. And so one of the things we're really trying to understand as a UX organization is what are the behaviors, what are the leading behaviors and the lagging behaviors that a suggest a customer is gonna want to do? A POC and then B, what's gonna make them tip from the 20% of POCs to go to M to go to the ML ops kind of distance and how can the UX support those outcomes? So this, that's really helpful to under understand 'cause that seems like an area of opportunity in terms of like perhaps increasing conversions or the UX experiences that we can help with, you know, help support to help close those conversions. What are the pain points? What are the blockers? You know, when we get to the end of A POC, you know, what are the kind of objections that we hear in terms of moving to subs?",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    }
  ]
}
```

### Result 2: Achieve efficient GPU utilization and comprehensive cost monitoring for AI workloads on the platform.

Organizations aim to efficiently utilize their GPU resources and gain clear visibility into the costs associated with running AI workloads on-premise. This includes the ability to perform 'showback' and 'chargeback' for GPU costs, making cost management a "killer feature" for potential customers.

```json
{
  "object_type": "Result",
  "id": "res-002",
  "target_impact": "Optimized resource allocation and transparent cost management for AI operations.",
  "success_criteria": "Customers are able to efficiently provision and utilize GPUs for AI workloads and monitor the associated costs from a central location.",
  "evidence": [
    {
      "object_type": "Provenance",
      "id": "prov-res-002-1",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:08:02",
        "timestamp_out": "00:08:26",
        "quote": "It can be. A lot of times it's kinda driven by platform concerns, like how can we efficiently use our GPUs or like current sales motion is, hey we need you to take this open AI workload and show us that you can make it work with RO ai and the models that you have available Red Hat. So those are the key concerns we've seen.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-res-002-2",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:10:47",
        "timestamp_out": "00:11:15",
        "quote": "Well the installation of OpenShift AI is not, that is not that complicated. So that most of our clients are very comfortable of running the operator there. So they, they go ahead with that. The, the part of the installation process that is more complicated to them sometimes is how to enable GPUs so that the datas involved into that. Like, oh, oh I need to enable those GPUs so it has probably some hidden genes or something in the documentation that is not very straightforward for them to catch up with. So enabling GPUs for, for the platform, that's, that's the thing that gets some of our consultants to be there and and to extend to, to something else now.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-res-002-3",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:33:17",
        "timestamp_out": "00:34:05",
        "quote": "Ex existing distributed workloads that they would like to find a better alternative for. You know, at this point, like a lot of these organizations are mature, they have other AI platforms and they're looking at us as a, as a more private, more economical alternative. You know, so that's, that's kind of the pain point. Yeah. The other, the other pain, the, the other pain points around GPUs and, and they maybe they committed to, we, we wanna bring AI workloads on prem and we're doing chewed up by cloud hosting GPU costs. We want Red Hat to provide us with an efficient way to provision GPUs for the AI workloads that we wanna build. That's like the, the second pain point is just around hardware",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-res-002-4",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:47:29",
        "timestamp_out": "00:48:10",
        "quote": "Yeah. So those, we, we blessed, the next one was minimize the likelihood the A ML AI ML platform does not enable data scientists and OP teams to monitor the cost from central location. I feel like we just answered that question through our comments. I used to work on cost management for OpenShift and we had a GPU cost ticket that from Infineon that's just been floating around for a long time. And my spider sense is that's gonna be the killer kind of feature. It's like, how much am I spending and how can I do showback and chargeback? I don't know. Are y'all seeing that as a, a common need?",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    },
    {
      "object_type": "Provenance",
      "id": "prov-res-002-5",
      "evidence_block": {
        "source_filename": "RHOAI Customer Experience Service Blueprint,RHOAI Data Scientist Foundations: Desk Research on GPU Workload Usage,Business Automation Data Type Dictionary Usability Study 2022 Q1_AI Engagement Model Blueprinting - 2024/11/26 14:58 CST - Recording_undefined_DEIDENTIFIED",
        "timestamp_in": "00:48:10",
        "timestamp_out": "00:48:24",
        "quote": "Yes. I mean this is an example. If they're spending on spending with open ai, they wanna know like, hey, if I run this workload to OpenShift, what's gonna cost there? And we need accurate visibility to that.",
        "citation": "",
        "evidence_type": "direct_quote"
      }
    }
  ]
}
```

---
Would you like to hear my favorite data point?