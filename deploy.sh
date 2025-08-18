#!/bin/bash

set -e  # エラーで止める

# 環境変数
export PROJECT_ID=gsc-nasu-san
export SERVICE_NAME=gsc-ai-project
export IMAGE_NAME=gcr.io/$PROJECT_ID/$SERVICE_NAME
export REGION=asia-northeast1

# .env ファイルが存在するか確認
if [ ! -f .env ]; then
  echo ".env ファイルが見つかりません"
  exit 1
fi

# env.yaml を作成
echo "🔧 .env から env.yaml を生成中..."
echo "" > env.yaml

# .envファイルを安全に処理
while IFS='=' read -r key value; do
  # コメント行と空行をスキップ
  [[ "$key" =~ ^[[:space:]]*# ]] && continue
  [[ -z "$key" ]] && continue
  
  # キーと値をクリーンアップ（引用符を保持）
  key=$(echo "$key" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
  
  # JSON値の場合はシングルクオーテーションを使用
  if [[ "$key" == "FIREBASE_CREDENTIALS_JSON" ]]; then
    # Firebase認証情報はシングルクオーテーションで囲む
    echo "$key: '$value'" >> env.yaml
  elif [[ "$value" =~ ^[[:space:]]*\" ]]; then
    # 既にダブルクオーテーションで囲まれている場合はそのまま使用
    echo "$key: $value" >> env.yaml
  else
    # ダブルクオーテーションで囲まれていない場合は追加
    echo "$key: \"$value\"" >> env.yaml
  fi
done < .env

# GCP 設定
echo "✅ プロジェクトを設定: $PROJECT_ID"
gcloud config set project $PROJECT_ID
gcloud services enable run.googleapis.com

# Docker イメージをビルド & アップロード
echo "🐳 Docker イメージをビルド中..."
gcloud builds submit --tag $IMAGE_NAME .

# Cloud Run にデプロイ
echo "🚀 Cloud Run にデプロイ中..."
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --env-vars-file env.yaml \
  --timeout 300 \
  --memory 2Gi \
  --cpu 1 \
  --max-instances 10 \
  --min-instances 1

# env.yaml を削除
echo "🧹 env.yaml を削除中..."
rm env.yaml

echo "✅ デプロイ完了！"