import os


def system_notification(title, message):
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


if __name__ == '__main__':
    system_notification('title', 'message')
