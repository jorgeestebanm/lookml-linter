import os
from linter.config_validator import ConfigValidator
from linter.lookml_linter import LookMlLinter
from linter.lookml_project_parser import LookMlProjectParser
from linter.rules_engine import RulesEngine


def main():
    # Validate config.yaml file
    validator = ConfigValidator(
        os.environ['INPUT_CONFIGFILE'],
        os.environ['INPUT_FILEPATHS']
    )
    validator.validate()

    # Retrieve rules from config and data from LookML files
    rules = RulesEngine(validator.config).rules
    data = LookMlProjectParser().get_parsed_lookml_files()

    # Run linter and save/print output
    linter = LookMlLinter(data, rules)
    linter.run()
    error_log = linter.get_errors()
    print(error_log)
    linter.save_errors(error_log, '_lookml-linter-output.txt')

    # Fail GitHub Action only if linter has errors (warnings do not count)
    assert linter.has_errors == False, 'LookML Linter detected an error warning, please resolve any error warning to complete Pull Request'


main()
