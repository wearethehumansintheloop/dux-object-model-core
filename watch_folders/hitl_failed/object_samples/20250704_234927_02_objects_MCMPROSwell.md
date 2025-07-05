Here are the extracted Problems, Behaviors, and Results from the provided sources, formatted according to the DUX v9.5 schema with detailed markdown summaries and JSON blocks, including Provenance objects for each piece of evidence.

***

### Problems

#### Problem 1: Organizational Culture Stifles Agility
**Markdown Summary:**
Organizations aiming for digital transformation often face challenges from legacy cultures characterized by command and control, an 'inside out' value orientation, and rigid processes and hierarchies. These cultural factors abstract product creators from customers, thereby stifling the organization's ability to pivot quickly and adapt to changing customer expectations. This necessitates an operational transformation beyond just technology to capitalize on the benefits of platforms like MCMP.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-001",
  "job_statement": "When organizations attempt digital transformation, they want to pivot quickly and adapt to changing customer expectations, so they can capitalize on the benefits of new technologies like MCMP.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-001-1"
    },
    {
      "provenance_id": "PROV-PROB-001-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-001-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Legacy cultures of command and control, ‘inside out’ value orientation, and rigid layers of process and hierarchy that abstract product creators from customers often stifle an organization’s ability to pivot quickly and move at the speed of changing customer expectation.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-001-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "As an accelerator of digital transformation, MCMP requires not only technology transformation, but operational transformation to capitalize on its benefits.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 2: Deployment Focus is Technology-Centric, Not People & Process
**Markdown Summary:**
Early deployments of the IBM MultiCloud Management Platform (MCMP) have predominantly concentrated on "what the platform can do" from a technology standpoint, rather than adequately addressing "what do we need to do to use the platform" and how the implied operational transformation is enabled. This gap signifies a significant oversight where the focus remains on technology, neglecting the crucial aspects of people and processes within the multi/hybrid cloud operating model.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-002",
  "job_statement": "When deploying multi/hybrid cloud platforms like MCMP, organizations want to enable holistic operational transformation, so they can fully capitalize on platform benefits beyond just technology.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-002-1"
    },
    {
      "provenance_id": "PROV-PROB-002-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-002-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Much of the focus in these early deployments has been on “what the platform can do”, and not nearly enough focus has been given to “what do we need to do to use the platform”, and almost no focus has been given to how the implied transformation is enabled.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-002-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "In the full scope of the multi/hybrid cloud operating model, we’ve been focused on the technology, not the people and process. The intent of this document is to begin to address this observed gap.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 3: Companies are Unprepared for Digital Disruption
**Markdown Summary:**
A significant portion of Fortune 500 companies are at risk of not existing in the next decade, with over 85% of business executives anticipating disruption but only 44% feeling adequately prepared. This widespread unpreparedness is driving companies to seek cloud technologies for digital transformation, contributing to a trillion-dollar cloud computing market.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-003",
  "job_statement": "When companies face digital disruption, they want to be adequately prepared, so they can ensure their continued existence and leverage cloud technologies for transformation.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-003-1"
    },
    {
      "provenance_id": "PROV-PROB-003-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-003-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "A study from the John M. Olin School of Business at Washington University estimates that 40 percent of today’s Fortune 500 companies on the S&P 500 will no longer exist in 10 years. According to the MIT Sloan Management Review survey of 3700 business executives, more than 85% expect to be disrupted, but only 44% felt adequately prepared for it.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-003-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "As a result companies are looking to cloud technologies to digitally transform their business, contributing to a $1 trillion dollar cloud computing market.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 4: Difficulty Obtaining Granular Performance Data from Cost Management
**Markdown Summary:**
Users find it challenging to drill down into the underlying performance data, such as CPU and memory usage, from the cost management views in the cloud console. While high-level cost data is available, accessing the granular performance metrics that power optimization efforts is difficult, requiring internal workarounds like exporting data to Tableau or Postgres for analysis.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-004",
  "job_statement": "When analyzing cloud costs, I want to easily access and drill down into granular performance data like CPU and memory utilization, so I can conduct detailed performance optimizations.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-004-1"
    },
    {
      "provenance_id": "PROV-PROB-004-2"
    },
    {
      "provenance_id": "PROV-PROB-004-3"
    },
    {
      "provenance_id": "PROV-PROB-004-4"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-004-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:10:21",
    "timestamp_out": null,
    "quote": "one of our challenges is in the cost management, like cost explorer, the data is very cost based. Like we, it's, I I, I know there's some high level views of like CPU memory volumes, which is, is good, but I haven't found a way to drill down into that to actually see what that underlying data is from a cost management perspective.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-004-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:46:24",
    "timestamp_out": null,
    "quote": "So from the cloud console perspective, I think I mentioned this a little bit earlier, but the exploring the data and cost management, it's, it can be hard to find the performance data compared to the cost data, right?",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-004-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:46:24",
    "timestamp_out": null,
    "quote": "A lot of the views in the cloud console are, you know, here's the daily costs, you know, which is, which is cool, but would like to, it, it would be nice to be able to explore that CPU memory, core data, et cetera, the stuff that powers those performance optimizations from the cloud console as well.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-004-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:46:24",
    "timestamp_out": null,
    "quote": "So because we have our own view of it in Tableau, but it would be great to have a live data view of it, you know, from the Red Hat cloud side, just kind of rapid fire going through some of these.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 5: Cost Management Operator Can Enter Broken State with Stale Data
**Markdown Summary:**
At scale, OpenShift clusters face a pain point where the cost management operator can enter a broken state, preventing data flow (e.g., due to Prometheus issues or storage becoming read-only), and teams are unaware of this issue. This leads to gaps in historical data and a lack of proactive alerts, making it difficult to maintain accurate cost visibility and optimization efforts.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-005",
  "job_statement": "When managing OpenShift clusters at scale, I want to proactively know if the cost management operator is functioning correctly and data is flowing, so I can ensure continuous and accurate cost visibility.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-005-1"
    },
    {
      "provenance_id": "PROV-PROB-005-2"
    },
    {
      "provenance_id": "PROV-PROB-005-3"
    },
    {
      "provenance_id": "PROV-PROB-005-4"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-005-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:15:13",
    "timestamp_out": null,
    "quote": "Yeah, so our challenge is that we have a lot of OpenShift clusters at scale... in the past, this is a pain point we've had where the cost management operator will be in a broken state and we don't know that that's the case.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-005-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:15:13",
    "timestamp_out": null,
    "quote": "For example, if there's a issue with Prometheus, so like for example, when our network storage goes out, the storage can swap to a read- only mode, and then that blocks rights. And then both Prometheus and cost management operator can't continue off.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-005-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:16:19",
    "timestamp_out": null,
    "quote": "So really that's, that's the pain point is how do we know proactively when we have to go and check out the cost management operator pod because it's not flowing data and we don't want to just forget about it. And then in, in a month we come back and there's a, a big gap of data.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-005-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprintWalkthrough.m4a",
    "timestamp_in": "00:03:13",
    "timestamp_out": "00:03:30",
    "quote": "one of the big pain points that we heard in terms of the configuration um of for alerts for usage spikes is that our product has the opportunity to support them better and has the opportunity to not only put usage alerts um at the cluster level, but perhaps the pod level and the container level.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 6: Difficulty Retaining Granular Historical Metrics
**Markdown Summary:**
Organizations struggle with retaining granular historical metrics for more than a short period (e.g., beyond two weeks or four months in cost management) because increased granularity leads to greater complexity and significant storage requirements. This limitation hinders the ability to analyze long-term trends for capacity planning and historical pivoting against usage information.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-006",
  "job_statement": "When analyzing historical cloud resource usage, I want to retain granular metrics for long periods, so I can conduct accurate capacity planning and trend analysis.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-006-1"
    },
    {
      "provenance_id": "PROV-PROB-006-2"
    },
    {
      "provenance_id": "PROV-PROB-006-3"
    },
    {
      "provenance_id": "PROV-PROB-006-4"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-006-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:18:12",
    "timestamp_out": null,
    "quote": "So that's the furthest we go. I mean there are teams that do build their own dashboards for that and use tools like Grafana and to build those, those views per workload and per pod and that sort of thing. But no one's really doing it with like a long- term view",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-006-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:08:44",
    "timestamp_out": null,
    "quote": "you don't get per second metrics but it's breaking it down per hour, per day, per week, per month. And generating these reports based on utilization metrics... And we can go back roughly, I think we're up to three, three to four years now. We actually haven't purged any of the data because it's, you know, we're not getting that per second granularity.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-006-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "And a, a big reason why that was the case was because we needed longer term retention for the data. Cost management was only storing data for about four months and we needed historical trends going back at least, you know, five, seven years.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-006-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprintWalkthrough.m4a",
    "timestamp_in": "00:01:54",
    "timestamp_out": "00:02:16",
    "quote": "their needs for capacity planning require a much larger volume of historic data while the resource optimization is much more of a time and place kind of shorter time scale that they're looking at. So a lot of the customers that we spoke to are trying to serve both their capacity planning and their resource optimization needs by consuming the data through their APIs which often leads to workarounds right where they're rolling their own dashboards through Tableau or Grafana or PowerBI in order to not only present this resource optimization view but a capacity planning lens as well.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 7: Rigid Namespace Limits and Difficulty Negotiating Resources
**Markdown Summary:**
Application teams are constrained by namespace limits imposed by infrastructure teams, and they face significant challenges when trying to negotiate for higher quotas, with such requests often being denied. This creates a rigid environment where teams must fit within predefined resource buckets, hindering their ability to scale or adapt to increased demand without extensive back-and-forth.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-007",
  "job_statement": "When operating within namespace limits, I want to easily adjust my resource quotas based on application needs, so I can ensure optimal performance and scalability.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-007-1"
    },
    {
      "provenance_id": "PROV-PROB-007-2"
    },
    {
      "provenance_id": "PROV-PROB-007-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-007-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Think it's a little, basically the infrastructure team has imposed limits per namespace for the teams, and then the teams have to fit in there and then there's a negotiation from those teams with the infrastructure team if they want more. And so far that's pretty much been a no.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-007-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:17:04",
    "timestamp_out": null,
    "quote": "Yeah, yeah, exactly. There, there is a lot of back and forth, you know, as their tenants are planning new deployments or you know, bringing in onboarding new applications a lot of the time there, there's, you know, they want, you know, naturally they want more resources for those applications, for those deployments. So there is a bit of a, I guess a negotiation.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-007-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprintWalkthrough.m4a",
    "timestamp_in": "00:03:00",
    "timestamp_out": "00:03:13",
    "quote": "as we move out of this negotiation phase, right, we see um we start to see, you know, they're deploying to production. And one of the big pain points that we heard in terms of the configuration um of for alerts for usage spikes is that our product has the opportunity to support them better and has the opportunity to not only put usage alerts um at the cluster level, but perhaps the pod level and the container level. So that level of granular alerting control is something that's very important in terms of enabling that self-service experience that our platform engineering teams are hoping to enable.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 8: Lack of Visibility into Costing Impacts of Pipeline Changes
**Markdown Summary:**
Teams performing pipeline work and service chart work to simplify developer processes often lack good visibility into how modifications or changes to pipelines, resources, and limits can have drastic effects on costing. This absence of direct insight makes it difficult to understand the financial implications of their development efforts.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-008",
  "job_statement": "When making changes to pipelines and services, I want to understand the real-time costing impacts, so I can optimize resource allocation effectively.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-008-1"
    },
    {
      "provenance_id": "PROV-PROB-008-2"
    },
    {
      "provenance_id": "PROV-PROB-008-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-008-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "So we do quite a bit of pipeline work and service, you know, service chart work to make it easier on other people. So as a result, we tend to use a lot of resources indirectly. So if we, for instance, modify or change any of our pipelines, resources, limits, et cetera, can have drastic effects on costing, but we don't really have good visibility into that.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-008-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "So we do quite a bit of pipeline work and service, you know, service chart work to make it easier on other people. So as a result, we tend to use a lot of resources indirectly. So if we, for instance, modify or change any of our pipelines, resources, limits, et cetera, can have drastic effects on costing, but we don't really have good visibility into that.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-008-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "So we do quite a bit of pipeline work and service, you know, service chart work to make it easier on other people . So as a result, we tend to use a lot of resources indirectly. So if we, for instance, modify or change any of our pipelines, resources, limits, et cetera, can have drastic effects on costing, but we don't really have good visibility into that.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 9: Difficulty Applying Changes in a Decentralized GitOps Model
**Markdown Summary:**
In decentralized environments utilizing GitOps, platform teams face a challenge when needing to apply changes or strong recommendations to configurations. Resources in the environment are often overwritten by Argo CD configurations, requiring the platform team to work directly with each application team. While this ensures understanding, it becomes difficult due to the distributed model where each team manages its own workloads and production environments.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-009",
  "job_statement": "When managing a decentralized GitOps environment, I want to efficiently apply configuration changes and optimization recommendations, so I can ensure consistent and optimized workloads.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-009-1"
    },
    {
      "provenance_id": "PROV-PROB-009-2"
    },
    {
      "provenance_id": "PROV-PROB-009-3"
    },
    {
      "provenance_id": "PROV-PROB-009-4"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-009-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:41:10",
    "timestamp_out": null,
    "quote": "And so we can't just patch resources out in the environment because those would be overwritten by the Argo CD configuration. So that's one of our challenges is, you know, when we do need or strongly need or want to apply a change, we have to work with a team, which is in part good because we wanna make sure that they understand what we're doing and such.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-009-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:41:10",
    "timestamp_out": null,
    "quote": "But it can also be a challenge because of this kind of distributed model where each team is responsible for their own workloads and their own production and stuff. And we are just kind of the, the gatekeepers of the environment.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-009-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:41:10",
    "timestamp_out": null,
    "quote": "And so we can't patch resources out in the environment because those would be overwritten by the Argo CD configuration. So that's one of our challenges is, you know, when we do need or strongly need or want to apply a change, we have to work with a team, which is in part good because we wanna make sure that they understand what we're doing and such.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-009-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:41:10",
    "timestamp_out": null,
    "quote": "But it can also be a challenge because of this kind of distributed model where each team is responsible for their own workloads and their own production and stuff. And we are just kind of the, the gatekeepers of the environment.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 10: Chargeback/Showback Not Implemented or Aligned with Org Culture
**Markdown Summary:**
For some organizations, chargeback and showback activities for cloud resource consumption are not yet in place, nor are they currently planned. This is often due to the nature of the organization (e.g., public institution) or a lack of corporate planning to move in that direction, making it difficult to incentivize teams to reduce consumption based on direct cost accountability.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-010",
  "job_statement": "When managing cloud resource consumption, I want to implement chargeback and showback, so I can hold teams accountable for their costs and incentivize reduced consumption.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-010-1"
    },
    {
      "provenance_id": "PROV-PROB-010-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-010-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:20:31",
    "timestamp_out": null,
    "quote": "So then the chargeback and showback activity isn't in place yet. Is that accurate? ... Yeah, I don't think that's planned because that's not how this organization works at the moment.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-010-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:21:04",
    "timestamp_out": null,
    "quote": "For me personally, it would be easier if we could just charge the teams what they cost and then they really start thinking about, Hey, I need to consume less. But yeah, I don't know the the corporate planning on that or if they want to move that way or not. Then the why and the how behind it, it's a public institution, so yeah.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 11: Optimization Suggestions Not Always Suitable for Critical Workloads
**Markdown Summary:**
Automated optimization suggestions from the console may not be suitable for critical production applications, such as Kafka, where a "heavy over allocation" or decent buffer of compute resources is intentionally maintained for mission-critical reliability and to handle rare burst events. Users find the suggestions sometimes "cutting it close" and must cautiously review and adjust them based on their specific workload requirements.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-011",
  "job_statement": "When receiving optimization recommendations, I want to ensure they align with the specific requirements of critical applications, so I can balance cost efficiency with reliability and performance for mission-critical workloads.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-011-1"
    },
    {
      "provenance_id": "PROV-PROB-011-2"
    },
    {
      "provenance_id": "PROV-PROB-011-3"
    },
    {
      "provenance_id": "PROV-PROB-011-4"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-011-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:02:42",
    "timestamp_out": null,
    "quote": "So we just kind of look in the console, see what it suggests and kind of take it with a grain of salt, 'cause sometimes the suggestions it does make might not be what we want, for like for example Kafka, we kind of want that heavy over allocation for production. Where the suggestions might be just a little too, I don't know, cutting it close I guess I guess you could say.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-011-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:13:33",
    "timestamp_out": null,
    "quote": "I think for like for example the Kafka example, we do want a decent buffer of compute just 'cause there it's like mission critical application. And so we've purposely have done that and I, I haven't looked at actually what the optimizer suggests for it, but I'm sure it'll suggest probably like 50% less than what we've done at a minimum.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-011-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:13:33",
    "timestamp_out": null,
    "quote": "But we do see like burst and stuff like that where it does get a little closer to the allocation but it's kind of, they're somewhat rare events though, but it does happen.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROB-011-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:02:42",
    "timestamp_out": null,
    "quote": "So we just kind of look in the console, see what it suggests and kind of take it with a grain of salt, 'cause sometimes the suggestions it does make might not be what we want, for like for example Kafka, we kind of want that heavy over allocation for production. Where the suggestions might be just a little too, I don't know, cutting it close I guess I guess you could say.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 12: Automated Optimization Application is Too Risky/Lacks Control
**Markdown Summary:**
Automatically applying recommended configurations, especially based on short historical windows like the past 7 days, is considered too risky due to potential impacts from peak utilization. Users express a need for manual review and control, preferring a button-triggered application rather than full automation, and requiring integration with existing source control systems like Jira or GitHub for changes. This indicates a general reluctance to fully automate due to a desire for manual control, akin to not being ready for "autopilot".

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-012",
  "job_statement": "When optimizing resource configurations, I want to safely apply recommendations, so I can maintain control and integrate changes with existing workflows.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-012-1"
    },
    {
      "provenance_id": "PROV-PROB-012-2"
    },
    {
      "provenance_id": "PROV-PROB-012-3"
    },
    {
      "provenance_id": "PROV-PROB-012-4"
    },
    {
      "provenance_id": "PROV-PROB-012-5"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-012-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Past 7 days automatic application of recommended configuration is a little bit risky - because of the Peak utilization",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-012-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "What is the window that we want? Should be a button instead of automatic, one person should still review it. Needs to go to source config - JIRA, pull request github, something that updates.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-012-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:33:00",
    "timestamp_out": null,
    "quote": "Yeah, I don't know. That's a hard problem actually. But ... Yeah, it's, it's like the equivalent of autopilot basically where I don't think anyone's really ready to give up manual control or whatnot or completely take their hands off the wheel essentially.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-012-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:33:00",
    "timestamp_out": null,
    "quote": "Yeah, I don't know. That's a hard problem actually. But ... Yeah, it's, it's like the equivalent of autopilot basically where I don't think anyone's really ready to give up manual control or whatnot or completely take their hands off the wheel essentially.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-012-5",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:05:57",
    "timestamp_out": null,
    "quote": "Yeah, I'm sure there'll be configurations. You'd have to you know, give it hints of like don't go below this or above these thresholds or you know, like a window or you know, 'cause yeah you're right. Like it can break things pretty easily if not done right.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 13: Alert Fatigue from Noisy Alerts
**Markdown Summary:**
When alerts for platform usage are initially created, they tend to be very "noisy," leading to users ignoring all alarms and monitors. Significant effort is required to tune these alerts to ensure they are quiet and only deliver warnings or critical (Sev 1) issues, which happen infrequently.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-013",
  "job_statement": "When monitoring cloud environments, I want to receive actionable and relevant alerts, so I can avoid alert fatigue and respond only to critical issues.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-013-1"
    },
    {
      "provenance_id": "PROV-PROB-013-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-013-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:14:41",
    "timestamp_out": null,
    "quote": "Yeah, when we first created alerts for the platform, it was really noisy and we, we definitely made a lot of effort to tune those all out. 'cause you know, when it's too noisy you just ignore all the alarms and monitors, right?",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-013-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:14:41",
    "timestamp_out": null,
    "quote": "So yeah, now it's really quiet. We only really get warnings in like sev ones, well sev ones don't happen that often but, but yeah, that's kind of the gist of it.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 14: Manual Effort for Optimization Tweaks
**Markdown Summary:**
Users desire an ultimate state where they don't have to manually perform optimization tweaks, envisioning an automated process where an operator automatically adjusts resource requests and limits based on metrics. Currently, this process requires manual intervention, which can be tricky with systems like Argo syncing configurations.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-014",
  "job_statement": "When optimizing cloud resources, I want to eliminate manual tweaking of configurations, so I can achieve continuous and effortless optimization.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-014-1"
    },
    {
      "provenance_id": "PROV-PROB-014-2"
    },
    {
      "provenance_id": "PROV-PROB-014-3"
    },
    {
      "provenance_id": "PROV-PROB-014-4"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-014-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:05:25",
    "timestamp_out": null,
    "quote": "I think the ultimate would be not having to do it at all where it's all automatic automated where the operator can just make those tweaks for you based on metrics.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-014-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:29:22",
    "timestamp_out": null,
    "quote": "the use case I would use it for is kinda what we talked about for is to try and automate the optimization suggestions so we don't have to do go to the console at all.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-014-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:30:25",
    "timestamp_out": null,
    "quote": "Automate as in, in the cluster set the request and limits on the deployment or pod or you know, whatever workload it is for you automatically. Which, which is a little tricky 'cause we have Argo syncing things and it would, you know, there'd be some conflict there but, but the gist of it would be like automatic vertical, I don't know if you'd call it vertical scaling but for vertical tuning.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-014-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:30:25",
    "timestamp_out": null,
    "quote": "Automate as in, in the cluster set the request and limits on the deployment or pod or you know, whatever workload it is for you automatically. Which, which is a little tricky 'cause we have Argo syncing things and it would, you know, there'd be some conflict there but, but the gist of it would be like automatic vertical, I don't know if you'd call it vertical scaling but for vertical tuning.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 15: Painful Onboarding Process and Limited Adoption
**Markdown Summary:**
The onboarding process, particularly for accessing the hybrid cloud console, is described as painful due to issues like the lack of SSO. This difficulty has led to organizations limiting onboarding only to team leads to reduce the burden on the platform team, which in turn limits broader adoption and self-service capabilities for application teams.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-015",
  "job_statement": "When onboarding new users to cloud platforms, I want a streamlined and easy process, so I can achieve widespread adoption and enable self-service.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-015-1"
    },
    {
      "provenance_id": "PROV-PROB-015-2"
    },
    {
      "provenance_id": "PROV-PROB-015-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-015-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:34:55",
    "timestamp_out": null,
    "quote": "I would say the big thing with and mentioned before was adding SSO to the hybrid console, Just onboarding is a bit painful. That's why we actually limited onboarding for team leads just to kind of lower the burden for us.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-015-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprintWalkthrough.m4a",
    "timestamp_in": "00:02:44",
    "timestamp_out": "00:02:59",
    "quote": "And you know one of the other challenges in terms of enabling self-service visibility is within the context of hybrid cloud console. There isn't an SSO solution. So that's another reason why the customers are working around sort of what Red Hat's providing in order to deliver this self-service experience that their application teams need in order to onboard and manage their applications uh compliant uh in a compliant fashion.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-015-3",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Onboarding to MCMP and gathering specifics for MCMP is likely not a complete view of the full onboarding requirement.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 16: Users Cannot Request New Services Not in Catalog
**Markdown Summary:**
When consumers or users (like Maureen and Craig) cannot find a needed service in the existing catalog, they lack an effective way to request a new one. The operating model needs to support continuous, user-driven expansion of services, or it risks losing user favor and stalling digital transformation enablement.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-016",
  "job_statement": "When a desired service is not available, I want to easily request its addition to the catalog, so I can ensure continuous access to needed resources.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-016-1"
    },
    {
      "provenance_id": "PROV-PROB-016-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-016-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "When Maureen and Craig don’t see what they need, they need a way to request a new service.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-016-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "The operating model must be able to support continuous, user-driven expansion, or it will quickly lose favor with the users and will stall in its enablement of the transformation.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 17: Difficulty Achieving Fully Optimized State Due to Continuous Development
**Markdown Summary:**
Achieving a "finally optimized" state for applications is challenging and perhaps impossible in the context of ongoing software development. Constraints are constantly changing with new releases, making continuous optimization a moving target where optimization efforts can sometimes become more expensive than simply letting the current state persist.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-017",
  "job_statement": "When undergoing continuous software development, I want to achieve and maintain an optimized application state, so I can ensure efficient resource utilization despite evolving constraints.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-017-1"
    },
    {
      "provenance_id": "PROV-PROB-017-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-017-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "I don't know that you would ever have something finally optimized in with ongoing software development just because the, the constraints are constantly changing as you do more releases.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-017-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "I think in our environment it's, as long as you're not too much of an outlier, you don't get enough attention to require optimization simply because, you know, at a certain point the optimization becomes more expensive than just letting it go.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 18: Lack of Detailed API Documentation for Customization
**Markdown Summary:**
A significant underserved outcome for users of AI/ML platforms is the lack of detailed documentation for a platform's API when they want to perform customizations. This hinders their ability to integrate and extend the platform effectively.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-018",
  "job_statement": "When customizing an AI/ML platform, I want access to detailed API documentation, so I can integrate and extend its functionalities effectively.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-018-1"
    },
    {
      "provenance_id": "PROV-PROB-018-2"
    },
    {
      "provenance_id": "PROV-PROB-018-3"
    },
    {
      "provenance_id": "PROV-PROB-018-4"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-018-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that there is no detailed documentation of a platform's API when I want to do customization.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-018-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that there is no detailed documentation of a platform's API when I want to do customization.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-018-3",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that there is no detailed documentation of a platform's API when I want to do customization.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-018-4",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that there is no detailed documentation of a platform's API when I want to do customization.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 19: Business Stakeholders Cannot Use Model Predictions Actionably
**Markdown Summary:**
Business stakeholders encounter a problem where they cannot use the predictions generated by AI/ML models in an actionable way. This gap between model output and practical application is an underserved outcome, indicating a need for better integration or interpretation of model results for business use.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-019",
  "job_statement": "When AI/ML models generate predictions, business stakeholders want to use them in an actionable way, so they can make informed decisions and derive business value.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-019-1"
    },
    {
      "provenance_id": "PROV-PROB-019-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-019-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that business stakeholders cannot use the model's predictions in an actionable way.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-019-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that business stakeholders cannot use the model's predictions in an actionable way.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 20: AI/ML Platform Fails to Address Lifecycle Needs
**Markdown Summary:**
Users find that their existing AI/ML platform often fails to adequately address their needs across the entire AI/ML lifecycle, which includes data gathering, model development, deployment, and monitoring. This indicates a fragmentation or inadequacy in platform functionality for end-to-end AI/ML operations.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-020",
  "job_statement": "When managing the AI/ML lifecycle, I want my platform to comprehensively address all my needs from data gathering to model monitoring, so I can execute end-to-end AI/ML operations effectively.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-020-1"
    },
    {
      "provenance_id": "PROV-PROB-020-2"
    },
    {
      "provenance_id": "PROV-PROB-020-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-020-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that my AI/ML platform fails to address my needs across the AI/ML lifecycle (e.g., gather data, develop model, deploy model, model monitoring).",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-020-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that my AI/ML platform fails to address my needs across the AI/ML lifecycle (e.g., gather data, develop model, deploy model, model monitoring).",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-020-3",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that my AI/ML platform fails to address my needs across the AI/ML lifecycle (e.g., gather data, develop model, deploy model, model monitoring).",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 21: AI/ML Models Not Checked for Data Toxicity, Bias, or PII
**Markdown Summary:**
There is a significant concern that AI/ML models are not adequately checked and filtered for data toxicity, bias, and Personal Identifying Information (PII). This unmet need highlights a critical gap in responsible AI development and deployment practices.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-021",
  "job_statement": "When developing and deploying AI/ML models, I want to ensure they are checked and filtered for data toxicity, bias, and PII, so I can maintain ethical standards and compliance.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-021-1"
    },
    {
      "provenance_id": "PROV-PROB-021-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-021-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that an AI/ML model has not been checked and filtered for data toxicity, bias, and Personal Identifying Information.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-021-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that an AI/ML model has not been checked and filtered for data toxicity, bias, and Personal Identifying Information.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 22: Insufficient Environment Resources for LLM Experimentation
**Markdown Summary:**
Users face the problem of not having sufficient environment resources (e.g., big enough laptops, adequate cloud environment access) to effectively experiment, tune, and test Large Language Models (LLMs). This resource constraint hinders the development and optimization of LLM-based applications.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-022",
  "job_statement": "When experimenting with LLMs, I want to have sufficient environment resources, so I can effectively tune and test them.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-022-1"
    },
    {
      "provenance_id": "PROV-PROB-022-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-022-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that I don't have the environment resources I need to experiment, tune, and test an LLM (e.g. big enough laptop, cloud environment access).",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-022-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that I don't have the environment resources I need to experiment, tune, and test an LLM (e.g. big enough laptop, cloud environment access).",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 23: Time-consuming Onboarding for New Team Members to AI/ML Serving Solutions
**Markdown Summary:**
New team members face a significant time burden when trying to get up to speed on maintaining a wide range of AI/ML serving solutions. This indicates a lack of streamlined processes or documentation for quickly onboarding individuals to existing infrastructure and models.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-023",
  "job_statement": "When new team members join, I want them to get up to speed quickly on AI/ML serving solutions, so they can contribute effectively without extensive ramp-up time.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-023-1"
    },
    {
      "provenance_id": "PROV-PROB-023-2"
    },
    {
      "provenance_id": "PROV-PROB-023-3"
    },
    {
      "provenance_id": "PROV-PROB-023-4"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-023-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the time it takes to get up to speed to maintain a wide range of AI/ML serving solutions when I join a new team.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-023-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the time it takes to get up to speed to maintain a wide range of AI/ML serving solutions when I join a new team.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-023-3",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the time it takes to get up to speed to maintain a wide range of AI/ML serving solutions when I join a new team.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-023-4",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the time it takes to get up to speed to maintain a wide range of AI/ML serving solutions when I join a new team.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 24: Inefficient Data Management and Access for AI/ML Models
**Markdown Summary:**
Users experience significant effort in efficiently managing and accessing data required for building AI/ML models. This indicates bottlenecks in data pipelines, storage, or retrieval mechanisms that impede the model development process.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-024",
  "job_statement": "When building AI/ML models, I want to efficiently manage and access data, so I can streamline the model development process.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-024-1"
    },
    {
      "provenance_id": "PROV-PROB-024-2"
    },
    {
      "provenance_id": "PROV-PROB-024-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-024-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the effort to efficiently manage and access data for building AI/ML models.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-024-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the effort to efficiently manage and access data for building AI/ML models.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-024-3",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the effort to efficiently manage and access data for building AI/ML models.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 25: Excessive Time/Effort for Fine-tuning LLMs During Efficiency Evaluation
**Markdown Summary:**
Users spend considerable time and effort during efficiency evaluation to test various parameter settings when fine-tuning Large Language Models (LLMs). This indicates a need for more efficient and automated tuning processes to accelerate LLM development.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-025",
  "job_statement": "When fine-tuning LLMs, I want to minimize the time and effort for efficiency evaluation, so I can accelerate the tuning process and model development.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-025-1"
    },
    {
      "provenance_id": "PROV-PROB-025-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-025-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the time and effort it takes during efficiency evaluation to test a set of parameter settings when fine tuning my LLM.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-025-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the time and effort it takes during efficiency evaluation to test a set of parameter settings when fine tuning my LLM.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 26: Difficulty Selecting the Best GenAI Model for Specific Use Cases
**Markdown Summary:**
Users find it challenging to select the Generative AI (GenAI) model that performs optimally for their specific use cases. This indicates a need for better guidance, evaluation tools, or model repositories to aid in model selection.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-026",
  "job_statement": "When implementing GenAI, I want to easily select the model that performs best for my specific use case, so I can achieve optimal results.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-026-1"
    },
    {
      "provenance_id": "PROV-PROB-026-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-026-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the effort to select the GenAI model that performs the best for my specific use case.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-026-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the effort to select the GenAI model that performs the best for my specific use case.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 27: LLM Responses are Not Explainable, Predictable, or Repeatable
**Markdown Summary:**
A key problem identified is the lack of explainability, predictability, and repeatability in Large Language Model (LLM) responses. This makes it difficult for users to trust and rely on LLMs for critical applications, hindering their adoption and effective use.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-027",
  "job_statement": "When using LLMs, I want their responses to be explainable, predictable, and repeatable, so I can trust and reliably integrate them into my applications.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-027-1"
    },
    {
      "provenance_id": "PROV-PROB-027-2"
    },
    {
      "provenance_id": "PROV-PROB-027-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-027-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that LLM responses are not explainable, predictable and repeatable.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-027-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that LLM responses are not explainable, predictable and repeatable.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-027-3",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that LLM responses are not explainable, predictable and repeatable.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 28: Overlooking Significant Differences Between Production and Training Model Responses
**Markdown Summary:**
There is a likelihood of overlooking significant differences between the response values of production models and their training counterparts. This gap indicates issues in model monitoring or validation processes that could lead to performance degradation or unexpected behavior in live environments.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-028",
  "job_statement": "When deploying AI/ML models, I want to easily identify significant differences between production and training model responses, so I can ensure consistent performance and prevent issues.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-028-1"
    },
    {
      "provenance_id": "PROV-PROB-028-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-028-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood of overlooking significant differences of the response values of production models compared to training models.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-028-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood of overlooking significant differences of the response values of production models compared to training models.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 29: Difficulty for Data Science Teams to Build and Deploy AI/ML Models
**Markdown Summary:**
Data science teams face challenges and take significant time to build and deploy AI/ML models, indicating a need for streamlined processes and tooling to accelerate the development-to-deployment pipeline.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-029",
  "job_statement": "When building AI/ML models, data science teams want to efficiently build and deploy them, so they can accelerate time-to-market for new models.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-029-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-029-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the time it takes for a data science team to build and deploy AI/ML models.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 30: High Effort to Provision Infrastructure for AI/ML Models
**Markdown Summary:**
Users expend considerable effort provisioning the necessary infrastructure for training and serving AI/ML models. This indicates a bottleneck in setting up compute resources, storage, and networking, which slows down the model lifecycle.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-030",
  "job_statement": "When preparing for AI/ML model training and serving, I want to minimize the effort to provision infrastructure, so I can rapidly set up and scale my environments.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-030-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-030-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the effort it takes to provision the right infrastructure for training and serving my AI/ML models.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 31: Time-consuming Automated Runtime Performance Testing
**Markdown Summary:**
Users experience significant time spent on running automated runtime performance testing for datasets and code versions. This suggests a need for more efficient or accelerated testing frameworks to improve the speed of validation in AI/ML workflows.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-031",
  "job_statement": "When performing automated runtime performance testing, I want to minimize the time it takes for any given dataset and code version, so I can accelerate testing cycles.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-031-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-031-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the time it takes to run automated runtime performance testing for any given dataset and in any code version.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 32: AI/ML Platform Fails to Support End-to-End GenAI Workflows
**Markdown Summary:**
A key underserved outcome is the likelihood that the AI/ML platform fails to adequately support end-to-end Generative AI (GenAI) workflows, including bringing in foundation models, customizing them with user data, serving them, and integrating them into applications. This highlights a need for more comprehensive platform capabilities for GenAI.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-032",
  "job_statement": "When working with Generative AI, I want my AI/ML platform to fully support end-to-end workflows, so I can seamlessly bring in, customize, serve, and integrate foundation models.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-032-1"
    },
    {
      "provenance_id": "PROV-PROB-032-2"
    },
    {
      "provenance_id": "PROV-PROB-032-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-032-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that my AI/ML platform fails to support end to end genAI workflows (e.g., bring in foundation models, customize foundation models with their own data, serve foundation models and integrate them into apps).",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-032-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that my AI/ML platform fails to support end to end genAI workflows (e.g., bring in foundation models, customize foundation models with their own data, serve foundation models and integrate them into apps).",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-032-3",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that my AI/ML platform fails to support end to end genAI workflows (e.g., bring in foundation models, customize foundation models with their own data, serve foundation models and integrate them into apps).",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 33: Lack of Centralized Monitoring for Deployed Models
**Markdown Summary:**
The AI/ML platform often fails to enable data scientists and operations teams to monitor their entire fleet of deployed models from a central location. This dispersed visibility makes it challenging to maintain oversight and respond effectively to issues across all production models.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-033",
  "job_statement": "When managing deployed AI/ML models, I want to monitor the entire fleet from a central location, so I can maintain comprehensive oversight and respond efficiently to issues.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-033-1"
    },
    {
      "provenance_id": "PROV-PROB-033-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-033-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that an AI/ML platform does not enable data scientists and Ops teams to monitor the entire fleet of deployed models from a central location.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-033-2",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the likelihood that an AI/ML platform does not enable data scientists and Ops teams to monitor the entire fleet of deployed models from a central location.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 34: High Effort to Automatically Retrain AI/ML Models
**Markdown Summary:**
Users find that significant effort is required to automatically retrain AI/ML models with up-to-date data. This challenge indicates a need for more streamlined and automated processes for continuous model adaptation and improvement.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-034",
  "job_statement": "When updating AI/ML models, I want to minimize the effort to automatically retrain them with up-to-date data, so I can ensure models remain current and performant.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-034-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-034-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Minimize the effort it takes to automatically retrain AI/ML models with up-to-date data.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 35: Slow and Manual Model Development Process Hinders Accuracy Improvement
**Markdown Summary:**
The process of improving model accuracy is hampered by a slow and manual model development process. Users describe the need for tools to help identify and pinpoint issues causing failures or degradation of performance, and to streamline the process of tracking experiments and hyperparameter tuning.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-035",
  "job_statement": "When developing AI/ML models, I want a faster and more automated development process, so I can efficiently improve model accuracy and identify performance issues.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-035-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-035-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Slow and manual model dev process to improve model accuracy.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 36: Model Drift After Deployment
**Markdown Summary:**
Models experience drift after deployment, performing well initially but degrading over time. This indicates a need for better mechanisms to track and identify changes in model performance post-deployment, as well as to understand the underlying data shifts.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-036",
  "job_statement": "When AI/ML models are deployed, I want to proactively address model drift, so I can maintain their accuracy and performance over time.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-036-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-036-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Model drift after deployment.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 37: Lack of Standardized Testing Frameworks for Gen AI Models
**Markdown Summary:**
There is a struggle with ensuring a unified production-ready testing pipeline for Generative AI models. The lack of standardized testing frameworks means teams are forced to use various, sometimes non-ideal, approaches for testing LLM responses, leading to inconsistencies and inefficiencies.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-037",
  "job_statement": "When testing Generative AI models, I want standardized testing frameworks, so I can ensure consistent and efficient validation of LLM responses.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-037-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-037-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Lack of standardized testing frameworks.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 38: Expensive & Time-Consuming LLM Evaluation Tasks
**Markdown Summary:**
The tasks involved in evaluating Large Language Models (LLMs), particularly those requiring human input for evaluation (e.g., RLHF) or relying on subjective metrics, are expensive and time-consuming. This increases the effort and cost associated with releasing new models to production.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-038",
  "job_statement": "When evaluating LLMs, I want to minimize the expense and time consumed, so I can streamline the release process for new models.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-038-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-038-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Expensive & time consuming.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 39: Time and Resource Consumption for Fine-Tuning LLMs
**Markdown Summary:**
Fine-tuning Large Language Models (LLMs) is described as a timely and computationally intensive process, often requiring significant resources and taking considerable time. This challenge highlights a need for more efficient methods or tools to reduce the overhead of LLM fine-tuning.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-039",
  "job_statement": "When fine-tuning LLMs, I want to minimize time and resource consumption, so I can accelerate the fine-tuning process.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-039-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-039-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Time and resource consumption.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 40: Lack of Common Model Repository for Pretrained Models
**Markdown Summary:**
Even when platforms support training and fine-tuning models, there is a lack of a common repository for pretrained models. This makes it difficult for users to find, evaluate, and choose suitable models from a large collection, leading to manual effort in figuring out appropriate models.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-040",
  "job_statement": "When selecting pretrained models, I want access to a common model repository, so I can easily find and choose suitable models for my tasks.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-040-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-040-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Model repository.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 41: Lack of Standardization for LLM Algorithms
**Markdown Summary:**
There is a lack of standardization in which algorithms work best with LLMs, making it difficult to determine which LLM will suit a particular use case. This ambiguity complicates the development process and decision-making for LLM-based applications.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-041",
  "job_statement": "When developing with LLMs, I want standardized guidance on algorithms, so I can easily determine the best LLM for my use case.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-041-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-041-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Lack of standardization.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 42: Difficulty Converting Notebooks to Deployable Models
**Markdown Summary:**
Users find it challenging to convert a notebook (experimental ML code) into a deployable model and manage the handover between data scientists and MLOps teams. This process is complex due to dependencies, versioning issues, and communication gaps between teams.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-042",
  "job_statement": "When developing ML models in notebooks, I want to easily convert them into deployable models and hand them off to MLOps, so I can streamline the transition from experimentation to production.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-042-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-042-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "I don't think the ability to convert a notebook to a deployable model is so important. Data scientists can experiment in a notebook, but deployment is completely non-correlated. You can have different types of deployment strategies - download the trained weights and push it to AWS, deploy models through sagemaker etc. I don't think it is that important to zero down to one approach.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 43: Skill Mismatch Between Data Scientists and MLOps for Deployment
**Markdown Summary:**
A skill mismatch exists where data scientists may lack the deep technical knowledge required for deployment, and MLOps teams may not have sufficient data science knowledge to infer what the data scientist was trying to achieve. This gap impedes effective collaboration and the smooth transition of models to production.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-043",
  "job_statement": "When deploying ML models, I want to bridge the skill gap between data scientists and MLOps, so I can ensure effective collaboration and smooth model transitions to production.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-043-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-043-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "The coding level of data scientists is low (except a selected few) and the MLOps team do not typically have enough Data Science knowledge to infer what the Data Scientist was trying to do.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 44: Difficulty Choosing the Right Hardware for Deploying ML Models
**Markdown Summary:**
Users find it challenging to choose the right machine or hardware to deploy their ML models, especially when considering cost savings. This requires navigating various options and ensuring the selected hardware aligns with the model's requirements and budget constraints.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-044",
  "job_statement": "When deploying ML models, I want to easily choose the right hardware, so I can optimize performance and cost.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-044-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-044-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Another issue is choosing the right machine to deploy the ML model. Usually a data scientist uses a compute heavy machine while developing the model. But while deploying MLops require to select a best machine which suits the model requirement to save cost.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Problem 45: Handing Off Notebooks for Deployment is Bad Practice
**Markdown Summary:**
The practice of data scientists handling notebooks to other teams for production readiness is considered bad practice. It leads to issues like difficulty replicating environments, non-correlated deployments, and the need for significant manual effort to prepare production-ready code, which should ideally be managed in a shared codebase.

**JSON Schema Block:**
```json
{
  "object_type": "Problem",
  "id": "PROB-045",
  "job_statement": "When moving ML models to production, I want to avoid inefficient and risky handoffs of notebooks, so I can ensure robust and maintainable deployments.",
  "evidence": [
    {
      "provenance_id": "PROV-PROB-045-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-PROB-045-1",
  "evidence_block": {
    "source_filename": "Openshift AI User Outcome Survey Research Report",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Data scientists handling notebooks to other to implement production ready code is a bad practice and should be avoided. People responsible for writing production code should work together with people that build the model in the same codebase.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

### Behaviors

#### Behavior 1: Developer/Consumer Can Self-Service IT Services
**Markdown Summary:**
Maureen, as a Developer and Consumer of IT services, is able to find, order, access within one hour, and use the IT services needed for her job (system development and testing) in a completely self-service manner, with full confidence in the consumed services. This means her job remains the same, but the process of acquiring resources changes to a self-service model.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-001",
  "user_enablement": "Maureen, a Developer and Consumer of IT services, is able to find, order, access within 1 hour, and use the IT services she needs to do her job in a completely self-service manner.",
  "behavior_type": "system_interaction",
  "signals": [
    "self-service experience",
    "access within 1 hour",
    "confidence in services"
  ],
  "acceptance_criteria": [
    "User can independently browse and select services.",
    "Service provisioning is completed within 60 minutes.",
    "User reports high confidence in service reliability."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-001-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-001-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Maureen, a Developer and Consumer of IT services, can - in a completely self-service manner - find, order, access within 1 hour, and use the IT services she needs to do her job (system development and testing), completely confident that the services she consumes will be... In the MCMP operating model Maureen’s job does not change, but how she gets the resources to do her job changes.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 2: Lead Developer Can Integrate DevOps Tools via APIs for "No Touch" Consumption
**Markdown Summary:**
Craig, a Lead Developer and DevOps engineer, is able to find, access, and understand how to use APIs in a self-service and secure manner to integrate his team's DevOps and related CI/CD tools into MCMP facilities. This enables Maureen to have a "no touch" experience when consuming the IT services she needs.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-002",
  "user_enablement": "Craig, Senior Developer and DevOps engineer, is able to integrate his team's DevOps and related (CI/CD) tools into MCMP facilities using APIs.",
  "behavior_type": "system_integration",
  "signals": [
    "self-service API access",
    "secure integration",
    "Maureen's 'no touch' experience"
  ],
  "acceptance_criteria": [
    "Craig can find and access all necessary APIs.",
    "Integration with CI/CD tools is seamless and secure.",
    "Maureen can consume services without manual intervention."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-002-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-002-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Craig, Senior Developer and DevOps engineer, can - in a completely self-service and secure manner - find, access, and understand how to use the APIs needed to integrate his team's DevOps and related (CI/CD) tools into to the facilities of MCMP, so that Maureen can have a \"no touch\" experience in consuming the IT services she needs to do her job.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 3: IT Finance Management Can Facilitate Cost Transparency
**Markdown Summary:**
Jane, from Enterprise IT Finance, is able to facilitate cost transparency and provide a clear understanding of IT spend across multiple cloud providers, lines of business, and operations teams. This empowers her to manage and optimize cloud resource consumption, including budget management.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-003",
  "user_enablement": "Jane, from Enterprise IT Finance, is able to facilitate cost transparency and a clear understanding of IT spend.",
  "behavior_type": "financial_management",
  "signals": [
    "visibility across cloud providers",
    "visibility across lines of business",
    "visibility across operations teams"
  ],
  "acceptance_criteria": [
    "Jane can generate reports showing IT spend by provider.",
    "Jane can generate reports showing IT spend by line of business.",
    "Jane can generate reports showing IT spend by operations team."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-003-1"
    },
    {
      "provenance_id": "PROV-BEH-003-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-003-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Jane, from Enterprise IT Finance, can facilitate cost transparency and a clear understanding of IT spend across multiple cloud providers, lines of business, and operations teams.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-003-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Her role is to manage and optimize the consumption of cloud resources. Jane is also primarily responsible for budget management, so she needs clear and near-real-time visibility to budget status.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 4: IT Operations Director Can Identify Governance Gaps
**Markdown Summary:**
Shawn, as an IT Operations Director, is able to identify gaps in governance and control coverage within the cloud estate in a self-service manner, on a continuous basis. This enables him to manage operations of the cloud estate, balancing control with speed, and transforming IT service consumption and governance.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-004",
  "user_enablement": "Shawn, IT Operation Director, is able to identify gaps in governance and control coverage in the cloud estate.",
  "behavior_type": "governance_monitoring",
  "signals": [
    "self-service identification",
    "continuous monitoring",
    "visibility into cloud estate"
  ],
  "acceptance_criteria": [
    "Shawn can independently identify governance gaps.",
    "Gap identification occurs regularly without manual intervention.",
    "Comprehensive view of control coverage is available."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-004-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-004-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Shawn, IT Operation Director, can identify gaps in governance and control coverage in the cloud estate, self-service, on a continuous basis. As a user of MCMP he is looking to manage operations of the cloud estate. He cares about visibility and governance and works closely with Jane to optimize consumption, while balancing control with speed. As a supplier in the MCMP ecosystem, he is using MCMP as a service delivery channel that transforms how IT services are consumed and governed in his enterprise.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 5: IT Operations Management Can Enable Self-Service Monitoring
**Markdown Summary:**
Sonya, the IT Operations Manager, is able to enable service owners to monitor and manage their own resources in a self-service manner. This involves ensuring tagging strategies are properly implemented and balancing deep technical knowledge with a cost-minded perspective.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-005",
  "user_enablement": "Sonya, the IT Ops Manager, is able to enable service owners to monitor and manage their own resources (self-service).",
  "behavior_type": "service_enablement",
  "signals": [
    "service owners self-managing resources",
    "proper tagging implementation"
  ],
  "acceptance_criteria": [
    "Service owners report ability to self-monitor and manage resources.",
    "Tagging strategies are consistently applied across resources."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-005-1"
    },
    {
      "provenance_id": "PROV-BEH-005-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-005-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Sonya, the IT Ops Manager, can enable service owners to monitor and manage their own resources [self service], reducing the mean time to resolve issues with their resources by 15%.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-005-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Sonya liaises between the lines of business and central IT to ensure tagging strategies are properly implemented.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 6: Sourcing Manager Can See Holistic Resource Costs
**Markdown Summary:**
Roberta, a Sourcing Manager, is able to see a holistic view of the enterprise’s existing resource costs with each provider. This capability allows her to understand overall cloud consumption by provider, service type, and business unit, aiding in forecasting, planning, and managing supplier commitments.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-006",
  "user_enablement": "Roberta, a Sourcing Manager, is able to see a holistic view of the enterprise’s existing resource costs with each provider.",
  "behavior_type": "financial_visibility",
  "signals": [
    "understanding overall cloud consumption",
    "ability to forecast and plan"
  ],
  "acceptance_criteria": [
    "Roberta can access aggregated cost data per provider.",
    "Roberta can generate reports on consumption by service type and business unit.",
    "Cost data is comprehensive enough to inform supplier negotiations."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-006-1"
    },
    {
      "provenance_id": "PROV-BEH-006-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-006-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Roberta, a Sourcing Manager, can see a holistic view of the enterprise’s existing resource costs with each provider enabling a stronger position to negotiate discounted pricing.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-006-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "As a user of MCMP, she needs to understand overall consumption of cloud - by provider, type of service, and business unit – to forecast and plan accordingly and to manage supplier commitments.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 7: VP of Sales Can Provide Comprehensive IT Services Catalog
**Markdown Summary:**
Steve, as VP of Sales, is able to provide his customers with a catalog of IT services that fulfills at least 90% of the market’s needs. This enables him and his team to leverage MCMP as a channel for selling offerings and to act as a feedback mechanism for market needs and opportunities.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-007",
  "user_enablement": "Steve, VP of Sales, is able to provide his customers with a catalog of IT services.",
  "behavior_type": "sales_enablement",
  "signals": [
    "catalog breadth",
    "market needs fulfillment"
  ],
  "acceptance_criteria": [
    "Steve can present a unified service catalog to customers.",
    "The catalog satisfies a high percentage of identified market demands."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-007-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-007-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Steve, VP of Sales, can provide his customers with a catalog of IT services that fulfills at least 90% of the market’s needs. Steve and his team are the face of the Reseller/Service Provider to the marketplace and the feedback mechanism for the needs and opportunities of the marketplace to Reseller/Service Provider offering management.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 8: Project Manager Can Understand Project Spend in Real Time
**Markdown Summary:**
Fran, a Project Manager, is able to reliably and in real time understand the status of her team’s spend in relation to her project budget. This capability is critical for managing costs and resources associated with her projects after setting up teams and ordering services.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-008",
  "user_enablement": "Fran is able to understand the status of her team’s spend in relationship to her project budget.",
  "behavior_type": "financial_monitoring",
  "signals": [
    "reliable spend status",
    "real-time budget visibility"
  ],
  "acceptance_criteria": [
    "Fran can access project spend data consistently.",
    "Spend data updates immediately as costs accrue.",
    "Fran can compare spend against budget targets."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-008-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-008-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Fran is able to understand the status of her team’s spend in relationship to her project budget reliably and in real time. Once the project is under way, Fran is responsible for managing the costs and resources associated to her project.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 9: CIO/IT Leader Can Track and Communicate Transformation Progress
**Markdown Summary:**
Margaret, the CIO/IT Leader, is able to understand and continuously communicate the progress of her operational transformation month to month. This enables her to align IT strategy with business needs and ensure that IT is aligned with digital transformation objectives, often by setting overall cloud strategy.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-009",
  "user_enablement": "Margaret is able to understand and continuously communicate the progress of her operational transformation.",
  "behavior_type": "strategic_oversight",
  "signals": [
    "monthly progress communication",
    "alignment of IT strategy to business needs"
  ],
  "acceptance_criteria": [
    "Margaret can access up-to-date transformation metrics.",
    "Progress reports are shared consistently and clearly.",
    "IT strategy demonstrably supports digital transformation objectives."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-009-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-009-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Margaret is able to understand and continuously communicate the progress of her operational transformation month to month. Her job is to align IT to the needs of the business. Where digital transformation is in focus, she must insure IT is aligned to the objectives of the digital transformation, which often entails setting overall cloud strategy.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 10: IBM Project Executive Can Recommend Transformation Paths
**Markdown Summary:**
Phillipe, the senior IBM executive responsible for the client relationship, is able to make recommendations on transformation paths. These recommendations are based on a repository of best practices from previous MCMP implementations, allowing him to guide clients effectively.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-010",
  "user_enablement": "Phillipe, a client project executive, is able to make recommendations on transformation path.",
  "behavior_type": "advisory",
  "signals": [
    "recommendations based on best practices",
    "reduced client time to value"
  ],
  "acceptance_criteria": [
    "Phillipe can access a comprehensive repository of MCMP best practices.",
    "Clients receive actionable transformation path recommendations.",
    "Client time to value metrics show improvement."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-010-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-010-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Phillipe, a client project executive is able to make recommendations on transformation path based on a repository of best practices from previous implementations of MCMP to reduce a client's time to value from 180 days to 90 days.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 11: Customer Support Can Recommend Configurations Based on Best Practices
**Markdown Summary:**
Emily, a Customer Support and Sales Through Service representative, is able to make recommendations on configuration. These recommendations are based on a repository of best practices from previous MCMP implementations, helping to reduce a client's time to value. Emily serves as the first line of support and ambassador for MCMP, conveying customer requirements and product offerings.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-011",
  "user_enablement": "Emily is able to make recommendations on configuration, based on a repository of best practices.",
  "behavior_type": "customer_support",
  "signals": [
    "configuration recommendations provided",
    "reduced client time to value",
    "customer onboarding efficiency"
  ],
  "acceptance_criteria": [
    "Emily can access and utilize best practice repositories for configurations.",
    "Clients successfully implement recommended configurations.",
    "Client onboarding and transition phases are smooth and efficient."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-011-1"
    },
    {
      "provenance_id": "PROV-BEH-011-2"
    },
    {
      "provenance_id": "PROV-BEH-011-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-011-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Emily is able to make recommendations on configuration, based on a repository of best practices from previous implementations of MCMP to reduce a client's time to value from 180 days to 90 days.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-011-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Emily is the first line of support between the users of the MCMP – those using MCMP to consume services and do their jobs – and the back-office support structure. Emily fields questions, requests for new services, and acts as the ambassador from MCMP to the consumer personas.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-011-3",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "In that environment she helps onboard and orient customers, and acts as the eyes and ears of the Service Provider – conveying in customer requirements and conveying out product offerings.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 12: Platform Admin Can Establish and See Relationships Between Users, Policies, and Accounts
**Markdown Summary:**
Marshall, an IT Administrator, is able to establish and see the relationships between users, groups, policies, and accounts without needing to navigate to multiple discrete interfaces. This streamlines his role in onboarding and supporting customers, configuring MCMP for use by organizations.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-012",
  "user_enablement": "Marshall, an IT Administrator, is able to establish and see the relationships between users, groups, policies, and accounts without needing to navigate to multiple discrete interfaces.",
  "behavior_type": "platform_configuration",
  "signals": [
    "unified view of relationships",
    "reduced navigation effort"
  ],
  "acceptance_criteria": [
    "Marshall can map user-to-policy and account relationships easily.",
    "No need to switch between different UIs for relationship visibility.",
    "Configuration tasks are completed efficiently."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-012-1"
    },
    {
      "provenance_id": "PROV-BEH-012-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-012-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Marshall, an IT Administrator, is able to establish and see the relationships between users, groups, policies, and accounts without needing to navigate to multiple discrete interfaces.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-012-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Marshall will proceed to configure MCMP for use by Sonya’s organization. He will set up teams, approval policies, initial budget(s) Marshall will also trigger the custom/integration development, if in scope, with the IBM MCMP Delivery team.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 13: IT Finance Manager Can Be Automatically Notified of Over-Budget Resources
**Markdown Summary:**
Jane, the IT Finance Manager, is able to be automatically notified of over-budget cloud resources on her own terms, without requiring manual analysis. This enhances her ability to manage consumption and ensure financial management policies are correctly implemented.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-013",
  "user_enablement": "Jane, IT Finance Manager, is able to be automatically notified of over budget cloud resources, on her own terms without manual analysis.",
  "behavior_type": "alert_reception",
  "signals": [
    "automatic notifications",
    "customizable terms",
    "no manual analysis required"
  ],
  "acceptance_criteria": [
    "Jane receives alerts for budget overruns automatically.",
    "Alerts are tailored to Jane's preferences and thresholds.",
    "Manual effort for identifying over-budget resources is eliminated."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-013-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-013-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Jane, IT Finance Manager, can be automatically notified of over budget cloud resources, on her own terms without manual analysis. The persona of Jane will depend on budgets and associated policies to help her manage consumption, so care must be taken in the operating model to make sure they are correctly representing and implementing the financial management policies of the business.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 14: IT Finance Manager Can Enable Proactive Budget Monitoring for Owners
**Markdown Summary:**
Jane, the IT Finance Manager, is able to enable budget owners to proactively monitor and manage their costs through self-service capabilities. This decentralizes financial oversight and helps ensure that budget owners have real-time visibility into their spend.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-014",
  "user_enablement": "Jane, the IT Finance Manager, is able to enable budget owners to proactively monitor and manage their costs (self-service).",
  "behavior_type": "financial_enablement",
  "signals": [
    "budget owners actively monitoring",
    "self-service cost management"
  ],
  "acceptance_criteria": [
    "Budget owners access and utilize cost monitoring tools independently.",
    "Budget owners report ability to manage their costs proactively."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-014-1"
    },
    {
      "provenance_id": "PROV-BEH-014-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-014-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Jane, the IT Finance Manager, can enable budget owners to proactively monitor and manage their costs [self service].",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-014-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Approvers need to understand not just the impact of a particular order on their budget, but need ongoing visibility of the status of their budget(s) with respect to spend.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 15: Developer Can Understand Spend in Relation to Budget
**Markdown Summary:**
Craig, a developer, is able to understand the status of his spend in relationship to his budget. This allows him to see the cost and budget impact when he places an order for a service.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-015",
  "user_enablement": "Craig is able to understand the status of his spend in relationship to his budget.",
  "behavior_type": "financial_awareness",
  "signals": [
    "visibility of spend vs. budget",
    "awareness of cost impact on orders"
  ],
  "acceptance_criteria": [
    "Craig can view his current spend and remaining budget.",
    "Craig understands the cost implications before confirming service orders."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-015-1"
    },
    {
      "provenance_id": "PROV-BEH-015-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-015-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Craig is able to understand the status of his spend in relationship to his budget.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-015-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "When Maureen and/or Craig place an order for a service, they should know the cost and budget impact, as should the assigned approver.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 16: IT Finance Manager Can View Consumed Cloud Resources for Chargeback
**Markdown Summary:**
Jane, the IT Finance Manager, is able to view currently consumed cloud resources, gaining an accurate understanding of which assets belong to which departments. This enables easy charge-back and reconciliation efforts and aids in optimizing cloud spend.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-016",
  "user_enablement": "Jane, IT Finance Manager, is able to view currently consumed cloud resources and understand asset allocation by department.",
  "behavior_type": "financial_reporting",
  "signals": [
    "accurate understanding of asset ownership",
    "enabled charge-back and reconciliation",
    "cloud spend reduction"
  ],
  "acceptance_criteria": [
    "Jane can access a dashboard of consumed cloud resources.",
    "Asset ownership is clearly mapped to departments.",
    "Charge-back and reconciliation processes are simplified."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-016-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-016-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Jane, IT Finance Manager, can view currently consumed cloud resources, gaining an accurate understanding of which assets belong to which departments, enabling easy charge-back and reconciliation efforts in days rather than weeks and reducing cloud spend by 20%.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 17: Billing Analyst Can Generate Itemized Invoices Automatically
**Markdown Summary:**
Charlotte, a billing analyst, is able to generate itemized invoices allocated by budget owners based on actual consumption automatically within 30 minutes. This capability is especially pronounced in the Reseller/Service Provider environment, where she resolves billing inquiries and contributes to customer delight and growth opportunities.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-017",
  "user_enablement": "Charlotte, a billing analyst, is able to generate itemized invoices allocated by budget owners based on actual consumption automatically within 30 minutes.",
  "behavior_type": "billing_automation",
  "signals": [
    "automatic invoice generation",
    "invoice generation within 30 minutes",
    "billing inquiry resolution"
  ],
  "acceptance_criteria": [
    "Invoices are generated without manual intervention.",
    "Invoices are available within 30 minutes of request/trigger.",
    "Invoices accurately reflect actual consumption and allocation.",
    "Charlotte can effectively resolve billing inquiries."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-017-1"
    },
    {
      "provenance_id": "PROV-BEH-017-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-017-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Charlotte, a billing analyst, can generate itemized invoices allocated by budget owners based on actual consumption automatically within 30 minutes.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-017-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Much more pronounced in the Reseller/Service Provider environment, Charlotte is the resolver for billing inquiries and billing issue resolution, and in the spirit of Sales Through Service represents a touch-point opportunity to delight the customer and explore new opportunities and growth in the customer relationship.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 18: Users Can Self-Service Requests for New Services with Visibility
**Markdown Summary:**
When users like Craig or Emily don’t see a needed service, they are able to self-service a request for a new service and receive immediate response with continuous visibility into the status of their request. This process is crucial for continuous, user-driven expansion of services.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-018",
  "user_enablement": "When Craig/Emily don’t see what they need, they are able to self-service a request for a new service, and have immediate response with continuous visibility into the status of their request.",
  "behavior_type": "service_request",
  "signals": [
    "self-service request submission",
    "immediate response to request",
    "continuous status visibility"
  ],
  "acceptance_criteria": [
    "Users can submit new service requests without assistance.",
    "Confirmation of request submission is instant.",
    "Users can track the progress of their request at any time."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-018-1"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-018-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "When Craig/Emily don’t see what they need, they can self-service a request for a new service, and have immediate response with continuous visibility into the status of their request. The operating model must be able to support continuous, user-driven expansion, or it will quickly lose favor with the users and will stall in its enablement of the transformation.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 19: Digital Strategy Director Can Rapidly Capitalize on Market Opportunities
**Markdown Summary:**
Ted, a Digital Strategy Director, is able to capitalize on newly identified market opportunities by bringing a pilot experience to his customers in a month, significantly faster than traditional timelines. This involves ensuring the service portfolio provides the right service at the right time, aligning with strategic campaigns or competitive opportunities.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-019",
  "user_enablement": "Ted, a Digital Strategy Director, is able to capitalize on a newly identified market opportunity by bringing a pilot experience to his customers in a month.",
  "behavior_type": "market_responsiveness",
  "signals": [
    "rapid pilot deployment",
    "strategic portfolio alignment"
  ],
  "acceptance_criteria": [
    "Pilot experiences are launched within one month of opportunity identification.",
    "Service portfolio consistently meets market needs.",
    "Ted can effectively initiate new service development in response to strategic cues."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-019-1"
    },
    {
      "provenance_id": "PROV-BEH-019-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-019-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Ted, a Digital Strategy Director, can capitalize on a newly identified market opportunity, bringing a pilot experience to his customers in a month as opposed to six - nine months.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-019-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "The Ted persona plays a key role in this life cycle, making sure the service portfolio is providing the right service at the right time. ... Ted may want to insert a new service into the development pipeline as part of a strategic campaign or competitive opportunity.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 20: Digital Service Owner Can Commercialize Products Efficiently and Compliantly
**Markdown Summary:**
Patricia, a Digital Service Owner, is able to commercialize a service product to meet catalog compliance, merchandising, documentation, and pricing requirements with zero errors, adding no more than 4 hours to her work. She takes direction from strategic roles and collaborates with architects and suppliers to develop services ready for the MCMP catalog.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-020",
  "user_enablement": "Patricia can commercialize a service product to meet catalog compliance, merchandising, documentation, and pricing requirements with zero error adding no more than 4 hours to her work.",
  "behavior_type": "product_commercialization",
  "signals": [
    "zero errors in commercialization",
    "minimal time added to work (<= 4 hours)",
    "compliance with catalog standards"
  ],
  "acceptance_criteria": [
    "Service products consistently meet all catalog requirements.",
    "The process of commercialization is highly efficient.",
    "Products are easily understandable and usable for customers."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-020-1"
    },
    {
      "provenance_id": "PROV-BEH-020-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-020-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Patricia can commercialize a service product to meet catalog compliance, merchandising, documentation, and pricing requirements with zero error adding no more than 4 hours to her work.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-020-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "She takes direction from Ted and Steve, combines it with her knowledge of her target market and the strategy of her product line, then works with Jonathan and/or suppliers to develop and make ready services to be published to the MCMP catalog. Patricia is also responsible for pricing of her offerings, and making her service products understandable (description and offering collateral), and usable (knowledgebase, FAQs, etc).",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 21: Digital Service Architect Can Create Standardized, Compliant, and Optimized Patterns
**Markdown Summary:**
Jonathan, a Digital Service Architect (working with Alvin, SRE), is able to create standardized, compliant, scalable, cost-effective, and reliable patterns. This capability involves capturing requirements, designing service products, authoring templates, and composing services, bridging operations expertise with DevOps practices to ensure high-quality, optimized services.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-021",
  "user_enablement": "Jonathan, a Digital Service Architect (and Alvin, SRE), is able to create standardized compliant, scalable, cost-effective and reliable patterns.",
  "behavior_type": "service_design",
  "signals": [
    "pattern standardization",
    "compliance adherence",
    "scalability of patterns",
    "cost-effectiveness of patterns",
    "reliability of patterns"
  ],
  "acceptance_criteria": [
    "Patterns are consistently applied across services.",
    "Services meet all regulatory and internal compliance standards.",
    "Patterns support high-scale deployments.",
    "Cost analysis confirms efficiency of designed services.",
    "Designed services demonstrate high uptime and minimal failures."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-021-1"
    },
    {
      "provenance_id": "PROV-BEH-021-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-021-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Jonathan, a Digital Service Architect (and Alvin, SRE), is able to create standardized compliant, scalable, cost-effective and reliable patterns, resulting in services that are 100% compliant, defect-free and cost optimized.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-021-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Jonathan represents the category of roles involved in the process of capturing requirements for service products, service product design, template authoring, and service composition. ... Alvin works with Jonathan (and others responsible for automation/template development) to introduce resilience and operational controls into the design and authoring of templates (automation patterns). Alvin bridges operations expertise and discipline to the world of DevOps and “platform as code”.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 22: Content Lifecycle Manager Can Onboard and Validate Catalog Submissions Independently
**Markdown Summary:**
Stacy, the Catalog Curator, is able to onboard and validate any new catalog submission without needing to consult others for compliance, pricing, sizing, technical, commercial, and role-based access information. She coordinates with various personas (Patricia for descriptions, Jonathan for content, Ted for direction) to pull together content for publishing and also monitors content catalog usage"
  ],
  "acceptance_criteria": [
    "Stacy can approve catalog submissions without external dependency.",
    "All required information for submission is self-contained or accessible.",
    "Catalog content is consistently accurate and well-managed.",
    "Stacy regularly assesses catalog performance metrics."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-022-1"
    },
    {
      "provenance_id": "PROV-BEH-022-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-022-1",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Stacy, the Catalog Curator can onboard and validate any new catalog sub ission without calling anybody for the required compliance, pricing, sizing, technical, commercial and role-based access information and IBM Services Stacy takes the package from Patricia and publishes it in the MCMP catalog.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-022-2",
  "evidence_block": {
    "source_filename": "IBM_MCMP_OM_TLV2.3_2020-1-8.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "She must coordinate with Patricia to get service product descriptions, logos, and pricing. Jonathan provides the raw content - the developed and tested, composed service. Ted provides the direction on categorization and overall portfolio. Stacy pulls it all together. ... She also needs to be plugged in to how the content is being used and by whom so she can help Ted understand how the portfolio is performing.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 23: Platform Engineering Compares Actual Usage with Requested Amount
**Markdown Summary:**
The Platform Engineering Team is able to compare the actual usage of resources with the requested amount by extracting data from the Cost Management Metrics Operator API. This is done when app teams request larger namespace quotas, allowing them to validate if the requested amount is truly needed based on historical usage and scaling projections.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-023",
  "user_enablement": "Platform Engineering Team is able to compare Actual Usage with Requested Amount via data extracted from Cost Mgmt Metrics Operator API.",
  "behavior_type": "resource_validation",
  "signals": [
    "data extraction from API",
    "usage vs. request comparison"
  ],
  "acceptance_criteria": [
    "Platform team can access usage data from Cost Management Metrics Operator API.",
    "The comparison accurately reflects resource consumption patterns.",
    "Justification for requested quotas is data-driven."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-023-1"
    },
    {
      "provenance_id": "PROV-BEH-023-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-023-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Compares Actual Usage with Requested Amount via data extracted from Cost Mgmt Metrics Operator API.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-023-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:10:21",
    "timestamp_out": null,
    "quote": "In that case, we have our own view on the Tableau side, and we would say, okay, what are, what have they actually been using versus what they're requesting? And if they're not going to, based on what, how they're gonna scale up, do they really need this amount?",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 24: Platform Engineering Exports Cost Management Data to Internal Databases
**Markdown Summary:**
The Platform Engineering Team is able to export data from the Cost Management Metrics Operator API into an internal Postgres database. This workaround is implemented to overcome limitations in the cost management tool, such as limited historical data retention, enabling local analysis and longer-term trend building.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-024",
  "user_enablement": "Platform Engineering Team is able to export data from Cost Mgmt Metrics Operator API into Postgres.",
  "behavior_type": "data_management",
  "signals": [
    "data extraction automation",
    "longer-term data retention",
    "local data analysis"
  ],
  "acceptance_criteria": [
    "Data from Cost Management API is successfully transferred to Postgres.",
    "Historical data is retained beyond the native tool's limits.",
    "Internal analysis processes can leverage the extracted data."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-024-1"
    },
    {
      "provenance_id": "PROV-BEH-024-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-024-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Exports data from Cost Mgmt Metrics Operator API into Postgres.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-024-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "I implemented a process to extract data from the cost management API stored into Postgres database, and then we do all of our analysis local side. And a, a big reason why that was the case was because we needed longer term retention for the data. Cost management was only storing data for about four months and we needed historical trends going back at least, you know, five, seven years.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 25: Platform Engineering Makes Recommendations for Namespace Quota
**Markdown Summary:**
The Platform Engineering Team is able to make recommendations for namespace quotas based on their analysis of actual usage versus
  "acceptance_criteria": [
    "Recommendations are supported by usage analysis.",
    "App teams receive clear guidance on quota adjustments.",
    "The negotiation process leads to optimized resource allocation."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-025-1"
    },
    {
      "provenance_id": "PROV-BEH-025-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-025-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Makes recommendation for namespace quota based on analysis.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-025-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:17:04",
    "timestamp_out": null,
    "quote": "So our team would, you know, when those requests come in, we would kind of look at these views to validate, you know, do we actually need more resources here or is there some improvement we can do to make better use of existing resources?",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 26: Application Teams Update Configurations Based on Platform Recommendations
**Markdown Summary:**
Application teams are able to update their configurations based on recommendations received from the Platform Team, often following a Tech Review process. This ensures that resource allocations are aligned with best practices and optimization goals.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-026",
  },
    {
      "provenance_id": "PROV-BEH-026-2"
    },
    {
      "provenance_id": "PROV-BEH-026-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-026-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "App team updates configurations based on Platform Team Recommendation / Tech Review.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-026-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:34citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-026-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:37:48",
    "timestamp_out": null,
    "quote": "So we would look at their, in their, in their tech review on their path to production and we would make suggestions there. And then those would be kind of required to implement or, or coordinate on, you know, what they think the correct value should be. So path to production is, is one where we clearly communicate that to them.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 27: Platform Team Configures Alerts on Homegrown Platform
**Markdown Summary:**
The Platform Engineering Team is able to configure monitoring and alerting on their homegrown platform. This is a workaround to address the gap in granular alerting control not fully supported by the Hybrid Cloud Console (HCC) platform, ensuring that they can proactively identify issues like cost management data not flowing.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-027",
  "user_enablement": "Platform Team is able to configure Monitor Alerting on Home Rolled Platform.",
  "behavior_type": "alerting_setup",
  "signals":provenance_id": "PROV-BEH-027-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-027-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Configures Monitor Alertsing on Home Rolled Platform.",
    "citation": "[1 seen, when data has not been updated from a source that we consider to be live. ... how do we know proactively when we have to go and check out the cost management operator pod because it's not flowing data and we don't want to just forget about it.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-027-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprintWalkthrough.m4a",
    "timestamp_in": "00:03:13",
    "timestamp_out": "00:03:30",
    "quote": "one of the big pain points that we heard in terms of the configuration um of for alerts for usage spikes is that our product has the opportunity to support them better and has the opportunity to not only put usage alerts um at the cluster level, but perhaps the pod level and the container level. So that level of granular alerting control is something that's very important in terms of enabling that self-service experience that our platform engineering teams are hoping to enable.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 28: Platform Team Monitors for Usage / Cost Spikes
**Markdown Summary:**
The Platform Engineering Team is able to monitor for usage and cost spikes. This is part of their effort to right-size resources and perform capacity planning, leveraging fine-tuned alerts on CPU utilization to proactively understand growth and expansion needs.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-028",
  "user_enablement": "Platform Team is able to monitor for Usage / Cost Spikes.",
  "behavior_type": "performance_monitoring",
  "signals": [
    "spike detection",
    "CPU utilization alerts",
    "capacity planning data"
  ],
  "acceptance_criteria": [
    "Usage and cost spikes are accurately detected
  "object_type": "Provenance",
  "id": "PROV-BEH-028-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Monitors for Usage / Cost Spikes.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-028-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:21:39",
    "timestamp_out": null,
    "quote": "So I would say that's one of our, our primary goals is right sizing also capacity planning. So understanding as are, are we going to, when are we going to need more clusters? How many do we need to scale up existing clusters? So we've created our own": null,
    "quote": "But the cost of management data we are leveraging to help create some of those forecasts for, you know, here's our growth over time, what does it look like and when are we going to have to expand? So, so that's used for strategic planning for capacity as well.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 29: Platform Team Receives Usage Threshold Alerts
**Markdown Summary:**
The Platform Engineering Team is able to receive usage threshold alerts. These alerts are designed to notify them when specific limits are exceeded, prompting action to expand clusters or investigate resource configurations.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-029",
  "user_enablement": "Platform Team is able to receive Usage Threshold Alert.",
  "behavior_type": "alert_reception",
  "signals": [
    "alert notificationBEH-029-3"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-029-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Receives Usage Threshold Alert.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-029-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:21:39",
    "timestamp_out": null,
    "quote": "So we've created our own alerts around our, our own fine tuned alerts around CPU utilization for tenants specifically, right? So filtering out all the system level name spaces and once that goes over a certain limit, you know, we have to expand the cluster and stuff like that.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-029-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:38:57",
    "timestamp_out": null,
    "quote": "We've also had like our on- call engineers. So in production specifically, let me, and then there's a third we have on- call engineers who are on like a weekly rotation. And part of the on- call engineer's responsibility is during the day when they're not handling any fires to go out through production and just, well this is, this has been our, our historical path, right? We're moving to like a new process but go, gone out to production and look what's there, see if there's any horrible events firing some crash loops, stuff like that. And sometimes they will discover, you know, these configurations out there in prod. And then we will, we have a contact email for the namespace that we request from the namespace as a service. So we will engage them through there, through email and in some cases through like a ServiceNow ticket and say, Hey, you know, these, these configurations seem very aggressively high, you know, can work to lower these.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 30: Teams Monitor Pod-level, Namespace, and Container Usage
**Markdown Summary:**
Teams are able to monitor usage at the pod level, namespace level, and container level. This granular visibility is crucial for understanding how application teams are consuming resources within their given quotas and for enabling self-service insights into resource consumption.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-030",
  "user_enablement": "Teams are able to monitor Pod-level, Namespace, and Container Usage.",
  "behavior_type": "resource_monitoring",
  "signals": [
    "granular usage data",
    "self-service visibility"
  ],
  "acceptance_criteria": [
    "Usage data is available at pod, namespace, and container levels.",
    "Teams can independently access and interpret their usage metrics.",
    "Monitoring informs resource allocation decisions within quotas."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-030-1"
    },
    {
      "provenance_id": "PROV-BEH-030-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-030-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Monitors Pod- level Usage. Monitors Namespace"quote": "the platform team is enabling a way to monitor the quota consumption. So how is this application team consuming within the quota that's been uh given to them and can the application team understand if they're approaching their quota limits as well? And that's how that self-service visibility piece really starts to um layer.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 31: Platform Team Enables Self-Service Visibility into Usage
**Markdown Summary:**
The Platform Team is able to enable self-service visibility into usage data, providing specific types of data to application teams. This goes beyond just creating dashboards, aiming to empower application teams to onboard and manage their applications compliantly by themselves.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-031",
  "user_enablement": "Platform Team is able to Enable Self- Service visibility into Usage.",
  "behavior_type": "self_service_enablement",
  "signals": [
    "data availability for self-service",
    "empowered app teams",
    "compliant application management"
  ],
  "acceptance_criteria": [
    "Application teams can independently access and interpret usage data.",
    "Self-service tools reduce dependency on platform team for insights.",
    "Applications are managed in compliance with policies."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-031-1"
    },
    {
      "provenance_id": "PROV-BEH-031-2
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-031-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprintWalkthrough.m4a",
    "timestamp_in": "00:02:29",
    "timestamp_out": "00:02:44",
    "quote": "when we talk about self-service visibility we're not just talking about creating PowerBI dashboards. or um graphfana dashboards. We're talking about actually making specific types of data available so that we can enable self-service for the application teams that we want to onboard onto the system.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 32: Platform Team Defines & Configures Cluster Quota Limits and Cost Models
**Markdown Summary:**
The Platform Team is able to define and configure cluster quota limits and internal cost models. This involves translating business goals into platform solutions, defining unit prices for capacity planning, and setting namespace limits.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-032",
  "user_enablement": "Platform Team is able to Define & Configure Cluster Quota Limits & Cost Models.",
  "behavior_type": "resource_governance",
  "signals": [
    "business goal translation",
    "unit price definition",
    "namespace limit enforcement"
  ],
  "acceptance_criteria": [
    "Quota limits are correctly configured based on strategic goals.",
    "Cost models accurately reflect resource consumption.",
    "Namespace limits are effectively applied to control resource usage."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-032-1"
    },
    {
      "provenance_id": "PROV-BEH-032-2"
    },
    {
      "provenance_id": "PROV-BEH-032-3"
    },
    {
      "provenance_
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-032-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Translate Biz Goals into Platform Team Solutions.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-032-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:10:25",
    "timestamp_out": null,
    "quote": "The infrastructure team has, you know, for instance, imposed a limit of, I think it was three CPUs and five gigs of ram per namespace. And so then the teams start trying to figure out how to make that happen.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-032-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprintWalkthrough.m4a",
    "timestamp_in": "00:02:16",
    "timestamp_out": "00:02:}
}
```

---

#### Behavior 33: Platform Team Defines & Calculates Unit Prices for Capacity Planning
**Markdown Summary:**
The Platform Team is able to define and calculate unit prices for capacity planning. This involves identifying a critical metric, such as CPU core hours, to gauge price and creating a cost model for the enterprise, which is then provided to financial leadership.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-033",
  "user_enablement": "Platform Team is able to Define & Calculate Unit Prices for Capacity Planning.",
  "behavior_type": "financial_modeling",
  "signals": [
    "unit price identification",
    "cost model creation",
    "reporting to leadership"
  ],
  "acceptance_criteria": [
    "Unit prices are clearly defined and consistently applied.",
    "The cost model accurately reflects enterprise resource consumption.",
    "Financial leadership receives actionable cost metrics."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-03 for Capacity Planning.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-033-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "And we have, we had to identify a unit price for the organization. And so there was a lot of discussion towards the end of last year of, you know, what's a good metric that we want to use to gauge price rather than like the cost model. We have kind of our own cost model, you could say, for the enterprise. And that is based on request CPU core hours. So that's the critical metric that we are providing to leadership and that we're using for our costs internally.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior ",
  "id": "BEH-034",
  "user_enablement": "An App Dev Team is able to automate CI/CD as a service.",
  "behavior_type": "service_automation",
  "signals": [
    "CI/CD pipeline automation",
    "developer onboarding ease",
    "GitOps pattern adoption"
  ],
  "acceptance_criteria": [
    "CI/CD processes are fully automated and self-service.",
    "New applications can be onboarded quickly and efficiently.",
    "Teams consistently use standardized pipeline charts for deployments."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-034-1"
    },
    {
      "provenance_id": "PROV-BEH-034-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-034-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.out": null,
    "quote": "We have a infrastructure team we call Fellowship of the Pod that basically exposes OpenShift and Tekton, Argo to the individual teams via an app of apps pattern. So we're GitOps, you know, you've essentially got a GitOps applications repository that points to a whole bunch of different Argo applications that individually will have a GitOps Repo that they share per application. And then there's a source code repo that basically gets built the GitOps Argo applications, almost all of them reference a Brightly pipeline chart to do all of the CI/CD. So you've essentially got a top level Helm chart with a dependency of the chart that we produce that's versioned. Teams pull that in, they can get a, you know, CICD pipeline that does image scanning, builds. I'm trying to remember all the different, some unit tests, integration tests, Sonar is integrated there, a whole bunch of other, other stuff going on. But essentially they, they pull in the chart, set a bunch of values in the values file, and that basically builds their application and deploys it as a, you know, a service or whatnot. We've got Quarkus, Node, DotNet, and then we've got some JavaScript frontend stuff that we're working on putting into CDN.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 35: Bell Canada Provides Self-Service Portal for Tenants
**Markdown Summary:**
Bell Canada is able to provide a self-service portal that is available to all tenants (users). This portal aggregates Prometheus data, samples it by hour, day, week, and month, and generates reports based on utilization metrics. It offers a historical view of quota, allocation, and consumption for CPU, memory, and storage, allowing tenants to see their usage and aiding the platform team in resource allocation decisions.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-035",
  "user_enablement": "Bell Canada is able to provide a self-service portal with long-term historical usage metrics for tenants.",
  "behavior_type": "self_service_reporting",
  "signals": [
    "portal availability to all tenants",
    "aggregated utilization metrics",
    "historical data retention (3-4 years)"
  ],
  "acceptance_criteria": [
    "Tenants can access the portal and view their resource consumption.",
    "Reports provide breakdown of quota, allocation, and usage.",
    "Data retention supports long-term trend analysis for resource allocation."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-01",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:12:12",
    "timestamp_out": null,
    "quote": "So yeah, this is our portal, self- serve. We make it available to all, all our tenants. So all the users Ryan talked about that we support, everyone gets access to this and we use it for the kinda day one. So tenant onboarding and the day two they can use it to kind of get increased, better visibility across the environment. So all the clusters that we support, they're all attached to this and the portal's just, you know, it's interacting with the cluster reading data from it and displaying it so they can all get it in one place. And the, the resource consumption just kinda, and those reports are one part of that. But yeah, so tenants can come in here. This is the historical view that we're talking about. Just give a second to load.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```, per day, per week, per month. And generating these reports based on utilization metrics. So how large is the quota? How much base has been allocated from the quota? What's the actual consumption of the namespace and the pods?",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-035-3",
  "evidence_block": {
    "source_filename": " can make better decisions about how we're allocating resources and, and giving those resources to tenants because we use the cluster resource quota model.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-035-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:18:17",
    "timestamp_out": null,
    "quote": "And so what we try to do is, is digest that and make it consumable from a, a single view, so the total resources that they're allocated in their quota and do it over a longer period of time because you know, looking at the past two weeks isn't necessarily helpful or whatever the default retention is in the OpenShift metrics. So we need, we need a longer term view. So that's kind of why we built our own solution.",
    "citation": "[213,   "object_type": "Behavior",
  "id": "BEH-036",
  "user_enablement": "Teams are able to configure Pod-Level & namespace level Grafana Dashboards.",
  "behavior_type": "custom_reporting",
  "signals": [
    "custom dashboard creation",
    "granular workload views"
  ],
  "acceptance_criteria": [
    "Teams can independently create Grafana dashboards for their workloads.",
    "Dashboards provide detailed views at pod and namespace levels.",
    "Monitoring needs are met through custom solutions."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-036-1"
    },
    {
      "provenance_id": "PROV-BEH-036-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-036-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf,
    "timestamp_out": null,
    "quote": "I mean there are teams that do build their own dashboards for that and use tools like Grafana and to build those, those views per workload and per pod and that sort of thing. But no one's really doing it with like a long- term view",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 37: Cigna's OpenShift Engineering Team Supports Multi-Tenant OpenShift Platform
**Markdown Summary:**
Cigna's OpenShift Engineering Team is able to support the OpenShift platform in a multi-tenant mode.",
  "behavior_type": "platform_operations",
  "signals": [
    "management of 50+ clusters",
    "namespace as a service offering",
    "support for shared infra and DevOps workloads"
  ],
  "acceptance_criteria": [
    "OpenShift clusters operate reliably in multi-tenant mode.",
    "Teams can request and receive namespaces efficiently.",
    "Shared services and DevOps pipelines are effectively supported."
  ],
  "evidence": [
    ",
  "id": "PROV-BEH-037-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:03:59",
    "timestamp_out": null,
    "quote": "So I am on the OpenShift engineering team, and so we support the OpenShift platform. We have around 50 OpenShift clusters split out between non- production and production. And we're running all - all of our clusters are running in a multi- tenant mode,": "00:18:12",
    "timestamp_out": null,
    "quote": "Recently, some amount of like shared infrastructure services. So like we have a Redis offering that one of our infrastructure team provide. And so we work with them to provide the OpenShift clusters that they deploy on. ... And then like a third workload type would be like DevOps. So we have a few DevOps clusters that Jenkins workloads schedule onto.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
 And then like a third workload type would be like DevOps. So we have a few DevOps clusters that Jenkins workloads schedule onto.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-037-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:18:12",
    ":**
Bell Canada's platform teams are able to review requests for higher namespace quotas, utilizing a self-service Prometheus metrics portal with long-term retention history to check the math and justify claims. This enables them to pivot against historical information to validate requests, especially for high peak sales periods.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-038",
  "user_enablement": "Bell Canada platform teams are able to review requests for higher Namsespace quota.",
  "behavior_      "provenance_id": "PROV-BEH-038-2"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-038-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Reviews request for higher Namsespace quota.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-038-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:07:32",
    "timestamp_out": null,
    "quote": "For every tenant new or existing, we flow them through kind of a Prometheus grabbing metrics portal that production environments are able to investigate configurations to identify potential issues such as aggressive resource settings, crash loops, or other horrible events. They proactively engage application teams via email or ServiceNow tickets to suggest improvements and lower resource consumption.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-039",
  "user_enablement": "On-call engineers are able to investigate production configurations and engage teams for optimization.",
  "behavior_type": "proactive_monitoring",
  :**
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-039-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:38:57",
    "timestamp_out": null,
    "quote": "We've also had like our on- call engineers. So in production specifically, let me, and then there's a third we have on- call engineers who are on like a weekly rotation. And part of the on- call engineer's responsibility is during the day when they're not handling any fires to go out through production and just, well this is, this has been our, our historical path, right? We're moving to like a new process but go, gone out to production and look what's there, see if there's any horrible events firing some crash loops, stuff like that. And sometimes they will discover, you know, these configurations out there in prod. And then we will, we have a contact email for the namespace that we request from the namespace as a service. So we will engage them through there, more resources.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-040",
  "user_enablement": "Infrastructure teams are able to impose limits per namespace for the teams.",
  "behavior_type": "resource_allocation",
  "signals": [
    "limit enforcement",
    "negotiation with teams"
  ],
  "acceptance_criteria": [
    "Namespace limits are effectively set and enforced.",
    "Teams operate within allocatedsource_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Think it's a little, basically the infrastructure team has imposed limits per namespace for the teams, and then the teams have to fit in there and then there's a negotiation from those teams with the infrastructure team if they want more. And so far that's pretty much been a no.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{direct_quote"
  }
}
```

---

#### Behavior 41: Platform Teams Share Usage & Cost Trends Quarterly
**Markdown Summary:**
The platform team is able to share usage and cost trends on a quarterly basis with financial leadership and application teams. This report, focusing on metrics like request CPU core hours, provides visibility across the organization, drives the resource optimization process, and aids in strategic planning for capacity.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-_id": "PROV-BEH-041-1"
    },
    {
      "provenance_id": "PROV-BEH-041-2"
    },
    {
      "provenance_id": "PROV-BEH-041-3"
    },
    {
      "provenance_id": "PROV-BEH-041-4"
    }
  ]
}
```

**Provenance Object:**
```json
{
  "object_type": "Provenance",
  "id": "_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:06:00",
    "timestamp_out": null,
    "quote": "And so we, on a quarterly basis, we put together a report with a bunch of our, our data and then that goes up the, to the financial leadership and that, that's for our quarterly service report.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```96]",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-041-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprintWalkthrough.m4a",
    "timestamp_in": "00:03:52",
    "timestamp_out": "00:04:14",
    "quote": "one of the activities they primarily focus on is this quarterly cost report and that report gets distributed to leadership as well as the application teams and starts to give them an idea of where they can optimize what are the usage trends that might need some tweaking uh and provides that visibility across the rest of the organization. So this is one of the primary artifacts that drives this resource optimization process outside of the actual alerting pieces that they've had set up as well.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 42: Application Teams Design
  "user_enablement": "App Team is able to make Design Decisions on Application Architecture to comply with Quota Limits and Service Defaults.",
  "behavior_type": "architecture_design",
  "signals": [
    "resource calculation adjustments",
    "compliance with imposed limits"
  ],
  "acceptance_criteria": [
    "Application architectures are designed to fit within defined quotas.",
    "Teams can accurately calculate resource needs for their deployments.",
    "Applications operate efficiently within allocated namespace limits."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-042-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Makes Design Decisions on Application Architecture to comply with Quota Limits and Service Defaults.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-04 that happen.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-042-3",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:10:25",
    "timestamp_out": null,
    "quote": "you basically end up having to go per JVM.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-042-4",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:10:25",
    "timestamp_out": null,
    "quote": "And so then the teams start trying to figure out how to. These defaults dictate the minimum infrastructure needed when application teams consume CI/CD as a service, impacting the total cost of application ownership.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-043",
  "user_enablement": "Infrastructure Team is able to Set Pipeline Default Usage Requirements and Set Development Services Default usage Requirements.",
  "behavior_type": "default_configuration",
  "signals": [
    "pipeline defaults",
    "development service defaults",
    "total{
  "object_type": "Provenance",
  "id": "PROV-BEH-043-1",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": null,
    "timestamp_out": null,
    "quote": "Sets Pipeline Default Usage Requirements. Sets Development Services Default usage Requirements.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": " because when you start to think about total cost of application ownership for these CI/CD services. Are these the application teams cost? Are they the developer services team's cost? So, how do we break these applications into more granular pieces so we can actually facilitate those different conversations around what the total cost of application ownership might be?",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 44: Engineers Delegate Optimization Work to Application Teams
**Markdown Summary:**
Engineers are able to delegate optimization work, such as adjusting resource configurations,team ownership of workloads"
  ],
  "acceptance_criteria": [
    "Optimization tasks are successfully assigned to app teams.",
    "App teams take ownership of their workload optimizations.",
    "The decentralized model supports effective resource management."
  ],
  "evidence": [
    {
      "provenance_id": "PROV-BEH-044-1"
    },
    {
      "provenance_id": "PROV-BEH-044-2"
    }
  ]
}
```

**Provenance Object:**
```json
{ you, you know, delegate this work to them? I would delegate it to them assuming this is not one of my team's projects.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```
```json
{
  "object_type": "Provenance",
  "id": "PROV-BEH-044-2",
  "evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:41:10", alarms configured by the infrastructure side. This allows for application-specific monitoring tailored to their unique workloads.

**JSON Schema Block:**
```json
{
  "object_type": "Behavior",
  "id": "BEH-045",
  "user_enablement": "Devs are able to make their own alarms for their applications.",
  "behavior_type": "custom_alerting",
  "signals": [
    "application-specific alarms",
    "decentralized alerting"
  ],
  "acceptance_evidence_block": {
    "source_filename": "ROSwell_ServiceBlueprint.pdf",
    "timestamp_in": "00:15:26",
    "timestamp_out": null,
    "quote": "All, we have all our own alarms and then devs make, make their own for their applications. But from the infrastructure side it's all cluster related or self- service, you know, like databases and stuff like that and that have alarms, Kafka obviously and whatever else o's here.",
    "citation": "",
    "evidence_type": "direct_quote"
  }
}
```

---

#### Behavior 46: Platform Team Works on Communication Structures to Publish Insights
**Markdown Summary:**
The platform team is able to work on communication structures for how to publish insights, such as optimization opportunities, to distributed application teams. This is crucial in a decentralized model where dev teams have vertical integration and perform their own operations.

**JSON Schema