"""
Basic step definitions for sample feature.
Add your own step definitions here as you develop your features.
"""

from behave import given, when, then


@given('I have a basic setup')
def step_basic_setup(context):
    """Basic setup step - implement your setup logic here."""
    context.setup_complete = True


@when('I perform an action')
def step_perform_action(context):
    """Action step - implement your action logic here."""
    assert context.setup_complete, "Setup not completed"
    context.action_performed = True


@then('I should see the expected result')
def step_expected_result(context):
    """Verification step - implement your assertion logic here."""
    assert context.action_performed, "Action was not performed"
    assert True, "Expected result achieved"
