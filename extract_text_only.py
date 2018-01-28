

from lxml import html
from lxml import etree

def extract_text(html_text):
    tree = html.fromstring(html_text)
    for i in tree:
        print(i)
        print(i.children())


if __name__ == "__main__":
    html_text = '<div class="modern-line">\n                            <a href="javascript:void(0);" class="tooltip-link"><span class="tooltip-css tooltip-background"><h4 class="semi-bold">Let Rome be washed away in the Tiber</h4><p>Rome was built on the river Tiber.</p></span>Let Rome be washed away in the Tiber</a> and let the great empire\n                                fall. My place is here. Kingdoms are only dirt. The soil feeds\n                                animals as well as people, so how does having a kingdom separate\n                                humans from beasts? The noblest thing is to do what we&#8217;re doing,\n                                particularly when the couple is as well matched as we are. I demand\n                                that the world admit we are the perfect couple or else suffer the\n                                consequences.</div>\n                        \n                    '
    extract_text(html_text)