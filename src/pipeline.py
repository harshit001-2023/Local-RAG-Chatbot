# this is the Pipeline class that will be used to run the entire pipeline

from jinja2 import pass_context


class Pipeline:
    def __init__(self, config):
        self.config = config

    def run(self):
        # run the entire pipeline
        pass_context(self.config)

    