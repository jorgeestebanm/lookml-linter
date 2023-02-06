import os
from linter.config_validator import ConfigValidator
from linter.lookml_linter import LookMlLinter
from linter.rules_engine import RulesEngine
from linter.lookml_project_parser import LookMlProjectParser


def main():
    config_file = os.environ['INPUT_CONFIGFILE']

    validator = ConfigValidator(config_file)
    validator.validate()
    config = validator.config
    rules = RulesEngine(config).rules
    #LookMlProjectParser.root_file_path = path
    data = LookMlProjectParser().get_parsed_lookml_files()
    linter = LookMlLinter(data, rules)
    linter.run()
    output = linter.get_errors()
    print(output)
    f = open('lookml-linter-output.log', 'w')
    f.write(output)
    f.close()
    print(os.listdir('.'))
    assert linter.has_errors == False, "LookML Linter detected an error warning, please resolve any error warning to complete Pull Request"


main()
