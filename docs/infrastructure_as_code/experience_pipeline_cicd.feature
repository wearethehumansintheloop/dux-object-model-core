
Feature: connectRX Fence - Experience Pipeline CI/CD Validation

  This feature validates experience content, brand tone, and UX compliance using a structured pipeline.
  It ensures content passed to the connectRX GRAPHRAG complies with declared standards for branding, privacy, and trust messaging.

  Scenario Outline: Validate content asset before acceptance into connectRX governance GRAPHRAG
    Given a content asset "<asset_id>" with content:
      """<asset_body>"""
    When the content is evaluated by an LLM using connectRX guidance
    Then it must pass the following validations:
      | Validation Category     | Expected Outcome                       |
      | Branding Compliance     | ✅ Pass connectRX tone & aesthetic     |
      | Privacy Conformance     | ✅ No PII exposure, correct framing    |
      | Structural Alignment    | ✅ Complies with DUX object model      |
      | Domain Alignment        | ✅ Matches domain_object_model_guide   |
      | BDD Spec Readiness      | ✅ Usable in .feature and steps.py     |

    Examples:
      | asset_id       | asset_body                      |
      | homepage_copy  | Welcome to connectRX...         |
      | badge_tooltip  | Commitment verified privately   |
