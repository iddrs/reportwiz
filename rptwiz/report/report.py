from rptwiz import VisualizationBase
from jinja2 import Template


class Report:

    def __init__(self, env: dict, viz: dict[str, str]):
        self.viz = viz
        self.env = env


    def to_html(self, template: Template, **kwargs) -> str:
        return template.render(env=self.env, viz=self.viz, **kwargs)