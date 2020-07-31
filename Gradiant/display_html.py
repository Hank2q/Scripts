from os import system, popen


def div(content=None, **kwargs):
    content = content or ''
    if '_class' in kwargs.keys():
        kwargs['class'] = kwargs['_class']
        del kwargs['_class']
    attrs = ' '.join([f'{k}="{v}"' for k, v in kwargs.items()])
    return f'<div {attrs}>{content}</div>'


def make_html(hexes):
    with open('gradiant.html', 'w') as html:
        content = ''
        for hexa in hexes:
            content += div(div(f'#{hexa}', style='background-color: white;'),
                           style=f'text-align: center; height: 160px; width: 130px; background-color: #{hexa}') + '\n'
        print(div(content=content, style='display: flex;'), file=html)
    system('gradiant.html')
