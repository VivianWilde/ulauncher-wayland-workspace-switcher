from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction


class XfwmWorkspaceExtension(Extension):

    def __init__(self):
        super(XfwmWorkspaceExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        for i in range(5):
            items.append(ExtensionResultItem(icon='images/workspace-switcher-top-left.svg',
                                             name='Item %s' % i,
                                             description='Item description %s' % i,
                                             on_enter=HideWindowAction()))

        return RenderResultListAction(items)

if __name__ == '__main__':
    XfwmWorkspaceExtension().run()
