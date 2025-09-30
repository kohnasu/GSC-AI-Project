from SlackBot import SlackBot

# まずグループ分け→半分に分ける group=1 賛成が先 group=2 反対が先
# グループ間のトピックも適当に決めたい
# グループ内で順番をランダムに振る 
# 同じトピックでも賛成、反対を同数にしたい

# → トピック分けについて
# 3*2に分ける ここはテーマの近さで決める
# 3つにまとめたものをそれぞれ前半後半にする

# 人分けについて
# 2群に分ける(Group = 1 or 2)
# 群内で順番をランダムに振る





# chat_conditions_template = {
#     "cloent_id": {
#         "group(str)": "Group?",
#         "day(int)": {
#             "topic": "Topic?",
#             "partner_chatbot": "PartnerChatbot?",
#         }
#     }
# }



# 賛成か反対か
# それぞれに対する反応