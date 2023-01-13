def msg_processor(msg_code):
    '''
    msg_processor returns a msg object with 'msg', 'type'
    where 'msg' corresponds to the message user sees
    and 'type' is the color of the alert element

    codes:
        - 0 : 필수값을 모두 채워주세요       - 1 : User does not exist
        - 2 : Unable to retrieve tweets
        - 3 : Successfully deleted user
    '''

    msg_code = int(msg_code)

    msg_list = [
        (
            '검색어를 입력해주세요!',
            'danger'
        ),
    ]

    return {
        'msg':msg_list[msg_code][0],
        'type':msg_list[msg_code][1]
    }
