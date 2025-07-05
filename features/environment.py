"""
Behave environment configuration.
This file contains hooks that run before and after scenarios, features, etc.
"""


def before_all(context):
    """Runs once before all features."""
    print("Starting test suite...")


def after_all(context):
    """Runs once after all features."""
    print("Test suite completed.")


def before_feature(context, feature):
    """Runs before each feature."""
    print(f"Starting feature: {feature.name}")


def after_feature(context, feature):
    """Runs after each feature."""
    print(f"Completed feature: {feature.name}")


def before_scenario(context, scenario):
    """Runs before each scenario."""
    print(f"Starting scenario: {scenario.name}")
    # Initialize any scenario-specific context here
    context.setup_complete = False
    context.action_performed = False


def after_scenario(context, scenario):
    """Runs after each scenario."""
    print(f"Completed scenario: {scenario.name}")
    # Clean up any scenario-specific resources here
