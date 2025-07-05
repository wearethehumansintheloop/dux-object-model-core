Here are the extracted DUX objects from the provided source material, following the specified schema and formatting requirements.

---

### **Problem 1: Poor Cloud Cost Forecasting Accuracy**

Nubank initially faced **significant inaccuracies in its cloud cost forecasting**, experiencing a substantial **75% budget deviation** at one point. This indicated a lack of reliable financial predictability, described as "wishful thinking" rather than actual forecasting, which they admitted "sucked". This issue became a strategic priority due to their rapid growth and the necessity of efficiency when serving millions of customers.

```json
{
  "dux_version": "9.5",
  "object_type": "Problem",
  "id": "P-NUBANK-001",
  "title": "Poor Cloud Cost Forecasting Accuracy",
  "description": "Nubank experienced extremely high deviations in their cloud cost forecasts, reaching 75% budget deviation at one point, indicating a severe lack of financial predictability and control over their skyrocketing cloud spend.",
  "status": "active",
  "impact": "Inability to make informed strategic decisions regarding new products, market entry, and overall strategies due to unreliable cost projections.",
  "evidence": [
    {
      "statement": "At one point, we had 75% budget deviation. We weren't forecasting. We were wishful thinking. We sucked.",
      "source_id": "4",
      "timestamp": "50:16-50:24",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "Forecasting our cloud spend became a strategic priority. It feeds product and leadership's decision making on new products, entering new markets and new strategies.",
      "source_id": "4",
      "timestamp": "49:51-50:02",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "our cloud spend skyrocket. With great costs comes great responsibility. And when you serve millions of customers who count every, you can't afforder afford inefficiencies.",
      "source_id": "3, 4",
      "timestamp": "49:35-49:51",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    }
  ]
}
```

---

### **Behavior 1: Iterative Attempts at Centralized and Granular Budgeting Models**

To address the initial forecasting problem, Nubank engaged in a series of iterative behaviors. They first attempted a **single, company-wide budget using regression**, which proved ineffective. They then evolved to splitting budgets into **two parts across eight business units**, which also failed to improve accuracy. Subsequently, they adopted a more granular approach, creating **45 budgets across all business units**, including horizontals and verticals. While this fostered some FinOps culture and exposed big spenders, the accuracy remained "not so great".

```json
{
  "dux_version": "9.5",
  "object_type": "Behavior",
  "id": "B-NUBANK-001",
  "title": "Iterative Attempts at Centralized and Granular Budgeting Models",
  "description": "Nubank tried various budgeting approaches, starting with a single company-wide budget, then splitting it into two across eight business units, and finally creating 45 granular budgets across all business units to improve cloud cost forecasting accuracy.",
  "category": "Operational Strategy",
  "activity_type": "Experimentation",
  "evidence": [
    {
      "statement": "So, we had to fix it. And at first we did what any self-respecting tech company would do, we said let's build a model. We started with one budget for the entire company, just one, out of regression.",
      "source_id": "5",
      "timestamp": "50:24-50:35",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "Then we split interest into two parts. Across eight business units and it still didn't work.",
      "source_id": "5",
      "timestamp": "50:47-50:53",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "So next we got really granular. 45 budgets across all our business units, including horizontals and verticals.",
      "source_id": "6",
      "timestamp": "50:59-51:12",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    }
  ]
}
```

---

### **Result 1: Persistent Inaccuracy and Limited Impact from Initial Attempts**

Despite Nubank's initial efforts with various budgeting models (single, two-part, and 45 granular budgets), the result was a **continuation of poor forecasting accuracy**. The early attempts "didn't work" and produced forecasts as unreliable as the start time of a Brazilian barbecue. Even with 45 budgets, while it helped to build a FinOps culture and exposed high spenders, the accuracy was "still not so great".

```json
{
  "dux_version": "9.5",
  "object_type": "Result",
  "id": "R-NUBANK-001",
  "title": "Persistent Inaccuracy and Limited Impact from Initial Attempts",
  "description": "Nubank's initial forecasting models, ranging from a single company-wide budget to 45 granular budgets, failed to significantly improve cloud cost forecasting accuracy, with early attempts explicitly stated as 'not working' and forecasts remaining unreliable.",
  "outcome_type": "Negative",
  "evidence": [
    {
      "statement": "Basically like putting all of your ingredients into a blender at the same time and hope it works. It sounds efficient at first, but let me tell you, it doesn't work.",
      "source_id": "5",
      "timestamp": "50:35-50:47",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "Then we split interest into two parts. Across eight business units and it still didn't work. Our forecasts were about as reliable as the start time of a Brazilian barbecue.",
      "source_id": "5, 6",
      "timestamp": "50:47-50:59",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "It also exposes the big spenders but accuracy, still not so great.",
      "source_id": "6",
      "timestamp": "51:18-51:23",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    }
  ]
}
```

---

### **Problem 2: Insufficient Granularity in Demand Driver Application**

Even after implementing 45 budgets and using demand drivers, Nubank realized that **relying on just one demand driver per budget was often insufficient** for accurate cloud cost forecasting. This problem was particularly acute for complex business units (BUs) that had **multiple cost layers behaving differently**, necessitating a more nuanced approach than a single variable could provide.

```json
{
  "dux_version": "9.5",
  "object_type": "Problem",
  "id": "P-NUBANK-002",
  "title": "Insufficient Granularity in Demand Driver Application",
  "description": "After initial attempts, Nubank identified that relying on a single demand driver per budget was insufficient for accurate forecasting, especially for complex business units with multiple distinct cost layers.",
  "status": "active",
  "impact": "Continued struggle with forecasting accuracy despite adopting demand drivers, preventing full strategic utility of cost data.",
  "evidence": [
    {
      "statement": "But still, not enough. Why? Because one demand driver oftentimes just isn't enough. It's like trying to explain Brazilian music just with Samba, it's a classic but it doesn't tell you the whole story.",
      "source_id": "8",
      "timestamp": "52:10-52:17",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "Some BUs were complex for one variable. There were multiple cost layers, each behaving differently so we encouraged BUs to within their one budget create buckets with own demand drivers.",
      "source_id": "8",
      "timestamp": "52:22-52:34",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    }
  ]
}
```

---

### **Behavior 2: Implementing Highly Granular, Demand-Driver-Based Budget Buckets**

To overcome the limitations of single demand drivers, Nubank shifted tactics again, emphasizing **highly granular budgeting using multiple "buckets" within each business unit**, each tied to its own specific demand driver. This involved encouraging BUs to track different infrastructure components or products, leading to the creation of **over 100 such buckets** across Nubank, all projected with relevant business metrics like customers, transactions, or log-in messages that truly drive costs. This distributed responsibility, empowering each BU to own its forecast.

```json
{
  "dux_version": "9.5",
  "object_type": "Behavior",
  "id": "B-NUBANK-002",
  "title": "Implementing Highly Granular, Demand-Driver-Based Budget Buckets",
  "description": "Nubank encouraged business units to create multiple 'buckets' within their budgets, each with its own specific demand driver, leading to over 100 such granular buckets across the organization, based on real business metrics.",
  "category": "Cloud Cost Management",
  "activity_type": "Methodology Refinement",
  "evidence": [
    {
      "statement": "So, we had to change tactics once again. We started using demand driver, real business metrics like customers, transactions, log-in security messages, things that actually drive costs and that the business already owns and forecasts anyways.",
      "source_id": "6, 7",
      "timestamp": "51:23-51:33",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "This shifted responsibility each BU owned its forecast by multiplying the expected unit cost with this demand driver. No more black box budgeting, no more excuses.",
      "source_id": "7",
      "timestamp": "51:33-51:48",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "Some BUs created up to 26 buckets, tracking different infrastructure components or products. Yes, it was more effort, yes, there was some shouting, but in the end, we had over 100 buckets across Nubank, all projected with demand drivers.",
      "source_id": "8, 9",
      "timestamp": "52:34-52:45",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    }
  ]
}
```

---

### **Result 2: Dramatic Improvement in Forecasting Accuracy and Enhanced Cost Awareness**

The implementation of highly granular, demand-driver-based budget buckets led to a **dramatic improvement in Nubank's cloud cost forecasting accuracy**, reducing budget deviation from an initial 75% to **less than 1%**. This significant achievement fostered **leadership trust**, enabling them to finally base strategic decisions on the cloud cost forecasts. Furthermore, this approach propelled **greater cost awareness** throughout the organization, as every team within their BU now owns and actively manages its "sales made budget".

```json
{
  "dux_version": "9.5",
  "object_type": "Result",
  "id": "R-NUBANK-002",
  "title": "Dramatic Improvement in Forecasting Accuracy and Enhanced Cost Awareness",
  "description": "Nubank successfully reduced cloud cost forecasting deviation from 75% to less than 1%, gaining leadership trust and significantly increasing cost awareness across all teams through granular, demand-driver-based budgeting.",
  "outcome_type": "Positive",
  "evidence": [
    {
      "statement": "And guess what? This took us down from 75% deviation to less than 1% in this year. That's a huge win.",
      "source_id": "9",
      "timestamp": "52:45-52:51",
      "maturity": "04_quantified",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "Leadership trusts us and can -- (Applause). Thank you. Leadership reacted equally and now they can finally base their decision-making on our forecasts for our Cloud cost efficiency ratio.",
      "source_id": "9",
      "timestamp": "52:51-53:12",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "It also helped us to push cost awareness even further. Now every team within their own BU have their own sales made budget that they live and breathe.",
      "source_id": "10",
      "timestamp": "53:12-53:17",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    }
  ]
}
```

---

### **Fit Template: Cloud Cost Forecasting Transformation**

This Fit Template describes Nubank's journey to transform its cloud cost forecasting from a highly inaccurate, "wishful thinking" process to a precise strategic tool. Facing **severe budget deviations (up to 75%)** and the inability to reliably plan for their skyrocketing cloud spend, Nubank iteratively refined its approach. Initial attempts with centralized and then moderately granular budgets failed to yield significant improvement. The pivotal shift was **implementing a highly granular, demand-driver-based forecasting model**, where business units created over 100 "buckets" each with its own relevant demand driver. This systematic refinement resulted in a **dramatic reduction in forecasting deviation to less than 1%**, solidifying leadership trust and deeply embedding cost awareness throughout the organization. This demonstrates how **increased granularity and tying costs directly to business drivers transformed cloud cost forecasting into a strategic asset for growth and efficiency**.

```json
{
  "dux_version": "9.5",
  "object_type": "FitTemplate",
  "id": "FT-NUBANK-001",
  "title": "Cloud Cost Forecasting Transformation",
  "description": "Nubank's journey from highly inaccurate cloud cost forecasting (75% deviation) to achieving less than 1% deviation by adopting a granular, demand-driver-based budgeting methodology, empowering business units and fostering enterprise-wide cost awareness.",
  "problem_id": "P-NUBANK-001",
  "behavior_id": "B-NUBANK-002",
  "result_id": "R-NUBANK-002",
  "justification": "This chain directly links the severe problem of cloud cost forecasting inaccuracy to the specific, iterative behavior of implementing granular, demand-driver-based budgeting, and quantifies the dramatic positive result of reduced deviation and increased cost awareness, which enabled strategic decision-making and efficient scaling.",
  "insight_status": "validated",
  "evidence": [
    {
      "statement": "At one point, we had 75% budget deviation. We weren't forecasting. We were wishful thinking. We sucked.",
      "source_id": "4",
      "timestamp": "50:16-50:24",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "We started using demand driver, real business metrics like customers, transactions, log-in security messages, things that actually drive costs and that the business already owns and forecasts anyways. ... we encouraged BUs to within their one budget create buckets with own demand drivers. Some BUs created up to 26 buckets, tracking different infrastructure components or products. ... in the end, we had over 100 buckets across Nubank, all projected with demand drivers.",
      "source_id": "6, 7, 8, 9",
      "timestamp": "51:23-52:45",
      "maturity": "03_observed",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    },
    {
      "statement": "This took us down from 75% deviation to less than 1% in this year. That's a huge win. Leadership trusts us and can finally base their decision-making on our forecasts for our Cloud cost efficiency ratio. It also helped us to push cost awareness even further. Now every team within their own BU have their own sales made budget that they live and breathe.",
      "source_id": "9, 10",
      "timestamp": "52:45-53:17",
      "maturity": "04_quantified",
      "provenance": {
        "source_type": "Keynote Excerpt",
        "title": "NUBANK KeyNote FinOps LIVE",
        "speaker": "Th Thomas (Nubank)",
        "duration_segment": "48:05-53:46"
      }
    }
  ]
}
```

---

Would you like to hear my favorite data point?