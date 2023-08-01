from linter.rule import Severity
from linter.rules.field_description_requires_minimum_length import (
    FieldDescriptionRequiresMinimumLength,
)


def test_run_method_succeeds_with_non_hidden_field_with_minimum_length_description() -> (
    None
):
    rule = FieldDescriptionRequiresMinimumLength(Severity.ERROR.value)

    field = {
        "type": "string",
        "sql": "${TABLE}.sku",
        "hidden": "no",
        "name": "sku",
        "description": "testing with a long description",
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_with_non_hidden_field_with_short_description() -> None:
    rule = FieldDescriptionRequiresMinimumLength(Severity.ERROR.value)

    field = {
        "type": "string",
        "sql": "${TABLE}.sku",
        "hidden": "no",
        "name": "sku",
        "description": "testing",
    }
    rule_result = rule.run(field)
    assert rule_result == False


def test_run_method_succeeds_with_hidden_field_without_description() -> None:
    rule = FieldDescriptionRequiresMinimumLength(Severity.ERROR.value)

    field = {"type": "string", "sql": "${TABLE}.sku", "hidden": "yes", "name": "sku"}
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_succeeds_with_non_hidden_field_without_descriptions() -> None:
    rule = FieldDescriptionRequiresMinimumLength(Severity.ERROR.value)

    field = {"type": "string", "sql": "${TABLE}.sku", "name": "sku"}
    rule_result = rule.run(field)
    assert rule_result == True
