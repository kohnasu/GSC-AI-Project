#!/usr/bin/env python3
"""
スラックアプリの設定状況を詳細に確認するスクリプト
"""
from dotenv import load_dotenv
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

def check_bot_info():
    """ボットの情報を確認"""
    bot_token = os.getenv("MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN")
    
    if not bot_token:
        print("❌ Bot Token が設定されていません")
        return None
    
    try:
        client = WebClient(token=bot_token)
        auth_test = client.auth_test()
        
        print("=== ボット情報 ===")
        print(f"Bot User ID: {auth_test['user_id']}")
        print(f"Bot Name: {auth_test.get('user', 'Unknown')}")
        print(f"Team: {auth_test['team']}")
        print(f"Team ID: {auth_test['team_id']}")
        
        return auth_test
    except Exception as e:
        print(f"❌ ボット情報取得エラー: {e}")
        return None

def check_app_permissions():
    """アプリの権限を確認"""
    bot_token = os.getenv("MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN")
    
    if not bot_token:
        print("❌ Bot Token が設定されていません")
        return
    
    try:
        client = WebClient(token=bot_token)
        
        print("\n=== 必要な権限 ===")
        required_scopes = [
            "chat:write",
            "channels:history", 
            "groups:history",
            "im:history",
            "mpim:history",
            "app_mentions:read"
        ]
        
        for scope in required_scopes:
            print(f"   - {scope}")
        
        print("\n⚠️  注意: 実際の権限はスラックアプリの設定画面で確認してください")
        
    except Exception as e:
        print(f"❌ 権限確認エラー: {e}")

def check_event_subscriptions():
    """Event Subscriptionsの設定を確認"""
    print("\n=== Event Subscriptions設定 ===")
    print("スラックアプリの設定画面で以下を確認してください:")
    print("1. Event Subscriptions が有効になっているか")
    print("2. Socket Mode が有効になっているか")
    print("3. 以下のイベントが有効になっているか:")
    print("   - message.channels")
    print("   - message.groups") 
    print("   - message.im")
    print("   - message.mpim")
    print("   - app_mention")

def check_channel_invitation():
    """チャンネル招待状況を確認"""
    bot_token = os.getenv("MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN")
    
    if not bot_token:
        print("❌ Bot Token が設定されていません")
        return
    
    try:
        client = WebClient(token=bot_token)
        
        print("\n=== チャンネル招待確認 ===")
        print("ボットがチャンネルに招待されているか確認してください:")
        print("1. スラックで `/invite @ボット名` を実行")
        print("2. またはチャンネル設定からボットを招待")
        
        # 利用可能なチャンネルを取得
        try:
            channels = client.conversations_list(types="public_channel,private_channel")
            print(f"\n利用可能なチャンネル数: {len(channels['channels'])}")
            for channel in channels['channels'][:5]:  # 最初の5つを表示
                print(f"   - #{channel['name']} (ID: {channel['id']})")
        except SlackApiError as e:
            if e.response['error'] == 'missing_scope':
                print("⚠️  channels:read 権限がありません")
            else:
                print(f"⚠️  チャンネル一覧取得エラー: {e.response['error']}")
                
    except Exception as e:
        print(f"❌ チャンネル確認エラー: {e}")

def test_message_sending():
    """テストメッセージ送信"""
    bot_token = os.getenv("MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN")
    
    if not bot_token:
        print("❌ Bot Token が設定されていません")
        return
    
    try:
        client = WebClient(token=bot_token)
        
        print("\n=== メッセージ送信テスト ===")
        print("このテストは手動で実行してください:")
        print("1. スラックで任意のチャンネルにメッセージを送信")
        print("2. または @ボット名 でメンション")
        print("3. アプリのログでイベントが受信されているか確認")
        
    except Exception as e:
        print(f"❌ メッセージ送信テストエラー: {e}")

def main():
    print("=== スラックアプリ設定詳細チェック ===")
    
    # 環境変数チェック
    print("\n1. 環境変数チェック:")
    env_vars = {
        "MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN": os.getenv("MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN"),
        "MANAGER_LOCAL_SIGNING_SECRET": os.getenv("MANAGER_LOCAL_SIGNING_SECRET"),
        "MANAGER_LOCAL_APP_LEVEL_TOKEN": os.getenv("MANAGER_LOCAL_APP_LEVEL_TOKEN"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
    }
    
    for var, value in env_vars.items():
        if value:
            print(f"   ✅ {var}: 設定済み")
        else:
            print(f"   ❌ {var}: 未設定")
    
    # ボット情報確認
    bot_info = check_bot_info()
    
    # 権限確認
    check_app_permissions()
    
    # Event Subscriptions確認
    check_event_subscriptions()
    
    # チャンネル招待確認
    check_channel_invitation()
    
    # メッセージ送信テスト
    test_message_sending()
    
    print("\n=== 次のステップ ===")
    print("1. スラックアプリの設定画面で Event Subscriptions を確認")
    print("2. ボットをチャンネルに招待")
    print("3. アプリを再起動: python3 main.py -l")
    print("4. スラックでメッセージを送信してテスト")

if __name__ == "__main__":
    main()