from behave import given, when, then

@given('the brand guide includes typefaces, colors, UI behavior, and emotional tone requirements')
def step_impl(context):
    context.brand_guide = {
        'headlines_font': 'Cormorant Garamond',
        'body_font': 'Inter',
        'colors': ['#FF6B6B', '#D8CAB8', '#FAF3EC', '#A8D5BA', '#8B7355'],
        'animation': ['liquid glass', 'gentle notification'],
        'mood': 'boutique gelato-in-Venice',
        'prohibited_elements': ['system fonts', 'PII', 'test details', 'clinical iconography']
    }

@when('checking typeface usage')
def step_impl(context):
    context.output_fonts = getattr(context, 'output_fonts', [])

@then('headlines must use "Cormorant Garamond"')
def step_impl(context):
    assert 'Cormorant Garamond' in context.output_fonts, "Headlines must use Cormorant Garamond."

@then('supporting text must use "Inter"')
def step_impl(context):
    assert 'Inter' in context.output_fonts, "Supporting text must use Inter."

@then('no system UI fonts or generics are allowed')
def step_impl(context):
    forbidden = ['Arial', 'Helvetica', 'Times New Roman', 'System UI']
    assert all(font not in forbidden for font in context.output_fonts), "System fonts detected."

@when('checking color usage')
def step_impl(context):
    context.output_colors = getattr(context, 'output_colors', [])

@then('only the following HEX codes are allowed:')
def step_impl(context):
    for row in context.table:
        assert row['HEX Code'] in context.output_colors, f"Color {row['HEX Code']} not in output."

@then('UI must use rounded corners and Apple Wallet-style shadows')
def step_impl(context):
    assert 'rounded_corners' in context.output_styles
    assert 'wallet_shadow' in context.output_styles

@then('badge icons must be animated with a liquid glass effect')
def step_impl(context):
    assert 'liquid glass' in context.output_animations

@then('no medical or clinical iconography is allowed')
def step_impl(context):
    assert 'clinical_icon' not in context.output_elements

@then('no PII or test result data is included')
def step_impl(context):
    assert not context.contains_pii, "PII or test results found."

@then('animations must use liquid glass effect for trust badges')
def step_impl(context):
    assert 'liquid glass' in context.output_animations

@then('all transitions should be smooth (ideally 60fps)')
def step_impl(context):
    assert '60fps' in context.performance_targets

@then('notification animation must be gentle and privacy-preserving')
def step_impl(context):
    assert 'gentle_notification' in context.output_animations

@then('the tone must evoke confidence, reassurance, and privacy')
def step_impl(context):
    for word in ['confidence', 'reassurance', 'privacy']:
        assert word in context.emotional_tone

@then('avoid any clinical, alarming, or stressful indicators')
def step_impl(context):
    for word in ['clinical', 'alarming', 'stress']:
        assert word not in context.emotional_tone

@then('visual mood must feel like "boutique gelato-in-Venice"')
def step_impl(context):
    assert 'gelato-in-Venice' in context.visual_mood
