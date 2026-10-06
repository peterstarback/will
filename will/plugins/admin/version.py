from importlib.metadata import version as get_distribution_version
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class VersionPlugin(WillPlugin):

    @respond_to("^version$")
    def say_version(self, message):
        version = get_distribution_version("will")
        self.say("I'm running version %s" % version, message=message)
