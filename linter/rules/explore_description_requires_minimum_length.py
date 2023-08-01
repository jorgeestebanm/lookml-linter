from linter.rule import Rule
from typing import Any, Tuple


class ExploreDescriptionRequiresMinimumLength(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ("explore",)

    def run(self, explore: Any) -> bool:
        if not "description" in explore:
            return True
        if len(explore["description"]) < 20:
            return False
        return True
