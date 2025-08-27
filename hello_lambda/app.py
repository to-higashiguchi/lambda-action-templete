import json
import os


def lambda_handler(event, context):
    # 環境変数を取得
    environment = os.environ.get("ENVIRONMENT", "development")
    log_level = os.environ.get("LOG_LEVEL", "debug")
    app_name = os.environ.get("APP_NAME", "hello_lambda")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello_world",
                "environment": environment,
                "log_level": log_level,
                "app_name": app_name,
            }
        ),
    }
