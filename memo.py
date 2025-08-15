"""
INFO:slack_app:Received message: {
    'user': 'U096NJW1KEK', 
    'type': 'message', 
    'ts': '1755262699.447039', 
    'client_msg_id': '42e14911-025b-4546-b055-075c5df2775e', 
    'text': 'こんにちは', 
    'team': 'T0973LKR5GS', 
    'blocks': [
        {
            'type': 'rich_text', 
            'block_id': 'f0HCs', 
            'elements': [
                {
                    'type': 'rich_text_section', 
                    'elements': [
                        {
                            'type': 'text', 
                            'text': 'こんにちは'
                        }
                    ]
                }
            ]
        }
    ], 
    'channel': 'C09A5L6304B', 
    'event_ts': '1755262699.447039', 
    'channel_type': 'group'
}

{
    'ok': True, 
    'user': {
        'id': 'U096NJW1KEK', 
        'name': 'fusawa', 
        'is_bot': False, 
        'updated': 1753270712, 
        'is_app_user': False, 
        'team_id': 'T0973LKR5GS', 
        'deleted': False, 
        'color': 'ea2977', 
        'is_email_confirmed': True, 
        'real_name': 'Yugo Fusawa', 
        'tz': 'Asia/Tokyo', 
        'tz_label': 'Japan Standard Time', 
        'tz_offset': 32400, 
        'is_admin': False, 
        'is_owner': False, 
        'is_primary_owner': False, 
        'is_restricted': False, 
        'is_ultra_restricted': False, 
        'who_can_share_contact_card': 'EVERYONE', 
        'profile': {
            'real_name': 'Yugo Fusawa', 
            'display_name': 'Yugo Fusawa', 
            'avatar_hash': '02ef2d7dea8c', 
            'real_name_normalized': 'Yugo Fusawa', 
            'display_name_normalized': 'Yugo Fusawa', 
            'image_24': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_24.png', 
            'image_32': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_32.png', 
            'image_48': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_48.png', 
            'image_72': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_72.png', 
            'image_192': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_192.png', 
            'image_512': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_512.png', 
            'image_1024': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_1024.png', 
            'image_original': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_original.png', 
            'is_custom_image': True, 
            'first_name': 'Yugo', 
            'last_name': 'Fusawa', 
            'team': 'T0973LKR5GS', 
            'title': '', 
            'phone': '', 
            'skype': '', 
            'status_text': '', 
            'status_text_canonical': '', 
            'status_emoji': '', 
            'status_emoji_display_info': [], 
            'status_expiration': 0
        }
    }
}

INFO:slack_app:Processing message from channel C09A5L6304B: こんにちは
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"

INFO:slack_app:Received message: {
    'user': 'U09A12GDEEP', 
    'type': 'message', 
    'ts': '1755262705.030699', 
    'bot_id': 'B09A12GD335', 
    'app_id': 'A09A6D0ET9T', 
    'text': 'こんにちは！今日はどんなことをお話ししましょうか？', 
    'team': 'T0973LKR5GS', 
    'bot_profile': {
        'id': 'B09A12GD335', 
        'deleted': False, 
        'name': '凪', 
        'updated': 1755090273, 
        'app_id': 'A09A6D0ET9T', 
        'user_id': 'U09A12GDEEP', 
        'icons': {
            'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 
            'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 
            'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'
        }, 
        'team_id': 'T0973LKR5GS'
    }, 
    'blocks': [
        {
            'type': 'rich_text', 
            'block_id': 'Vs2+', 
            'elements': [
                {
                    'type': 'rich_text_section', 
                    'elements': [
                        {
                            'type': 'text', 
                            'text': 'こんにちは！今日はどんなことをお話ししましょうか？'
                        }
                    ]
                }
            ]
        }
    ], 
    'channel': 'C09A5L6304B', 
    'event_ts': '1755262705.030699', 
    'channel_type': 'group'
}

{
    'ok': True, 
    'user': {
        'id': 'U09A12GDEEP', 
        'name': 'nagi', 
        'is_bot': True, 
        'updated': 1755090273, 
        'is_app_user': False, 
        'team_id': 'T0973LKR5GS', 
        'deleted': False, 
        'color': '235e5b', 
        'is_email_confirmed': False, 
        'real_name': '凪', 
        'tz': 'America/Los_Angeles', 
        'tz_label': 'Pacific Daylight Time', 
        'tz_offset': -25200, 
        'is_admin': False, 
        'is_owner': False, 
        'is_primary_owner': False, 
        'is_restricted': False, 
        'is_ultra_restricted': False, 
        'who_can_share_contact_card': 'EVERYONE', 
        'profile': {
            'real_name': '凪', 
            'display_name': '', 
            'avatar_hash': 'g0e3bad0111a', 
            'real_name_normalized': '凪', 
            'display_name_normalized': '', 
            'image_24': 'https://secure.gravatar.com/avatar/0e3bad0111ae92f32cdc66bb0476e7d2.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0010-24.png', 
            'image_32': 'https://secure.gravatar.com/avatar/0e3bad0111ae92f32cdc66bb0476e7d2.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0010-32.png', 
            'image_48': 'https://secure.gravatar.com/avatar/0e3bad0111ae92f32cdc66bb0476e7d2.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0010-48.png', 
            'image_72': 'https://secure.gravatar.com/avatar/0e3bad0111ae92f32cdc66bb0476e7d2.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0010-72.png', 
            'image_192': 'https://secure.gravatar.com/avatar/0e3bad0111ae92f32cdc66bb0476e7d2.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0010-192.png', 
            'image_512': 'https://secure.gravatar.com/avatar/0e3bad0111ae92f32cdc66bb0476e7d2.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0010-512.png', 
            'first_name': '凪', 
            'last_name': '', 
            'team': 'T0973LKR5GS', 
            'title': '', 
            'phone': '', 
            'skype': '', 
            'status_text': '', 
            'status_text_canonical': '', 
            'status_emoji': '', 
            'status_emoji_display_info': [], 
            'status_expiration': 0, 
            'bot_id': 'B09A12GD335', 
            'api_app_id': 'A09A6D0ET9T', 
            'always_active': False
        }
    }
}
"""

"""
INFO:slack_app:Received message: {
    'user': 'U096NJW1KEK', 
    'type': 'message', 
    'ts': '1755262850.087799', 
    'client_msg_id': 'd55cc55b-d703-45f7-858e-212f88e90dfb', 
    'text': 'a', 
    'team': 'T0973LKR5GS', 
    'blocks': [
        {
            'type': 'rich_text', 
            'block_id': '9gSJ+', 
            'elements': [
                {
                    'type': 'rich_text_section', 
                    'elements': [
                        {
                            'type': 'text', 
                            'text': 'a'
                        }
                    ]
                }
            ]
        }
    ], 
    'channel': 'C09A5L6304B', 
    'event_ts': '1755262850.087799', 
    'channel_type': 'group'
}

{
    'ok': True, 
    'user': {
        'id': 'U096NJW1KEK', 
        'name': 'fusawa', 
        'is_bot': False, 
        'updated': 1753270712, 
        'is_app_user': False, 
        'team_id': 'T0973LKR5GS', 
        'deleted': False, 
        'color': 'ea2977', 
        'is_email_confirmed': True, 
        'real_name': 'Yugo Fusawa', 
        'tz': 'Asia/Tokyo', 
        'tz_label': 'Japan Standard Time', 
        'tz_offset': 32400, 
        'is_admin': False, 
        'is_owner': False, 
        'is_primary_owner': False, 
        'is_restricted': False, 
        'is_ultra_restricted': False, 
        'who_can_share_contact_card': 'EVERYONE', 
        'profile': {
            'real_name': 'Yugo Fusawa', 
            'display_name': 'Yugo Fusawa', 
            'avatar_hash': '02ef2d7dea8c', 
            'real_name_normalized': 'Yugo Fusawa', 
            'display_name_normalized': 'Yugo Fusawa', 
            'image_24': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_24.png', 
            'image_32': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_32.png', 
            'image_48': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_48.png', 
            'image_72': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_72.png', 
            'image_192': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_192.png', 
            'image_512': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_512.png', 
            'image_1024': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_1024.png', 
            'image_original': 'https://avatars.slack-edge.com/2025-07-23/9242871994804_02ef2d7dea8c9b516619_original.png', 
            'is_custom_image': True, 
            'first_name': 'Yugo', 
            'last_name': 'Fusawa', 
            'team': 'T0973LKR5GS', 
            'title': '', 
            'phone': '', 
            'skype': '', 
            'status_text': '', 
            'status_text_canonical': '', 
            'status_emoji': '', 
            'status_emoji_display_info': [], 
            'status_expiration': 0
        }
    }
}

INFO:slack_app:Processing message from channel C09A5L6304B: a
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"

INFO:slack_app:Received message: {
    'user': 'U09AAKK4KMJ', 
    'type': 'message', 
    'ts': '1755262854.772109', 
    'bot_id': 'B09AAKK4K8C', 
    'app_id': 'A09AKGCA72M', 
    'text': 'こんにちは！どうしたのかな？話したいことがあれば教えてね。', 
    'team': 'T0973LKR5GS', 
    'bot_profile': {
        'id': 'B09AAKK4K8C', 
        'deleted': False, 
        'name': '蓮', 
        'updated': 1755089891, 
        'app_id': 'A09AKGCA72M', 
        'user_id': 'U09AAKK4KMJ', 
        'icons': {
            'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 
            'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 
            'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'
        }, 
        'team_id': 'T0973LKR5GS'
    }, 
    'blocks': [
        {
            'type': 'rich_text', 
            'block_id': 'uw8m', 
            'elements': [
                {
                    'type': 'rich_text_section', 
                    'elements': [
                        {
                            'type': 'text', 
                            'text': 'こんにちは！どうしたのかな？話したいことがあれば教えてね。'
                        }
                    ]
                }
            ]
        }
    ], 
    'channel': 'C09A5L6304B', 
    'event_ts': '1755262854.772109', 
    'channel_type': 'group'
}

{
    'ok': True, 
    'user': {
        'id': 'U09AAKK4KMJ', 
        'name': 'ren', 
        'is_bot': True, 
        'updated': 1755089891, 
        'is_app_user': False, 
        'team_id': 'T0973LKR5GS', 
        'deleted': False, 
        'color': '2b6836', 
        'is_email_confirmed': False, 
        'real_name': '蓮', 
        'tz': 'America/Los_Angeles', 
        'tz_label': 'Pacific Daylight Time', 
        'tz_offset': -25200, 
        'is_admin': False, 
        'is_owner': False, 
        'is_primary_owner': False, 
        'is_restricted': False, 
        'is_ultra_restricted': False, 
        'who_can_share_contact_card': 'EVERYONE', 
        'profile': {
            'real_name': '蓮', 
            'display_name': '', 
            'avatar_hash': 'g5d40e75a44e', 
            'real_name_normalized': '蓮', 
            'display_name_normalized': '', 
            'image_24': 'https://secure.gravatar.com/avatar/5d40e75a44ef4f2383c0db7d218ae295.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-24.png', 
            'image_32': 'https://secure.gravatar.com/avatar/5d40e75a44ef4f2383c0db7d218ae295.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-32.png', 
            'image_48': 'https://secure.gravatar.com/avatar/5d40e75a44ef4f2383c0db7d218ae295.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-48.png', 
            'image_72': 'https://secure.gravatar.com/avatar/5d40e75a44ef4f2383c0db7d218ae295.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-72.png', 
            'image_192': 'https://secure.gravatar.com/avatar/5d40e75a44ef4f2383c0db7d218ae295.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-192.png', 
            'image_512': 'https://secure.gravatar.com/avatar/5d40e75a44ef4f2383c0db7d218ae295.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-512.png', 
            'first_name': '蓮', 
            'last_name': '', 
            'team': 'T0973LKR5GS', 
            'title': '', 
            'phone': '', 
            'skype': '', 
            'status_text': '', 
            'status_text_canonical': '', 
            'status_emoji': '', 
            'status_emoji_display_info': [], 
            'status_expiration': 0, 
            'bot_id': 'B09AAKK4K8C', 
            'api_app_id': 'A09AKGCA72M', 
            'always_active': False
        }
    }
}

INFO:slack_app:Ignoring bot message
"""