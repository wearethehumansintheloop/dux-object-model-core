# Object Model v4 Tags  
@protocol-accelerating-delivery @protocol-task-jtbd-identification
@journey-cross-functional @phase-align-outcomes @task-identify-jtbd

Feature: Identify High-Opportunity Jobs to be Done (JTBD)
  As a cross-functional squad member
  I want to identify and score the highest-opportunity JTBD
  So that we focus on delivering outsized value for users, customers, and the business

  Background:
    Given a cross-functional squad with PM, Engineering, and UX members is assembled
    And quantitative and qualitative user/customer insights are available
    And JTBD opportunity scoring methodology is established
    And business/customer proxies are available for validation

  @jtbd-scoring @opportunity-assessment
  Scenario: Score and rank JTBDs by Opportunity Score
    Given multiple JTBDs have been surfaced from user insights
    And each JTBD represents a potential area of user/customer value
    When the squad scores JTBDs using Opportunity Score methodology
    Then JTBDs are ranked by their Opportunity Score values
    And JTBDs with scores greater than 10 are highlighted as highest value
    And the scoring rationale is documented for each JTBD
    And business impact and user need underservice levels are captured

  @consensus-building @stakeholder-alignment  
  Scenario: Select top-scoring JTBD with stakeholder consensus
    Given JTBDs have been scored and ranked by Opportunity Score
    And business/customer proxies are engaged in the selection process
    When the squad selects the top-scoring JTBD as the focal point
    Then explicit rationale for the selection is documented
    And business/customer proxies agree with the selection
    And all squad members can articulate why this JTBD wins
    And the selected JTBD becomes the foundation for outcome definition

  @real-world-validation @sales-insights
  Scenario: Identify high-opportunity JTBD for sales dashboard project
    Given a squad is building a sales dashboard with multiple stakeholder requests
    And insights have been gathered from sales leaders, customer support, and end users
    When the squad applies JTBD identification process
    Then they surface "Help sales leaders get accurate pipeline insights in real-time" as a key JTBD
    And this JTBD receives an Opportunity Score of 13
    And the score reflects critical unmet need and strategic business differentiator status
    And the squad unanimously selects this JTBD for focus
    And they document that solving this will drive rapid adoption and business value

  @cross-functional-insights @user-research
  Scenario: Gather comprehensive insights across all user touchpoints
    Given the squad needs to identify high-opportunity JTBDs
    When they gather insights from multiple sources
    Then sales leaders provide strategic business context and pain points
    And customer support shares frequent user complaints and requests
    And actual end users describe their current workflows and frustrations
    And quantitative data reveals usage patterns and bottlenecks
    And qualitative feedback exposes unmet needs and desired outcomes
    And all insights are synthesized into potential JTBDs for scoring

  @validation-checkpoint @business-alignment
  Scenario: Validate JTBD selection meets business requirements
    Given a top JTBD has been selected based on Opportunity Score
    When business stakeholders review the selection
    Then the JTBD aligns with strategic business objectives
    And the JTBD addresses a proven customer/user pain point
    And the business impact potential is clearly articulated
    And resource allocation to this JTBD is justified by the opportunity
    And the selection passes business/customer proxy approval
    And the whole squad commits to this JTBD as their focal point

  @anti-pattern @scope-expansion
  Scenario: Prevent selection of multiple JTBDs that dilute focus
    Given multiple JTBDs have high Opportunity Scores
    And stakeholders want to address several opportunities simultaneously
    When the squad applies JTBD selection discipline
    Then only one JTBD is selected as the primary focus
    And other high-scoring JTBDs are documented for future consideration
    And the rationale for single-JTBD focus is clearly communicated
    And stakeholders understand the value of concentrated effort
    And the squad maintains clarity on their singular outcome target
