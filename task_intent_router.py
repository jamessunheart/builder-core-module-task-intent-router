import re

class TaskIntentRouter:
    """
    A smart routing engine that analyzes user input and task metadata
    to delegate requests to the appropriate modules or tools.
    """

    def __init__(self):
        self.routing_rules = {
            "diagnostic": "self_diagnostic_engine",
            "scan": "self_diagnostic_engine",
            "debug": "self_diagnostic_engine",
            "optimize": "self_diagnostic_engine",
            "route": "task_intent_router",
            "module": "module_manager",
            "deploy": "module_manager",
            "register": "module_manager"
        }

    def route(self, user_input):
        """
        Determines the correct module or tool to handle a given input.
        Returns a dictionary with routing decision and confidence.
        """
        matched_targets = []
        for keyword, target in self.routing_rules.items():
            if re.search(rf"\\b{keyword}\\b", user_input, re.IGNORECASE):
                matched_targets.append(target)

        if matched_targets:
            # Prioritize based on first match for now
            return {
                "decision": matched_targets[0],
                "matched_keywords": matched_targets,
                "confidence": min(0.9, 0.6 + 0.1 * len(matched_targets))
            }
        else:
            return {
                "decision": "fallback_handler",
                "matched_keywords": [],
                "confidence": 0.3
            }

    def update_routing_rule(self, keyword, module_name):
        self.routing_rules[keyword] = module_name

    def show_rules(self):
        return self.routing_rules