## 🧭 DUX Object Model — User Outcome Logic

### 🎯 Definition
A **User Outcome** represents the observable benefit a user enjoys as a result of engaging in key behaviors within a given user flow. It is used to **link behavioral evidence to business impact** by way of success metrics, key signals, and intended degree of change.

---

### 🧠 Conceptual Flow

```plaintext
User Flow → Sequence of Behaviors → Each Behavior emits Signals
       ↓
User Outcome ← derives key behaviors + key signals from flow context
       ↓
Result ← defines Success Metrics + degree of change needed
       ↓
Target Impact ← business- or system-level performance indicator (e.g., P&L, OKR)
```

---

### 🔗 Object Relationships
- **User Outcome ↔ User Flow**: outcome is contextualized by a flow — flow includes ordered behaviors
- **User Outcome ↔ Result**: outcome operationalizes the result — success criteria live in the Result
- **User Outcome ↔ Key Behaviors**: derived from associated user flow behaviors
- **User Outcome ↔ Key Signals**: inferred or assigned based on the signals emitted by those behaviors

---

### 🧬 Derivation Logic
- A **User Outcome** emerges as a **junction object** formed when a Behavior and Result come together — like Voltron. It only comes into being when:
  - A **Result** exists that defines the desired success metric and impact target
  - A **User Flow** is linked, containing sequenced **Behaviors** with traceable signals
  - Those **Behaviors** emit or infer measurable **Signals** tied to progress toward the Result

This means:
- **User Outcome** is a dynamic synthesis — it binds **Result** (the "what") and **Behavior** (the "how") together, forming an **observable benefit** to the user

The **degree of signal change** is derived by:
  - The thresholds defined in the Result’s success metrics
  - Signal weightings or sensitivities from linked Behaviors
  - Triggers based on timing, usage frequency, or other flow-based dynamics

---

### 📦 Field Summary
| Field                | Source             | Description |
|---------------------|--------------------|-------------|
| `result_id`         | Result             | Links the outcome to the business/customer goal |
| `user_flow_id`      | User Flow          | Flow context used to derive behaviors and signals |
| `key_behavior_ids`  | Derived from Flow  | Sequence of behaviors linked to outcome achievement |
| `key_signal_ids`    | Derived from Behaviors | Specific signals emitted that can be observed or measured |
| `success_metric_id` | From Result        | Metric that this outcome helps move |
| `degree_of_change`  | Computed           | How much the signal must change to impact the success metric |
| `impact_target`     | From Result        | Business measure that improves when success metric is hit |

---

### 💡 Use in Generation / Recommendation
An LLM should be able to:
- Infer probable behaviors and signals based on a given Result
- Suggest missing fields for a User Outcome based on its related flow
- Recommend signal-to-metric mappings using known success metrics and behavior patterns

---

### 🔒 Governance
- User Outcome validity requires:
  - At least 1 key behavior
  - At least 1 associated signal
  - Traceability to a Result object
  - Explicit or inferred degree of change

---

Would you like to now:
- Generate `.json` examples for this object?
- Create a `.feature` file to test derivation logic?
- Hook this into the visual chain (Problem → Behavior → Result → Outcome)?

